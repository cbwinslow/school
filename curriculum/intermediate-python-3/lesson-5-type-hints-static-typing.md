# Lesson 5: Type Hints and Static Typing

## Overview
This lesson covers Python's type hinting system and static typing, enabling better code documentation, IDE support, and error detection before runtime.

## Learning Objectives
By the end of this lesson, students will be able to:
- Add type hints to functions and variables
- Use basic and advanced type annotations
- Understand the benefits of static typing
- Use type checking tools like mypy
- Work with generic types and type variables
- Handle optional and union types
- Create type aliases for complex types
- Use protocols for structural subtyping
- Apply type hints in real-world scenarios

## Topics

### 5.1 Basic Type Hints

#### Function Type Hints
```python
def greet(name: str) -> str:
    """Function with type hints."""
    return f"Hello, {name}!"

# Usage
result = greet("Alice")  # result is inferred as str

# Multiple parameters
def add(a: int, b: int) -> int:
    return a + b

# Return type can be None
def get_user_by_id(user_id: int) -> Optional[User]:
    # Returns User object or None
    pass

# No return value
def log_message(message: str) -> None:
    print(f"LOG: {message}")
```

#### Variable Type Hints
```python
# Basic types
age: int = 25
name: str = "Bob"
is_active: bool = True

# Type hints without initialization
price: float
# price = "10"  # This would be flagged by type checker

# Collections
names: List[str] = ["Alice", "Bob", "Charlie"]
numbers: Dict[str, int] = {"one": 1, "two": 2}
coordinates: Tuple[int, int] = (10, 20)

# Type aliases for complex types
UserId = NewType('UserId', int)
user_id: UserId = UserId(123)
```

### 5.2 Advanced Type Hints

#### Optional and Union Types
```python
from typing import Optional, Union

# Optional type
def get_user_by_id(user_id: int) -> Optional[User]:
    """Returns User or None."""
    pass

# Union types
def process_value(value: Union[int, float, str]) -> str:
    """Accepts multiple types."""
    if isinstance(value, (int, float)):
        return str(value)
    return value

# Literal types (Python 3.8+)
def set_display_mode(mode: Literal['light', 'dark', 'auto']) -> None:
    """Only accepts specific string values."""
    pass
```

#### Generic Types
```python
from typing import TypeVar, Generic, List

# Type variables
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0

# Usage
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
```

#### Type Aliases
```python
from typing import Dict, List, Tuple

# Type aliases
UserId = int
UserName = str
UserEmail = str

# Complex type aliases
UserData = Dict[str, Union[int, str, bool]]
UserRecord = Tuple[UserId, UserName, UserEmail, UserData]

# Using type aliases
def create_user(user_id: UserId, name: UserName, email: UserEmail) -> UserRecord:
    return (user_id, name, email, {})

# Even more complex
def process_users(users: List[UserRecord]) -> Dict[UserId, UserData]:
    return {user_id: data for user_id, name, email, data in users}
```

### 5.3 Protocols and Structural Subtyping

#### Protocol Basics
```python
from typing import Protocol

# Protocol defines a contract based on structure
class SupportsGreeting(Protocol):
    def greet(self) -> str:
        """Return a greeting message."""
        pass

class Person:
    def __init__(self, name: str):
        self.name = name
    
    def greet(self) -> str:
        return f"Hello, I'm {self.name}"

class Robot:
    def __init__(self, model: str):
        self.model = model
    
    def greet(self) -> str:
        return f"Beep boop, I'm {self.model}"

# Function that works with any SupportsGreeting
def greet_user(entity: SupportsGreeting) -> None:
    print(entity.greet())

# Usage
person = Person("Alice")
robot = Robot("T-1000")

greet_user(person)  # Valid
greet_user(robot)   # Valid - doesn't need to inherit from Person
```

#### Generic Protocols
```python
from typing import TypeVar, Protocol

T = TypeVar('T')

class Container(Protocol[T]):
    def get(self, key: str) -> T:
        """Get item by key."""
        pass
    
    def set(self, key: str, value: T) -> None:
        """Set item by key."""
        pass

class InMemoryCache(Container[str]):
    def __init__(self):
        self._data: Dict[str, str] = {}
    
    def get(self, key: str) -> str:
        return self._data.get(key, "")
    
    def set(self, key: str, value: str) -> None:
        self._data[key] = value

class DatabaseStore(Container[int]):
    def __init__(self, db):
        self.db = db
    
    def get(self, key: str) -> int:
        # Query database
        return 0
    
    def set(self, key: str, value: int) -> None:
        # Update database
        pass

# Function that works with any Container
def process_container(container: Container[T]) -> None:
    container.set("key", "value")
    result = container.get("key")
    print(f"Got: {result}")
```

### 5.4 Type Checking and Tools

