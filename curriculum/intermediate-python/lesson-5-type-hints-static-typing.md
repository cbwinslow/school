# Lesson 5: Type Hints and Static Typing

## Lesson Overview
This lesson covers type hints and static typing in Python, focusing on how to add type annotations to code for better documentation, error detection, and IDE support. Students will learn how to use type hints effectively and integrate them with static type checkers.

## Learning Objectives
By the end of this lesson, students will be able to:
- Add type hints to functions and variables
- Use basic type annotations (int, str, list, dict, etc.)
- Work with generic types and type parameters
- Use the typing module for complex type hints
- Apply type hints to class methods and properties
- Use type aliases for better readability
- Integrate mypy for static type checking
- Understand the benefits and limitations of type hints

## Topics Covered

### 5.1 Basic Type Hints
```python
def greet(name: str) -> str:
    """Function with type hints"""
    return f"Hello, {name}!"

# Usage
message = greet("Alice")
print(message)

# Variable type hints
age: int = 25
name: str = "Bob"

# Type hints with default values
def calculate_area(
    width: float = 0.0,
    height: float = 0.0
) -> float:
    return width * height

# Type hints for multiple return values
def get_user_info(user_id: int) -> tuple[str, int]:
    """Return name and age"""
    return "Alice", 30

# Type hints for optional parameters
def send_message(
    recipient: str,
    message: str,
    priority: int = 1
) -> bool:
    print(f"Sending to {recipient}: {message}")
    return True

# Type hints for None return

def log_message(message: str) -> None:
    print(f"LOG: {message}")

# Type hints for any

def process_data(data: any) -> any:
    return data
```

### 5.2 Generic Types and Type Parameters
```python
from typing import List, Dict, Tuple, Set, Optional, Union

# List type hints

def process_items(items: List[int]) -> List[int]:
    return [item * 2 for item in items]

# Dict type hints

def get_user_data(user_id: int) -> Dict[str, Union[str, int]]:
    return {"id": user_id, "name": "Alice", "age": 30}

# Tuple type hints

def get_coordinates() -> Tuple[float, float, float]:
    return (12.34, 56.78, 90.12)

# Set type hints

def unique_items(items: Set[int]) -> Set[int]:
    return {item for item in items if item > 0}

# Optional type hints

def get_optional_value(value: Optional[int]) -> Optional[int]:
    return value if value is not None else 0

# Union type hints

def process_value(value: Union[int, float, str]) -> str:
    return str(value)

# Type aliases

UserId = int
UserName = str
User = Dict[str, Union[UserId, UserName, int]]


def create_user(user_id: UserId, name: UserName, age: int) -> User:
    return {"id": user_id, "name": name, "age": age}
```

### 5.3 Class Type Hints
```python
from typing import Generic, TypeVar

# Type variables
T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content
    
    def get_content(self) -> T:
        return self.content

# Usage
int_box = Box[int](42)
str_box = Box[str]("Hello")

print(int_box.get_content())  # 42
print(str_box.get_content())  # Hello

# Class methods with type hints
class MathOperations:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        return a * b

# Properties with type hints
class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

### 5.4 Advanced Type Hints
```python
from typing import Callable, Iterable, Iterator, Protocol

# Callable type hints

def process_with_callback(
    data: List[int],
    callback: Callable[[int], int]
) -> List[int]:
    return [callback(item) for item in data]

# Iterable and Iterator type hints

def process_iterable(
    items: Iterable[int]
) -> Iterator[int]:
    for item in items:
        yield item * 2

# Protocol (structural subtyping)
class SupportsAdd(Protocol):
    def __add__(self, other: Any) -> Any:
        ...


def add_protocol(a: SupportsAdd, b: SupportsAdd) -> SupportsAdd:
    return a + b

# Generic protocols
class Container(Protocol[T]):
    def get(self) -> T:
        ...
    
    def put(self, item: T) -> None:
        ...

# Type checking with mypy

# mypy example.py
# Success: no type errors
# Error: type mismatch
```

### 5.5 Type Checking and Best Practices
```python
# mypy configuration
# mypy.ini
# [mypy]
# python_version = 3.11
# warn_return_any = True
# warn_unused_configs = True
# disallow_untyped_defs = True

# Type checking in development

def add_numbers(a: int, b: int) -> int:
    return a + b

# This will be caught by mypy
# result = add_numbers(1, "2")  # Error: incompatible types

# Type comments (for older Python versions)

def legacy_function(a, b):
    # type: (int, int) -> int
    return a + b

# Type stubs
# For third-party libraries without type hints

# Using type hints with dataclasses
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    name: str
    email: Optional[str] = None
    age: Optional[int] = None

# Type hints with async functions
import asyncio

async def fetch_data(url: str) -> dict:
    await asyncio.sleep(1)
    return {"url": url, "data": "example"}

# Type hints with context managers
from contextlib import contextmanager

@contextmanager
def open_file(path: str, mode: str):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()
```
    """Send a message with optional priority"""
    print(f"Sending to {recipient}: {message}")
    return True
```

