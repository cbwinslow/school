# 🛠️ Agent Skills Definitions

## Overview

This file defines the specific skills each agent possesses. Agents reference these definitions when performing their roles.

---

## 🎯 Orchestrator Skills

### Skill: Route Request
**Description**: Analyze student request and route to appropriate agent
**Input**: Student message, current state
**Output**: Target agent, context package

```yaml
skill:
  name: route_request
  description: "Analyze student intent and route to correct agent"
  inputs:
    - student_message: string
    - current_state: object
  outputs:
    - target_agent: string
    - context: object
    - action: string
  logic: |
    1. Parse student message for intent
    2. Check current state
    3. Match intent to agent capabilities
    4. Package context for target agent
    5. Return routing decision
```

### Skill: Update State
**Description**: Update student progress after completing work
**Input**: Assessment results, competencies
**Output**: Updated state file

```yaml
skill:
  name: update_state
  description: "Update student progress tracking"
  inputs:
    - assessment_results: object
    - competencies: object
  outputs:
    - updated_tracker: string
  logic: |
    1. Parse assessment results
    2. Update competency scores
    3. Log completed items
    4. Update milestones
    5. Write to tracker file
```

### Skill: Generate Progress Report
**Description**: Create weekly/monthly progress summary
**Input**: Student state, time period
**Output**: Progress report markdown

```yaml
skill:
  name: generate_progress_report
  description: "Create formatted progress report"
  inputs:
    - student_state: object
    - period: string
  outputs:
    - report: markdown
  logic: |
    1. Gather completed items for period
    2. Calculate competency changes
    3. Identify trends
    4. Generate recommendations
    5. Format as markdown
```

---

## 🏗️ Curriculum Architect Skills

### Skill: Design Module
**Description**: Create complete module structure for a topic
**Input**: Topic, student level, prerequisites
**Output**: Module specification

```yaml
skill:
  name: design_module
  description: "Design a complete learning module"
  inputs:
    - topic: string
    - student_level: string
    - known_concepts: array
  outputs:
    - module_spec: object
  logic: |
    1. Define learning objectives
    2. Determine scope and depth
    3. Create prerequisite chain
    4. Sequence lessons
    5. Define project
    6. Create assessment criteria
```

### Skill: Adapt Curriculum
**Description**: Modify curriculum based on student performance
**Input**: Performance data, gaps identified
**Output**: Adjusted learning path

```yaml
skill:
  name: adapt_curriculum
  description: "Adjust curriculum based on performance"
  inputs:
    - performance_data: object
    - gaps: array
  outputs:
    - adjusted_path: array
  logic: |
    1. Analyze success rates
    2. Identify struggling areas
    3. Insert remedial content if needed
    4. Adjust difficulty
    5. Update learning path
```

### Skill: Create Prerequisite Chain
**Description**: Define dependencies between concepts
**Input**: Target concept
**Output**: Prerequisite tree

```yaml
skill:
  name: create_prerequisite_chain
  description: "Map concept dependencies"
  inputs:
    - target_concept: string
  outputs:
    - prerequisite_tree: object
  logic: |
    1. Identify what must be known first
    2. Check student current knowledge
    3. Build dependency tree
    4. Determine optimal learning order
```

---

## 📚 Lesson Generator Skills

### Skill: Generate Lesson
**Description**: Create complete lesson from outline
**Input**: Lesson outline, difficulty
**Output**: Full lesson content

```yaml
skill:
  name: generate_lesson
  description: "Create detailed lesson content"
  inputs:
    - outline: object
    - difficulty: string
    - student_level: string
  outputs:
    - lesson: markdown
  logic: |
    1. Expand each concept
    2. Create explanations
    3. Generate code examples (basic → advanced)
    4. Write real-world analogies
    5. Create visual diagrams
    6. Call Problem Creator for exercises
    7. Assemble final lesson
```

### Skill: Create Code Example
**Description**: Generate runnable code examples
**Input**: Concept, difficulty, language
**Output**: Annotated code

```yaml
skill:
  name: create_code_example
  description: "Generate code examples"
  inputs:
    - concept: string
    - difficulty: string
    - language: string
  outputs:
    - code: string
    - comments: array
  logic: |
    1. Select appropriate pattern
    2. Write clean, runnable code
    3. Add explanatory comments
    4. Include error handling
    5. Follow style guidelines
```

### Skill: Generate Diagram
**Description**: Create visual representations
**Input**: Concept, complexity
**Output**: ASCII art or Mermaid diagram

```yaml
skill:
  name: generate_diagram
  description: "Create visual diagrams"
  inputs:
    - concept: string
    - complexity: string
  outputs:
    - diagram: string
    - format: "ascii" | "mermaid"
  logic: |
    1. Identify key components
    2. Determine relationships
    3. Choose diagram type
    4. Generate visual representation
```

---

## 🧩 Problem Creator Skills

### Skill: Create Exercise
**Description**: Generate coding exercises
**Input**: Concepts, difficulty, type
**Output**: Exercise with tests

