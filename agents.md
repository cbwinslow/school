# 🤖 Agent System Documentation

## Overview
This directory contains the agent system for the Python & TypeScript Curriculum. Each agent has a specific role in the learning workflow.

## Agent Hierarchy

```
ORCHESTRATOR (Entry Point)
├── CURRICULUM ARCHITECT
│   ├── LESSON GENERATOR
│   └── PROBLEM CREATOR
├── PROJECT DESIGNER
├── ASSESSMENT GRADER
└── MENTOR AGENT
```

## Agent Files

| File | Purpose | Invokes |
|------|---------|---------|
| `orchestrator.md` | Central coordinator, routes requests | All agents |
| `curriculum-architect.md` | Designs learning paths, module structures | Lesson Generator, Problem Creator |
| `lesson-generator.md` | Creates detailed lesson content | Problem Creator |
| `problem-creator.md` | Generates coding challenges | None |
| `project-designer.md` | Designs project specifications | None |
| `assessment-grader.md` | Evaluates student submissions | None |
| `mentor-agent.md` | Provides help when stuck | None |

## Agent Headers
Each agent file must include this YAML header:

```yaml
---
name: agent-name
description: Clear description
context_required: "../CONTEXT.md"
skills_required: "../skills/definitions.md"
tools_required: "../tools/definitions.md"
---
```

## Context Requirements
All agents require the main context file:
- `CONTEXT.md` - Project overview and student information
- `SYSTEM.md` - System architecture and workflows

## Skills & Tools
Agents use skills and tools defined in:
- `skills/definitions.md` - Available AI skills
- `tools/definitions.md` - Available tools and utilities

## Request Processing

### Orchestrator Flow
```yaml
Input: "Generate a lesson on Python decorators"
├── Analyze context and student state
├── Route to Curriculum Architect
│   ├── Define scope and objectives
│   ├── Design module structure
│   └── Generate lesson outline
├── Call Lesson Generator
│   ├── Expand concepts
│   ├── Write content
│   ├── Create examples
│   └── Generate diagrams
├── Call Problem Creator
│   ├── Design exercises
│   ├── Create test cases
│   └── Generate starter code
└── Assemble final response
```

## Agent Communication

### Message Format
Agents communicate using structured YAML:

```yaml
response:
  status: "success" | "error" | "in_progress"
  message: "Clear description of result"
  data:
    key: value
  next_steps:
    - "Suggested next action"
    - "Optional follow-up"
```

### Error Handling
- Use clear error messages
- Include troubleshooting steps
- Provide context for failures
- Suggest alternative approaches

## Development Guidelines

### Adding New Agents
1. Create agent file in `agents/` directory
2. Include required YAML header
3. Define clear purpose and usage
4. Document request/response formats
5. Update agent hierarchy if needed

### Agent Testing
- Test with various input scenarios
- Verify context is properly included
- Check error handling works correctly
- Validate output format and quality

### Performance
- Keep responses concise but complete
- Use caching for repeated operations
- Handle long-running tasks asynchronously
- Provide progress indicators when appropriate

## Security Considerations

### Input Validation
- Validate all inputs before processing
- Sanitize user-provided content
- Handle malicious inputs gracefully

### Output Safety
- Escape HTML in generated content
- Validate code examples before sharing
- Avoid executing untrusted code

### Privacy
- Never store sensitive student information
- Use anonymized data for analytics
- Comply with data protection regulations

## Maintenance

### Updates
- Review agent files quarterly
- Update skills and tools as needed
- Monitor agent performance and usage
- Collect feedback for improvements

### Documentation
- Keep agent documentation current
- Update examples and usage patterns
- Document any breaking changes
- Maintain a changelog for major updates

## Troubleshooting

### Common Issues
- Agent not found: Check file path and name
- Context missing: Verify CONTEXT.md is included
- Skills not available: Check skills_required path
- Tools not working: Verify tools_required path

### Debug Mode
Enable debug logging to trace agent execution:
```yaml
debug: true
log_level: "DEBUG"
```

## Version History

### 1.0 (March 2026)
- Initial agent system implementation
- Core agents defined
- Basic routing and coordination

### 1.1 (Planned)
- Enhanced error handling
- Performance optimizations
- Additional agent types

## Support

### Getting Help
- Check agent documentation first
- Review error messages carefully
- Test with simple inputs
- Verify all required files are present

### Contributing
- Follow existing patterns and conventions
- Test thoroughly before submitting
- Update documentation for changes
- Maintain backward compatibility