### 5.2 Container Types
```python
from typing import List, Dict, Tuple, Set

# List type hints
def process_numbers(numbers: List[int]) -> List[int]:
    """Process a list of numbers"""
    return [n * 2 for n in numbers]

# Dictionary type hints
def count_words(text: str) -> Dict[str, int]:
    """Count word frequencies"""
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

# Tuple type hints
def get_coordinates() -> Tuple[float, float, float]:
    """Return 3D coordinates"""
    return (12.5, 45.3, 78.9)

# Set type hints
def unique_items(items: Set[int]) -> Set[int]:
    """Return unique items"""
    return items

# Nested container types
def process_data(
    data: Dict[str, List[int]]
) -> Dict[str, int]:
    """Process nested data structures"""
    result = {}
    for key, values in data.items():
        result[key] = sum(values)
    return result
```

### 5.3 Generic Types
```python
from typing import TypeVar, Generic

# Type variables
T = TypeVar('T')

# Generic class
def find_first(items: List[T], target: T) -> int:
    """Find the index of the first occurrence of target"""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

# Generic function
def first_element(items: List[T]) -> T:
    """Return the first element of a list"""
    if items:
        return items[0]
    raise ValueError("List is empty")

# Generic class
def swap_elements(items: List[T], i: int, j: int) -> List[T]:
    """Swap two elements in a list"""
    if i < 0 or i >= len(items) or j < 0 or j >= len(items):
        raise IndexError("Index out of range")
    
    items[i], items[j] = items[j], items[i]
    return items
```

### 5.4 Complex Type Hints
```python
from typing import Optional, Union, Any, Callable

# Optional type hints
def get_user(user_id: int) -> Optional[dict]:
    """Return user data or None if not found"""
    users = {1: {"name": "Alice", "age": 30}}
    return users.get(user_id)

# Union type hints
def process_value(value: Union[int, float, str]) -> str:
    """Process different types of values"""
    if isinstance(value, (int, float)):
        return f"Number: {value}"
    return f"String: {value}"

# Any type hints
def process_anything(value: Any) -> str:
    """Process any type of value"""
    return str(value)

# Callable type hints
def apply_operation(
    numbers: List[int],
    operation: Callable[[int], int]
) -> List[int]:
    """Apply a function to each number"""
    return [operation(n) for n in numbers]

# Usage
def square(x: int) -> int:
    return x ** 2

def double(x: int) -> int:
    return x * 2

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
doubled = apply_operation(numbers, double)
```

### 5.5 Class Type Hints
```python
from typing import List, Dict, Optional

class User:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
    
    def greet(self) -> str:
        """Return a greeting message"""
        return f"Hello, I'm {self.name}"
    
    def is_adult(self) -> bool:
        """Check if user is an adult"""
        return self.age >= 18

class UserManager:
    def __init__(self):
        self.users: Dict[int, User] = {}
    
    def add_user(self, user: User) -> None:
        """Add a user to the manager"""
        self.users[user.age] = user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get a user by ID"""
        return self.users.get(user_id)
    
    def get_adults(self) -> List[User]:
        """Get all adult users"""
        return [user for user in self.users.values() if user.is_adult()]

# Usage
manager = UserManager()
manager.add_user(User("Alice", 25))
manager.add_user(User("Bob", 17))
adults = manager.get_adults()
```

### 5.6 Type Aliases
```python
from typing import List, Dict, Tuple

# Type aliases for better readability
UserId = int
UserName = str
UserAge = int

# Using type aliases
UserRecord = Dict[UserName, UserAge]
UserList = List[UserId]

# Functions using type aliases
def get_user_name(user_id: UserId) -> UserName:
    """Get user name by ID"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id, "Unknown")

# Complex type aliases
Point = Tuple[float, float]
Color = Tuple[int, int, int]

# Functions using complex type aliases
def calculate_distance(
    point1: Point,
    point2: Point
) -> float:
    """Calculate distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Classes using type aliases
class Shape:
    def __init__(self, points: List[Point]):
        self.points: List[Point] = points
    
    def area(self) -> float:
        """Calculate area (placeholder)"""
        return 0.0
```

### 5.7 Static Type Checking with mypy
```python
# mypy configuration
# mypy.ini
# [mypy]
# python_version = 3.8
# warn_return_any = True
# warn_unused_configs = True

# Example code to check with mypy

def add_numbers(a: int, b: int) -> int:
    return a + b

# This will cause a mypy error
# result = add_numbers(5, "3")  # Error: Argument 2 has incompatible type "str"; expected "int"

# Correct usage
result = add_numbers(5, 3)  # OK

# Type checking in practice

def process_data(
    data: List[Union[int, float]],
    operation: str
) -> Union[int, float, None]:
    """Process data with type checking"""
    if operation == "sum":
        return sum(data)
    elif operation == "average":
        if data:
            return sum(data) / len(data)
        return None
    else:
        raise ValueError(f"Unknown operation: {operation}")

# Usage
numbers = [1, 2, 3, 4, 5]
total = process_data(numbers, "sum")
avg = process_data(numbers, "average")
```

## Exercises

### Exercise 5.1: Type Hints
Add type hints to a simple calculator program.

### Exercise 5.2: Generic Functions
Create generic functions that work with different data types.

### Exercise 5.3: Type Checking
Use mypy to check a Python module for type errors.

### Exercise 5.4: Type Aliases
Create type aliases for a data processing application.

## Assessment Questions

1. What is the purpose of type hints in Python?
2. How do you handle optional return values with type hints?
3. What is the difference between List[int] and list[int]?
4. When would you use a type alias?

## Real-World Applications
- Building large-scale applications with better code documentation
- Creating libraries and APIs with clear interfaces
- Improving IDE support and code completion
- Detecting type-related bugs before runtime
- Facilitating code maintenance and refactoring