```yaml
skill:
  name: create_exercise
  description: "Generate coding exercise"
  inputs:
    - concepts: array
    - difficulty: string
    - type: "fill-blank" | "debug" | "implement" | "multiple-choice"
  outputs:
    - exercise: object
  logic: |
    1. Design problem statement
    2. Create starter code
    3. Generate test cases
    4. Write hints
    5. Create solution
    6. Define success criteria
```

### Skill: Generate Test Cases
**Description**: Create comprehensive test cases
**Input**: Function spec, edge cases
**Output**: Test code

```yaml
skill:
  name: generate_test_cases
  description: "Create test cases for exercises"
  inputs:
    - function_spec: object
    - edge_cases: array
  outputs:
    - tests: string
  logic: |
    1. Create basic functionality tests
    2. Add edge case tests
    3. Include performance tests if relevant
    4. Write clear assertions
```

### Skill: Create Starter Code
**Description**: Generate template code for exercises
**Input**: Requirements, language
**Output**: Starter template

```yaml
skill:
  name: create_starter_code
  description: "Generate starter code template"
  inputs:
    - requirements: array
    - language: string
  outputs:
    - starter_code: string
  logic: |
    1. Create function/class skeleton
    2. Add TODO comments
    3. Include type hints
    4. Add docstring template
```

---

## 🚀 Project Designer Skills

### Skill: Design Project
**Description**: Create project specifications
**Input**: Concepts to apply, difficulty
**Output**: Project spec

```yaml
skill:
  name: design_project
  description: "Design a learning project"
  inputs:
    - concepts: array
    - difficulty: string
    - time_estimate: string
  outputs:
    - project_spec: object
  logic: |
    1. Define project scope
    2. Create functional requirements
    3. Define technical requirements
    4. Design architecture
    5. Generate starter code
    6. Create grading rubric
```

### Skill: Generate Starter Code
**Description**: Create project skeleton
**Input**: Architecture, tech stack
**Output**: Project files

```yaml
skill:
  name: generate_starter_code
  description: "Generate project starter code"
  inputs:
    - architecture: object
    - tech_stack: object
  outputs:
    - files: object
  logic: |
    1. Create directory structure
    2. Generate main entry point
    3. Create module skeletons
    4. Add configuration template
    5. Include test template
```

### Skill: Create Architecture Diagram
**Description**: Design system architecture
**Input**: Requirements, components
**Output**: Architecture diagram

```yaml
skill:
  name: create_architecture_diagram
  description: "Create system architecture diagram"
  inputs:
    - requirements: array
    - components: array
  outputs:
    - diagram: string
  logic: |
    1. Identify components
    2. Define relationships
    3. Show data flow
    4. Generate visual diagram
```

---

## ✅ Assessment Grader Skills

### Skill: Run Tests
**Description**: Execute test cases against submission
**Input**: Code, test cases
**Output**: Test results

```yaml
skill:
  name: run_tests
  description: "Execute test suite"
  inputs:
    - code: string
    - tests: string
    - language: string
  outputs:
    - results: object
  logic: |
    1. Parse code and tests
    2. Execute test suite
    3. Capture pass/fail
    4. Record errors
    5. Calculate score
```

### Skill: Analyze Code Quality
**Description**: Check code style and structure
**Input**: Code, language
**Output**: Quality report

```yaml
skill:
  name: analyze_code_quality
  description: "Analyze code quality"
  inputs:
    - code: string
    - language: string
  outputs:
    - quality_report: object
  logic: |
    1. Check style compliance
    2. Analyze complexity
    3. Check for duplication
    4. Verify naming conventions
    5. Generate report
```

### Skill: Generate Feedback
**Description**: Create detailed feedback report
**Input**: Test results, quality analysis
**Output**: Feedback markdown

```yaml
skill:
  name: generate_feedback
  description: "Generate detailed feedback"
  inputs:
    - test_results: object
    - quality_analysis: object
    - rubric: object
  outputs:
    - feedback: markdown
  logic: |
    1. Calculate overall score
    2. Identify strengths
    3. List areas for improvement
    4. Provide specific suggestions
    5. Recommend next steps
```

### Skill: Update Competencies
**Description**: Update skill scores based on performance
**Input**: Assessment results
**Output**: Updated competencies

```yaml
skill:
  name: update_competencies
  description: "Update competency scores"
  inputs:
    - assessment_results: object
    - current_competencies: object
  outputs:
    - updated_competencies: object
  logic: |
    1. Map assessment to skills
    2. Calculate score changes
    3. Apply to competencies
    4. Track evidence
```

---

## 🧑‍🏫 Mentor Agent Skills

### Skill: Generate Hint
**Description**: Create progressive hints without solutions
**Input**: Problem, student attempts
**Output**: Hint (level-appropriate)

```yaml
skill:
  name: generate_hint
  description: "Generate helpful hint"
  inputs:
    - problem: object
    - student_attempts: array
    - hint_level: number
  outputs:
    - hint: string
  logic: |
    1. Analyze what student has tried
    2. Identify knowledge gap
    3. Create hint at appropriate level
    4. Avoid giving solution
    5. Include guiding question
```

