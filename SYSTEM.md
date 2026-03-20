# 🔧 Curriculum System Documentation

## How the Multi-Agent System Works

This document explains the internal workings of the recursive curriculum generation system, the agent coordination protocols, and how lessons, projects, and exercises are created.

---

## 🎯 System Overview

The curriculum system is a **recursive, multi-agent architecture** where specialized AI agents collaborate to create a personalized learning experience. The system continuously generates, evaluates, and refines educational content based on student progress and feedback.

### Core Principles

1. **Recursive Generation**: Agents call other agents to build complex content
2. **Adaptive Difficulty**: System adjusts based on success rates
3. **Quality Assurance**: Multiple validation layers ensure quality
4. **Continuous Improvement**: Feedback loops refine content over time
5. **Personalization**: Content adapts to individual learning styles

---

## 🏗️ Agent Architecture

### Agent Hierarchy

```
ORCHESTRATOR (Top Level)
├── CURRICULUM ARCHITECT
│   ├── LESSON GENERATOR
│   └── PROBLEM CREATOR
├── PROJECT DESIGNER
├── ASSESSMENT GRADER
└── MENTOR AGENT
```

### Agent Communication Protocol

Agents communicate through structured prompts and responses:

```yaml
# Agent Request Format
agent: target_agent_name
action: specific_action
context:
  student_level: intermediate
  current_module: advanced-python
  completed_lessons: [lesson-1, lesson-2]
  performance_metrics:
    success_rate: 0.85
    avg_completion_time: 45m
request:
  type: generate_lesson
  topic: decorators
  difficulty: intermediate
```

```yaml
# Agent Response Format
agent: lesson_generator
status: success
content:
  lesson_id: "py-decorators-01"
  title: "Python Decorators Deep Dive"
  sections: [...]
  exercises: [...]
  estimated_time: "60 minutes"
metadata:
  difficulty: intermediate
  prerequisites: ["functions", "closures"]
  learning_objectives: [...]
```

---

## 🔄 Recursive Generation Loop

The system uses a recursive approach where each agent can invoke other agents to complete complex tasks.

