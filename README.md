# 🚀 Advanced Python & TypeScript Programming Curriculum

## ⚡ AI-Powered Learning System

A comprehensive, recursive curriculum system designed for **intermediate-to-advanced developers** who want to master Python, TypeScript, and AI programming. Built with a multi-agent architecture that generates lessons, projects, exercises, and provides personalized guidance.

---

## 🎯 Who This Is For

You already know the basics. You can write functions, use loops, and understand basic OOP. Now you want to:

- Build real-world applications
- Master advanced language features
- Learn AI/LLM programming
- Understand how things work under the hood
- Create professional-grade code
- Develop AI agents and tools

---

## 🏗️ System Architecture

This curriculum uses a **recursive multi-agent system** that continuously generates and refines learning material based on your progress.

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                              │
│            (coordinates all agents)                          │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│  Curriculum   │ │    Lesson     │ │    Problem    │
│  Architect    │ │  Generator    │ │   Creator     │
└───────────────┘ └───────────────┘ └───────────────┘
        │               │               │
        ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│   Project     │ │  Assessment   │ │    Mentor     │
│  Designer     │ │    Grader     │ │    Agent      │
└───────────────┘ └───────────────┘ └───────────────┘
```

### Agent Roles

| Agent | Purpose |
|-------|---------|
| **Orchestrator** | Coordinates all agents, manages learning flow |
| **Curriculum Architect** | Designs module structure and learning paths |
| **Lesson Generator** | Creates detailed lessons with examples |
| **Problem Creator** | Generates coding challenges and exercises |
| **Project Designer** | Builds project specifications and starter code |
| **Assessment Grader** | Evaluates submissions and provides feedback |
| **Mentor Agent** | Provides help when you're stuck |

---

## 📚 Curriculum Modules

### Phase 1: Intermediate Foundations (Weeks 1-4)

| Module | Topics | Projects |
|--------|--------|----------|
| **Intermediate Python** | Advanced OOP, decorators, generators, typing | CLI Tool with Plugins |
| **Intermediate TypeScript** | Advanced types, generics, async patterns | REST API with Auth |
| **Testing Mastery** | pytest, Jest, mocking, TDD | Test Suite Builder |
| **Database Design** | SQLAlchemy, Prisma, migrations | Database Migration Tool |

### Phase 2: Advanced Development (Weeks 5-8)

| Module | Topics | Projects |
|--------|--------|----------|
| **Advanced Python** | Metaclasses, descriptors, C extensions | Performance Profiler |
| **Advanced TypeScript** | Type inference, conditional types, decorators | Framework Internals |
| **API Development** | FastAPI, tRPC, GraphQL, OpenAPI | Full-Stack API |
| **System Design** | Patterns, architecture, scalability | Distributed Task Queue |

### Phase 3: AI Programming (Weeks 9-12)

| Module | Topics | Projects |
|--------|--------|----------|
| **Prompt Engineering** | Techniques, testing, optimization | Prompt Toolkit |
| **LLM Integration** | LangChain, OpenAI, streaming | RAG Chatbot |
| **AI Agents** | Tool use, planning, orchestration | AI Agent Framework |
| **MCP Development** | Server creation, tools, resources | Custom MCP Server |

### Phase 4: Full-Stack Mastery (Weeks 13-16)

| Module | Topics | Projects |
|--------|--------|----------|
| **Full-Stack Python** | FastAPI + React, auth, deployment | SaaS Dashboard |
| **Full-Stack TypeScript** | Next.js, tRPC, Prisma | Real-time App |
| **DevOps & Deployment** | Docker, CI/CD, monitoring | Deployment Pipeline |
| **Portfolio & Capstone** | Professional showcase | Capstone Project |

---

## 🚀 Getting Started

### 1. Start with the Orchestrator

```markdown
Use: agents/orchestrator.md

Ask: "I know Python and TypeScript basics. I want to start with 
intermediate Python. Generate my first lesson and project."
```

### 2. Follow the Generated Path

The orchestrator will:
- Assess your current level
- Generate appropriate lessons
- Create exercises and projects
- Provide feedback on submissions
- Adapt difficulty as you progress

### 3. Track Your Progress

Use the progress tracker in `progress/tracker.md` to:
- Log completed lessons
- Track project submissions
- Monitor skill development
- View competency levels

---

## 📁 Directory Structure

```
course-curriculum/
├── README.md                    # This file
├── SYSTEM.md                    # How the system works
├── agents/                      # AI agent definitions
│   ├── orchestrator.md          # Main coordinator
│   ├── curriculum-architect.md  # Module designer
│   ├── lesson-generator.md      # Lesson creator
│   ├── problem-creator.md       # Exercise generator
│   ├── project-designer.md      # Project builder
│   ├── assessment-grader.md     # Submission evaluator
│   └── mentor-agent.md          # Help provider
├── curriculum/                  # Learning modules
│   ├── intermediate-python.md
│   ├── intermediate-typescript.md
│   ├── advanced-python.md
│   ├── advanced-typescript.md
│   ├── testing-mastery.md
│   ├── api-development.md
│   ├── ai-programming.md
│   ├── fullstack-development.md
│   └── devops-deployment.md
├── projects/                    # Project specifications
│   ├── README.md
│   ├── cli-tool-with-plugins/
│   ├── rest-api-with-auth/
│   ├── database-migration-tool/
│   ├── rag-chatbot/
│   ├── ai-agent-framework/
│   ├── mcp-server/
│   ├── saas-dashboard/
│   └── capstone-project/
├── exercises/                   # Coding challenges
│   ├── README.md
│   ├── python-challenges/
│   ├── typescript-challenges/
│   ├── algorithm-challenges/
│   └── system-design-challenges/
├── grading/                     # Assessment rubrics
│   ├── rubrics.md
│   ├── code-quality-standards.md
│   └── project-rubrics/
├── templates/                   # Reusable templates
│   ├── lesson-template.md
│   ├── project-template.md
│   ├── exercise-template.md
│   └── assessment-template.md
├── progress/                    # Tracking
│   ├── tracker.md
│   ├── competency-levels.md
│   └── certificates.md
└── resources/                   # References
    ├── python-resources.md
    ├── typescript-resources.md
    ├── ai-resources.md
    └── tools-and-setup.md