### Skill: Explain Concept
**Description**: Clarify concepts with analogies
**Input**: Concept, student confusion
**Output**: Explanation

```yaml
skill:
  name: explain_concept
  description: "Explain concept clearly"
  inputs:
    - concept: string
    - student_confusion: string
  outputs:
    - explanation: markdown
  logic: |
    1. Identify core confusion
    2. Create real-world analogy
    3. Provide simple example
    4. Build to complex case
    5. Check understanding
```

### Skill: Debug Guidance
**Description**: Help identify bugs without fixing
**Input**: Code, error
**Output**: Debugging steps

```yaml
skill:
  name: debug_guidance
  description: "Guide debugging process"
  inputs:
    - code: string
    - error: string
  outputs:
    - debug_steps: array
  logic: |
    1. Analyze error message
    2. Identify likely cause
    3. Suggest debugging steps
    4. Provide print statements
    5. Guide toward solution
```

### Skill: Encourage
**Description**: Provide positive reinforcement
**Input**: Student frustration
**Output**: Encouragement

```yaml
skill:
  name: encourage
  description: "Provide encouragement"
  inputs:
    - frustration_level: string
    - progress_made: string
  outputs:
    - encouragement: string
  logic: |
    1. Acknowledge difficulty
    2. Highlight progress
    3. Normalize struggle
    4. Provide motivation
    5. Suggest next step
```

### Skill: Research YouTube Videos
**Description**: Find and recommend relevant YouTube tutorials for visual learners
**Input**: topic, difficulty, learning_style
**Output**: Curated list of video recommendations

```yaml
skill:
  name: research_youtube_videos
  description: "Find and recommend relevant YouTube video tutorials"
  inputs:
    - topic: string
    - difficulty: string
    - learning_style: "visual" | "auditory" | "kinesthetic"
  outputs:
    - videos: array
    - recommended_order: array
    - why_recommended: string
  logic: |
    1. Identify topic keywords
    2. Search for relevant video tutorials
    3. Categorize by difficulty and style
    4. Order by learning progression
    5. Add recommendations and context
```

### Skill: Explain with Analogy
**Description**: Use real-world analogies to simplify complex concepts
**Input**: concept, student_confusion
**Output**: Analogy-based explanation

```yaml
skill:
  name: explain_with_analogy
  description: "Explain complex concepts using real-world analogies"
  inputs:
    - concept: string
    - student_confusion: string
  outputs:
    - analogy: string
    - explanation: markdown
    - visual_representation: string
  logic: |
    1. Identify the core concept
    2. Find relatable real-world parallel
    3. Map concept elements to analogy
    4. Create visual representation
    5. Connect analogy back to code
```

### Skill: Break Down Complex Concept
**Description**: Decompose complicated topics into digestible steps
**Input**: complex_concept, student_level
**Output**: Step-by-step breakdown with checkpoints

```yaml
skill:
  name: break_down_complex_concept
  description: "Decompose complex topics into manageable learning steps"
  inputs:
    - complex_concept: string
    - student_level: string
  outputs:
    - steps: array
    - checkpoints: array
    - estimated_time: string
    - prerequisites: array
  logic: |
    1. Identify all sub-concepts
    2. Order by dependency
    3. Create progressive steps
    4. Add comprehension checkpoints
    5. Estimate time for each step
    6. Include practice after each step
```

### Skill: Provide Detailed Guidance
**Description**: Offer comprehensive, in-depth help and step-by-step walkthroughs
**Input**: topic, depth_level, student_context
**Output**: Detailed explanation with examples and practice

```yaml
skill:
  name: provide_detailed_guidance
  description: "Provide comprehensive, detailed help and step-by-step guidance"
  inputs:
    - topic: string
    - depth_level: "quick" | "guided" | "deep_dive"
    - student_context: object
  outputs:
    - detailed_explanation: markdown
    - worked_examples: array
    - practice_exercises: array
    - related_resources: array
  logic: |
    1. Assess student's current understanding
    2. Choose appropriate depth level
    3. Build comprehensive explanation
    4. Include multiple examples
    5. Add practice exercises
    6. Link to related resources
```

---

## 🔬 Repository Analysis Skills (from github_repo_to_curriculum_generator.py)

### Skill: Repository Code Analyzer
**Description**: Analyzes GitHub repositories to extract structure, concepts, and key files
**Input**: repo_owner, repo_name, github_token (optional)
**Output**: Concepts array, key files, language, dependency graph

