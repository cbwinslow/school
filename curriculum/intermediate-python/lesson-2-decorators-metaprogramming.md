# Lesson 2: Decorators and Metaprogramming

## Overview

This lesson explores Python's powerful decorator and metaprogramming capabilities, allowing developers to write more concise, reusable, and dynamic code.

## Duration
2-3 hours

## Prerequisites
- Understanding of functions as first-class objects
- Basic knowledge of classes and objects
- Familiarity with Python syntax

## Topics Covered

### 1. Function Decorators
- Basic decorator syntax and patterns
- Parameterized decorators
- Decorator with arguments
- Preserving metadata with `functools.wraps`

### 2. Class Decorators
- Decorating classes vs functions
- Class decorator patterns
- Metaclasses vs class decorators
- Dynamic class modification

### 3. Decorator Patterns
- Authentication and authorization decorators
- Logging and timing decorators
- Caching decorators
- Validation decorators

### 4. Metaclasses
- Creating custom metaclasses
- Metaclass usage patterns
- Singleton pattern with metaclasses
- Class registration with metaclasses

### 5. Introspection and Reflection
- Inspecting objects at runtime
- Dynamic attribute access
- Modifying classes at runtime
- Using `getattr`, `setattr`, `hasattr`

## Key Concepts

### Function Decorators
```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### Parameterized Decorators
```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello():
    print("Hello!")

