# 🔧 Agent Tools Definitions

## Overview

This file defines the tools and utilities available to agents for performing their tasks. These are conceptual tools that represent actions agents can take.

---

## 📁 File Operations

### Tool: Read File
**Description**: Read contents of a file
**Agent Access**: All agents

```yaml
tool:
  name: read_file
  description: "Read file contents"
  parameters:
    path: string (required)
  returns: string (file contents)
  usage: |
    Used to read curriculum files, student state, templates, etc.
```

### Tool: Write File
**Description**: Create or overwrite a file
**Agent Access**: All agents

```yaml
tool:
  name: write_file
  description: "Write content to file"
  parameters:
    path: string (required)
    content: string (required)
  returns: boolean (success)
  usage: |
    Used to create lessons, exercises, projects, update progress, etc.
```

### Tool: List Files
**Description**: List files in a directory
**Agent Access**: All agents

```yaml
tool:
  name: list_files
  description: "List files in directory"
  parameters:
    path: string (required)
    recursive: boolean (optional, default: false)
  returns: array of file paths
  usage: |
    Used to discover available modules, find student submissions, etc.
```

---

## 🧪 Code Execution

### Tool: Execute Code
**Description**: Run code and capture output
**Agent Access**: Assessment Grader, Problem Creator

```yaml
tool:
  name: execute_code
  description: "Execute code and return results"
  parameters:
    code: string (required)
    language: string (required: "python" | "typescript")
    timeout: number (optional, default: 30)
  returns:
    stdout: string
    stderr: string
    exit_code: number
    execution_time: number
  usage: |
    Used to run test cases, validate code examples, check submissions.
```

### Tool: Run Tests
**Description**: Execute test suite
**Agent Access**: Assessment Grader

```yaml
tool:
  name: run_tests
  description: "Run test suite against code"
  parameters:
    code: string (required)
    tests: string (required)
    language: string (required)
  returns:
    passed: number
    failed: number
    total: number
    details: array of test results
    score: number (0-1)
  usage: |
    Used to grade student submissions.
```

---

## 📊 Analysis Tools

### Tool: Analyze Code Quality
**Description**: Check code style and structure
**Agent Access**: Assessment Grader

```yaml
tool:
  name: analyze_code_quality
  description: "Analyze code quality metrics"
  parameters:
    code: string (required)
    language: string (required)
  returns:
    style_score: number (0-1)
    complexity: number
    issues: array
    suggestions: array
  usage: |
    Used to provide code quality feedback.
```

### Tool: Check Documentation
**Description**: Verify documentation completeness
**Agent Access**: Assessment Grader

```yaml
tool:
  name: check_documentation
  description: "Check documentation coverage"
  parameters:
    code: string (required)
    language: string (required)
  returns:
    docstring_coverage: number (0-1)
    missing: array
    quality: string
  usage: |
    Used to assess documentation quality.
```

---

## 🎯 Generation Tools

### Tool: Generate Code
**Description**: Generate code based on specifications
**Agent Access**: Lesson Generator, Problem Creator, Project Designer

```yaml
tool:
  name: generate_code
  description: "Generate code from specifications"
  parameters:
    specification: object (required)
    language: string (required)
    style: string (optional: "basic" | "intermediate" | "advanced")
  returns:
    code: string
    comments: array
  usage: |
    Used to create code examples, starter code, solutions.
```

### Tool: Generate Markdown
**Description**: Generate formatted markdown content
**Agent Access**: All agents

```yaml
tool:
  name: generate_markdown
  description: "Generate markdown content"
  parameters:
    template: string (required)
    data: object (required)
  returns: string (markdown)
  usage: |
    Used to create lessons, documentation, reports.
```

### Tool: Generate Diagram
**Description**: Create visual diagrams
**Agent Access**: Lesson Generator, Project Designer

```yaml
tool:
  name: generate_diagram
  description: "Generate visual diagram"
  parameters:
    type: string (required: "flowchart" | "sequence" | "class" | "er")
    components: array (required)
    format: string (optional: "mermaid" | "ascii")
  returns: string (diagram code)
  usage: |
    Used to visualize architecture, data flow, concepts.
```