```yaml
skill:
  name: analyze_github_repo
  description: "Analyze GitHub repository structure and extract educational concepts"
  inputs:
    - repo_owner: string
    - repo_name: string
    - github_token: string (optional)
  outputs:
    - main_concepts: array[CodeConcept]
    - key_files: array[string]
    - language: string
    - dependency_graph: object
  implementation: |
    1. Initialize GitHubRepoAnalyzer(token)
    2. Call _fetch_repo_metadata(owner, repo_name)
    3. Call _get_repo_file_tree(owner, repo_name, branch)
    4. Call _identify_key_files(files)
    5. Call _extract_main_concepts(owner, repo_name, key_files)
    6. Call _build_dependency_graph(concepts)
    7. Return RepoAnalysis object
  code_example: |
    analyzer = GitHubRepoAnalyzer(token=GITHUB_TOKEN)
    repo_analysis = analyzer.analyze_repository("pytorch", "pytorch")
    # Returns: RepoAnalysis with concepts, key_files, dependency_graph
```

### Skill: Code Concept Extractor
**Description**: Extracts programming concepts from repository code files
**Input**: owner, repo_name, key_files
**Output**: List of CodeConcept objects

```yaml
skill:
  name: extract_code_concepts
  description: "Parse code files to extract classes, functions, and patterns"
  inputs:
    - owner: string
    - repo_name: string
    - key_files: array[string]
  outputs:
    - concepts: array[CodeConcept]
  implementation: |
    1. For each key_file (top 5):
       a. Call _fetch_file_content(owner, repo_name, file_path)
       b. Call _parse_code_concepts(content, file_path)
       c. Extract language via _detect_language(file_path)
       d. Call language-specific extractor (_extract_python_concepts, etc.)
    2. Deduplicate concepts by name
    3. Return top 10 concepts
  code_example: |
    concepts = analyzer._extract_main_concepts("pytorch", "pytorch", [
        "torch/__init__.py",
        "torch/nn/__init__.py",
        "torch/optim/__init__.py"
    ])
```

---

## 📚 Enhanced Lesson Generator Skills

### Skill: Lesson Content Generator
**Description**: Generates structured lessons with concepts, code examples, and explanations
**Input**: concept, difficulty_level, repository_context
**Output**: Lesson title, content, code examples, key takeaways

```yaml
skill:
  name: generate_lesson_content
  description: "Create detailed lesson content with line-by-line explanations"
  inputs:
    - concept: CodeConcept
    - difficulty_level: "foundation" | "intermediate" | "advanced"
    - repository_context: RepoAnalysis
  outputs:
    - lesson_title: string
    - content: string
    - code_examples: array
    - key_takeaways: array
    - resources: array
  implementation: |
    1. Call _generate_lesson_title(level, concept)
    2. Call _generate_lesson_concepts(concept, level)
    3. Call _generate_lesson_content(concept, level)
    4. Call _generate_code_walkthrough(concept)
    5. Call _generate_key_takeaways(concept)
    6. Call _generate_lesson_resources(concept)
    7. Return assembled lesson object
  code_example: |
    lesson = generator._generate_lesson(
        topic_id="unit_01_topic_01",
        lesson_index=0,
        topic_name="Array Fundamentals",
        difficulty=DifficultyLevel.BEGINNER
    )
    # Returns: Lesson with notes, code_examples, key_concepts, learning_objectives
```

### Skill: Key Takeaway Generator
**Description**: Generates key takeaways for a concept
**Input**: concept (CodeConcept)
**Output**: List of takeaway strings

```python
def _generate_key_takeaways(self, concept: CodeConcept) -> List[str]:
    """Generate key takeaways for a concept."""
    return [
        f"{concept.name} is {concept.description}",
        f"It's located in: {concept.file_path}",
        f"Complexity level: {concept.complexity}/5",
        "It's used throughout the codebase in multiple contexts",
        "Mastering this concept is crucial for contributing to the project"
    ]
```

### Skill: Lesson Resource Generator
**Description**: Generates lesson resources linking to repository files
**Input**: concept (CodeConcept)
**Output**: List of resource dictionaries

```python
def _generate_lesson_resources(self, concept: CodeConcept) -> List[Dict[str, str]]:
    """Generate lesson resources."""
    return [
        {
            "type": "github_file",
            "title": f"View in repository: {concept.file_path}",
            "url": f"{self.repo.repo_url}/blob/main/{concept.file_path}"
        },
        {
            "type": "documentation",
            "title": "Official Repository README",
            "url": f"{self.repo.repo_url}"
        }
    ]
```

---

## 🧩 Enhanced Problem Creator Skills

### Skill: Problem Title Generator
**Description**: Generates problem titles based on level and concept
**Input**: level, concept
**Output**: Problem title string

```python
def _generate_problem_title(self, level: str, concept: CodeConcept) -> str:
    """Generate problem title."""
    titles = {
        "foundation": f"Practice: Implement basic {concept.name}",
        "intermediate": f"Build: Create a {concept.name} component",
        "advanced": f"Challenge: Optimize {concept.name} for performance"
    }
    return titles.get(level, f"Problem: {concept.name}")
```

### Skill: Problem Description Generator
**Description**: Generates problem descriptions with context and requirements
**Input**: concept, level, repository_name
**Output**: Formatted problem description