print(say_hello())
```

### Class Decorators
```python
def add_logging(cls):
    original_init = cls.__init__
    
    def __init__(self, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        original_init(self, *args, **kwargs)
    
    cls.__init__ = __init__
    return cls

@add_logging
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Bob", 25)
```

### Metaclasses
```python
declare_registry = {}

def register_class(cls):
    declare_registry[cls.__name__] = cls
    return cls

@register_class
def MyClass:
    pass

print(declare_registry)
```

### Singleton Metaclass
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Database connection established"

conn1 = DatabaseConnection()
conn2 = DatabaseConnection()
print(conn1 is conn2)  # True
```

## Project Integration

### Command Registration System

The CLI tool uses decorators for automatic command registration:

```python
command_registry = {}

def command(name: str, description: str = ""):
    def decorator(func):
        command_registry[name] = {
            "function": func,
            "description": description
        }
        return func
    return decorator

@command("hello", "Say hello to someone")
def hello_command(name: str):
    return f"Hello, {name}!"

@command("add", "Add two numbers")
def add_command(a: float, b: float):
    return a + b
```

### Plugin Discovery with Decorators
```python
def plugin(category: str):
    def decorator(cls):
        cls._plugin_category = category
        return cls
    return decorator

@plugin("input")
class FileInputPlugin:
    def read(self, path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

@plugin("output")
class ConsoleOutputPlugin:
    def write(self, content: str) -> None:
        print(content)
```

### Authentication Decorator
```python
def authenticated(func):
    def wrapper(*args, **kwargs):
        if not hasattr(args[0], 'user') or not args[0].user.is_authenticated:
            raise PermissionError("Authentication required")
        return func(*args, **kwargs)
    return wrapper

class SecureCLI:
    def __init__(self, user):
        self.user = user
    
    @authenticated
    def sensitive_operation(self):
        return "Performing sensitive operation..."
```

## Exercises

### Exercise 1: Basic Decorator
Create a decorator that measures the execution time of a function and prints the result.

### Exercise 2: Parameterized Decorator
Create a decorator that retries a function up to N times if it fails with a specific exception.

### Exercise 3: Class Decorator
Create a class decorator that adds a `to_json()` method to any class, converting its attributes to a JSON string.

### Exercise 4: Metaclass Registration
Create a metaclass that automatically registers all classes that use it in a global registry.

### Exercise 5: Plugin System
Create a plugin system using decorators where plugins can be discovered and loaded dynamically.

## Real-World Applications

- **Web frameworks** (Flask, Django) using decorators for routing
- **Authentication systems** with decorator-based access control
- **Caching mechanisms** with decorators for memoization
- **Plugin architectures** using class decorators for discovery
- **Database ORMs** using metaclasses for model definition
- **API clients** with decorators for request/response handling

## Common Pitfalls

- **Losing function metadata** without `functools.wraps`
- **Overcomplicating simple functions** with unnecessary decorators
- **Circular dependencies** in decorator chains
- **Performance overhead** from excessive decoration
- **Debugging difficulties** with wrapped functions
- **Metaclass conflicts** when multiple metaclasses are involved

## Assessment Criteria

Students will be evaluated on:
- **Decorator Implementation** (30%): Correct use of decorator patterns and syntax
- **Metaprogramming Understanding** (25%): Proper use of metaclasses and introspection
- **Code Quality** (20%): Clean, readable, and maintainable code
- **Project Integration** (15%): Effective use in CLI tool context
- **Testing** (10%): Unit tests for decorated functions and classes

## Additional Resources

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [Metaclasses in Python](https://realpython.com/python-metaclasses/)
- [Effective Python: Decorators](https://effectivepython.com/)
- [Python Metaclasses Guide](https://python-patterns.guide/)
- [Decorator Pattern](https://refactoring.guru/design-patterns/decorator)
- [functools.wraps Documentation](https://docs.python.org/3/library/functools.html#functools.wraps)
```

### 2.4 Metaclasses
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}
    
    def set(self, key, value):
        self.settings[key] = value
    
    def get(self, key):
        return self.settings.get(key)

# Usage
config1 = Config()
config2 = Config()
config1.set("theme", "dark")
print(config2.get("theme"))  # Should print "dark"
```
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

@repeat(5)
def count_down():
    for i in range(3, 0, -1):
        print(i)
    print("Go!")

# Usage
greet("Alice")
count_down()
```
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

@repeat(5)
def count_down():
    for i in range(5, 0, -1):
        print(i)
```

### 2.3 Class Decorators
```python
def add_methods(cls):
    def new_method(self):
        return f"Instance of {self.__class__.__name__}"
    
    cls.new_method = new_method
    return cls

@add_methods
class MyClass:
    pass

@add_methods
class AnotherClass:
    pass

# Usage
obj1 = MyClass()
print(obj1.new_method())  # Instance of MyClass

obj2 = AnotherClass()
print(obj2.new_method())  # Instance of AnotherClass
```

### 2.4 Decorators for Authentication
```python
def require_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = kwargs.get('user')
            if user is None or user.role != role:
                raise PermissionError(f"User must be {role} to access this function")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

@require_role('admin')
def delete_user(user, target_user):
    print(f"Deleting user {target_user.name}")

@require_role('manager')
def update_user(user, target_user, new_data):
    print(f"Updating user {target_user.name}")
```

### 2.5 Caching Decorators
```python
def cache(max_size=128):
    from collections import OrderedDict
    
    def decorator(func):
        cache_store = OrderedDict()
        
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache_store:
                cache_store.move_to_end(key)
                return cache_store[key]
            
            result = func(*args, **kwargs)
            cache_store[key] = result
            
            if len(cache_store) > max_size:
                cache_store.popitem(last=False)
            
            return result
        
        return wrapper
    return decorator

@cache(max_size=32)
def expensive_computation(x):
    print(f"Computing for {x}...")
    return x ** 2
```

### 2.6 Class Method and Static Method Decorators
```python
def validate_input(func):
    def wrapper(cls, *args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("All arguments must be numbers")
        return func(cls, *args, **kwargs)
    return wrapper

class Calculator:
    @classmethod
    @validate_input
    def add(cls, a, b):
        return a + b
    
    @classmethod
    @validate_input
    def multiply(cls, a, b):
        return a * b
    
    @staticmethod
    @validate_input
    def power(base, exponent):
        return base ** exponent
```

### 2.7 Metaclasses
```python
def validate_attributes(cls_name, bases, attrs):
    if 'name' not in attrs:
        raise TypeError("Class must have a 'name' attribute")
    
    if 'age' in attrs and not isinstance(attrs['age'], int):
        raise TypeError("'age' must be an integer")
    
    return type(cls_name, bases, attrs)

class PersonMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name}")
        return validate_attributes(name, bases, attrs)

class Person(metaclass=PersonMeta):
    name = "Unknown"
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This will raise an error:
# class InvalidPerson(metaclass=PersonMeta):
#     age = "twenty"  # Invalid type
```

### 2.8 Decorator Pattern
```python
class DataSource:
    def get_data(self):
        raise NotImplementedError

class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename
    
    def get_data(self):
        with open(self.filename, 'r') as f:
            return f.read()

class DataSourceDecorator(DataSource):
    def __init__(self, data_source):
        self._data_source = data_source
    
    def get_data(self):
        return self._data_source.get_data()

class EncryptionDecorator(DataSourceDecorator):
    def get_data(self):
        data = super().get_data()
        return self.encrypt(data)
    
    def encrypt(self, data):
        # Simple XOR encryption for demonstration
        key = 42
        return ''.join(chr(ord(c) ^ key) for c in data)

class CompressionDecorator(DataSourceDecorator):
    def get_data(self):
        data = super().get_data()
        return self.compress(data)
    
    def compress(self, data):
        # Simple run-length encoding for demonstration
        import re
        return re.sub(r'(.)\1+', lambda m: m.group(1) + str(len(m.group(0))), data)
```

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Execution {i + 1}/{times}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

@repeat(2)
def calculate():
    return 42

# Usage
say_hello()
print(calculate())
```

### 3. Using functools.wraps

```python
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

# Usage
slow_function()
print(slow_function.__name__)  # slow_function (preserved)
```

### 4. Class Decorators

```python
def add_methods(cls):
    def method_one(self):
        return f"Instance of {self.__class__.__name__}"
    
    def method_two(self):
        return "This is method two"
    
    cls.method_one = method_one
    cls.method_two = method_two
    return cls

@add_methods
class MyClass:
    pass

# Usage
obj = MyClass()
print(obj.method_one())
print(obj.method_two())
```

### 5. Decorators with State

```python
def counter(func):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    
    wrapper.count = lambda: count
    return wrapper

@counter
def process_data(data):
    return len(data)

# Usage
process_data([1, 2, 3])
process_data([4, 5, 6, 7])
print(f"Total calls: {process_data.count()}")
```

### 6. Common Decorator Patterns

#### Logging Decorator

```python
def logger(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{level}] Finished {func.__name__}")
            return result
        return wrapper
    return decorator

@logger("DEBUG")
def complex_operation(x, y):
    return x ** y
```

#### Validation Decorator

```python
def validate(**validators):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Validate positional arguments
            for i, (arg, validator) in enumerate(zip(args, validators.values())):
                if not validator(arg):
                    raise ValueError(f"Argument {i} failed validation")
            
            # Validate keyword arguments
            for name, value in kwargs.items():
                if name in validators and not validators[name](value):
                    raise ValueError(f"Argument {name} failed validation")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate(
    age=lambda x: isinstance(x, int) and x > 0,
    name=lambda x: isinstance(x, str) and len(x) > 0
)
def create_user(name, age):
    return {"name": name, "age": age}
```

### 7. Metaclasses

```python
def make_debug_meta(name, bases, attrs):
    # Create a new class with debug capabilities
    new_class = type(name, bases, attrs)
    
    # Add debug method to all classes created with this metaclass
    def debug(self):
        print(f"Debug info for {self.__class__.__name__}:")
        for key, value in self.__dict__.items():
            print(f"  {key}: {value}")
    
    new_class.debug = debug
    return new_class

class DebugMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        
        # Add debug method
        def debug(self):
            print(f"Debug info for {self.__class__.__name__}:")
            for key, value in self.__dict__.items():
                print(f"  {key}: {value}")
        
        new_class.debug = debug
        return new_class

class MyClass(metaclass=DebugMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Usage
obj = MyClass(10, 20)
obj.debug()
```

### 8. Decorator Factories

```python
def create_decorator_factory(name):
    def decorator_factory(message):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{name}] {message}")
                result = func(*args, **kwargs)
                print(f"[{name}] Completed {func.__name__}")
                return result
            return wrapper
        return decorator
    return decorator_factory

# Create specific decorators
log_info = create_decorator_factory("INFO")
log_error = create_decorator_factory("ERROR")

@log_info("Processing request")
def handle_request(data):
    return f"Processed: {data}"

@log_error("Critical operation")
def critical_operation():
    return "Critical result"
```

## Exercises

### Exercise 1: Create a Timing Decorator

Create a decorator that measures execution time and logs it. Add features like:
- Configurable logging level
- Memory usage tracking
- Support for async functions

### Exercise 2: Build a Caching Decorator

Create a decorator that caches function results:
- Implement LRU (Least Recently Used) cache
- Add cache size limits
- Support for cache invalidation
- Handle mutable arguments

### Exercise 3: Implement a Validation System

Create a comprehensive validation decorator system:
- Support for multiple validation rules
- Custom error messages
- Validation for different data types
- Integration with Pydantic models

### Exercise 4: Create a Plugin System

Build a plugin system using decorators:
- Plugin discovery mechanism
- Plugin registration
- Plugin lifecycle management
- Configuration handling

## Assessment Questions

1. What is the difference between a decorator and a higher-order function?
2. Why is functools.wraps important in decorator implementation?
3. How do metaclasses differ from class decorators?
4. What are the potential pitfalls of using decorators?
5. How would you create a decorator that works with both sync and async functions?