### Primary Generation Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. STUDENT REQUEST                                              │
│    "Generate a lesson on Python decorators"                     │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. ORCHESTRATOR receives and routes request                     │
│    - Analyzes student level                                     │
│    - Checks prerequisites                                       │
│    - Determines appropriate agents                              │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. CURRICULUM ARCHITECT designs lesson structure                │
│    - Defines learning objectives                                │
│    - Determines topic scope                                     │
│    - Creates section outline                                    │
│    - Calls LESSON GENERATOR for content                         │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. LESSON GENERATOR creates detailed content                    │
│    - Writes explanations                                        │
│    - Creates code examples                                      │
│    - Generates diagrams                                         │
│    - Calls PROBLEM CREATOR for exercises                        │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. PROBLEM CREATOR generates exercises                          │
│    - Creates coding challenges                                  │
│    - Defines success criteria                                   │
│    - Provides starter code                                      │
│    - Creates test cases                                         │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. ORCHESTRATOR assembles final lesson                          │
│    - Combines all generated content                             │
│    - Validates completeness                                     │
│    - Returns to student                                         │
└─────────────────────────────────────────────────────────────────┘
```

### Assessment and Feedback Loop

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. STUDENT SUBMITS completed work                               │
│    - Code files                                                 │
│    - Test results                                               │
│    - Documentation                                              │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. ASSESSMENT GRADER evaluates submission                       │
│    - Runs automated tests                                       │
│    - Analyzes code quality                                      │
│    - Checks best practices                                      │
│    - Generates feedback report                                  │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. ORCHESTRATOR updates student profile                         │
│    - Records competency changes                                 │
│    - Updates progress metrics                                   │
│    - Identifies knowledge gaps                                  │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. CURRICULUM ARCHITECT adapts learning path                    │
│    - Adjusts difficulty if needed                               │
│    - Recommends remedial content if gaps found                  │
│    - Generates next appropriate lesson                          │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. CYCLE REPEATS with adapted content                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Agent Specifications

### 1. Orchestrator (`orchestrator.md`)

**Role**: Central coordinator that manages the learning flow

**Responsibilities**:
- Route student requests to appropriate agents
- Maintain student state and progress
- Coordinate multi-agent workflows
- Ensure quality and completeness
- Handle error recovery

**Can Invoke**:
- Curriculum Architect
- Project Designer
- Assessment Grader
- Mentor Agent

### 2. Curriculum Architect (`curriculum-architect.md`)

**Role**: Designs learning paths and module structures

**Responsibilities**:
- Define module boundaries and scope
- Create learning objective hierarchies
- Design prerequisite chains
- Generate lesson outlines
- Coordinate with Lesson Generator and Problem Creator

**Can Invoke**:
- Lesson Generator
- Problem Creator

### 3. Lesson Generator (`lesson-generator.md`)

**Role**: Creates detailed lesson content

**Responsibilities**:
- Write explanatory content
- Create code examples
- Generate diagrams and visualizations
- Provide real-world analogies
- Include industry context

**Can Invoke**:
- Problem Creator (for exercises)

### 4. Problem Creator (`problem-creator.md`)

**Role**: Generates coding challenges and exercises

**Responsibilities**:
- Create diverse problem types
- Define success criteria
- Generate test cases
- Provide starter code
- Create progressive difficulty levels

**Can Invoke**:
- None (leaf agent)

### 5. Project Designer (`project-designer.md`)

**Role**: Builds project specifications and starter code

**Responsibilities**:
- Design project architecture
- Create requirement specifications
- Generate starter code templates
- Define acceptance criteria
- Provide implementation guidance

**Can Invoke**:
- None (leaf agent)

### 6. Assessment Grader (`assessment-grader.md`)

**Role**: Evaluates submissions and provides feedback

**Responsibilities**:
- Analyze code quality
- Run automated checks
- Evaluate against rubrics
- Generate detailed feedback
- Update competency tracking

**Can Invoke**:
- Mentor Agent (for detailed explanations)

### 7. Mentor Agent (`mentor-agent.md`)

**Role**: Provides help and guidance when stuck

**Responsibilities**:
- Answer specific questions
- Debug issues
- Explain concepts
- Provide hints (without solutions)
- Escalate if needed

**Can Invoke**:
- None (leaf agent)

---

## 📝 Content Generation Templates

### Lesson Template Structure

```markdown
# Lesson {N}: {Title}

## Overview
- Duration: {time}
- Difficulty: {level}
- Prerequisites: {list}

## Learning Objectives
By the end of this lesson, you will:
1. {objective_1}
2. {objective_2}
3. {objective_3}

## Theory & Concepts
### {Concept_1}
{explanation}

### {Concept_2}
{explanation}

## Code Examples
### Example 1: {title}
{code_with_comments}

### Example 2: {title}
{code_with_comments}

## Hands-On Exercises
### Exercise 1: {title}
- Description: {what_to_do}
- Starter Code: {template}
- Success Criteria: {requirements}
- Hints: {optional_hints}

### Exercise 2: {title}
{same_structure}

## Real-World Application
{how_this_is_used_in_industry}

## Summary
{key_takeaways}

## Next Steps
{what_comes_next}
```

### Project Template Structure

```markdown
# Project: {Name}

## Description
{what_youre_building}

## Learning Objectives
- {objective_1}
- {objective_2}
- {objective_3}

## Requirements
### Functional Requirements
1. {requirement_1}
2. {requirement_2}

### Technical Requirements
1. {tech_requirement_1}
2. {tech_requirement_2}

### Non-Functional Requirements
1. {performance}
2. {security}
3. {usability}

## Architecture
{system_design_diagram}

## Starter Code
{initial_project_structure}