```python
def _generate_problem_description(
    self, concept: CodeConcept, level: str
) -> str:
    """Generate problem description."""
    return f"""
Write a program that demonstrates understanding of {concept.name}.

Context: {concept.description}

Your Task:
1. Understand how {concept.name} works
2. Implement the required functionality
3. Ensure your code follows the patterns used in {self.repo.repo_name}
4. Test your implementation thoroughly

Success Criteria:
- Code runs without errors
- Functionality matches requirements
- Code follows project conventions
- All tests pass
"""
```

### Skill: Starter Code Generator
**Description**: Generates starter code templates for problems
**Input**: concept (CodeConcept)
**Output**: Starter code string

```python
def _generate_starter_code(self, concept: CodeConcept) -> str:
    """Generate starter code template."""
    return f"""
# TODO: Implement {concept.name}

class {concept.name}:
    \"\"\"Implementation of {concept.name}.\"\"\"
    
    def __init__(self):
        # Initialize state
        pass
    
    def process(self, data):
        \"\"\"Process data using {concept.name}.\"\"\"
        # TODO: Implement
        pass

# Test your implementation:
if __name__ == "__main__":
    obj = {concept.name}()
    result = obj.process([1, 2, 3])
    print(result)
"""
```

### Skill: Acceptance Criteria Generator
**Description**: Generates acceptance criteria for problems
**Input**: concept, level
**Output**: List of acceptance criteria strings

```python
def _generate_acceptance_criteria(
    self, concept: CodeConcept, level: str
) -> List[str]:
    """Generate acceptance criteria."""
    return [
        "Implementation uses correct algorithms and patterns",
        "Code handles edge cases appropriately",
        "All tests pass successfully",
        "Code follows project style guidelines",
        "Implementation matches expected behavior",
        "Documentation is clear and complete"
    ]
```

### Skill: Solution Outline Generator
**Description**: Generates solution outlines for problems
**Input**: concept, level
**Output**: Formatted solution outline

```python
def _generate_solution_outline(
    self, concept: CodeConcept, level: str
) -> str:
    """Generate solution outline."""
    return f"""
## Solution Outline for {concept.name}

### Approach
1. Analyze the problem requirements
2. Design your solution using {concept.name}
3. Implement step by step
4. Test with provided examples
5. Optimize if needed

### Key Steps
1. Create the main class/function
2. Implement core logic
3. Add error handling
4. Write comprehensive tests
5. Document your code

### Reference Implementation
Check {concept.file_path} in the actual repository for guidance
on how {concept.name} is implemented in production code.
"""
```

### Skill: Hints Generator
**Description**: Generates hints for problems
**Input**: concept, level
**Output**: List of hint strings

```python
def _generate_hints(self, concept: CodeConcept, level: str) -> List[str]:
    """Generate problem hints."""
    return [
        f"Review the lesson on {concept.name}",
        f"Look at how {concept.name} is used in {concept.file_path}",
        "Start with a simple version, then add complexity",
        "Test your solution with multiple inputs",
        "Compare your solution with the reference implementation"
    ]
```

---

## 🎓 Enhanced Quiz Generator Skills

### Skill: Question Text Generator
**Description**: Generates quiz question text
**Input**: concept, level
**Output**: Question text string

```python
def _generate_question_text(
    self, concept: CodeConcept, level: str
) -> str:
    """Generate quiz question."""
    return f"What is the primary purpose of {concept.name} in {self.repo.repo_name}?"
```

### Skill: Question Options Generator
**Description**: Generates multiple choice options
**Input**: concept, index
**Output**: List of option strings

```python
def _generate_question_options(
    self, concept: CodeConcept, index: int
) -> List[str]:
    """Generate multiple choice options."""
    return [
        "Option A: Correct answer",
        "Option B: Common misconception 1",
        "Option C: Common misconception 2",
        "Option D: Distractor"
    ]
```

### Skill: Question Explanation Generator
**Description**: Generates explanations for quiz answers
**Input**: concept (CodeConcept)
**Output**: Explanation string

```python
def _generate_question_explanation(self, concept: CodeConcept) -> str:
    """Generate question explanation."""
    return f"""
{concept.name} is used for: {concept.description}

This is a core concept in {self.repo.repo_name} that appears in multiple
places throughout the codebase. Understanding it is essential for making
meaningful contributions to the project.
"""
```

---

## 🎯 Module Outcome Generator Skills

### Skill: Module Outcome Generator
**Description**: Generates learning outcomes for modules
**Input**: level (string)
**Output**: Outcome description string

```python
def _generate_module_outcome(self, level: str) -> str:
    """Generate module learning outcome."""
    outcomes = {
        "foundation": "You'll understand the basic concepts needed to read and understand the codebase",
        "intermediate": "You'll be able to apply these concepts to solve real problems",
        "advanced": "You'll have deep knowledge and can optimize and improve implementations",
        "capstone": "You'll make your first meaningful contribution to the open-source project"
    }
    return outcomes.get(level, "You'll gain practical experience")
```

---

## 🚀 Enhanced Project Generator Skills

### Skill: Project Description Generator
**Description**: Generates capstone project descriptions
**Input**: repository (RepoAnalysis)
**Output**: Formatted project description

