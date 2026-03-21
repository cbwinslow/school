# Lesson 2: Decorators and Metaprogramming

## Lesson Overview
This lesson explores decorators and metaprogramming techniques in Python. Students will learn how to create reusable decorators, understand class decorators, and use metaprogramming to dynamically modify code behavior.

## Learning Objectives
By the end of this lesson, students will be able to:
- Create and use function decorators
- Implement class decorators
- Use decorators with arguments
- Understand and use metaclasses
- Create decorators for timing, logging, and caching
- Apply decorators to class methods and static methods
- Use decorators for authentication and authorization
- Understand the decorator pattern and its applications

## Topics Covered

### 2.1 Function Decorators
```python
import time
from functools import wraps
from typing import Callable, Any

def timer_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def logger_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def retry_decorator(max_retries: int = 3, delay: float = 1.0):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

# Usage
@timer_decorator
@logger_decorator
@retry_decorator(max_retries=3, delay=0.5)
def compute_risky_operation(x: int, y: int) -> int:
    if x < 0 or y < 0:
        raise ValueError("Negative values not allowed")
    return x ** y

result = compute_risky_operation(2, 10)
print(f"Result: {result}")
```

### 2.2 Class Decorators
```python
from typing import Type, Dict, Any

def singleton(cls: Type[Any]) -> Type[Any]:
    """Class decorator to implement Singleton pattern"""
    instances: Dict[Type[Any], Any] = {}
    
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
def DatabaseConnection:
    def __init__(self):
        self.connected = False
        print("Initializing database connection...")
    
    def connect(self):
        if not self.connected:
            print("Connecting to database...")
            self.connected = True
    
    def disconnect(self):
        if self.connected:
            print("Disconnecting from database...")
            self.connected = False

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")  # True
```

### 2.3 Decorators with Arguments
```python
from typing import Callable, Any

def validate_input(**validators: Callable) -> Callable:
    """Decorator for validating function arguments"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Validate positional arguments
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            for name, value in bound_args.arguments.items():
                if name in validators:
                    validator = validators[name]
                    if not validator(value):
                        raise ValueError(f"Invalid value for {name}: {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_input(
    age=lambda x: isinstance(x, int) and x >= 0,
    email=lambda x: isinstance(x, str) and '@' in x
)
def register_user(name: str, age: int, email: str) -> dict:
    return {
        "name": name,
        "age": age,
        "email": email
    }

# Usage
user1 = register_user("Alice", 25, "alice@example.com")
# register_user("Bob", -5, "bob")  # This would raise ValueError
```

### 2.4 Metaclasses
```python
from typing import Type, Dict, Any

def enforce_methods(*methods: str):
    """Metaclass to enforce implementation of specific methods"""
    class EnforceMethodsMeta(type):
        def __new__(cls, name: str, bases: tuple, namespace: Dict[str, Any]) -> Type[Any]:
            for method in methods:
                if method not in namespace:
                    raise TypeError(f"Class {name} must implement method: {method}")
            return super().__new__(cls, name, bases, namespace)
    return EnforceMethodsMeta

class AbstractProcessor(metaclass=enforce_methods('process', 'validate')):
    """Base class that requires process and validate methods"""
    pass

class DataProcessor(AbstractProcessor):
    def process(self, data: dict) -> dict:
        return {k: v * 2 for k, v in data.items()}
    
    def validate(self, data: dict) -> bool:
        return all(isinstance(v, (int, float)) for v in data.values())

# Usage
dp = DataProcessor()
data = {'a': 1, 'b': 2}
if dp.validate(data):
    result = dp.process(data)
    print(result)  # {'a': 2, 'b': 4}
```

### 2.5 Class Decorators for Registration
```python
from typing import List, Type, Dict, Any

class CommandRegistry:
    """Registry for command classes"""
    _registry: Dict[str, Type[Any]] = {}
    
    @classmethod
    def register(cls, name: str):
        def decorator(cmd_class: Type[Any]) -> Type[Any]:
            cls._registry[name] = cmd_class
            return cmd_class
        return decorator
    
    @classmethod
    def get_command(cls, name: str) -> Type[Any]:
        return cls._registry.get(name)

@CommandRegistry.register("hello")
class HelloCommand:
    def execute(self, name: str) -> str:
        return f"Hello, {name}!"

@CommandRegistry.register("goodbye")
class GoodbyeCommand:
    def execute(self, name: str) -> str:
        return f"Goodbye, {name}!"

# Usage
hello_cmd = CommandRegistry.get_command("hello")()
print(hello_cmd.execute("Alice"))  # Hello, Alice!
```

## Exercises

### Exercise 2.1: Timing Decorator
Create a decorator that measures the execution time of functions and methods:
- Should work with any function
- Should print the execution time in seconds
- Should preserve the original function's metadata
- Add an option to log the timing information to a file

### Exercise 2.2: Authentication Decorator
Create a decorator for user authentication:
- Should check if a user is authenticated before allowing function execution
- Should support different permission levels (admin, user, guest)
- Should redirect to login if not authenticated
- Should cache authentication status for performance

### Exercise 2.3: Caching Decorator
Create a caching decorator for expensive function calls:
- Should cache results based on function arguments
- Should support time-based cache expiration
- Should limit the cache size
- Should provide a way to clear the cache

### Exercise 2.4: Plugin System with Decorators
Create a plugin system using decorators:
- Should allow plugins to register themselves automatically
- Should support plugin categories
- Should provide plugin discovery and loading
- Should handle plugin dependencies

## Assessment Questions

1. What is the difference between a decorator and a higher-order function?
2. How does the `@wraps` decorator from `functools` help when creating decorators?
3. Explain how class decorators differ from function decorators.
4. What are metaclasses, and when would you use them?
5. How can decorators be used to implement design patterns like Singleton or Factory?