## Implementation Guide
### Phase 1: {name}
{instructions}

### Phase 2: {name}
{instructions}

### Phase 3: {name}
{instructions}

## Testing
{test_requirements}

## Submission Checklist
- [ ] All functional requirements met
- [ ] Tests passing
- [ ] Documentation complete
- [ ] Code follows style guide

## Grading Rubric
{detailed_rubric}
```

### Exercise Template Structure

```markdown
## Exercise: {title}

### Problem Statement
{clear_description_of_what_to_solve}

### Input/Output
- Input: {description}
- Output: {description}

### Examples
\`\`\`
Example 1:
Input: {input}
Output: {output}
Explanation: {why}

Example 2:
Input: {input}
Output: {output}
Explanation: {why}
\`\`\`

### Constraints
- {constraint_1}
- {constraint_2}

### Starter Code
\`\`\`{language}
{template_code}
\`\`\`

### Test Cases
\`\`\`{language}
{test_code}
\`\`\`

### Hints
1. {hint_1}
2. {hint_2}

### Solution Approach
{high_level_approach_without_full_solution}
```

---

## 🔍 Quality Assurance Process

### Content Validation Steps

1. **Completeness Check**
   - All required sections present
   - Code examples are runnable
   - Exercises have test cases
   - Prerequisites are listed

2. **Accuracy Verification**
   - Code examples execute correctly
   - Concepts are explained accurately
   - Best practices are followed
   - No outdated information

3. **Difficulty Calibration**
   - Content matches target difficulty
   - Prerequisites are appropriate
   - Exercises have clear progression
   - Time estimates are realistic

4. **Pedagogical Review**
   - Learning objectives are clear
   - Examples support concepts
   - Exercises reinforce learning
   - Progression is logical

### Automated Checks

```yaml
validation:
  code_examples:
    - syntax_valid: true
    - runs_without_errors: true
    - follows_style_guide: true
  exercises:
    - has_test_cases: true
    - tests_pass_with_solution: true
    - difficulty_appropriate: true
  content:
    - has_learning_objectives: true
    - has_prerequisites: true
    - has_estimated_time: true
    - sections_complete: true
```

---

## 📊 Student State Management

### Progress Tracking Schema

```yaml
student:
  id: "student-001"
  level: "intermediate"
  
  competencies:
    python:
      oop: 0.85
      decorators: 0.70
      async: 0.60
      typing: 0.75
    typescript:
      types: 0.80
      generics: 0.65
      async: 0.70
      decorators: 0.55
    ai:
      prompt_engineering: 0.50
      llm_integration: 0.40
      agents: 0.30
  
  completed:
    lessons:
      - id: "py-oop-01"
        score: 0.90
        time: "45m"
      - id: "py-decorators-01"
        score: 0.85
        time: "60m"
    exercises:
      - id: "ex-oop-01"
        attempts: 1
        score: 1.0
      - id: "ex-decorators-01"
        attempts: 2
        score: 0.80
    projects:
      - id: "proj-cli-tool"
        score: 0.88
        feedback: "..."
  
  current:
    module: "advanced-python"
    lesson: "py-async-01"
    project: "proj-rest-api"
  
  metrics:
    avg_completion_time: "52m"
    success_rate: 0.85
    streak: 7
    total_hours: 120
```

### Adaptive Difficulty Logic

```python
def determine_next_difficulty(student, current_lesson):
    success_rate = student.metrics.success_rate
    current_score = current_lesson.score
    
    if success_rate > 0.90 and current_score > 0.85:
        return "increase"  # Move to harder content
    elif success_rate < 0.70 or current_score < 0.60:
        return "decrease"  # Provide easier content
    elif 0.70 <= success_rate <= 0.90:
        return "maintain"  # Stay at current level
    else:
        return "remedial"  # Review prerequisites
```

---

## 🔄 Recursive Generation Examples

