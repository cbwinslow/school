# Starter Code Template - CLI Tool with Plugin System

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

# Initialize the tool
python -m cli_tool init

# Run a command
python -m cli_tool run hello

# Interactive mode
python -m cli_tool
```

## Code Implementation

### main.py
```python
import click
from cli_tool.commands import CommandRegistry
from cli_tool.config import Config
from cli_tool.utils.exceptions import CLIError

@click.group()
@click.option('--config', '-c', default='config.yaml',
              help='Configuration file path')
@click.pass_context
def cli(ctx, config):
    """Main CLI interface"""
    ctx.obj = {
        'config': Config.from_file(config),
        'registry': CommandRegistry()
    }

@cli.command()
@click.pass_context
def init(ctx):
    """Initialize the CLI tool"""
    config = ctx.obj['config']
    # Initialize configuration, create default files, etc.

@cli.command()
@click.argument('command_name')
@click.pass_context
def run(ctx, command_name):
    """Run a specific command"""
    registry = ctx.obj['registry']
    try:
        command = registry.get_command(command_name)
        if command:
            command.execute()
        else:
            raise CLIError(f"Command '{command_name}' not found")
    except CLIError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli()
```

### commands/base.py
```python
from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseCommand(ABC):
    """Base class for commands"""
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
    
    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the command"""
        pass
    
    def validate(self, **kwargs) -> bool:
        """Validate command arguments"""
        return True
    
    def help(self) -> str:
        """Return help text for the command"""
        return self.description

class HelloCommand(BaseCommand):
    """Example command that says hello"""
    def __init__(self):
        super().__init__("hello", "Say hello to someone")
    
    def execute(self, name: str = "World") -> None:
        print(f"Hello, {name}!")

class GoodbyeCommand(BaseCommand):
    """Example command that says goodbye"""
    def __init__(self):
        super().__init__("goodbye", "Say goodbye to someone")
    
    def execute(self, name: str = "World") -> None:
        print(f"Goodbye, {name}!")
```

### plugins/base.py
```python
from abc import ABC, abstractmethod
from typing import Dict, Any

class BasePlugin(ABC):
    """Base class for plugins"""
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self.config = None
    
    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """Initialize the plugin with configuration"""
        pass
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Execute the plugin's main functionality"""
        pass
    
    def shutdown(self) -> None:
        """Clean up resources when plugin is unloaded"""
        pass

class PluginRegistry:
    """Registry for plugins"""
    def __init__(self):
        self.plugins: Dict[str, Type[BasePlugin]] = {}
        self.loaded_plugins: Dict[str, BasePlugin] = {}
    
    def register(self, name: str, plugin_class: Type[BasePlugin]) -> None:
        """Register a plugin class"""
        self.plugins[name] = plugin_class
    
    def load_plugin(self, name: str, *args, **kwargs) -> BasePlugin:
        """Load and instantiate a plugin"""
        if name not in self.plugins:
            raise PluginNotFoundError(f"Plugin '{name}' not found")
        
        if name in self.loaded_plugins:
            return self.loaded_plugins[name]
        
        plugin_class = self.plugins[name]
        instance = plugin_class(*args, **kwargs)
        self.loaded_plugins[name] = instance
        return instance
    
    def discover_plugins(self, package_name: str) -> None:
        """Discover plugins in a package"""
        import importlib
        import pkgutil
        
        package = importlib.import_module(package_name)
        path = package.__path__
        
        for _, module_name, _ in pkgutil.iter_modules(path):
            if module_name.startswith('plugin_'):
                importlib.import_module(f"{package_name}.{module_name}")
```

### utils/context.py
```python
import contextlib
import time
from typing import Any, Generator

@contextlib.contextmanager
def resource_manager(resource_name: str):
    """Context manager for resource handling"""
    print(f"Acquiring {resource_name}...")
    resource = acquire_resource(resource_name)
    try:
        yield resource
    finally:
        print(f"Releasing {resource_name}...")
        release_resource(resource)

@contextlib.contextmanager
def timer(name: str):
    """Context manager for timing operations"""
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"{name} took {elapsed:.4f} seconds")

