# 📊 Python Scripts Analysis & Agent Skills Integration

## Overview

This document analyzes the three Python scripts in the course-curriculum directory and maps them to potential agent skills for the curriculum system.

---

## 📁 Script Inventory

| Script | Lines | Purpose | Key Capabilities |
|--------|-------|---------|------------------|
| `curriculum_repo_list.py` | ~220 | Generate curated repository lists | Repository curation, multi-format output |
| `github_repo_to_curriculum_generator.py` | ~550 | Analyze GitHub repos & generate curriculum | GitHub API, code analysis, curriculum generation |
| `recursive_curriculum_generator.py` | ~700 | Generate curriculum content recursively | Lesson/problem/quiz generation, difficulty scaling |

---

## 🔍 Detailed Analysis

### 1. curriculum_repo_list.py

**What It Does:**
- Maintains curated lists of learning repositories for TypeScript, Python, and AI/ML
- Generates structured output in JSON, Markdown, and CSV formats
- Includes metadata: stars, topics, difficulty level, "best for" descriptions

**Key Classes:**
- `CurriculumRepository`: Data model for repository metadata
- `CurriculumGenerator`: Generates formatted output files

**Strengths:**
- Well-structured data model
- Multi-format output support
- Comprehensive repository metadata
- 21 curated repositories across 3 domains

**Potential as Agent Skills:**

| Skill Name | Agent | Description |
|------------|-------|-------------|
| `generate_repo_list` | Curriculum Architect | Generate curated learning resource lists |
| `search_repos_by_topic` | Curriculum Architect | Find repositories by topic/keyword |
| `get_repos_by_level` | Curriculum Architect | Filter repositories by difficulty |
| `export_repo_data` | Orchestrator | Export repository data in various formats |

---

### 2. github_repo_to_curriculum_generator.py

**What It Does:**
- Analyzes GitHub repositories via API
- Extracts code concepts from Python, TypeScript, JavaScript, Java files
- Generates complete curriculum: lessons, problems, quizzes, capstone projects
- Outputs structured JSON and Markdown curriculum files

**Key Classes:**
- `GitHubRepoAnalyzer`: Fetches and analyzes repository structure
- `CurriculumFromRepoGenerator`: Generates curriculum from analysis
- `CodeConcept`: Represents extracted programming concepts
- `AIAgentSkill`: Agent skill specification

**Strengths:**
- Real GitHub API integration
- Multi-language code analysis (Python, TS, JS, Java)
- Complete curriculum generation pipeline
- Progressive difficulty (Foundation → Intermediate → Advanced → Capstone)

**Potential as Agent Skills:**

| Skill Name | Agent | Description |
|------------|-------|-------------|
| `analyze_github_repo` | Curriculum Architect | Analyze repository structure and extract concepts |
| `extract_code_concepts` | Lesson Generator | Extract key programming concepts from code |
| `generate_curriculum_from_repo` | Curriculum Architect | Create complete curriculum from a repository |
| `create_capstone_from_repo` | Project Designer | Generate capstone project based on repository |
| `build_dependency_graph` | Curriculum Architect | Map concept dependencies in codebase |

---

### 3. recursive_curriculum_generator.py

**What It Does:**
- Generates comprehensive curriculum content recursively
- Creates lessons, problems, quizzes, projects, answer keys
- Supports nested curriculum structures with arbitrary depth
- Progressive difficulty scaling
- Domain-specific templates (TypeScript, Python, AI/ML)

**Key Classes:**
- `ContentGenerator`: Main content generation engine
- `Lesson`, `Problem`, `Question`, `Project`: Content item models
- `Topic`, `Unit`, `Curriculum`: Hierarchical structure models

**Strengths:**
- Recursive tree traversal for nested content
- Multiple content types (lessons, problems, quizzes, projects, answer keys)
- Domain-specific templates
- Automatic difficulty progression
- Comprehensive markdown output generation

**Potential as Agent Skills:**