```

---

## 🎓 Competency Levels

| Level | Description | Requirements |
|-------|-------------|--------------|
| **L1: Intermediate** | Can build basic applications | 2 projects, 80% exercises |
| **L2: Advanced** | Can design complex systems | 4 projects, 85% exercises |
| **L3: Specialist** | Expert in specific domain | 6 projects, 90% exercises |
| **L4: Professional** | Industry-ready developer | 8 projects, 95% exercises |
| **L5: Expert** | Can architect systems | Capstone + portfolio |

---

## 🔧 Prerequisites

- Python 3.11+ installed
- Node.js 18+ installed
- VS Code or similar IDE
- Git basics
- Command line familiarity
- **Already know**: Variables, functions, loops, basic OOP

---

## 📖 How to Use This System

### For Lessons
1. Ask orchestrator for a lesson on topic X
2. Lesson generator creates detailed content
3. Complete the lesson and exercises
4. Submit for assessment
5. Get feedback and move to next topic

### For Projects
1. Request a project from project designer
2. Get specification and starter code
3. Implement the project
4. Submit for grading
5. Iterate based on feedback

### For Help
1. Describe your problem to mentor agent
2. Get contextual guidance
3. Try suggested solutions
4. Escalate if still stuck

### For Assessment
1. Submit completed work
2. Receive detailed feedback
3. Address identified issues
4. Resubmit if needed
5. Track competency progression

---

## 🤖 AI Programming Focus

This curriculum includes a dedicated AI programming track covering:

- **Prompt Engineering**: Techniques, testing, optimization
- **LLM Integration**: API usage, streaming, context management
- **AI Agents**: Tool use, planning, memory, orchestration
- **MCP Development**: Server creation, tool providers, resources
- **RAG Systems**: Vector databases, embeddings, retrieval
- **AI Workflows**: Multi-agent coordination, pipelines
- **Industry Standards**: Best practices, security, evaluation

---

## 📊 Progress Tracking

Your progress is tracked across multiple dimensions:

- **Lessons Completed**: Content mastery
- **Exercises Solved**: Problem-solving ability
- **Projects Built**: Practical application
- **Code Quality**: Best practices adherence
- **Competency Level**: Overall skill assessment

---

## 🆘 Getting Help

### Stuck on a Lesson?
→ Use `mentor-agent.md` with context about what you've tried

### Need Project Guidance?
→ Use `project-designer.md` to get architecture advice

### Want Feedback?
→ Use `assessment-grader.md` to submit your work

### Curriculum Questions?
→ Use `orchestrator.md` for navigation and planning

---

## 📝 Contributing to the Curriculum

The system is designed to be self-improving:

1. **Feedback Loop**: Assessment results inform curriculum updates
2. **Difficulty Adaptation**: System adjusts based on success rates
3. **Content Generation**: Agents create new material as needed
4. **Quality Assurance**: Multiple agents validate generated content

---

## 🎯 Learning Outcomes

After completing this curriculum, you will be able to:

- ✅ Build production-grade Python and TypeScript applications
- ✅ Design and implement complex system architectures
- ✅ Develop AI-powered applications and agents
- ✅ Create and deploy MCP servers
- ✅ Write comprehensive test suites
- ✅ Implement CI/CD pipelines
- ✅ Apply industry best practices and design patterns
- ✅ Debug and optimize performance
- ✅ Work with databases and APIs effectively
- ✅ Deploy applications to production

---

## 📅 Estimated Timeline

| Pace | Duration | Hours/Week |
|------|----------|------------|
| **Full-time** | 16 weeks | 40 hours |
| **Part-time** | 24 weeks | 20 hours |
| **Self-paced** | 32+ weeks | 10 hours |

---

## 🔗 Quick Links

- [System Documentation](SYSTEM.md)
- [Agent Directory](agents/)
- [Curriculum Modules](curriculum/)
- [Project Specifications](projects/)
- [Exercise Library](exercises/)
- [Grading Rubrics](grading/)
- [Progress Tracker](progress/tracker.md)

---

**Version**: 2.0  
**Last Updated**: March 2026  
**Status**: Active Development  
**Focus**: Intermediate to Advanced Development + AI Programming