### Example 1: Generating a Complete Module

```
User: "Generate a module on Python async programming"

ORCHESTRATOR → CURRICULUM ARCHITECT:
  "Design module structure for Python async"

CURRICULUM ARCHITECT returns:
  Module: python-async
  Lessons: [async-basics, asyncio-deep-dive, concurrent-futures, 
            async-patterns, real-world-async]
  Prerequisites: [functions, decorators, generators]

For each lesson, CURRICULUM ARCHITECT → LESSON GENERATOR:
  "Generate lesson on {topic} at {difficulty}"

LESSON GENERATOR → PROBLEM CREATOR:
  "Generate {n} exercises for {lesson}"

ORCHESTRATOR assembles complete module
```

### Example 2: Assessing and Adapting

```
Student submits exercise solution

ORCHESTRATOR → ASSESSMENT GRADER:
  "Evaluate submission for {exercise_id}"

ASSESSMENT GRADER returns:
  score: 0.75
  feedback: [...]
  gaps: ["error-handling", "edge-cases"]

ORCHESTRATOR → CURRICULUM ARCHITECT:
  "Student has gaps in {gaps}. Adapt next lesson."

CURRICULUM ARCHITECT → LESSON GENERATOR:
  "Generate remedial content for {gaps}"

ORCHESTRATOR presents adapted content to student
```

---

## 🛠️ Technical Implementation

### Agent Invocation Pattern

When using these agents in VS Code or with AI assistants:

```
# Step 1: Start with Orchestrator
Use the orchestrator.md agent file and provide:

"I'm a student at intermediate level. I've completed:
- Python OOP basics
- TypeScript type system
- Basic API development

I want to learn about Python decorators."

# Step 2: Orchestrator processes and delegates
The orchestrator will:
1. Check your competency profile
2. Verify prerequisites are met
3. Call curriculum-architect for structure
4. Call lesson-generator for content
5. Call problem-creator for exercises
6. Return complete lesson package

# Step 3: Complete the lesson
Work through the generated content

# Step 4: Submit for assessment
Use assessment-grader.md to submit your work

# Step 5: Receive feedback and next lesson
The cycle continues
```

### State Persistence

Student state is maintained in `progress/tracker.md`:

```markdown
## Current Progress

### Active Module: Advanced Python
- Completed Lessons: 3/5
- Current Lesson: py-async-01
- Exercises Completed: 12/15
- Project Status: In Progress

### Competency Scores
- Python OOP: 85%
- Python Decorators: 70%
- Python Async: 60%
...
```

---

## 🎯 Best Practices for Using the System

### For Students

1. **Always start with the orchestrator** for curriculum navigation
2. **Be specific** about what you want to learn
3. **Provide context** about your current state
4. **Complete exercises** before moving to next lesson
5. **Submit for assessment** to get feedback
6. **Use mentor agent** when stuck (don't struggle alone)

### For Content Generation

1. **Specify difficulty level** clearly
2. **List prerequisites** explicitly
3. **Include real-world examples** in every lesson
4. **Provide progressive exercises** from easy to hard
5. **Create comprehensive test cases** for all exercises
6. **Document everything** clearly

### For Assessment

1. **Run all tests** before submitting
2. **Include documentation** with submissions
3. **Address feedback** before moving on
4. **Track your progress** regularly
5. **Ask for clarification** if feedback is unclear

---

## 🔗 Related Documents

- [README.md](README.md) - Main curriculum overview
- [agents/orchestrator.md](agents/orchestrator.md) - Orchestrator agent
- [agents/curriculum-architect.md](agents/curriculum-architect.md) - Architect agent
- [progress/tracker.md](progress/tracker.md) - Progress tracking
- [grading/rubrics.md](grading/rubrics.md) - Assessment rubrics

---

**System Version**: 2.0  
**Last Updated**: March 2026  
**Architecture**: Recursive Multi-Agent  
**Status**: Production Ready