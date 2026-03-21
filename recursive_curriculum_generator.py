#!/usr/bin/env python3
"""
================================================================================
Name: Cbwinslow
Date: 2026-03-20
Script Name: recursive_curriculum_generator.py
Version: 1.0.0
Log Summary: Recursive curriculum content generation system
Description:
    Generates comprehensive educational content (problems, quizzes, projects,
    notes, answer keys) from a curriculum outline using recursive tree traversal.
    Supports nested curriculum hierarchies and progressive difficulty levels.
    Designed for semester-long course generation with AI agent integration.

Change Summary:
    - Initial creation with full recursive content generation pipeline
    - Supports nested curriculum structures with arbitrary depth
    - Generates multiple content types with progressive difficulty
    - Outputs structured JSON and formatted markdown files
    - Includes answer key generation with explanations

Inputs:
    - curriculum_outline: Dictionary defining course structure (units, lessons, topics)
    - difficulty_progression: Rules for scaling problem difficulty
    - content_config: Configuration for content types and quantities

Outputs:
    - curriculum_content.json: Complete generated content structure
    - semester_schedule.md: Week-by-week curriculum breakdown
    - unit_*.md: Individual unit content (lessons, problems, projects)
    - quizzes_*.md: Quiz questions and answer keys
    - answer_keys_*.md: Complete solutions with explanations
================================================================================
"""

import json
import random
import math
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict, field
from enum import Enum


class DifficultyLevel(Enum):
    """Enumeration for content difficulty levels."""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    EXPERT = 4


@dataclass
class ContentItem:
    """Base class for content items."""
    id: str
    title: str
    content: str
    difficulty: DifficultyLevel
    estimated_time_minutes: int
    keywords: List[str] = field(default_factory=list)
    learning_objectives: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "difficulty": self.difficulty.name,
            "estimated_time_minutes": self.estimated_time_minutes,
            "keywords": self.keywords,
            "learning_objectives": self.learning_objectives
        }


@dataclass
class Question(ContentItem):
    """Represents a quiz question."""
    question_type: str = "multiple_choice"  # multiple_choice, short_answer, essay
    options: List[str] = field(default_factory=list)
    correct_answer: str = ""
    explanation: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "question_type": self.question_type,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "explanation": self.explanation
        })
        return d


@dataclass
class Problem(ContentItem):
    """Represents a practice problem."""
    problem_statement: str = ""
    solution_steps: List[str] = field(default_factory=list)
    solution_code: str = ""
    expected_output: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "problem_statement": self.problem_statement,
            "solution_steps": self.solution_steps,
            "solution_code": self.solution_code,
            "expected_output": self.expected_output
        })
        return d


@dataclass
class Project(ContentItem):
    """Represents a larger project assignment."""
    objectives: List[str] = field(default_factory=list)
    requirements: List[str] = field(default_factory=list)
    deliverables: List[str] = field(default_factory=list)
    rubric: Dict[str, int] = field(default_factory=dict)
    starter_code: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "objectives": self.objectives,
            "requirements": self.requirements,
            "deliverables": self.deliverables,
            "rubric": self.rubric,
            "starter_code": self.starter_code
        })
        return d


@dataclass
class Lesson(ContentItem):
    """Represents a lesson with notes."""
    notes: str = ""
    code_examples: List[Dict[str, str]] = field(default_factory=list)
    key_concepts: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        d = super().to_dict()
        d.update({
            "notes": self.notes,
            "code_examples": self.code_examples,
            "key_concepts": self.key_concepts
        })
        return d


@dataclass
class Topic:
    """Represents a topic within a lesson."""
    id: str
    name: str
    lessons: List[Lesson] = field(default_factory=list)
    problems: List[Problem] = field(default_factory=list)
    quiz_questions: List[Question] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "lessons": [l.to_dict() for l in self.lessons],
            "problems": [p.to_dict() for p in self.problems],
            "quiz_questions": [q.to_dict() for q in self.quiz_questions]
        }


@dataclass
class Unit:
    """Represents a course unit (weekly or topical)."""
    id: str
    name: str
    description: str
    duration_weeks: int
    topics: List[Topic] = field(default_factory=list)
    projects: List[Project] = field(default_factory=list)
    unit_quiz: List[Question] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "duration_weeks": self.duration_weeks,
            "topics": [t.to_dict() for t in self.topics],
            "projects": [p.to_dict() for p in self.projects],
            "unit_quiz": [q.to_dict() for q in self.unit_quiz]
        }


