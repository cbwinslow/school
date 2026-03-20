# 📚 Project Context & Knowledge Base

## Overview

This is the **master context file** for the Python & TypeScript Curriculum System. Include this file (or its contents) with every agent interaction to ensure consistent, informed responses.

---

## 🎯 Project Identity

```yaml
project:
  name: "Python & TypeScript Advanced Curriculum"
  version: "2.0"
  type: "AI-Powered Learning System"
  purpose: "Help intermediate developers master Python, TypeScript, and AI programming"
  
  student:
    level: "intermediate"
    knows: ["Python basics", "TypeScript basics", "OOP fundamentals"]
    goals: ["Build real applications", "Learn AI programming", "Master advanced concepts"]
    style: "project-first"
```

---

## 🏗️ System Architecture

### Agent Hierarchy

```
ORCHESTRATOR (Entry Point)
├── CURRICULUM ARCHITECT
│   ├── LESSON GENERATOR
│   └── PROBLEM CREATOR
├── PROJECT DESIGNER
├── ASSESSMENT GRADER
└── MENTOR AGENT
```

### Agent Roles

| Agent | Role | Invokes | Purpose |
|-------|------|---------|---------|
| Orchestrator | Coordinator | All agents | Main entry point, routes requests |
| Curriculum Architect | Designer | Lesson Generator, Problem Creator | Creates module structures |
| Lesson Generator | Creator | Problem Creator | Writes detailed lessons |
| Problem Creator | Creator | None | Generates coding exercises |
| Project Designer | Creator | None | Builds project specifications |
| Assessment Grader | Evaluator | None | Grades submissions |
| Mentor Agent | Helper | None | Provides hints when stuck |

### Recursive Flow

```
Student Request
    ↓
Orchestrator analyzes context
    ↓
Curriculum Architect designs structure
    ↓
Lesson Generator creates content
    ↓
Problem Creator generates exercises
    ↓
Student completes work
    ↓
Assessment Grader evaluates
    ↓
Mentor Agent helps if stuck
    ↓
Orchestrator updates state and generates next
```

---

## 📁 File Structure

```
course-curriculum/
├── CONTEXT.md                    # This file (include with every prompt)
├── README.md                     # Main overview
├── SYSTEM.md                     # System documentation
├── agents/                       # Agent definitions
│   ├── orchestrator.md
│   ├── curriculum-architect.md
│   ├── lesson-generator.md
│   ├── problem-creator.md
│   ├── project-designer.md
│   ├── assessment-grader.md
│   └── mentor-agent.md
├── curriculum/                   # Learning modules
│   └── ai-programming.md
├── grading/
│   └── rubrics.md
└── progress/
    └── tracker.md
```

---

## 🎓 Curriculum Modules

### Phase 1: Intermediate Foundations (Weeks 1-4)
- Intermediate Python (decorators, generators, typing)
- Intermediate TypeScript (advanced types, generics, async)
- Testing Mastery (pytest, Jest, TDD)
- Database Design (SQLAlchemy, Prisma)

### Phase 2: Advanced Development (Weeks 5-8)
- Advanced Python (metaclasses, descriptors, C extensions)
- Advanced TypeScript (conditional types, decorators, frameworks)
- API Development (FastAPI, tRPC, GraphQL)
- System Design (patterns, architecture, scalability)

### Phase 3: AI Programming (Weeks 9-12)
- Prompt Engineering
- LLM Integration
- AI Agents
- MCP Development
- RAG Systems

### Phase 4: Full-Stack Mastery (Weeks 13-16)
- Full-Stack Python
- Full-Stack TypeScript
- DevOps & Deployment
- Portfolio & Capstone

---

## 🚀 Project Portfolio

### Core Projects
1. CLI Tool with Plugin System (4-6 hours)
2. REST API with Authentication (8-12 hours)
3. Database Migration Tool (6-8 hours)
4. Real-Time Chat Backend (12-16 hours)

### AI Projects
5. AI Chatbot with Memory (6-8 hours)
6. RAG Document Assistant (8-12 hours)
7. AI Agent Framework (12-16 hours)
8. MCP Server (8-12 hours)

### Full-Stack Projects
9. SaaS Dashboard (16-24 hours)
10. Real-Time App with WebSockets (16-24 hours)
11. Deployment Pipeline (8-12 hours)
12. Capstone Project (24+ hours)

---

## 📊 Grading Standards

### Scale
- A (90-100): Excellent
- B (80-89): Good
- C (70-79): Satisfactory
- D (60-69): Below Expectations
- F (<60): Failing

### Categories
- Functionality: 40%
- Code Quality: 25-30%
- Documentation: 15%
- Testing: 10-15%
- Best Practices: 5%

### Pass Criteria
- Exercise: Score ≥ 60%, code runs, core functionality works
- Project: Score ≥ 70%, all features implemented, documentation present

---

## 🎯 Competency Skills

### Python Skills
- OOP, Decorators, Generators, Async/Await, Type Hints, Testing, Web Frameworks, Database

### TypeScript Skills
- Type System, Generics, Async Patterns, React, Node.js, Testing

### AI Skills
- Prompt Engineering, LLM API, AI Agents, RAG Systems, MCP Development

---

## 🔧 Technical Standards

### Python
- PEP 8 style
- Type hints required
- Docstrings for all public functions
- pytest for testing
- Virtual environments

### TypeScript
- ESLint/Prettier
- Strict type checking
- JSDoc comments
- Jest for testing
- npm/yarn package management

### Both
- Git version control
- README documentation
- Error handling
- Input validation
- Environment variables for config

---

## 📝 Prompt Template

When using agents, include this context:

```
## Context
{Paste this CONTEXT.md file}

## Agent
{Paste the specific agent file}

## Request
{Your specific question or task}

## Current State
- Current module: {if applicable}
- Completed lessons: {list}
- Current competencies: {scores}
```

---

## 🔄 Validation Checklist

After generating any content, verify:

- [ ] Learning objectives are clear
- [ ] Code examples are runnable
- [ ] Prerequisites are listed
- [ ] Difficulty level is appropriate
- [ ] Estimated time is provided
- [ ] Exercises have test cases
- [ ] Documentation is complete
- [ ] Best practices are followed

---

## 📚 Quick Reference

### Start Here
- New student: Read `README.md`, then use `agents/orchestrator.md`
- Continuing: Use `progress/tracker.md` to check status

### Get Help
- Stuck on lesson: Use `agents/mentor-agent.md`
- Need feedback: Use `agents/assessment-grader.md`
- Want next lesson: Use `agents/orchestrator.md`

### Track Progress
- Update `progress/tracker.md` after each session
- Log hours and competencies

---

**Context Version**: 1.0  
**Last Updated**: March 2026  
**Include With**: Every agent interaction