| Skill Name | Agent | Description |
|------------|-------|-------------|
| `generate_lesson_content` | Lesson Generator | Create detailed lesson content |
| `generate_practice_problems` | Problem Creator | Generate practice problems with solutions |
| `generate_quiz_questions` | Problem Creator | Create quiz questions with explanations |
| `generate_unit_project` | Project Designer | Design unit-level projects |
| `generate_answer_key` | Assessment Grader | Create answer keys with explanations |
| `calculate_difficulty_progression` | Curriculum Architect | Calculate optimal difficulty scaling |
| `generate_semester_schedule` | Curriculum Architect | Create week-by-week schedule |

---

## 📊 Skills Summary Matrix

| Script | Skills Generated | Primary Agent | Secondary Agents |
|--------|-----------------|---------------|------------------|
| `curriculum_repo_list.py` | 3 | Curriculum Architect | Orchestrator |
| `github_repo_to_curriculum_generator.py` | 5 | Curriculum Architect | Lesson Generator, Project Designer |
| `recursive_curriculum_generator.py` | 7 | Lesson Generator, Problem Creator | Curriculum Architect, Assessment Grader |
| **Total** | **15 new skills** | | |

---

## 🛠️ Recommended Agent Skills Mapping

### New Skills for Curriculum Architect

```yaml
skill:
  name: discover_learning_resources
  description: "Find and curate learning repositories for a topic"
  script: curriculum_repo_list.py
  inputs:
    - topic: string
    - level: "beginner" | "intermediate" | "advanced"
    - language: string
  outputs:
    - repositories: array
    - format: "json" | "markdown" | "csv"
  implementation: |
    1. Query CurriculumGenerator repos (TYPESCRIPT/PYTHON/AIML)
    2. Filter by topic, level, language
    3. Generate formatted output
    4. Return curated list

skill:
  name: analyze_repository_for_curriculum
  description: "Analyze a GitHub repository to design curriculum"
  script: github_repo_to_curriculum_generator.py
  inputs:
    - repo_owner: string
    - repo_name: string
    - github_token: string (optional)
    - target_audience: string
  outputs:
    - repo_analysis: object
    - curriculum_structure: object
  implementation: |
    1. Initialize GitHubRepoAnalyzer
    2. Call analyze_repository()
    3. Extract concepts and dependencies
    4. Generate curriculum structure
    5. Return analysis and structure
```

### New Skills for Lesson Generator

```yaml
skill:
  name: generate_lesson_from_outline
  description: "Generate complete lesson from outline recursively"
  script: recursive_curriculum_generator.py
  inputs:
    - topic_name: string
    - lesson_index: number
    - difficulty: "beginner" | "intermediate" | "advanced"
    - domain: "typescript" | "python" | "aiml"
  outputs:
    - lesson: object
    - notes: string
    - code_examples: array
  implementation: |
    1. Initialize ContentGenerator(domain)
    2. Call _generate_lesson()
    3. Include notes, examples, concepts
    4. Return lesson object

skill:
  name: generate_code_walkthrough
  description: "Generate code walkthrough from repository analysis"
  script: github_repo_to_curriculum_generator.py
  inputs:
    - concept: CodeConcept
    - repository: string
  outputs:
    - walkthrough: string
    - annotated_code: string
```

### New Skills for Problem Creator

```yaml
skill:
  name: generate_progressive_problems
  description: "Generate problems with increasing difficulty"
  script: recursive_curriculum_generator.py
  inputs:
    - topic: string
    - num_problems: number
    - base_difficulty: string
    - domain: string
  outputs:
    - problems: array
    - solutions: array

skill:
  name: create_quiz_from_content
  description: "Generate quiz questions from lesson content"
  script: recursive_curriculum_generator.py
  inputs:
    - topic: string
    - num_questions: number
    - difficulty: string
  outputs:
    - questions: array
    - answer_key: array
```

### New Skills for Project Designer