```python
def _generate_project_description(self) -> str:
    """Generate capstone project description."""
    return f"""
In this capstone project, you'll contribute directly to {self.repo.repo_name}.

You've learned the key concepts and patterns. Now it's time to apply that
knowledge to make a real impact on an actual open-source project.

What You'll Do:
1. Find an issue or feature to work on
2. Fork the repository and create a feature branch
3. Implement your solution following project conventions
4. Write tests and documentation
5. Submit a pull request
6. Respond to code review feedback
7. See your contribution merged into the main codebase

Why This Matters:
- Real-world experience contributing to open source
- Builds portfolio credentials
- Learn from expert code reviewers
- Become part of a community
"""
```

### Skill: Project Requirements Generator
**Description**: Generates project requirements
**Input**: repository (RepoAnalysis)
**Output**: List of requirement strings

```python
def _generate_project_requirements(self) -> List[str]:
    """Generate project requirements."""
    return [
        f"Must be a valid contribution to {self.repo.repo_name}",
        "Complete all acceptance criteria",
        "Write unit tests (minimum 90% code coverage)",
        "Document your code with docstrings/comments",
        "Follow the project's code style and conventions",
        "Create a detailed pull request description",
        "Respond professionally to all code review comments",
        "Successfully merge your PR into the repository"
    ]
```

### Skill: Example Tasks Generator
**Description**: Generates example tasks for capstone projects
**Input**: None (uses self.repo)
**Output**: List of example task strings

```python
def _generate_example_tasks(self) -> List[str]:
    """Generate example tasks for capstone."""
    return [
        "Fix a bug from the project's issue tracker",
        "Implement a new feature request",
        "Add missing tests or improve test coverage",
        "Improve documentation or add examples",
        "Optimize performance in a critical section",
        "Refactor code to improve maintainability"
    ]
```

### Skill: Getting Started Guide Generator
**Description**: Generates getting started guide for projects
**Input**: repository (RepoAnalysis)
**Output**: Dictionary of step descriptions

```python
def _generate_getting_started_guide(self) -> Dict[str, str]:
    """Generate getting started guide."""
    return {
        "step_1": f"Clone the repository: git clone {self.repo.repo_url}.git",
        "step_2": "Create a feature branch: git checkout -b feature/your-feature-name",
        "step_3": "Set up the development environment following the repository's README",
        "step_4": "Find an issue to work on in the GitHub Issues",
        "step_5": "Implement your solution",
        "step_6": "Write tests and documentation",
        "step_7": "Push your branch and create a pull request",
        "step_8": "Respond to review feedback",
        "step_9": "Celebrate your contribution!"
    }
```

---

## 🤖 AI Agent Skill Factory

### Class: AIAgentSkillFactory
**Description**: Creates reusable AI agent skills for curriculum generation

```python
class AIAgentSkillFactory:
    """Creates reusable AI agent skills for curriculum generation."""

    @staticmethod
    def create_skills_from_curriculum(
        curriculum: Dict[str, Any]
    ) -> List[AIAgentSkill]:
        """Create AI agent skills from curriculum."""
        skills = [
            AIAgentSkill(
                skill_id="skill_repo_analyzer",
                skill_name="Repository Code Analyzer",
                description="Analyzes GitHub repositories to extract structure, concepts, and key files",
                input_schema={
                    "type": "object",
                    "properties": {
                        "repo_owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                        "github_token": {"type": "string", "optional": True}
                    }
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "main_concepts": {"type": "array"},
                        "key_files": {"type": "array"},
                        "language": {"type": "string"},
                        "dependency_graph": {"type": "object"}
                    }
                },
                dependencies=[],
                llm_prompt_template="""Analyze the following repository structure and concepts.
Extract key programming patterns and educational value: {repo_analysis}"""
            ),
            AIAgentSkill(
                skill_id="skill_lesson_generator",
                skill_name="Lesson Content Generator",
                description="Generates structured lessons with concepts, code examples, and explanations",
                input_schema={
                    "type": "object",
                    "properties": {
                        "concept": {"type": "object"},
                        "difficulty_level": {"type": "string"},
                        "repository_context": {"type": "object"}
                    }
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "lesson_title": {"type": "string"},
                        "content": {"type": "string"},
                        "code_examples": {"type": "array"},
                        "key_takeaways": {"type": "array"}
                    }
                },
                dependencies=["skill_repo_analyzer"],
                llm_prompt_template="""Generate an educational lesson about {concept}
for {difficulty_level} learners. Use these code examples as reference:
{code_snippets} Context: {repo_context}"""
            ),
            AIAgentSkill(
                skill_id="skill_problem_generator",
                skill_name="Practice Problem Generator",
                description="Generates practice problems with acceptance criteria and solution hints",
                input_schema={
                    "type": "object",
                    "properties": {
                        "concept": {"type": "object"},
                        "difficulty": {"type": "string"},
                        "num_problems": {"type": "integer"}
                    }
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "problems": {"type": "array"},
                        "starter_code": {"type": "string"},
                        "test_cases": {"type": "array"}
                    }
                },
                dependencies=["skill_lesson_generator"],
                llm_prompt_template="""Create {num_problems} practice problems for
{concept} at {difficulty} level. Include acceptance criteria, starter code, and hints."""
            ),
            AIAgentSkill(
                skill_id="skill_quiz_generator",
                skill_name="Quiz Question Generator",
                description="Generates assessment questions with multiple question types and explanations",
                input_schema={
                    "type": "object",
                    "properties": {
                        "module_content": {"type": "object"},
                        "num_questions": {"type": "integer"},
                        "question_types": {"type": "array"}
                    }
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "questions": {"type": "array"},
                        "answer_key": {"type": "object"},
                        "difficulty_distribution": {"type": "object"}
                    }
                },
                dependencies=["skill_lesson_generator"],
                llm_prompt_template="""Generate {num_questions} quiz questions about
the following content: {module_content}
Include question types: {question_types}
Ensure questions test deep understanding, not just memorization."""
            ),
            AIAgentSkill(
                skill_id="skill_project_generator",
                skill_name="Capstone Project Synthesizer",
                description="Generates capstone project specifications that guide real-world contribution",
                input_schema={
                    "type": "object",
                    "properties": {
                        "repository": {"type": "object"},
                        "learned_concepts": {"type": "array"},
                        "target_difficulty": {"type": "string"}
                    }
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "project_title": {"type": "string"},
                        "objectives": {"type": "array"},
                        "requirements": {"type": "array"},
                        "deliverables": {"type": "array"},
                        "example_tasks": {"type": "array"}
                    }
                },
                dependencies=[
                    "skill_repo_analyzer",
                    "skill_lesson_generator",
                    "skill_problem_generator"
                ],
                llm_prompt_template="""Create a capstone project specification for {repository}.
The learner has mastered: {learned_concepts}
Project should: Integrate all learned concepts, be valuable to the repository, guide real contribution."""
            )
        ]
        return skills
```

