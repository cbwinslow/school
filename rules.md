# 📋 Project Rules & Conventions

## Code Style

### Python
- Follow PEP 8 style guide
- Use type hints for all function parameters and returns
- Use docstrings for all classes and public methods
- Maximum line length: 100 characters
- Use 4 spaces for indentation

### Naming Conventions
- Classes: PascalCase (e.g., `CurriculumGenerator`)
- Functions/methods: snake_case (e.g., `generate_lesson`)
- Constants: UPPER_SNAKE_CASE (e.g., `DEFAULT_OUTPUT_DIR`)
- Private methods: prefix with underscore (e.g., `_generate_id`)

## File Organization

### Script Headers
All Python scripts must include:
```python
#!/usr/bin/env python3
"""
================================================================================
Name: [Author]
Date: [Date]
Script Name: [filename.py]
Version: [X.Y.Z]
Description: [Brief description]
================================================================================
"""
```

### Data Classes
- Use `@dataclass` for data models
- Include `to_dict()` method for serialization
- Use `field(default_factory=list)` for mutable defaults

## Agent Conventions

### Skill Definition Format
```yaml
skill:
  name: skill_name
  description: "Clear description"
  inputs:
    - param_name: type
  outputs:
    - output_name: type
```

## Directory Structure

```
course-curriculum/
├── CONTEXT.md                    # Main context file
├── agents/                       # Agent definitions
│   ├── orchestrator.md
│   ├── curriculum-architect.md
│   ├── lesson-generator.md
│   ├── problem-creator.md
│   ├── project-designer.md
│   ├── assessment-grader.md
│   └── mentor-agent.md
├── curriculum/                   # Learning modules
├── grading/                      # Assessment rubrics
├── knowledge/                    # Reference materials
├── progress/                     # Progress tracking
├── skills/                       # Skill definitions
├── tools/                        # Tool definitions
└── validation/                   # Validation scripts
```

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