```yaml
skill:
  name: design_project_from_repo
  description: "Design capstone project based on repository"
  script: github_repo_to_curriculum_generator.py
  inputs:
    - repo_analysis: RepoAnalysis
    - difficulty: string
  outputs:
    - project_spec: object
    - starter_code: string
    - rubric: object

skill:
  name: generate_unit_project
  description: "Generate project for a course unit"
  script: recursive_curriculum_generator.py
  inputs:
    - unit_id: string
    - unit_name: string
    - difficulty: string
    - domain: string
  outputs:
    - project: object
    - deliverables: array
    - rubric: object
```

### New Skills for Assessment Grader

```yaml
skill:
  name: generate_answer_key
  description: "Generate answer keys for quizzes and problems"
  script: recursive_curriculum_generator.py
  inputs:
    - unit: Unit object
    - include_explanations: boolean
  outputs:
    - answer_key: object
    - problem_solutions: array
```

---

---

## 📖 Line-by-Line Code Explanations

### curriculum_repo_list.py - Key Methods

#### `__init__` - Initialize Generator
```python
def __init__(self):
    """Initialize the curriculum generator."""
    self.all_repos = self.TYPESCRIPT_REPOS + self.PYTHON_REPOS + self.AIML_REPOS
    self.output_dir = Path(".")
```
- **Parameters**: None
- **Returns**: Initializes instance with 21 repositories across 3 domains
- **Integration**: Can be called by Curriculum Architect to get available resources

#### `generate_json` - JSON Output
```python
def generate_json(self, filename: str = "curriculum_repos.json") -> None:
    """Generate JSON output file."""
    data = {
        "metadata": { ... },
        "repositories": [repo.to_dict() for repo in self.all_repos]
    }
    with open(self.output_dir / filename, 'w') as f:
        json.dump(data, f, indent=2)
```
- **Parameters**: `filename` (optional, default: "curriculum_repos.json")
- **Returns**: None (writes to file)
- **Integration**: Returns structured data for agent consumption

---

### github_repo_to_curriculum_generator.py - Key Methods

#### `GitHubRepoAnalyzer.analyze_repository` - Main Analysis
```python
def analyze_repository(self, owner: str, repo_name: str) -> RepoAnalysis:
    """Analyze a GitHub repository and extract key concepts."""
    # Step 1: Fetch metadata
    repo_metadata = self._fetch_repo_metadata(owner, repo_name)
    
    # Step 2: Get file tree
    files = self._get_repo_file_tree(owner, repo_name, repo_metadata["default_branch"])
    analysis.key_files = self._identify_key_files(files)
    
    # Step 3: Extract concepts
    concepts = self._extract_main_concepts(owner, repo_name, analysis.key_files)
    analysis.main_concepts = concepts
    
    # Step 4: Build dependency graph
    analysis.dependency_graph = self._build_dependency_graph(concepts)
```
- **Parameters**: `owner` (string), `repo_name` (string)
- **Returns**: `RepoAnalysis` object with concepts, key_files, dependency_graph
- **Integration**: Core skill for Curriculum Architect

#### `_extract_python_concepts` - Python Parser
```python
def _extract_python_concepts(self, code: str, file_path: str) -> List[CodeConcept]:
    """Extract Python classes and functions."""
    concepts = []
    
    # Extract classes
    class_pattern = r"^class\s+(\w+)\s*(?:\(.*?\))?:"
    for match in re.finditer(class_pattern, code, re.MULTILINE):
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
        if not func_name.startswith("_"):  # Skip private
            concepts.append(CodeConcept(...))
```
- **Parameters**: `code` (string), `file_path` (string)
- **Returns**: List of `CodeConcept` objects
- **Integration**: Used by `extract_code_concepts` skill