---

## 📋 Skill Usage Rules

### When to Use Each Skill

| Situation | Agent | Skill |
|-----------|-------|-------|
| Student wants to learn topic | Orchestrator | route_request |
| Design new module | Curriculum Architect | design_module |
| Create lesson content | Lesson Generator | generate_lesson |
| Need practice problems | Problem Creator | create_exercise |
| Build project | Project Designer | design_project |
| Grade submission | Assessment Grader | run_tests, generate_feedback |
| Student stuck | Mentor Agent | generate_hint, explain_concept |
| Update progress | Orchestrator | update_state |
| **Analyze GitHub repo** | **Curriculum Architect** | **analyze_github_repo** |
| **Extract code concepts** | **Lesson Generator** | **extract_code_concepts** |
| **Generate curriculum from repo** | **Curriculum Architect** | **generate_curriculum_from_repo** |
| **Create capstone from repo** | **Project Designer** | **design_project_from_repo** |
| **Generate progressive problems** | **Problem Creator** | **generate_progressive_problems** |
| **Create quiz from content** | **Problem Creator** | **create_quiz_from_content** |
| **Generate answer key** | **Assessment Grader** | **generate_answer_key** |

### Skill Composition

Agents can combine skills:
```
Orchestrator:
  1. route_request → Curriculum Architect
  2. Curriculum Architect.design_module → Lesson Generator
  3. Lesson Generator.generate_lesson → Problem Creator
  4. Problem Creator.create_exercise → Return to student
  5. Student completes → Assessment Grader.run_tests
  6. Assessment Grader.generate_feedback → Student
  7. Orchestrator.update_state → Complete

GitHub-Based Curriculum Flow:
  1. Curriculum Architect.analyze_github_repo → Extract concepts
  2. Lesson Generator.generate_lesson_content → Create lessons
  3. Problem Creator.generate_progressive_problems → Create exercises
  4. Problem Creator.create_quiz_from_content → Create assessment
  5. Project Designer.design_project_from_repo → Create capstone
```


---

## 📚 Textbook Writer Skills

### Skill: Gap Analysis
**Description**: Analyzes lesson skeleton to identify missing educational elements
**Input**: lesson_skeleton, difficulty_level
**Output**: enrichment_plan with priorities

```yaml
skill:
  name: analyze_lesson_gaps
  description: "Identify what educational elements are missing from a lesson skeleton"
  inputs:
    - lesson_skeleton: object
    - difficulty_level: string
  outputs:
    - enrichment_plan: object
    - priority_areas: array
  logic: |
    1. Check narrative depth for each concept
    2. Identify missing visual aids
    3. Assess example quality and completeness
    4. Check for real-world context
    5. Verify reference material presence
    6. Create prioritized enrichment plan
```

### Skill: Generate Chapter Narrative
**Description**: Creates detailed narrative explanations for concepts
**Input**: concept, difficulty_level, context
**Output**: Full chapter with narrative, analogies, and explanations

