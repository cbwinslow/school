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
```

---

**Skills Version**: 1.0  
**Last Updated**: March 2026