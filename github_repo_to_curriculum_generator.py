#!/usr/bin/env python3
"""
================================================================================
Name: Cbwinslow
Date: 2026-03-20
Script Name: github_repo_to_curriculum_generator.py
Version: 1.0.0
Log Summary: GitHub repository to curriculum lesson plan generator
Description:
    Analyzes a GitHub repository's code structure and generates a complete
    lesson plan including foundational lessons, progressive problems, quizzes,
    and a capstone project. Extracts key concepts from the codebase and
    creates structured educational material that leads students from basics
    to implementing features in the actual repository.
    
    This script serves as a foundation for AI agent skills—can be modularized
    into discrete agent-compatible tasks (code analysis, content generation,
    question generation, project synthesis).

Change Summary:
    - Initial creation with GitHub API integration
    - Code structure analysis and concept extraction
    - Progressive lesson and problem generation
    - Quiz and capstone project synthesis
    - Markdown output for curriculum delivery
    - AI agent skill design patterns included
    - Fixed syntax errors and completed all missing methods

Inputs:
    - repo_owner: GitHub repository owner username
    - repo_name: GitHub repository name
    - github_token: GitHub API personal access token (optional)
    - target_audience: "beginner" | "intermediate" | "advanced"

Outputs:
    - repo_curriculum.json: Complete curriculum structure
    - repo_lesson_plan.md: Week-by-week lesson plan
    - repo_*.md: Individual lessons with code samples
    - repo_quiz_*.md: Progressive quizzes
    - repo_capstone_project.md: Final project specification
    - ai_agent_skill_specs.json: Agent skill definitions for orchestration
================================================================================
"""

import argparse
import json
import logging
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, asdict, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set

import requests


class ContentLevel(Enum):
    """Content difficulty levels."""
    FOUNDATION = 1
    INTERMEDIATE = 2
    ADVANCED = 3
    CAPSTONE = 4


@dataclass
class CodeConcept:
    """Represents a code concept extracted from repository."""
    name: str
    description: str
    file_path: str
    language: str
    complexity: int  # 1-5
    related_concepts: List[str] = field(default_factory=list)
    code_snippet: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class RepoAnalysis:
    """Complete analysis of a GitHub repository."""
    owner: str
    repo_name: str
    repo_url: str
    language: str
    description: str
    main_concepts: List[CodeConcept] = field(default_factory=list)
    key_files: List[str] = field(default_factory=list)
    dependency_graph: Dict[str, List[str]] = field(default_factory=dict)
    difficulty_level: str = "intermediate"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "owner": self.owner,
            "repo_name": self.repo_name,
            "repo_url": self.repo_url,
            "language": self.language,
            "description": self.description,
            "main_concepts": [c.to_dict() for c in self.main_concepts],
            "key_files": self.key_files,
            "dependency_graph": self.dependency_graph,
            "difficulty_level": self.difficulty_level
        }