---

## 📈 Progress Tools

### Tool: Read Progress
**Description**: Read student progress state
**Agent Access**: Orchestrator, Assessment Grader

```yaml
tool:
  name: read_progress
  description: "Read student progress from tracker"
  parameters:
    student_id: string (optional)
  returns:
    competencies: object
    completed: object
    current: object
    metrics: object
  usage: |
    Used to check student state before generating content.
```

### Tool: Update Progress
**Description**: Update student progress
**Agent Access**: Orchestrator, Assessment Grader

```yaml
tool:
  name: update_progress
  description: "Update student progress tracker"
  parameters:
    updates: object (required)
  returns: boolean (success)
  usage: |
    Used to record completed lessons, update competencies, log time.
```

---

## 🔍 Search Tools

### Tool: Search Content
**Description**: Search across curriculum content
**Agent Access**: All agents

```yaml
tool:
  name: search_content
  description: "Search for content across files"
  parameters:
    query: string (required)
    file_pattern: string (optional)
  returns:
    matches: array of {file, line, context}
  usage: |
    Used to find related content, prerequisites, examples.
```

### Tool: Find Prerequisites
**Description**: Find prerequisites for a topic
**Agent Access**: Curriculum Architect

```yaml
tool:
  name: find_prerequisites
  description: "Find prerequisites for a concept"
  parameters:
    concept: string (required)
  returns:
    required: array
    recommended: array
  usage: |
    Used to build prerequisite chains.
```

---

## 🧠 AI Tools

### Tool: Generate with LLM
**Description**: Use LLM to generate content
**Agent Access**: All agents

```yaml
tool:
  name: generate_with_llm
  description: "Generate content using LLM"
  parameters:
    prompt: string (required)
    context: string (optional)
    max_tokens: number (optional, default: 2000)
    temperature: number (optional, default: 0.7)
  returns:
    content: string
    tokens_used: number
  usage: |
    Core tool for generating all curriculum content.
```

### Tool: Analyze Text
**Description**: Analyze text for intent, sentiment, etc.
**Agent Access**: Orchestrator, Mentor Agent

```yaml
tool:
  name: analyze_text
  description: "Analyze text for intent and content"
  parameters:
    text: string (required)
    analysis_type: string (required: "intent" | "sentiment" | "complexity")
  returns:
    result: object
    confidence: number
  usage: |
    Used to understand student requests, assess frustration level.
```

---

## 🔗 Integration Tools

### Tool: Validate JSON
**Description**: Validate JSON structure
**Agent Access**: All agents

```yaml
tool:
  name: validate_json
  description: "Validate JSON against schema"
  parameters:
    data: string (required)
    schema: object (required)
  returns:
    valid: boolean
    errors: array
  usage: |
    Used to validate configurations, submissions, data.
```

### Tool: Format Code
**Description**: Format code according to style guide
**Agent Access**: Lesson Generator, Problem Creator

```yaml
tool:
  name: format_code
  description: "Format code to style standards"
  parameters:
    code: string (required)
    language: string (required)
  returns:
    formatted_code: string
    changes: array
  usage: |
    Used to ensure code examples follow style guidelines.
```

---

## 📋 Tool Usage Matrix

| Agent | File Ops | Code Exec | Analysis | Generation | Progress | Search | AI |
|-------|----------|-----------|----------|------------|----------|--------|-----|
| Orchestrator | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Curriculum Architect | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Lesson Generator | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Problem Creator | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ |
| Project Designer | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| Assessment Grader | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Mentor Agent | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |

---

## 🔐 Tool Security

### Safe Operations
- Read files: Always safe
- List files: Always safe
- Search: Always safe
- Read progress: Always safe

### Restricted Operations
- Write files: Only to project directory
- Execute code: Sandboxed environment
- Update progress: Requires validation

### Validation Required
- All file writes validated
- Code execution timeout enforced
- Progress updates must pass schema validation

---

**Tools Version**: 1.0  
**Last Updated**: March 2026