```yaml
skill:
  name: generate_chapter_narrative
  description: "Write detailed narrative sections explaining concepts"
  inputs:
    - concept: object
    - difficulty_level: string
    - student_context: object
  outputs:
    - chapter_content: markdown
    - analogies: array
    - misconceptions: array
  logic: |
    1. Identify the core concept
    2. Create engaging hook/motivation
    3. Develop real-world analogies
    4. Write progressive explanation (simple to complex)
    5. Address common misconceptions
    6. Add checkpoint questions
```

### Skill: Create Step-by-Step Tutorial
**Description**: Builds hands-on guided walkthroughs
**Input**: concept, code_examples, difficulty
**Output**: Tutorial with progressive steps and practice points

```yaml
skill:
  name: create_step_by_step_tutorial
  description: "Build guided coding tutorials with explanations"
  inputs:
    - concept: object
    - code_examples: array
    - difficulty: string
  outputs:
    - tutorial: markdown
    - checkpoints: array
    - practice_challenges: array
  logic: |
    1. Create setup instructions
    2. Break code into logical steps
    3. Add explanations for each step
    4. Include "Try It Yourself" moments
    5. Provide hints for challenges
    6. Add troubleshooting guidance
```

### Skill: Generate Diagrams
**Description**: Creates visual aids for complex concepts
**Input**: concept, diagram_type, complexity
**Output**: ASCII or Mermaid diagram with description

```yaml
skill:
  name: generate_diagrams
  description: "Create visual representations of concepts"
  inputs:
    - concept: object
    - diagram_type: "flow" | "comparison" | "hierarchy" | "sequence"
    - complexity: string
  outputs:
    - diagram: string
    - format: "ascii" | "mermaid"
    - description: string
  logic: |
    1. Identify key components to visualize
    2. Choose appropriate diagram type
    3. Generate ASCII art or Mermaid syntax
    4. Add clear labels
    5. Write description explaining the diagram
```

### Skill: Add Real-World Context
**Description**: Includes industry examples and case studies
**Input**: concept, domain
**Output**: Case studies, industry patterns, production examples

```yaml
skill:
  name: add_real_world_context
  description: "Add practical industry context and examples"
  inputs:
    - concept: object
    - domain: string
  outputs:
    - case_studies: array
    - industry_patterns: array
    - performance_notes: string
  logic: |
    1. Research real-world usage of concept
    2. Find relevant company/project examples
    3. Identify industry best practices
    4. Note performance considerations
    5. Add scaling considerations
```

### Skill: Create Reference Material
**Description**: Generates cheat sheets, glossaries, and quick references
**Input**: concept, patterns, terminology
**Output**: Reference sections for the lesson

```yaml
skill:
  name: create_reference_material
  description: "Generate quick reference materials"
  inputs:
    - concept: object
    - patterns: array
    - terminology: array
  outputs:
    - cheat_sheet: string
    - glossary: array
    - common_patterns: array
    - debugging_checklist: array
  logic: |
    1. Extract key syntax and patterns
    2. Create concise cheat sheet
    3. Define all terminology
    4. List common usage patterns
    5. Create debugging checklist
```

### Skill: Generate Learning Path
**Description**: Structures content with checkpoints and knowledge checks
**Input**: concepts, difficulty, duration
**Output**: Structured learning progression

```yaml
skill:
  name: generate_learning_path
  description: "Create structured learning progression with checkpoints"
  inputs:
    - concepts: array
    - difficulty: string
    - duration: string
  outputs:
    - learning_path: array
    - checkpoints: array
    - self_assessment: array
  logic: |
    1. Order concepts logically
    2. Add prerequisite connections
    3. Create checkpoint questions
    4. Build self-assessment criteria
    5. Connect to next lesson
```

### Skill: Add Source Citations
**Description**: Includes authoritative references and further reading
**Input**: concept, domain
**Output**: Curated list of sources and resources

```yaml
skill:
  name: add_source_citations
  description: "Add authoritative references and learning resources"
  inputs:
    - concept: object
    - domain: string
  outputs:
    - official_docs: array
    - recommended_reading: array
    - video_tutorials: array
    - community_resources: array
  logic: |
    1. Find official documentation links
    2. Curate relevant books/articles
    3. Find quality video tutorials
    4. Identify community resources
    5. Verify all links are current
```

### Skill: Create Worked Examples
**Description**: Builds fully-commented step-by-step code walkthroughs
**Input**: code_example, difficulty, concept
**Output**: Line-by-line explained code examples

```yaml
skill:
  name: create_worked_examples
  description: "Create detailed code walkthroughs with explanations"
  inputs:
    - code_example: string
    - difficulty: string
    - concept: object
  outputs:
    - worked_example: object
    - line_explanations: array
    - key_insights: array
  logic: |
    1. Start with simplest case
    2. Add detailed comments to every line
    3. Explain what each part does
    4. Build to more complex example
    5. Highlight best practices
    6. Show edge cases
```

---

**Skills Version**: 2.2  
**Last Updated**: March 2026  
**New Skills Added**: 28 (15 repository-based + 9 Textbook Writer + 4 Mentor Agent)