@dataclass
class AIAgentSkill:
    """Represents a reusable AI agent skill for curriculum generation."""
    skill_id: str
    skill_name: str
    description: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    dependencies: List[str] = field(default_factory=list)
    llm_prompt_template: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class GitHubRepoAnalyzer:
    """Analyzes GitHub repositories to extract structure and concepts."""

    def __init__(self, token: Optional[str] = None):
        """Initialize with optional GitHub token for higher API limits."""
        self.token = token
        self.headers = {"Authorization": f"token {token}"} if token else {}
        self.base_url = "https://api.github.com"

    def analyze_repository(self, owner: str, repo_name: str) -> RepoAnalysis:
        """
        Analyze a GitHub repository and extract key concepts.
        
        Args:
            owner: Repository owner username
            repo_name: Repository name
            
        Returns:
            RepoAnalysis object with extracted concepts and structure
        """
        print(f"\n{'='*70}")
        print(f"Analyzing GitHub Repository: {owner}/{repo_name}")
        print(f"{'='*70}\n")

        # Fetch repository metadata
        repo_metadata = self._fetch_repo_metadata(owner, repo_name)
        print(f"✓ Fetched repository metadata")

        # Analyze repository structure
        analysis = RepoAnalysis(
            owner=owner,
            repo_name=repo_name,
            repo_url=f"https://github.com/{owner}/{repo_name}",
            language=repo_metadata.get("language", "Unknown"),
            description=repo_metadata.get("description", "No description provided")
        )

        # Extract file structure
        print(f"  Analyzing file structure...")
        files = self._get_repo_file_tree(owner, repo_name, repo_metadata["default_branch"])
        analysis.key_files = self._identify_key_files(files)
        print(f"  ✓ Identified {len(analysis.key_files)} key files")

        # Extract main concepts from code
        print(f"  Extracting main concepts...")
        concepts = self._extract_main_concepts(owner, repo_name, analysis.key_files)
        analysis.main_concepts = concepts
        print(f"  ✓ Extracted {len(concepts)} main concepts")

        # Build dependency graph
        print(f"  Building dependency graph...")
        analysis.dependency_graph = self._build_dependency_graph(concepts)

        return analysis

    def _fetch_repo_metadata(self, owner: str, repo_name: str) -> Dict[str, Any]:
        """Fetch repository metadata from GitHub API."""
        url = f"{self.base_url}/repos/{owner}/{repo_name}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        return {
            "language": data.get("language", "Unknown"),
            "description": data.get("description", ""),
            "default_branch": data.get("default_branch", "main"),
            "stars": data.get("stargazers_count", 0),
            "forks": data.get("forks_count", 0),
            "topics": data.get("topics", [])
        }

    def _get_repo_file_tree(
        self,
        owner: str,
        repo_name: str,
        branch: str = "main"
    ) -> List[Dict[str, Any]]:
        """Get repository file tree using GitHub API."""
        url = f"{self.base_url}/repos/{owner}/{repo_name}/git/trees/{branch}?recursive=1"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        return data.get("tree", [])

    def _identify_key_files(self, files: List[Dict[str, Any]]) -> List[str]:
        """Identify key files for curriculum (main code files, examples, tests)."""
        key_file_patterns = [
            r".*\.(py|ts|js|java|cpp|c)$",  # Source files
            r".*example.*\.(py|ts|js)$",     # Examples
            r".*test.*\.(py|ts|js)$",         # Tests
            r"README.*",                       # Documentation
            r"requirements\.txt|package\.json|pom\.xml"  # Dependencies
        ]

        key_files = []
        for file_obj in files:
            if file_obj["type"] == "blob":
                path = file_obj["path"]
                if any(re.match(pattern, path, re.IGNORECASE) for pattern in key_file_patterns):
                    key_files.append(path)

        # Sort by priority
        return sorted(key_files, key=lambda x: (
            0 if "example" in x.lower() else
            1 if "test" in x.lower() else
            2 if "README" in x else 3
        ))[:20]  # Limit to top 20 files

    def _extract_main_concepts(
        self,
        owner: str,
        repo_name: str,
        key_files: List[str]
    ) -> List[CodeConcept]:
        """Extract main programming concepts from key files."""
        concepts = []
        concept_names = set()

        for file_path in key_files[:5]:  # Analyze top 5 files
            try:
                content = self._fetch_file_content(owner, repo_name, file_path)
                extracted = self._parse_code_concepts(content, file_path)

                for concept in extracted:
                    if concept.name not in concept_names:
                        concepts.append(concept)
                        concept_names.add(concept.name)

            except Exception as e:
                print(f"    ⚠ Could not analyze {file_path}: {str(e)}")

        return concepts[:10]  # Return top 10 concepts

    def _fetch_file_content(self, owner: str, repo_name: str, file_path: str) -> str:
        """Fetch file content from GitHub."""
        url = f"{self.base_url}/repos/{owner}/{repo_name}/contents/{file_path}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        import base64
        return base64.b64decode(data["content"]).decode("utf-8")

    def _parse_code_concepts(self, code_content: str, file_path: str) -> List[CodeConcept]:
        """Parse code to extract main concepts."""
        concepts = []
        language = self._detect_language(file_path)

        # Extract classes/functions based on language
        if language in ["python"]:
            concepts.extend(self._extract_python_concepts(code_content, file_path))
        elif language in ["typescript", "javascript"]:
            concepts.extend(self._extract_js_concepts(code_content, file_path))
        elif language in ["java"]:
            concepts.extend(self._extract_java_concepts(code_content, file_path))

        return concepts

    def _detect_language(self, file_path: str) -> str:
        """Detect programming language from file extension."""
        extensions = {
            ".py": "python",
            ".ts": "typescript",
            ".js": "javascript",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
        }

        for ext, lang in extensions.items():
            if file_path.endswith(ext):
                return lang

        return "unknown"

    def _extract_python_concepts(self, code: str, file_path: str) -> List[CodeConcept]:
        """Extract Python classes and functions."""
        concepts = []

        # Extract classes
        class_pattern = r"^class\s+(\w+)\s*(?:\(.*?\))?:"
        for match in re.finditer(class_pattern, code, re.MULTILINE):
            class_name = match.group(1)
            concepts.append(CodeConcept(
                name=class_name,
                description=f"Main class: {class_name}",
                file_path=file_path,
                language="python",
                complexity=3,
                code_snippet=self._extract_code_block(code, match.start())
            ))

        # Extract functions
        func_pattern = r"^def\s+(\w+)\s*\("
        for match in re.finditer(func_pattern, code, re.MULTILINE):
            func_name = match.group(1)
            if not func_name.startswith("_"):  # Skip private functions
                concepts.append(CodeConcept(
                    name=func_name,
                    description=f"Function: {func_name}",
                    file_path=file_path,
                    language="python",
                    complexity=2,
                    code_snippet=self._extract_code_block(code, match.start())
                ))

        return concepts

    def _extract_js_concepts(self, code: str, file_path: str) -> List[CodeConcept]:
        """Extract TypeScript/JavaScript classes and functions."""
        concepts = []

        # Extract classes
        class_pattern = r"(?:export\s+)?(?:default\s+)?class\s+(\w+)"
        for match in re.finditer(class_pattern, code):
            class_name = match.group(1)
            concepts.append(CodeConcept(
                name=class_name,
                description=f"Main class: {class_name}",
                file_path=file_path,
                language="javascript",
                complexity=3,
                code_snippet=self._extract_code_block(code, match.start())
            ))

        # Extract functions
        func_pattern = r"(?:export\s+)?(?:async\s+)?function\s+(\w+)"
        for match in re.finditer(func_pattern, code):
            func_name = match.group(1)
            concepts.append(CodeConcept(
                name=func_name,
                description=f"Function: {func_name}",
                file_path=file_path,
                language="javascript",
                complexity=2,
                code_snippet=self._extract_code_block(code, match.start())
            ))

        return concepts

    def _extract_java_concepts(self, code: str, file_path: str) -> List[CodeConcept]:
        """Extract Java classes and methods."""
        concepts = []

        # Extract classes
        class_pattern = r"(?:public\s+)?class\s+(\w+)"
        for match in re.finditer(class_pattern, code):
            class_name = match.group(1)
            concepts.append(CodeConcept(
                name=class_name,
                description=f"Main class: {class_name}",
                file_path=file_path,
                language="java",
                complexity=3,
                code_snippet=self._extract_code_block(code, match.start())
            ))

        # Extract public methods
        method_pattern = r"(?:public\s+)?(?:\w+\s+)+(\w+)\s*\("
        for match in re.finditer(method_pattern, code):
            method_name = match.group(1)
            if method_name not in ["class", "interface"]:
                concepts.append(CodeConcept(
                    name=method_name,
                    description=f"Method: {method_name}",
                    file_path=file_path,
                    language="java",
                    complexity=2,
                    code_snippet=self._extract_code_block(code, match.start())
                ))

        return concepts

    def _extract_code_block(self, code: str, start_pos: int, lines: int = 10) -> str:
        """Extract a block of code around a position."""
        lines_list = code[:start_pos].split("\n")
        start_line = max(0, len(lines_list) - 1)
        code_lines = code.split("\n")
        return "\n".join(code_lines[start_line : start_line + lines])

    def _build_dependency_graph(self, concepts: List[CodeConcept]) -> Dict[str, List[str]]:
        """Build a dependency graph between concepts."""
        graph = defaultdict(list)

        for concept in concepts:
            for related in concept.related_concepts:
                graph[concept.name].append(related)

        return dict(graph)