#### `CurriculumFromRepoGenerator._generate_lesson` - Lesson Creation
```python
def _generate_lessons(self, level: str, num_lessons: int) -> List[Dict[str, Any]]:
    """Generate lessons for a module."""
    for i in range(num_lessons):
        concept = self.repo.main_concepts[i % len(self.repo.main_concepts)]
        
        lesson = {
            "lesson_id": f"lesson_{level}_{i+1}",
            "title": self._generate_lesson_title(level, concept),
            "concepts": self._generate_lesson_concepts(concept, level),
            "content": self._generate_lesson_content(concept, level),
            "code_walkthrough": self._generate_code_walkthrough(concept),
            "key_takeaways": self._generate_key_takeaways(concept),
            "resources": self._generate_lesson_resources(concept)
        }
```
- **Parameters**: `level` (string), `num_lessons` (int)
- **Returns**: List of lesson dictionaries
- **Integration**: Used by `generate_lesson_content` skill

#### `_generate_key_takeaways` - Takeaway Generation
```python
def _generate_key_takeaways(self, concept: CodeConcept) -> List[str]:
    """Generate key takeaways."""
    return [
        f"{concept.name} is {concept.description}",
        f"It's located in: {concept.file_path}",
        f"Complexity level: {concept.complexity}/5",
        "It's used throughout the codebase in multiple contexts",
        "Mastering this concept is crucial for contributing to the project"
    ]
```
- **Parameters**: `concept` (CodeConcept)
- **Returns**: List of takeaway strings
- **Integration**: Used by Lesson Generator agent

---

### recursive_curriculum_generator.py - Key Methods

#### `generate_curriculum_recursive` - Main Entry
```python
def generate_curriculum_recursive(
    self,
    outline: Dict[str, Any],
    parent_path: str = ""
) -> Curriculum:
    """Recursively generate complete curriculum from outline."""
    curriculum = Curriculum(
        course_name=outline["course_name"],
        course_code=outline.get("course_code", "CS101"),
        level=outline.get("level", "Intermediate"),
        duration_weeks=outline.get("duration_weeks", 16)
    )
    
    for unit_idx, unit_outline in enumerate(units_outline):
        unit = self._generate_unit_recursive(unit_outline, ...)
        curriculum.units.append(unit)
```
- **Parameters**: `outline` (dict), `parent_path` (string)
- **Returns**: Complete `Curriculum` object
- **Integration**: Core skill for Curriculum Architect

#### `_generate_unit_recursive` - Unit Generation
```python
def _generate_unit_recursive(
    self,
    unit_outline: Dict[str, Any],
    unit_index: int = 0,
    total_units: int = 1,
    parent_path: str = ""
) -> Unit:
    """Recursively generate unit content."""
    unit = Unit(id=f"unit_{unit_index:02d}", name=unit_outline["name"])
    
    # Recursively generate topics
    for topic_idx, topic_outline in enumerate(topics_outline):
        topic = self._generate_topic_recursive(topic_outline, ...)
        unit.topics.append(topic)
    
    # Generate unit quiz
    unit.unit_quiz = self._generate_quiz(num_questions=8, ...)
```
- **Parameters**: `unit_outline` (dict), `unit_index` (int), `total_units` (int)
- **Returns**: `Unit` object with topics, quiz, projects
- **Integration**: Used by `generate_semester_schedule` skill

#### `_generate_quiz` - Quiz Generation
```python
def _generate_quiz(
    self,
    num_questions: int = 5,
    unit_id: str = "",
    difficulty: DifficultyLevel = DifficultyLevel.BEGINNER
) -> List[Question]:
    """Generate quiz questions with multiple difficulty levels."""
    for q_idx in range(num_questions):
        q_type = ["multiple_choice", "short_answer", "essay"][q_idx % 3]
        
        question = Question(
            id=self._generate_id("question"),
            title=f"Question {q_idx + 1}",
            question_type=q_type,
            difficulty=self._escalate_difficulty(difficulty, q_idx)
        )
        
        question.options = self._generate_options(q_type)
        question.correct_answer = question.options[0]
        question.explanation = self._generate_explanation(q_type)
```
- **Parameters**: `num_questions` (int), `unit_id` (string), `difficulty` (DifficultyLevel)
- **Returns**: List of `Question` objects
- **Integration**: Used by `create_quiz_from_content` skill

