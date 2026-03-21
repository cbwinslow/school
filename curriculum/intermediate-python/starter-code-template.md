# CLI Tool with Plugin System - Starter Code Template

This is a starter code template for the CLI tool project. It includes the basic structure and some example implementations to get you started.

## Project Structure

```
cli-tool/
├── cli_tool/
│   ├── __init__.py
│   ├── main.py              # Main CLI interface
│   ├── commands/            # Command implementations
│   │   ├── __init__.py
│   │   ├── base.py         # Base command class
│   │   ├── hello.py        # Example command
│   │   └── __init__.py
│   ├── plugins/             # Plugin system
│   │   ├── __init__.py
│   │   ├── loader.py        # Plugin loader
│   │   ├── registry.py      # Plugin registry
│   │   ├── base.py         # Base plugin class
│   │   └── __init__.py
│   ├── utils/               # Utility functions
│   │   ├── __init__.py
│   │   ├── context.py       # Context managers
│   │   ├── exceptions.py     # Custom exceptions
│   │   ├── types.py         # Type definitions
│   │   └── __init__.py
│   ├── config.py            # Configuration management
│   └── types.py             # Type definitions
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_commands.py
│   ├── test_plugins.py
│   └── __init__.py
├── pyproject.toml          # Project configuration
├── README.md               # Documentation
└── requirements.txt         # Dependencies
```

## Installation

1. Install Python 3.8 or later
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the CLI Tool

```bash
# Basic usage
python -m cli_tool --help

# Run hello command
python -m cli_tool hello Alice

# Run data processing
python -m cli_tool process csv data.csv
```

## Code Implementation

### 1. Main CLI Interface (`cli_tool/main.py`)

```python
import argparse
from typing import Any, Dict, List
from .commands import CommandRegistry
from .plugins import PluginRegistry
from .config import load_config
from .utils.exceptions import CliError

class CliTool:
    def __init__(self):
        self.config = load_config()
        self.command_registry = CommandRegistry()
        self.plugin_registry = PluginRegistry()
        
        # Load plugins
        self.plugin_registry.load_plugins(
            self.config.get("plugins", [])
        )
    
    def create_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description="CLI Tool with Plugin System",
            formatter_class=argparse.RawDescriptionHelpFormatter
        )
        
        # Add version information
        parser.add_argument(
            "--version", action="version",
            version=f"CLI Tool v{self.config.get('version', '1.0.0')}"
        )
        
        # Add subcommands
        subparsers = parser.add_subparsers(
            title="Commands",
            dest="command",
            required=True
        )
        
        # Register all commands
        for command in self.command_registry.get_all_commands():
            command_parser = subparsers.add_parser(
                command.name,
                help=command.help_text
            )
            command.add_arguments(command_parser)
        
        return parser
    
    def run(self, args: List[str] = None) -> int:
        try:
            parser = self.create_parser()
            parsed_args = parser.parse_args(args)
            
            # Get the command class
            command_class = self.command_registry.get_command(parsed_args.command)
            if not command_class:
                print(f"Unknown command: {parsed_args.command}")
                return 1
            
            # Create command instance and execute
            command = command_class()
            result = command.execute(parsed_args)
            
            return result if result is not None else 0
            
        except CliError as e:
            print(f"Error: {e}")
            return 1
        except Exception as e:
            print(f"Unexpected error: {e}")
            return 1


def main():
    tool = CliTool()
    exit_code = tool.run()
    exit(exit_code)


if __name__ == "__main__":
    main()
```

### 2. Command System (`cli_tool/commands/base.py`)

```python
import argparse
from typing import Any, Dict, List, Optional, Type
from functools import wraps

class Command:
    """Base class for all commands"""
    
    name: str = ""
    help_text: str = ""
    
    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add command-specific arguments"""
        pass
    
    def execute(self, args: argparse.Namespace) -> Optional[int]:
        """Execute the command"""
        raise NotImplementedError


def command(name: str, help_text: str):
    """Decorator for registering commands"""
    def decorator(cls: Type[Command]) -> Type[Command]:
        cls.name = name
        cls.help_text = help_text
        return cls
    return decorator


class CommandRegistry:
    """Registry for all available commands"""
    
    def __init__(self):
        self.commands: Dict[str, Type[Command]] = {}
    
    def register(self, command_class: Type[Command]) -> None:
        """Register a command class"""
        if not command_class.name:
            raise ValueError("Command must have a name")
        
        self.commands[command_class.name] = command_class
    
    def get_command(self, name: str) -> Optional[Type[Command]]:
        """Get a command by name"""
        return self.commands.get(name)
    
    def get_all_commands(self) -> List[Type[Command]]:
        """Get all registered commands"""
        return list(self.commands.values())
```

### 3. Plugin System (`cli_tool/plugins/base.py`)

```python
from typing import Any, Dict, List, Optional, Type
from abc import ABC, abstractmethod

class Plugin(ABC):
    """Base class for all plugins"""
    
    name: str = ""
    description: str = ""
    
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """Initialize the plugin with configuration"""
        pass
    
    @abstractmethod
    def execute(self, data: Any) -> Any:
        """Execute the plugin's functionality"""
        pass
    
    @abstractmethod
    def cleanup(self) -> None:
        """Clean up resources"""
        pass


class PluginRegistry:
    """Registry for all available plugins"""
    
    def __init__(self):
        self.plugins: Dict[str, Type[Plugin]] = {}
        self.instances: Dict[str, Plugin] = {}
    
    def register(self, plugin_class: Type[Plugin]) -> None:
        """Register a plugin class"""
        if not plugin_class.name:
            raise ValueError("Plugin must have a name")
        
        self.plugins[plugin_class.name] = plugin_class
    
    def load_plugin(self, name: str, config: Dict[str, Any]) -> Optional[Plugin]:
        """Load and initialize a plugin"""
        plugin_class = self.plugins.get(name)
        if not plugin_class:
            return None
        
        instance = plugin_class()
        instance.initialize(config)
        self.instances[name] = instance
        return instance
    
    def get_plugin(self, name: str) -> Optional[Plugin]:
        """Get a loaded plugin instance"""
        return self.instances.get(name)
    
    def list_plugins(self) -> List[str]:
        """List all available plugin names"""
        return list(self.plugins.keys())
```