@contextlib.contextmanager
def database_transaction(connection):
    """Context manager for database transactions"""
    try:
        connection.begin()
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise

@contextlib.contextmanager
def file_lock(file_path: str):
    """Context manager for file locking"""
    import fcntl
    file = open(file_path, 'r+')
    try:
        fcntl.flock(file, fcntl.LOCK_EX)
        yield file
    finally:
        fcntl.flock(file, fcntl.LOCK_UN)
        file.close()
```

### utils/exceptions.py
```python
class CLIError(Exception):
    """Base class for CLI errors"""
    pass

class PluginError(CLIError):
    """Error related to plugins"""
    pass

class CommandError(CLIError):
    """Error related to commands"""
    pass

class ConfigurationError(CLIError):
    """Error related to configuration"""
    pass

class ValidationError(CLIError):
    """Error related to validation"""
    pass

class ResourceError(CLIError):
    """Error related to resource management"""
    pass

class PluginNotFoundError(PluginError):
    """Plugin not found error"""
    pass

class CommandNotFoundError(CommandError):
    """Command not found error"""
    pass

class ConfigurationParseError(ConfigurationError):
    """Error parsing configuration file"""
    pass

class InvalidPluginError(PluginError):
    """Invalid plugin error"""
    pass

class PluginDependencyError(PluginError):
    """Plugin dependency error"""
    pass

class ResourceUnavailableError(ResourceError):
    """Resource unavailable error"""
    pass

class TimeoutError(ResourceError):
    """Timeout error"""
    pass
```

### config.py
```python
import yaml
from pathlib import Path
from typing import Dict, Any, Optional

class Config:
    """Configuration management class"""
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @classmethod
    def from_file(cls, file_path: str) -> 'Config':
        """Load configuration from file"""
        path = Path(file_path)
        if not path.exists():
            raise ConfigurationError(f"Config file {file_path} not found")
        
        try:
            with open(file_path, 'r') as f:
                config_data = yaml.safe_load(f)
            return cls(config_data)
        except yaml.YAMLError as e:
            raise ConfigurationParseError(f"Error parsing config file: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
    
    def save(self, file_path: str) -> None:
        """Save configuration to file"""
        path = Path(file_path)
        try:
            with open(file_path, 'w') as f:
                yaml.safe_dump(self.config, f)
        except Exception as e:
            raise ConfigurationError(f"Error saving config file: {e}")
```

## Exercise Suggestions

### Exercise 1: Basic CLI Tool
1. Implement the basic CLI structure
2. Add a simple "hello" command
3. Add configuration file support
4. Implement help system

### Exercise 2: Plugin System
1. Create a plugin registry
2. Implement plugin discovery
3. Add plugin loading and unloading
4. Create a simple plugin example

### Exercise 3: Context Managers
1. Implement resource managers
2. Add timing context managers
3. Create database transaction managers
4. Add file locking mechanisms

### Exercise 4: Error Handling
1. Create custom exception hierarchy
2. Implement comprehensive error handling
3. Add error logging
4. Create user-friendly error messages

### Exercise 5: Advanced Features
1. Add command chaining
2. Implement interactive mode
3. Add plugin dependency management
4. Create plugin isolation

## Assessment Criteria

### Functionality (40%)
- All core features work correctly
- Plugin system is robust
- Error handling is comprehensive
- Configuration management works properly

### Code Quality (30%)
- Code follows PEP 8 style guidelines
- Type hints are used throughout
- Documentation is clear and comprehensive
- Error messages are user-friendly

### Testing (20%)
- Unit tests cover all major functionality
- Integration tests work correctly
- Test coverage is adequate
- Tests handle edge cases

### Documentation (10%)
- README is clear and comprehensive
- Code comments are helpful
- Examples are provided and working
- API documentation is complete

## Next Steps

1. Complete the basic CLI tool
2. Implement the plugin system
3. Add context managers for resource handling
4. Create comprehensive error handling
5. Write tests for all components
6. Add documentation and examples
7. Polish and optimize the final product