#### `_calculate_difficulty` - Difficulty Scaling
```python
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
```
- **Parameters**: `unit_index` (int), `total_units` (int)
- **Returns**: `DifficultyLevel` enum value
- **Integration**: Used by `calculate_difficulty_progression` skill

---

## 🔄 Integration Architecture

### Script-to-Skill Conversion Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    PYTHON SCRIPT                            │
│  Classes │ Methods │ Templates                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   SKILL WRAPPER                             │
│  def skill_implementation(inputs: dict) -> dict:            │
│    1. Initialize script components                          │
│    2. Convert inputs to script format                       │
│    3. Execute script methods                                │
│    4. Convert outputs to skill format                       │
│    5. Return structured response                            │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    AGENT SKILL                              │
│  • Integrated into agent's skill registry                  │
│  • Callable via agent protocol                              │
│  • Returns structured data for downstream agents           │
└─────────────────────────────────────────────────────────────┘
```

### Agent Skill Composition Example

```
"Generate a Python curriculum from a GitHub repository"

Orchestrator
    ↓
Curriculum Architect
    ├── analyze_repository_for_curriculum (github_repo_to_curriculum_generator.py)
    ├── discover_learning_resources (curriculum_repo_list.py)
    └── generate_curriculum_from_repo
        ↓
Lesson Generator
    ├── generate_lesson_from_outline (recursive_curriculum_generator.py)
    └── generate_code_walkthrough
        ↓
Problem Creator
    ├── generate_progressive_problems (recursive_curriculum_generator.py)
    └── create_quiz_from_content
        ↓
Project Designer
    └── design_project_from_repo (github_repo_to_curriculum_generator.py)
```

---

## 📋 Implementation Checklist

### Phase 1: Foundation
- [ ] Create skill wrapper for `curriculum_repo_list.py`
- [ ] Implement `discover_learning_resources` skill
- [ ] Test with TypeScript, Python, AI/ML repositories
- [ ] Add to Curriculum Architect agent

### Phase 2: Repository Analysis
- [ ] Create skill wrapper for `github_repo_to_curriculum_generator.py`
- [ ] Implement `analyze_repository_for_curriculum` skill
- [ ] Implement `extract_code_concepts` skill
- [ ] Test with real GitHub repositories

### Phase 3: Content Generation
- [ ] Create skill wrapper for `recursive_curriculum_generator.py`
- [ ] Implement `generate_lesson_content` skill
- [ ] Implement `generate_practice_problems` skill
- [ ] Implement `create_quiz_from_content` skill

### Phase 4: Integration
- [ ] Implement `generate_answer_key` skill
- [ ] Implement `design_project_from_repo` skill
- [ ] Create end-to-end workflow tests
- [ ] Update agent skill definitions

---

## 🔧 Technical Considerations

### Dependencies
```
requests>=2.31.0        # GitHub API calls
python-dotenv>=1.0.0    # Environment variables
```

### Environment Variables
```bash
GITHUB_TOKEN=ghp_xxxxx  # Optional: Higher API rate limits
```

### Error Handling
- GitHub API rate limits
- Network errors
- Invalid repository names
- Missing file content
- Malformed curriculum outlines

---

## 🎯 Key Benefits

1. **Resource Discovery**: Agents can automatically find relevant learning repositories
2. **Code-Based Curriculum**: Generate curriculum from actual codebases
3. **Scalable Content**: Recursively generate unlimited content
4. **Consistent Quality**: Standardized templates and difficulty progression
5. **Multi-Domain Support**: TypeScript, Python, AI/ML all supported
6. **Automated Assessment**: Generate quizzes and answer keys automatically

---

**Analysis Version**: 1.0  
**Created**: March 2026  
**Status**: Ready for Implementation
