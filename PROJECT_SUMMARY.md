# 📚 AI-Powered Curriculum Generator

## Project Overview

An intelligent curriculum generation system that uses AI agents to create comprehensive learning materials from GitHub repositories and predefined content structures.

## 🎯 Purpose

Generate complete educational curricula including:
- Structured lessons with code examples
- Practice problems with progressive difficulty
- Quizzes and assessments
- Capstone projects based on real repositories
- Answer keys with explanations

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      RUN.PY                                 │
│                   (Entry Point)                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                             │
│              (Routes requests to agents)                    │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│  Curriculum  │   │   Lesson     │   │   Problem    │
│  Architect   │   │  Generator   │   │   Creator    │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   Project    │   │  Assessment  │   │    Mentor    │
│   Designer   │   │   Grader     │   │    Agent     │
└──────────────┘   └──────────────┘   └──────────────┘
```

## 📁 File Structure

```
course-curriculum/
├── .gitignore                    # Git ignore rules
├── .clinerules                   # Project rules and conventions
├── PROJECT_SUMMARY.md            # This file
├── CONTEXT.md                    # Full project context
├── SYSTEM.md                     # System documentation
├── README.md                     # Main overview
├── SCRIPTS-ANALYSIS.md           # Script analysis and skills mapping
│
├── agents/
│   └── agents.json               # Agent definitions
│
├── skills/
│   └── definitions.md            # Skill definitions (15+ skills)
│
├── curriculum_repo_list.py       # Repository curation script
├── github_repo_to_curriculum_generator.py  # GitHub analysis script
├── recursive_curriculum_generator.py       # Content generation script
│
├── run.py                        # Main run script (TUI/Web)
├── requirements.txt              # Python dependencies
│
├── curriculum/                   # Generated curriculum content
├── grading/                      # Grading rubrics
├── knowledge/                    # Knowledge base files
├── progress/                     # Student progress tracking
└── tools/                        # Tool definitions
```

## 🔧 Core Components

### 1. Python Scripts

| Script | Purpose |
|--------|---------|
| `curriculum_repo_list.py` | Curates 21+ learning repositories across TypeScript, Python, AI/ML |
| `github_repo_to_curriculum_generator.py` | Analyzes GitHub repos and generates curriculum |
| `recursive_curriculum_generator.py` | Recursively generates lessons, problems, quizzes |

### 2. Agent System

| Agent | Role |
|-------|------|
| Orchestrator | Routes requests, coordinates agents |
| Curriculum Architect | Designs module structures |
| Lesson Generator | Creates lesson content |
| Problem Creator | Generates exercises |
| Project Designer | Builds project specs |
| Assessment Grader | Evaluates submissions |
| Mentor Agent | Provides help and hints |

### 3. Skills (15+)

**Repository Analysis:**
- `analyze_github_repo` - Extract concepts from repos
- `extract_code_concepts` - Parse code files

**Content Generation:**
- `generate_lesson_content` - Create lessons
- `generate_progressive_problems` - Create exercises
- `create_quiz_from_content` - Generate quizzes
- `generate_answer_key` - Create answer keys

**Project Design:**
- `design_project_from_repo` - Create capstone projects

## 🚀 Usage

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run TUI
python run.py

# Or run web interface
python run.py --web

# Generate curriculum from GitHub repo
python run.py --repo pytorch/pytorch

# Generate from outline
python run.py --outline curriculum_outline.json
```

### Programmatic Usage

```python
from github_repo_to_curriculum_generator import (
    GitHubRepoAnalyzer,
    CurriculumFromRepoGenerator
)

# Analyze repository
analyzer = GitHubRepoAnalyzer()
repo_analysis = analyzer.analyze_repository("pytorch", "pytorch")

# Generate curriculum
generator = CurriculumFromRepoGenerator(repo_analysis)
curriculum = generator.generate_curriculum()
```

## 📊 Output Formats

- **JSON** - Machine-readable for API/agent consumption
- **Markdown** - Human-readable documentation
- **CSV** - Spreadsheet import

## 🔑 Key Features

1. **GitHub Integration** - Analyze real repositories
2. **Recursive Generation** - Unlimited content depth
3. **Progressive Difficulty** - Beginner → Advanced
4. **Multi-Domain** - TypeScript, Python, AI/ML
5. **Agent Orchestration** - Multiple specialized agents
6. **Skill Composition** - Combine skills for complex tasks

## 📝 Configuration

### Environment Variables

```bash
GITHUB_TOKEN=ghp_xxxxx  # Optional: Higher API rate limits
```

### Curriculum Outline Format

```json
{
  "course_name": "Advanced Python",
  "course_code": "PYTH301",
  "level": "Intermediate-Advanced",
  "duration_weeks": 16,
  "units": [
    {
      "name": "Unit Name",
      "topics": [
        {"name": "Topic 1", "num_lessons": 2, "num_problems": 3}
      ]
    }
  ]
}
```

## 🎓 Learning Path

```
Repository Analysis
        ↓
Concept Extraction
        ↓
Lesson Generation
        ↓
Problem Creation
        ↓
Quiz Generation
        ↓
Project Design
        ↓
Complete Curriculum
```

---

**Version**: 2.0  
**Status**: Production Ready  
**Last Updated**: March 2026