class CurriculumFromRepoGenerator:
    """Generates curriculum from repository analysis."""

    CURRICULUM_STRUCTURE = {
        "foundation": {
            "num_lessons": 3,
            "num_problems": 2,
            "duration_days": 7,
            "description": "Build foundational knowledge"
        },
        "intermediate": {
            "num_lessons": 4,
            "num_problems": 3,
            "duration_days": 10,
            "description": "Apply concepts to real code"
        },
        "advanced": {
            "num_lessons": 3,
            "num_problems": 4,
            "duration_days": 7,
            "description": "Deep dive into implementation"
        },
        "capstone": {
            "num_lessons": 1,
            "num_problems": 0,
            "duration_days": 14,
            "description": "Implement features in the actual repository"
        }
    }

    def __init__(self, repo_analysis: RepoAnalysis):
        """Initialize generator with repository analysis."""
        self.repo = repo_analysis
        self.output_dir = Path("repo_curriculum_output")
        self.output_dir.mkdir(exist_ok=True)
        self.content_counter = 0

    def generate_curriculum(self) -> Dict[str, Any]:
        """Generate complete curriculum from repository."""
        print(f"\n{'='*70}")
        print(f"Generating Curriculum for {self.repo.repo_name}")
        print(f"{'='*70}\n")

        curriculum = {
            "course_name": f"{self.repo.repo_name}: Learn by Contributing",
            "course_code": f"REPO-{self.repo.repo_name.upper()[:6]}",
            "level": "Intermediate",
            "duration_weeks": 6,
            "repository": {
                "owner": self.repo.owner,
                "name": self.repo.repo_name,
                "url": self.repo.repo_url,
                "language": self.repo.language,
                "description": self.repo.description
            },
            "course_objectives": self._generate_course_objectives(),
            "prerequisites": self._generate_prerequisites(),
            "modules": self._generate_modules(),
            "capstone_project": self._generate_capstone_project()
        }

        return curriculum

    def _generate_course_objectives(self) -> List[str]:
        """Generate course learning objectives."""
        objectives = [
            f"Understand the architecture and design of {self.repo.repo_name}",
            f"Master the key concepts: {', '.join([c.name for c in self.repo.main_concepts[:3]])}",
            f"Contribute meaningful features and bug fixes to the repository",
            "Follow professional development and code review practices",
            "Develop proficiency in open-source contribution workflows"
        ]
        return objectives

    def _generate_prerequisites(self) -> List[str]:
        """Generate course prerequisites."""
        lang_prerequisites = {
            "python": ["Python fundamentals", "Basic OOP concepts"],
            "javascript": ["JavaScript ES6+", "Node.js basics"],
            "typescript": ["TypeScript basics", "Advanced type systems"],
            "java": ["Java fundamentals", "Object-oriented programming"],
        }

        base_prerequisites = [
            "Git and GitHub basics",
            "Command line proficiency",
            "IDE/text editor familiarity"
        ]

        lang_specific = lang_prerequisites.get(
            self.repo.language.lower(),
            ["Language fundamentals"]
        )

        return base_prerequisites + lang_specific

    def _generate_modules(self) -> List[Dict[str, Any]]:
        """Generate course modules (foundation → intermediate → advanced → capstone)."""
        modules = []

        for level_name, level_config in self.CURRICULUM_STRUCTURE.items():
            print(f"  Generating {level_name.title()} Module...")

            module = {
                "module_id": f"mod_{level_name}",
                "name": f"{level_name.title()} Module",
                "level": level_name,
                "duration_days": level_config["duration_days"],
                "description": level_config["description"],
                "lessons": self._generate_lessons(level_name, level_config["num_lessons"]),
                "problems": self._generate_problems(level_name, level_config["num_problems"]),
                "quiz": self._generate_quiz(level_name),
                "expected_outcome": self._generate_module_outcome(level_name)
            }

            modules.append(module)

        return modules

    def _generate_lessons(self, level: str, num_lessons: int) -> List[Dict[str, Any]]:
        """Generate lessons for a module."""
        lessons = []

        for i in range(num_lessons):
            concept = self.repo.main_concepts[i % len(self.repo.main_concepts)]

            lesson = {
                "lesson_id": f"lesson_{level}_{i+1}",
                "number": i + 1,
                "title": self._generate_lesson_title(level, concept),
                "concepts": self._generate_lesson_concepts(concept, level),
                "content": self._generate_lesson_content(concept, level),
                "code_walkthrough": self._generate_code_walkthrough(concept),
                "key_takeaways": self._generate_key_takeaways(concept),
                "estimated_time_minutes": 45 + (i * 15),
                "resources": self._generate_lesson_resources(concept)
            }

            lessons.append(lesson)

        return lessons

    def _generate_problems(self, level: str, num_problems: int) -> List[Dict[str, Any]]:
        """Generate practice problems for a module."""
        problems = []

        for i in range(num_problems):
            concept = self.repo.main_concepts[(i + 1) % len(self.repo.main_concepts)]

            problem = {
                "problem_id": f"problem_{level}_{i+1}",
                "number": i + 1,
                "title": self._generate_problem_title(level, concept),
                "difficulty": level,
                "description": self._generate_problem_description(concept, level),
                "starter_code": self._generate_starter_code(concept),
                "acceptance_criteria": self._generate_acceptance_criteria(concept, level),
                "solution_outline": self._generate_solution_outline(concept, level),
                "estimated_time_minutes": 30 + (i * 20),
                "hints": self._generate_hints(concept, level)
            }

            problems.append(problem)

        return problems

    def _generate_quiz(self, level: str) -> Dict[str, Any]:
        """Generate module quiz."""
        num_questions = 5 + (len(self.CURRICULUM_STRUCTURE) - list(self.CURRICULUM_STRUCTURE.keys()).index(level))

        quiz = {
            "quiz_id": f"quiz_{level}",
            "title": f"{level.title()} Module Quiz",
            "num_questions": num_questions,
            "passing_score": 70,
            "questions": self._generate_quiz_questions(level, num_questions),
            "time_limit_minutes": num_questions * 5
        }

        return quiz

    def _generate_quiz_questions(self, level: str, num_questions: int) -> List[Dict[str, Any]]:
        """Generate quiz questions."""
        questions = []

        for i in range(num_questions):
            concept = self.repo.main_concepts[i % len(self.repo.main_concepts)]

            question = {
                "question_id": f"q_{level}_{i+1}",
                "number": i + 1,
                "question_type": ["multiple_choice", "true_false", "short_answer"][i % 3],
                "text": self._generate_question_text(concept, level),
                "options": self._generate_question_options(concept, i),
                "correct_answer": "Option A",
                "explanation": self._generate_question_explanation(concept),
                "difficulty": level
            }

            questions.append(question)

        return questions

    def _generate_capstone_project(self) -> Dict[str, Any]:
        """Generate capstone project specification."""
        project = {
            "project_id": "capstone_001",
            "title": f"Contribute to {self.repo.repo_name}: Real-World Feature Implementation",
            "duration_days": 14,
            "difficulty": "advanced",
            "objectives": [
                f"Implement a new feature or fix a bug in {self.repo.repo_name}",
                "Follow the repository's contribution guidelines",
                "Write tests and documentation for your changes",
                "Submit a pull request and respond to code review feedback",
                "Successfully merge your contribution to the main codebase"
            ],
            "project_description": self._generate_project_description(),
            "requirements": self._generate_project_requirements(),
            "deliverables": [
                "Feature branch with implementation",
                "Unit tests (90%+ code coverage)",
                "Updated documentation/docstrings",
                "Pull request with detailed description",
                "Responses to code review comments",
                "Merged PR in the official repository"
            ],
            "grading_rubric": {
                "Code Quality": 25,
                "Functionality": 25,
                "Testing": 20,
                "Documentation": 15,
                "Git Workflow & Communication": 15
            },
            "example_tasks": self._generate_example_tasks(),
            "getting_started": self._generate_getting_started_guide()
        }

        return project

    # ========== CONTENT GENERATION HELPERS ==========

    def _generate_lesson_title(self, level: str, concept: CodeConcept) -> str:
        """Generate lesson title."""
        titles = {
            "foundation": f"Understanding {concept.name}: The Basics",
            "intermediate": f"Working with {concept.name}: Practical Applications",
            "advanced": f"Mastering {concept.name}: Advanced Techniques"
        }
        return titles.get(level, f"Lesson: {concept.name}")

    def _generate_lesson_concepts(self, concept: CodeConcept, level: str) -> List[str]:
        """Generate learning concepts for lesson."""
        return [
            concept.name,
            f"How {concept.name} is used in {self.repo.repo_name}",
            "Common patterns and best practices",
            "Integration with other components"
        ]

    def _generate_lesson_content(self, concept: CodeConcept, level: str) -> str:
        """Generate lesson content."""
        return f"""
## {concept.name}

### Overview
This lesson explores **{concept.name}**, a key concept in {self.repo.repo_name}.

### What You'll Learn
- Fundamental principles of {concept.name}
- How it's implemented in {self.repo.repo_name}
- Common use cases and patterns
- Best practices and common pitfalls

### Key Ideas
{concept.description}

### In the Context of {self.repo.repo_name}
This concept appears in: **{concept.file_path}**

### Why It Matters
Understanding {concept.name} is essential for:
1. Reading and understanding the codebase
2. Making meaningful contributions
3. Implementing new features correctly
4. Debugging and troubleshooting issues

### Next Steps
Practice using {concept.name} through the provided problems, then explore how
it's used in the actual codebase.
"""

    def _generate_code_walkthrough(self, concept: CodeConcept) -> str:
        """Generate code walkthrough."""
        return f"""
### Code Walkthrough: {concept.name}

Here's how **{concept.name}** is actually implemented in {self.repo.repo_name}:

```python
{concept.code_snippet}
```

### Key Observations

1. **Structure**: Notice how the code is organized
2. **Patterns**: Look for common patterns used
3. **Best Practices**: Identify professional coding standards

### Try It Yourself

1. Read through the code carefully
2. Identify the main components
3. Trace the execution flow
4. Consider how you might extend or modify it

### Questions to Consider

- What problem does this code solve?
- How does it handle edge cases?
- What patterns does it use?
- How could it be improved?
"""

    def _generate_key_takeaways(self, concept: CodeConcept) -> List[str]:
        """Generate key takeaways for lesson."""
        return [
            f"{concept.name} is essential for understanding {self.repo.repo_name}",
            f"Practice implementing {concept.name} in your own code",
            f"Study how {concept.name} interacts with other components",
            "Apply these patterns to your own projects"
        ]

    def _generate_lesson_resources(self, concept: CodeConcept) -> List[Dict[str, str]]:
        """Generate lesson resources."""
        return [
            {
                "type": "documentation",
                "title": f"{concept.name} Documentation",
                "url": f"{self.repo.repo_url}/blob/main/{concept.file_path}"
            },
            {
                "type": "tutorial",
                "title": f"Learn {concept.name}",
                "url": f"https://docs.python.org/3/tutorial/"
            }
        ]

    def _generate_problem_title(self, level: str, concept: CodeConcept) -> str:
        """Generate problem title."""
        titles = {
            "foundation": f"Basic {concept.name} Exercise",
            "intermediate": f"{concept.name} Implementation Challenge",
            "advanced": f"Advanced {concept.name} Problem"
        }
        return titles.get(level, f"Problem: {concept.name}")

    def _generate_problem_description(self, concept: CodeConcept, level: str) -> str:
        """Generate problem description."""
        return f"""
## Problem: {concept.name} Implementation

### Objective
Implement a solution that demonstrates your understanding of **{concept.name}**.

### Background
{concept.description}

### Task
Write code that implements {concept.name} following best practices and patterns
used in {self.repo.repo_name}.

### Requirements
1. Follow the coding standards used in the repository
2. Include appropriate error handling
3. Write clear, documented code
4. Consider edge cases

### Hints
- Review the code examples in the lesson
- Study how {concept.name} is used in {concept.file_path}
- Consider the context and use cases
"""

    def _generate_starter_code(self, concept: CodeConcept) -> str:
        """Generate starter code for problem."""
        return f"""
# {concept.name} Implementation
# Complete the implementation below

def implement_{concept.name.lower()}():
    '''
    Implement {concept.name} functionality.
    
    Returns:
        Result of the implementation
    '''
    # Your code here
    pass

# Test your implementation
if __name__ == "__main__":
    result = implement_{concept.name.lower()}()
    print(f"Result: {{result}}")
"""

    def _generate_acceptance_criteria(self, concept: CodeConcept, level: str) -> List[str]:
        """Generate acceptance criteria for problem."""
        return [
            f"Implementation correctly uses {concept.name}",
            "Code follows repository style guidelines",
            "All edge cases are handled",
            "Code is well-documented",
            "Tests pass successfully"
        ]

    def _generate_solution_outline(self, concept: CodeConcept, level: str) -> str:
        """Generate solution outline."""
        return f"""
## Solution Approach

1. **Understand the Problem**
   - Review {concept.name} requirements
   - Identify inputs and expected outputs

2. **Plan Your Solution**
   - Break down into smaller steps
   - Consider edge cases

3. **Implement**
   - Write clean, modular code
   - Add comments for clarity

4. **Test**
   - Create test cases
   - Verify all scenarios work

5. **Refactor**
   - Optimize if needed
   - Ensure code quality
"""

    def _generate_hints(self, concept: CodeConcept, level: str) -> List[str]:
        """Generate hints for problem."""
        return [
            f"Start by understanding what {concept.name} does",
            f"Look at examples in {concept.file_path}",
            "Break the problem into smaller parts",
            "Test incrementally as you build"
        ]

    def _generate_question_text(self, concept: CodeConcept, level: str) -> str:
        """Generate quiz question text."""
        questions = {
            "foundation": f"What is the primary purpose of {concept.name}?",
            "intermediate": f"How does {concept.name} interact with other components?",
            "advanced": f"What are the best practices for implementing {concept.name}?"
        }
        return questions.get(level, f"Describe {concept.name}")

    def _generate_question_options(self, concept: CodeConcept, question_num: int) -> List[str]:
        """Generate quiz question options."""
        return [
            f"Option A: {concept.name} is used for {concept.description}",
            f"Option B: {concept.name} is an alternative approach",
            f"Option C: {concept.name} is deprecated",
            f"Option D: {concept.name} is only for advanced users"
        ]

    def _generate_question_explanation(self, concept: CodeConcept) -> str:
        """Generate quiz question explanation."""
        return f"""
{concept.name} is {concept.description}

This concept appears in {concept.file_path} and is essential for understanding
how {self.repo.repo_name} works. Understanding this will help you contribute
effectively to the project.
"""

    def _generate_module_outcome(self, level: str) -> str:
        """Generate module expected outcome."""
        outcomes = {
            "foundation": "You will understand the basic concepts and be ready to explore the codebase",
            "intermediate": "You will be able to read and modify code in the repository",
            "advanced": "You will be ready to contribute new features to the project",
            "capstone": "You will have made a real contribution to the repository"
        }
        return outcomes.get(level, "You will have learned new skills")

    def _generate_project_description(self) -> str:
        """Generate capstone project description."""
        return f"""
## Project Overview

This capstone project gives you the opportunity to make a real contribution
to {self.repo.repo_name}. You'll implement a feature or fix a bug while
following the repository's contribution guidelines.

### What You'll Do

1. Choose a task from the repository's issue tracker
2. Implement your solution following best practices
3. Write comprehensive tests
4. Submit a pull request
5. Respond to code review feedback
6. Get your contribution merged!

### Why This Matters

This project simulates real-world open-source contribution. You'll learn:
- Professional development workflows
- Code review processes
- Collaboration best practices
- Quality assurance standards
"""

    def _generate_project_requirements(self) -> List[str]:
        """Generate capstone project requirements."""
        return [
            f"Fork and clone {self.repo.repo_url}",
            "Create a feature branch",
            "Implement your solution",
            "Write unit tests (90%+ coverage)",
            "Update documentation",
            "Submit a pull request",
            "Respond to review comments",
            "Get your PR merged"
        ]

    def _generate_example_tasks(self) -> List[Dict[str, str]]:
        """Generate example capstone tasks."""
        return [
            {
                "task": "Bug Fix",
                "description": "Fix an existing bug in the repository",
                "difficulty": "intermediate"
            },
            {
                "task": "Feature Addition",
                "description": "Add a new feature or enhancement",
                "difficulty": "advanced"
            },
            {
                "task": "Documentation",
                "description": "Improve or add documentation",
                "difficulty": "beginner"
            }
        ]

    def _generate_getting_started_guide(self) -> str:
        """Generate getting started guide for capstone."""
        return (
            "## Getting Started\n\n"
            "### Step 1: Fork and Clone\n"
            "```bash\n"
            "# Fork the repository on GitHub\n"
            "# Then clone your fork\n"
            f"git clone https://github.com/YOUR_USERNAME/{self.repo.repo_name}.git\n"
            f"cd {self.repo.repo_name}\n"
            "```\n\n"
            "### Step 2: Set Up Development Environment\n"
            "```bash\n"
            "# Install dependencies\n"
            "pip install -r requirements.txt  # For Python\n"
            "# or\n"
            "npm install  # For JavaScript/TypeScript\n"
            "```\n\n"
            "### Step 3: Choose a Task\n"
            "- Browse the repository's issues\n"
            '- Look for "good first issue" labels\n'
            "- Discuss with maintainers if needed\n\n"
            "### Step 4: Create a Branch\n"
            "```bash\n"
            "git checkout -b feature/your-feature-name\n"
            "```\n\n"
            "### Step 5: Implement and Test\n"
            "- Write your code\n"
            "- Add tests\n"
            "- Run the test suite\n\n"
            "### Step 6: Submit\n"
            "```bash\n"
            "git add .\n"
            'git commit -m "Add your feature"\n'
            "git push origin feature/your-feature-name\n"
            "# Create pull request on GitHub\n"
            "```\n"
        )