#### Using mypy
```python
# mypy.ini configuration
# [mypy]
# python_version = 3.9
# warn_return_any = True
# warn_unused_configs = True
# disallow_untyped_defs = True

# Example code to check

def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    return a / b

# mypy will flag this:
# result = divide(10, 0)  # No error at runtime, but type checking can help

# Correct usage
result = divide(10, 2)  # OK
```

#### Type Checking Best Practices
```python
# Use --strict flag for thorough checking
# mypy --strict my_module.py

# Common type checking options
# disallow_untyped_defs = True  # Require type hints for all functions
# disallow_incomplete_defs = True  # Don't allow partial type hints
# warn_redundant_casts = True  # Warn about unnecessary casts
# warn_unused_ignores = True  # Warn about unused # type: ignore

# Suppressing type errors (use sparingly)
x = "42"  # type: ignore  # Reason: external API returns wrong type

# Type comments for complex cases
x = 5  # type: int
```

### 5.5 Advanced Type Hint Patterns

#### Callable Types
```python
from typing import Callable

# Type hint for functions
def apply_operation(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    """Apply a binary operation."""
    return operation(a, b)

# Usage
result = apply_operation(lambda x, y: x + y, 3, 4)  # 7
result = apply_operation(lambda x, y: x * y, 3, 4)  # 12
```

#### Type Variables with Constraints
```python
from typing import TypeVar, Sequence

# Constrained type variable
T = TypeVar('T', int, float, str)

# This function only accepts int, float, or str

def find_max(values: Sequence[T]) -> T:
    """Find maximum value in a sequence."""
    if not values:
        raise ValueError("Empty sequence")
    return max(values)

# Usage
print(find_max([1, 2, 3]))        # OK
print(find_max([1.1, 2.2, 3.3]))  # OK
print(find_max(['a', 'b', 'c']))   # OK
# print(find_max([True, False]))  # Error: bool not in constraints
```

#### Recursive Types
```python
from typing import Dict, List, Union, Optional

# Recursive type for tree structures
TreeNode = Dict[str, Union[int, 'TreeNode', None]]

# Example tree
def create_tree() -> TreeNode:
    return {
        'value': 1,
        'left': {
            'value': 2,
            'left': None,
            'right': None
        },
        'right': {
            'value': 3,
            'left': None,
            'right': None
        }
    }

# Function to traverse tree
def sum_tree(node: TreeNode) -> int:
    if node is None:
        return 0
    return (node['value'] + 
            sum_tree(node['left']) + 
            sum_tree(node['right']))
```

### 5.6 Type Hints in Real-World Scenarios

#### Class Methods and Properties
```python
from typing import ClassVar, final

class BaseClass:
    class_counter: ClassVar[int] = 0  # Class variable
    
    def __init__(self, name: str):
        self.name: str = name
        BaseClass.class_counter += 1
    
    @final  # Cannot be overridden
    def get_name(self) -> str:
        return self.name
    
    @property
    def name_length(self) -> int:
        return len(self.name)
    
    @name_length.setter
    def name_length(self, length: int) -> None:
        raise AttributeError("Cannot set name_length directly")
```

#### Type Hints for Async Code
```python
import asyncio
from typing import Awaitable

async def fetch_data(url: str) -> Awaitable[dict]:
    """Fetch data from URL."""
    await asyncio.sleep(1)
    return {"url": url, "data": "example"}

# Type hint for coroutine
def process_data() -> Awaitable[None]:
    """Process data asynchronously."""
    data = await fetch_data("https://example.com")
    print(data)
```

#### Type Hints for Decorators
```python
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def log_calls(func: F) -> F:
    """Decorator that logs function calls."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a: int, b: int) -> int:
    return a + b

# Type checking ensures the decorator preserves type information
result: int = add(3, 4)  # Type checker knows this is int
```

## Exercises

### Exercise 5.1: Basic Type Hints
Add type hints to a simple calculator module.

### Exercise 5.2: Generic Data Structures
Implement a generic queue class with proper type hints.

### Exercise 5.3: Protocol Implementation
Create a protocol for a storage interface and implement it with different backends.

### Exercise 5.4: Type Checking
Write a module with type hints and verify it with mypy.

### Exercise 5.5: Complex Type Aliases
Create type aliases for a complex domain model (e.g., e-commerce system).

### Exercise 5.6: Type Hints for Decorators
Write a decorator that preserves type information.

## Assessment Questions

1. What are the benefits of using type hints in Python?
2. How do type variables enable generic programming?
3. What is the difference between nominal and structural subtyping?
4. When would you use a protocol versus an abstract base class?
5. How does mypy help catch errors before runtime?

## Real-World Applications
- Building large-scale applications with better maintainability
- Creating reusable libraries with clear interfaces
- Improving IDE support and autocompletion
- Catching bugs early in development
- Documenting code through type annotations
- Enabling static analysis and refactoring tools