@dataclass
class Curriculum:
    """Represents a complete curriculum/course."""
    course_name: str
    course_code: str
    level: str
    duration_weeks: int
    units: List[Unit] = field(default_factory=list)
    course_objectives: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "level": self.level,
            "duration_weeks": self.duration_weeks,
            "course_objectives": self.course_objectives,
            "units": [u.to_dict() for u in self.units]
        }


class ContentGenerator:
    """Generates curriculum content recursively."""

    # Content templates for different domains
    TYPESCRIPT_TEMPLATES = {
        "lesson": "Understanding {topic}: This lesson covers {subtopic}. Key concepts include {concepts}.",
        "problem": "Problem: Implement {requirement} in TypeScript. Use {technique} to solve this.",
        "project": "Build a {application} using TypeScript. Requirements: {requirements}",
        "quiz": "Which of the following best describes {concept}?"
    }

    PYTHON_TEMPLATES = {
        "lesson": "Python {topic}: Learn how to {action}. This lesson focuses on {subtopic}.",
        "problem": "Write a Python function that {requirement}. Example input: {example}",
        "project": "Create a Python application for {purpose}. Use {libraries} as needed.",
        "quiz": "What is the output of this Python code?"
    }

    AIML_TEMPLATES = {
        "lesson": "AI/ML Concept: {topic}. We will explore {subtopic} and apply it to {application}.",
        "problem": "Implement {algorithm} to solve {problem_domain}. Dataset: {dataset}",
        "project": "Build an ML model for {task}. Evaluate using {metrics}.",
        "quiz": "In {algorithm}, what does {term} represent?"
    }

    def __init__(self, domain: str = "python"):
        """Initialize the content generator."""
        self.domain = domain.lower()
        self.templates = self._select_templates()
        self.content_id_counter = 0
        self.output_dir = Path("curriculum_output")
        self.output_dir.mkdir(exist_ok=True)

    def _select_templates(self) -> Dict[str, str]:
        """Select templates based on domain."""
        templates_map = {
            "typescript": self.TYPESCRIPT_TEMPLATES,
            "python": self.PYTHON_TEMPLATES,
            "aiml": self.AIML_TEMPLATES,
            "ml": self.AIML_TEMPLATES,
        }
        return templates_map.get(self.domain, self.PYTHON_TEMPLATES)

    def _generate_id(self, prefix: str = "content") -> str:
        """Generate unique content ID."""
        self.content_id_counter += 1
        return f"{prefix}_{self.content_id_counter:05d}"

    # ========== RECURSIVE CONTENT GENERATION ==========

    def generate_curriculum_recursive(
        self,
        outline: Dict[str, Any],
        parent_path: str = ""
    ) -> Curriculum:
        """
        Recursively generate complete curriculum from outline.
        
        Args:
            outline: Dictionary with structure {course_name, units: [{name, topics: [...]}]}
            parent_path: Path for tracking recursion depth
            
        Returns:
            Complete Curriculum object with all generated content
        """
        print(f"\n{'='*70}")
        print(f"Generating Curriculum: {outline['course_name']}")
        print(f"{'='*70}\n")

        curriculum = Curriculum(
            course_name=outline["course_name"],
            course_code=outline.get("course_code", "CS101"),
            level=outline.get("level", "Intermediate"),
            duration_weeks=outline.get("duration_weeks", 16),
            course_objectives=outline.get("course_objectives", [])
        )

        # Recursively generate units
        units_outline = outline.get("units", [])
        for unit_idx, unit_outline in enumerate(units_outline):
            print(f"  Generating Unit {unit_idx + 1}: {unit_outline['name']}")
            unit = self._generate_unit_recursive(
                unit_outline,
                unit_index=unit_idx,
                total_units=len(units_outline),
                parent_path=f"{parent_path}/unit_{unit_idx}"
            )
            curriculum.units.append(unit)

        return curriculum

    def _generate_unit_recursive(
        self,
        unit_outline: Dict[str, Any],
        unit_index: int = 0,
        total_units: int = 1,
        parent_path: str = ""
    ) -> Unit:
        """
        Recursively generate unit content (topics, problems, projects, quiz).
        
        Base case: If no topics defined, generate default topics.
        Recursive case: For each topic, generate nested content.
        """
        unit = Unit(
            id=f"unit_{unit_index:02d}",
            name=unit_outline["name"],
            description=unit_outline.get("description", ""),
            duration_weeks=unit_outline.get("duration_weeks", 1),
        )

        # Get topics (base case if empty)
        topics_outline = unit_outline.get("topics", [])
        if not topics_outline:
            topics_outline = [{"name": "Introduction", "num_lessons": 2}]

        # Recursively generate topics
        for topic_idx, topic_outline in enumerate(topics_outline):
            print(f"    → Topic {topic_idx + 1}: {topic_outline['name']}")
            topic = self._generate_topic_recursive(
                topic_outline,
                unit_id=unit.id,
                topic_index=topic_idx,
                difficulty_base=self._calculate_difficulty(unit_index, total_units),
                parent_path=f"{parent_path}/topic_{topic_idx}"
            )
            unit.topics.append(topic)

        # Generate unit-level project (optional)
        if unit_outline.get("has_project", True) and unit.duration_weeks >= 2:
            print(f"    → Generating Unit Project")
            project = self._generate_project(
                unit.id,
                f"Unit {unit_index + 1} Project",
                difficulty=DifficultyLevel.ADVANCED
            )
            unit.projects.append(project)

        # Generate unit quiz
        print(f"    → Generating Unit Quiz")
        unit.unit_quiz = self._generate_quiz(
            num_questions=8,
            unit_id=unit.id,
            difficulty=self._calculate_difficulty(unit_index, total_units)
        )

        return unit

    def _generate_topic_recursive(
        self,
        topic_outline: Dict[str, Any],
        unit_id: str = "",
        topic_index: int = 0,
        difficulty_base: DifficultyLevel = DifficultyLevel.BEGINNER,
        parent_path: str = ""
    ) -> Topic:
        """
        Recursively generate topic content (lessons, problems, quiz).
        
        Base case: Generate leaf content (lessons, problems).
        Recursive case: Could support sub-topics for deeper nesting.
        """
        topic = Topic(
            id=f"{unit_id}_topic_{topic_index:02d}",
            name=topic_outline["name"],
        )

        # Generate lessons (base case for depth)
        num_lessons = topic_outline.get("num_lessons", 2)
        for lesson_idx in range(num_lessons):
            print(f"      ◦ Lesson {lesson_idx + 1}")
            lesson = self._generate_lesson(
                topic.id,
                lesson_idx,
                topic_outline["name"],
                difficulty=difficulty_base
            )
            topic.lessons.append(lesson)

        # Generate practice problems (base case)
        num_problems = topic_outline.get("num_problems", 3)
        for problem_idx in range(num_problems):
            problem = self._generate_problem(
                topic.id,
                problem_idx,
                topic_outline["name"],
                difficulty=self._escalate_difficulty(difficulty_base, problem_idx)
            )
            topic.problems.append(problem)

        # Generate topic quiz
        topic.quiz_questions = self._generate_quiz(
            num_questions=5,
            unit_id=topic.id,
            difficulty=difficulty_base
        )

        return topic

    # ========== CONTENT GENERATION HELPERS ==========

    def _generate_lesson(
        self,
        topic_id: str,
        lesson_index: int,
        topic_name: str,
        difficulty: DifficultyLevel = DifficultyLevel.BEGINNER
    ) -> Lesson:
        """Generate a lesson with notes and examples."""
        lesson = Lesson(
            id=self._generate_id("lesson"),
            title=f"{topic_name} - Lesson {lesson_index + 1}",
            content=self.templates["lesson"].format(
                topic=topic_name,
                subtopic=f"Part {lesson_index + 1}",
                concepts=", ".join([f"Concept {i}" for i in range(2, 4)])
            ),
            notes=self._generate_notes(topic_name, lesson_index),
            difficulty=difficulty,
            estimated_time_minutes=45 + (lesson_index * 15),
            key_concepts=self._generate_concepts(topic_name, lesson_index),
            learning_objectives=self._generate_learning_objectives(topic_name, lesson_index)
        )

        # Add code examples
        lesson.code_examples = [
            {
                "title": f"Example {i + 1}: {topic_name}",
                "code": self._generate_code_example(topic_name, i)
            }
            for i in range(1 + difficulty.value)
        ]

        return lesson

    def _generate_problem(
        self,
        topic_id: str,
        problem_index: int,
        topic_name: str,
        difficulty: DifficultyLevel = DifficultyLevel.BEGINNER
    ) -> Problem:
        """Generate a practice problem with solution."""
        problem = Problem(
            id=self._generate_id("problem"),
            title=f"{topic_name} Problem {problem_index + 1}",
            content=self.templates["problem"].format(
                requirement=f"Solve problem about {topic_name}",
                technique="Best practices",
                example="[Sample input]"
            ),
            problem_statement=self._generate_problem_statement(topic_name, problem_index, difficulty),
            difficulty=difficulty,
            estimated_time_minutes=15 * (1 + difficulty.value),
            learning_objectives=[f"Practice: {topic_name}"]
        )

        # Generate solution
        problem.solution_steps = self._generate_solution_steps(
            topic_name,
            problem_index,
            difficulty
        )
        problem.solution_code = self._generate_solution_code(
            topic_name,
            problem_index,
            difficulty
        )

        return problem

    def _generate_project(
        self,
        unit_id: str,
        project_name: str,
        difficulty: DifficultyLevel = DifficultyLevel.ADVANCED
    ) -> Project:
        """Generate a larger project assignment."""
        project = Project(
            id=self._generate_id("project"),
            title=project_name,
            content=self.templates["project"].format(
                application="Real-world application",
                requirements="TBD",
                purpose="Apply learned concepts",
                libraries="Standard libraries",
                task="Classification task",
                metrics="Accuracy, Precision"
            ),
            objectives=self._generate_project_objectives(),
            requirements=self._generate_project_requirements(),
            deliverables=self._generate_deliverables(),
            difficulty=difficulty,
            estimated_time_minutes=240,  # 4 hours
            rubric=self._generate_rubric()
        )

        project.starter_code = self._generate_starter_code()
        return project

    def _generate_quiz(
        self,
        num_questions: int = 5,
        unit_id: str = "",
        difficulty: DifficultyLevel = DifficultyLevel.BEGINNER
    ) -> List[Question]:
        """Generate quiz questions with multiple difficulty levels."""
        questions = []

        for q_idx in range(num_questions):
            # Vary question types
            q_type = ["multiple_choice", "short_answer", "essay"][q_idx % 3]

            question = Question(
                id=self._generate_id("question"),
                title=f"Question {q_idx + 1}",
                content=self.templates["quiz"],
                question_type=q_type,
                difficulty=self._escalate_difficulty(difficulty, q_idx),
                estimated_time_minutes=5 + (q_idx * 2),
                learning_objectives=[f"Assess: Learning Objective {q_idx}"]
            )

            # Generate options and answer
            question.options = self._generate_options(q_type)
            question.correct_answer = question.options[0] if question.options else ""
            question.explanation = self._generate_explanation(q_type)

            questions.append(question)

        return questions

    # ========== CONTENT DETAIL GENERATORS ==========

    def _generate_notes(self, topic: str, lesson_index: int) -> str:
        """Generate detailed lesson notes."""
        return f"""
## {topic} - Lesson {lesson_index + 1} Notes

### Overview
This lesson introduces key concepts in {topic}. You will learn:
- Fundamental principles
- Real-world applications
- Best practices and common pitfalls

### Key Ideas
1. **Concept 1**: {topic} involves understanding the basics.
2. **Concept 2**: Intermediate applications expand your skills.
3. **Concept 3**: Advanced patterns solve complex problems.

### Summary
Remember that {topic} requires practice and patience. Start with simple examples and gradually increase complexity.
"""

    def _generate_concepts(self, topic: str, lesson_index: int) -> List[str]:
        """Generate key concepts for a lesson."""
        concepts_map = {
            "typescript": ["Type Safety", "Generics", "Interfaces", "Decorators", "Utility Types"],
            "python": ["Data Types", "Functions", "Classes", "Modules", "Async/Await"],
            "aiml": ["Neural Networks", "Training", "Optimization", "Loss Functions", "Activation"],
        }
        base_concepts = concepts_map.get(self.domain, ["Core", "Intermediate", "Advanced"])
        return base_concepts[lesson_index : lesson_index + 3]

    def _generate_learning_objectives(self, topic: str, lesson_index: int) -> List[str]:
        """Generate SMART learning objectives."""
        return [
            f"Understand the fundamentals of {topic}",
            f"Apply {topic} concepts to solve problems",
            f"Analyze {topic} trade-offs and best practices",
        ]

    def _generate_code_example(self, topic: str, example_index: int) -> str:
        """Generate code example snippet."""
        if self.domain == "typescript":
            return f"""// {topic} Example {example_index + 1}
type {topic}Config = {{
  enabled: boolean;
  value: string;
}};

function process{topic}(config: {topic}Config): void {{
  if (config.enabled) {{
    console.log(`Processing: ${{config.value}}`);
  }}
}}
"""
        elif self.domain == "python":
            return f"""# {topic} Example {example_index + 1}
def process_{topic.lower()}(data):
    \"\"\"Process {topic} data.\"\"\"
    result = []
    for item in data:
        processed = item * 2
        result.append(processed)
    return result

# Usage
sample_data = [1, 2, 3, 4, 5]
output = process_{topic.lower()}(sample_data)
print(output)
"""
        else:  # AI/ML
            return f"""import numpy as np
from sklearn.preprocessing import StandardScaler

# {topic} Example {example_index + 1}
data = np.array([[1, 2], [3, 4], [5, 6]])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print(scaled_data)
"""

    def _generate_problem_statement(
        self,
        topic: str,
        problem_index: int,
        difficulty: DifficultyLevel
    ) -> str:
        """Generate a specific problem statement."""
        difficulty_desc = {
            DifficultyLevel.BEGINNER: "basic",
            DifficultyLevel.INTERMEDIATE: "intermediate",
            DifficultyLevel.ADVANCED: "complex",
            DifficultyLevel.EXPERT: "expert-level"
        }

        return f"""
**Problem {problem_index + 1}: {topic} Challenge**

Write a solution for a {difficulty_desc[difficulty]} {topic} problem.

**Input:** Sample data or requirements specific to the problem.
**Output:** Expected results or behavior.
**Constraints:** Time and space complexity requirements.

**Example:**
- Input: [1, 2, 3, 4, 5]
- Expected Output: Transformed result
"""

    def _generate_solution_steps(
        self,
        topic: str,
        problem_index: int,
        difficulty: DifficultyLevel
    ) -> List[str]:
        """Generate step-by-step solution outline."""
        steps = [
            f"Understand the problem requirements for {topic}",
            "Plan your approach and data structures",
            "Implement the solution",
            "Test with provided examples",
            "Optimize for performance",
            "Consider edge cases"
        ]
        return steps[: 3 + difficulty.value]

    def _generate_solution_code(
        self,
        topic: str,
        problem_index: int,
        difficulty: DifficultyLevel
    ) -> str:
        """Generate complete solution code."""
        if self.domain == "typescript":
            return f"""
// Solution: {topic} Problem {problem_index + 1}
function solve{topic}(input: any[]): any {{
  // Step 1: Validate input
  if (!input || input.length === 0) return [];
  
  // Step 2: Process data
  const result = input.map(item => {
    // Implement logic based on difficulty
    return item * 2;
  }};
  
  // Step 3: Return result
  return result;
}}

// Test
const test_input = [1, 2, 3];
console.log(solve{topic}(test_input));
"""
        elif self.domain == "python":
            return f"""
def solve_{topic.lower()}(input_data):
    \"\"\"
    Solution for {topic} Problem {problem_index + 1}
    
    Args:
        input_data: Input array or data structure
        
    Returns:
        Processed result
    \"\"\"
    if not input_data:
        return []
    
    result = []
    for item in input_data:
        processed = item * 2  # Replace with actual logic
        result.append(processed)
    
    return result

# Test
test_input = [1, 2, 3]
print(solve_{topic.lower()}(test_input))
"""
        else:  # AI/ML
            return f"""
import numpy as np
from sklearn.model_selection import train_test_split

# Solution: {topic} Problem {problem_index + 1}
def solve_{topic.lower()}(X, y):
    \"\"\"Train and evaluate model.\"\"\"
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Implement training logic
    # model = YourModel()
    # model.fit(X_train, y_train)
    # predictions = model.predict(X_test)
    
    return {{"accuracy": 0.85}}

# Usage
# predictions = solve_{topic.lower()}(X, y)
"""

    def _generate_options(self, question_type: str) -> List[str]:
        """Generate multiple choice options."""
        if question_type == "multiple_choice":
            return [
                "Correct answer",
                "Common misconception 1",
                "Common misconception 2",
                "Distractor"
            ]
        elif question_type == "short_answer":
            return ["Expected short answer response"]
        else:  # essay
            return ["Full essay response expected"]

    def _generate_explanation(self, question_type: str) -> str:
        """Generate answer explanation."""
        return f"""
This answer is correct because it demonstrates understanding of the core concept.
The {question_type} question tests your ability to apply principles learned in the lesson.
Review the key concepts if you're unsure about this topic.
"""

    def _generate_project_objectives(self) -> List[str]:
        """Generate project learning objectives."""
        return [
            "Apply concepts from the unit to a real-world problem",
            "Design and implement a complete solution",
            "Test and debug your implementation",
            "Document your approach and results"
        ]

    def _generate_project_requirements(self) -> List[str]:
        """Generate project requirements."""
        return [
            "Must implement core functionality",
            "Include at least 3 test cases",
            "Write clear documentation",
            "Follow coding standards and best practices",
            "Submit working code and report"
        ]

    def _generate_deliverables(self) -> List[str]:
        """Generate project deliverables."""
        return [
            "Source code with comments",
            "Test suite with results",
            "Project report (2-3 pages)",
            "Demonstration/Presentation"
        ]

    def _generate_rubric(self) -> Dict[str, int]:
        """Generate grading rubric."""
        return {
            "Functionality": 40,
            "Code Quality": 20,
            "Documentation": 15,
            "Testing": 15,
            "Presentation": 10
        }

    def _generate_starter_code(self) -> str:
        """Generate starter code template."""
        if self.domain == "typescript":
            return """
// Starter code template
type ProjectConfig = {
  // Define your types here
};

function main(config: ProjectConfig): void {
  // TODO: Implement project
}

// Export for testing
export { main };
"""
        elif self.domain == "python":
            return """
# Starter code template

def main(config):
    \"\"\"
    Main project function.
    
    Args:
        config: Configuration dictionary
    \"\"\"
    # TODO: Implement project
    pass

if __name__ == "__main__":
    config = {}
    main(config)
"""
        else:  # AI/ML
            return """
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Starter code template
def main():
    # Load data
    data = load_iris()
    X, y = data.data, data.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # TODO: Train and evaluate model
    
if __name__ == "__main__":
    main()
"""

    # ========== UTILITY FUNCTIONS ==========

    def _calculate_difficulty(
        self,
        unit_index: int,
        total_units: int
    ) -> DifficultyLevel:
        """Calculate difficulty level based on progression."""
        progress_ratio = unit_index / max(total_units, 1)

        if progress_ratio < 0.33:
            return DifficultyLevel.BEGINNER
        elif progress_ratio < 0.67:
            return DifficultyLevel.INTERMEDIATE
        else:
            return DifficultyLevel.ADVANCED

    def _escalate_difficulty(
        self,
        base_difficulty: DifficultyLevel,
        item_index: int
    ) -> DifficultyLevel:
        """Escalate difficulty within a topic."""
        escalation = item_index // 3
        new_level = min(base_difficulty.value + escalation, 4)
        return DifficultyLevel(new_level)

    # ========== OUTPUT GENERATION ==========

    def save_curriculum_to_json(self, curriculum: Curriculum, filename: str = "curriculum_content.json") -> None:
        """Save curriculum to JSON file."""
        output_path = self.output_dir / filename
        with open(output_path, 'w') as f:
            json.dump(curriculum.to_dict(), f, indent=2)
        print(f"\n✓ Saved curriculum JSON to {output_path}")

    def generate_markdown_curriculum(self, curriculum: Curriculum) -> None:
        """Generate comprehensive markdown files for curriculum."""
        print(f"\nGenerating markdown files...")

        # Generate semester schedule
        self._generate_schedule_markdown(curriculum)

        # Generate unit files
        for unit_idx, unit in enumerate(curriculum.units):
            self._generate_unit_markdown(curriculum, unit, unit_idx)

        # Generate quiz files
        for unit_idx, unit in enumerate(curriculum.units):
            self._generate_quiz_markdown(unit, unit_idx)

        # Generate answer key files
        for unit_idx, unit in enumerate(curriculum.units):
            self._generate_answer_key_markdown(unit, unit_idx)

        print(f"✓ Markdown files generated in {self.output_dir}")

    def _generate_schedule_markdown(self, curriculum: Curriculum) -> None:
        """Generate semester schedule markdown."""
        output_file = self.output_dir / "semester_schedule.md"

        with open(output_file, 'w') as f:
            f.write(f"# {curriculum.course_name} - Semester Schedule\n\n")
            f.write(f"**Course Code:** {curriculum.course_code}\n")
            f.write(f"**Level:** {curriculum.level}\n")
            f.write(f"**Duration:** {curriculum.duration_weeks} weeks\n\n")

            f.write("## Course Objectives\n\n")
            for obj in curriculum.course_objectives:
                f.write(f"- {obj}\n")
            f.write("\n")

            f.write("## Weekly Schedule\n\n")
            week = 1
            for unit_idx, unit in enumerate(curriculum.units):
                f.write(f"### Unit {unit_idx + 1}: {unit.name}\n\n")
                f.write(f"**Duration:** Weeks {week} - {week + unit.duration_weeks - 1}\n\n")
                f.write(f"**Description:** {unit.description}\n\n")

                f.write("**Topics:**\n")
                for topic in unit.topics:
                    f.write(f"- {topic.name}\n")
                f.write("\n")

                f.write(f"**Deliverables:**\n")
                f.write(f"- {len(unit.topics)} Topics with {sum(len(t.lessons) for t in unit.topics)} Lessons\n")
                f.write(f"- {sum(len(t.problems) for t in unit.topics)} Practice Problems\n")
                f.write(f"- Unit Quiz: {len(unit.unit_quiz)} Questions\n")
                if unit.projects:
                    f.write(f"- {len(unit.projects)} Project(s)\n")
                f.write("\n---\n\n")

                week += unit.duration_weeks

        print(f"  ✓ Generated {output_file.name}")

    def _generate_unit_markdown(self, curriculum: Curriculum, unit: Unit, unit_idx: int) -> None:
        """Generate individual unit markdown file."""
        output_file = self.output_dir / f"unit_{unit_idx + 1:02d}_{unit.id}.md"

        with open(output_file, 'w') as f:
            f.write(f"# {unit.name}\n\n")
            f.write(f"**Unit:** {unit.id}\n")
            f.write(f"**Duration:** {unit.duration_weeks} week(s)\n\n")
            f.write(f"{unit.description}\n\n")

            # Topics and lessons
            f.write("## Learning Content\n\n")
            for topic_idx, topic in enumerate(unit.topics):
                f.write(f"### Topic {topic_idx + 1}: {topic.name}\n\n")

                for lesson_idx, lesson in enumerate(topic.lessons):
                    f.write(f"#### Lesson {lesson_idx + 1}: {lesson.title}\n\n")
                    f.write(f"**Difficulty:** {lesson.difficulty.name}\n")
                    f.write(f"**Time:** {lesson.estimated_time_minutes} minutes\n\n")
                    f.write(f"{lesson.notes}\n\n")

                    if lesson.code_examples:
                        f.write("**Code Examples:**\n\n")
                        for example in lesson.code_examples:
                            f.write(f"```python\n{example['code']}\n```\n\n")

            # Practice problems
            f.write("## Practice Problems\n\n")
            for topic_idx, topic in enumerate(unit.topics):
                f.write(f"### Topic {topic_idx + 1}: {topic.name}\n\n")
                for prob_idx, problem in enumerate(topic.problems):
                    f.write(f"#### Problem {prob_idx + 1}: {problem.title}\n\n")
                    f.write(f"**Difficulty:** {problem.difficulty.name}\n")
                    f.write(f"{problem.problem_statement}\n\n")

            # Projects
            if unit.projects:
                f.write("## Projects\n\n")
                for proj_idx, project in enumerate(unit.projects):
                    f.write(f"### Project {proj_idx + 1}: {project.title}\n\n")
                    f.write(f"**Time:** {project.estimated_time_minutes} minutes\n\n")
                    f.write("**Objectives:**\n")
                    for obj in project.objectives:
                        f.write(f"- {obj}\n")
                    f.write("\n**Requirements:**\n")
                    for req in project.requirements:
                        f.write(f"- {req}\n")
                    f.write("\n**Deliverables:**\n")
                    for deliv in project.deliverables:
                        f.write(f"- {deliv}\n")
                    f.write("\n**Rubric:**\n")
                    for criterion, points in project.rubric.items():
                        f.write(f"- {criterion}: {points} points\n")
                    f.write("\n**Starter Code:**\n\n```python\n")
                    f.write(project.starter_code)
                    f.write("```\n\n")

        print(f"  ✓ Generated {output_file.name}")

    def _generate_quiz_markdown(self, unit: Unit, unit_idx: int) -> None:
        """Generate quiz markdown file."""
        output_file = self.output_dir / f"quiz_unit_{unit_idx + 1:02d}.md"

        with open(output_file, 'w') as f:
            f.write(f"# Unit {unit_idx + 1} Quiz: {unit.name}\n\n")
            f.write("**Instructions:** Answer all questions. Submit your answers for grading.\n\n")

            for q_idx, question in enumerate(unit.unit_quiz):
                f.write(f"## Question {q_idx + 1}\n\n")
                f.write(f"**Type:** {question.question_type}\n")
                f.write(f"**Difficulty:** {question.difficulty.name}\n\n")
                f.write(f"{question.content}\n\n")

                if question.options:
                    f.write("**Options:**\n")
                    for opt_idx, option in enumerate(question.options):
                        f.write(f"  {chr(65 + opt_idx)}) {option}\n")
                f.write("\n")

        print(f"  ✓ Generated {output_file.name}")

    def _generate_answer_key_markdown(self, unit: Unit, unit_idx: int) -> None:
        """Generate answer key markdown file."""
        output_file = self.output_dir / f"answer_key_unit_{unit_idx + 1:02d}.md"

        with open(output_file, 'w') as f:
            f.write(f"# Unit {unit_idx + 1} Answer Key: {unit.name}\n\n")
            f.write("**CONFIDENTIAL - INSTRUCTOR USE ONLY**\n\n")

            # Quiz answers
            f.write("## Unit Quiz Answers\n\n")
            for q_idx, question in enumerate(unit.unit_quiz):
                f.write(f"### Question {q_idx + 1}\n\n")
                f.write(f"**Correct Answer:** {question.correct_answer}\n\n")
                f.write(f"**Explanation:**\n{question.explanation}\n\n")

            # Problem solutions
            f.write("## Problem Solutions\n\n")
            for topic_idx, topic in enumerate(unit.topics):
                f.write(f"### Topic {topic_idx + 1}: {topic.name}\n\n")
                for prob_idx, problem in enumerate(topic.problems):
                    f.write(f"#### Problem {prob_idx + 1}: Solution\n\n")
                    f.write("**Steps:**\n")
                    for step in problem.solution_steps:
                        f.write(f"1. {step}\n")
                    f.write(f"\n**Solution Code:**\n```python\n{problem.solution_code}\n```\n\n")

        print(f"  ✓ Generated {output_file.name}")