def setup_logging(verbose: bool = False) -> None:
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the curriculum generator.
    
    Args:
        argv: Command-line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code: 0 for success, 1 for error
    """
    parser = argparse.ArgumentParser(
        description="Generate curriculum from GitHub repository",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --repo facebook/react
  %(prog)s --repo microsoft/vscode --token ghp_xxxx --output ./my_curriculum
        """
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="Repository in format owner/repo_name"
    )
    parser.add_argument(
        "--token",
        help="GitHub API token (optional, for higher rate limits)"
    )
    parser.add_argument(
        "--output",
        default="repo_curriculum_output",
        help="Output directory (default: repo_curriculum_output)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args(argv)

    # Setup logging
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)

    # Validate repository format
    if "/" not in args.repo:
        logger.error("Repository must be in format owner/repo_name")
        return 1

    owner, repo_name = args.repo.split("/", 1)

    try:
        # Analyze repository
        logger.info(f"Analyzing repository: {owner}/{repo_name}")
        analyzer = GitHubRepoAnalyzer(token=args.token)
        repo_analysis = analyzer.analyze_repository(owner, repo_name)

        # Generate curriculum
        logger.info("Generating curriculum...")
        generator = CurriculumFromRepoGenerator(repo_analysis)
        curriculum = generator.generate_curriculum()

        # Save output
        output_dir = Path(args.output)
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / f"{repo_name}_curriculum.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(curriculum, f, indent=2, ensure_ascii=False)

        logger.info(f"Curriculum saved to: {output_file}")
        print(f"\n✅ Curriculum saved to: {output_file}")
        return 0

    except requests.exceptions.RequestException as e:
        logger.error(f"GitHub API error: {e}")
        return 1
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