### 4. Context Managers (`cli_tool/utils/context.py`)

```python
import tempfile
import contextlib
from typing import Any, Generator

@contextlib.contextmanager
def file_processor(filename: str, mode: str = "r") -> Generator[Any, None, None]:
    """Context manager for file processing"""
    try:
        file = open(filename, mode)
        yield file
    finally:
        if file:
            file.close()


@contextlib.contextmanager
def temporary_file(**kwargs) -> Generator[str, None, None]:
    """Context manager for temporary files"""
    temp = tempfile.NamedTemporaryFile(**kwargs)
    try:
        yield temp.name
    finally:
        temp.close()


@contextlib.contextmanager
def database_connection(connection_string: str) -> Generator[Any, None, None]:
    """Context manager for database connections"""
    connection = None
    try:
        # Simulate database connection
        connection = f"Connection to {connection_string}"
        yield connection
    finally:
        if connection:
            print(f"Closing {connection}")


@contextlib.contextmanager
def plugin_context(plugin: Any) -> Generator[Any, None, None]:
    """Context manager for plugin execution"""
    try:
        yield plugin
    except Exception as e:
        print(f"Plugin error: {e}")
        raise
    finally:
        if hasattr(plugin, 'cleanup'):
            plugin.cleanup()
```

### 5. Custom Exceptions (`cli_tool/utils/exceptions.py`)

```python
class CliError(Exception):
    """Base class for CLI tool exceptions"""
    pass


class ValidationError(CliError):
    """Raised when data validation fails"""
    def __init__(self, field: str, message: str = "Invalid value"):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")


class PluginError(CliError):
    """Raised when plugin operations fail"""
    def __init__(self, plugin: str, message: str = "Plugin operation failed"):
        self.plugin = plugin
        self.message = message
        super().__init__(f"{plugin}: {message}")


class ConfigurationError(CliError):
    """Raised when configuration is invalid"""
    def __init__(self, message: str = "Invalid configuration"):
        super().__init__(message)


class CommandError(CliError):
    """Raised when command execution fails"""
    def __init__(self, command: str, message: str = "Command failed"):
        self.command = command
        self.message = message
        super().__init__(f"{command}: {message}")
```

### 6. Example Command (`cli_tool/commands/hello.py`)

```python
from .base import command, Command

@command("hello", "Say hello to someone")
class HelloCommand(Command):
    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("name", help="Name to greet")
    
    def execute(self, args: argparse.Namespace) -> int:
        print(f"Hello, {args.name}!")
        return 0
```

### 7. Example Plugin (`cli_tool/plugins/example.py`)

```python
from ..utils.exceptions import PluginError
from .base import Plugin

class ExamplePlugin(Plugin):
    name = "example"
    description = "Example plugin for demonstration"
    
    def initialize(self, config: dict) -> None:
        self.config = config
        print(f"Initializing {self.name} plugin with config: {config}")
    
    def execute(self, data: Any) -> Any:
        try:
            # Simple transformation
            if isinstance(data, str):
                return data.upper()
            return data
        except Exception as e:
            raise PluginError(self.name, str(e))
    
    def cleanup(self) -> None:
        print(f"Cleaning up {self.name} plugin")
```

### 8. Configuration (`cli_tool/config.py`)

```python
import json
import os
from typing import Any, Dict
from .utils.exceptions import ConfigurationError

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "plugins": [],
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30
}


def load_config(path: str = None) -> Dict[str, Any]:
    """Load configuration from file or use defaults"""
    config = DEFAULT_CONFIG.copy()
    
    # Use provided path or default location
    if not path:
        path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                file_config = json.load(f)
                config.update(file_config)
        except Exception as e:
            raise ConfigurationError(f"Failed to load config: {e}")
    
    return config


def validate_config(config: Dict[str, Any]) -> None:
    """Validate configuration"""
    if not isinstance(config.get("log_level"), str):
        raise ConfigurationError("log_level must be a string")
    
    if not isinstance(config.get("max_retries"), int):
        raise ConfigurationError("max_retries must be an integer")
    
    if not isinstance(config.get("timeout"), int):
        raise ConfigurationError("timeout must be an integer")
```

### 9. Type Definitions (`cli_tool/types.py`)

```python
from typing import Any, Dict, List, Optional, Union

# Common types
ConfigType = Dict[str, Any]
PluginConfigType = Dict[str, Any]
CommandArgsType = Dict[str, Any]

# Result types
ResultType = Union[int, str, dict, list, None]

# Plugin interface types
PluginType = Any
PluginInstanceType = Any

# Command interface types
CommandType = Any
CommandInstanceType = Any

# Context manager types
ContextManagerType = Any
```

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov mypy

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=cli_tool --cov-report=html

# Type checking
mypy cli_tool/
```

## Next Steps

1. Implement additional commands
2. Create more plugins
3. Add error handling
4. Write comprehensive tests
5. Add documentation
6. Optimize performance
7. Add configuration options

This template provides a solid foundation for building a comprehensive CLI tool with plugin architecture. You can extend it by adding more commands, plugins, and features as needed.