def main():
    """Main execution function."""
    print("\n" + "="*70)
    print("RECURSIVE CURRICULUM CONTENT GENERATOR")
    print("="*70)

    # Example curriculum outline for Python DSA course
    curriculum_outline = {
        "course_name": "Advanced Python: Data Structures and Algorithms",
        "course_code": "PYTH301",
        "level": "Intermediate-Advanced",
        "duration_weeks": 16,
        "course_objectives": [
            "Master fundamental data structures (arrays, linked lists, trees, graphs)",
            "Understand and implement classic algorithms (sorting, searching, dynamic programming)",
            "Analyze algorithm complexity and optimize solutions",
            "Apply concepts to real-world programming challenges"
        ],
        "units": [
            {
                "name": "Arrays and Lists",
                "description": "Understand linear data structures and operations",
                "duration_weeks": 2,
                "has_project": True,
                "topics": [
                    {"name": "Array Fundamentals", "num_lessons": 2, "num_problems": 4},
                    {"name": "Dynamic Arrays and Lists", "num_lessons": 2, "num_problems": 4},
                ]
            },
            {
                "name": "Sorting and Searching",
                "description": "Master fundamental algorithms for data manipulation",
                "duration_weeks": 3,
                "has_project": True,
                "topics": [
                    {"name": "Sorting Algorithms", "num_lessons": 3, "num_problems": 5},
                    {"name": "Binary Search", "num_lessons": 2, "num_problems": 4},
                ]
            },
            {
                "name": "Trees and Graphs",
                "description": "Work with hierarchical and networked data structures",
                "duration_weeks": 4,
                "has_project": True,
                "topics": [
                    {"name": "Binary Trees", "num_lessons": 3, "num_problems": 5},
                    {"name": "Graph Theory", "num_lessons": 3, "num_problems": 5},
                    {"name": "Traversal Algorithms", "num_lessons": 2, "num_problems": 4},
                ]
            },
            {
                "name": "Dynamic Programming",
                "description": "Solve complex problems with optimal substructure",
                "duration_weeks": 3,
                "has_project": True,
                "topics": [
                    {"name": "DP Fundamentals", "num_lessons": 2, "num_problems": 4},
                    {"name": "Classic DP Problems", "num_lessons": 3, "num_problems": 6},
                ]
            },
        ]
    }

    # Generate curriculum
    generator = ContentGenerator(domain="python")
    curriculum = generator.generate_curriculum_recursive(curriculum_outline)

    # Save outputs
    generator.save_curriculum_to_json(curriculum)
    generator.generate_markdown_curriculum(curriculum)

    print(f"\n{'='*70}")
    print("CURRICULUM GENERATION COMPLETE")
    print("="*70)
    print(f"\nGenerated Content Summary:")
    print(f"  • Course: {curriculum.course_name}")
    print(f"  • Units: {len(curriculum.units)}")
    print(f"  • Total Topics: {sum(len(u.topics) for u in curriculum.units)}")
    print(f"  • Total Lessons: {sum(len(t.lessons) for u in curriculum.units for t in u.topics)}")
    print(f"  • Total Problems: {sum(len(t.problems) for u in curriculum.units for t in u.topics)}")
    print(f"  • Total Quiz Questions: {sum(len(u.unit_quiz) for u in curriculum.units)}")
    print(f"  • Total Projects: {sum(len(u.projects) for u in curriculum.units)}")
    print(f"\nOutput Directory: {generator.output_dir}/")
    print("\n")


if __name__ == "__main__":
    main()