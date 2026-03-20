# 🐍 Python Best Practices Knowledge Base

## Overview
This knowledge file contains Python best practices, patterns, and common pitfalls. Reference this when creating Python lessons, reviewing code, or helping with Python questions.

---

## 🎯 Core Principles

### The Zen of Python
```python
import this
```

**Key Principles:**
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

---

## 📋 Code Style (PEP 8)

### Naming Conventions
```python
# Variables and functions: snake_case
user_name = "John"
def calculate_total():
    pass

# Classes: PascalCase
class UserManager:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
API_BASE_URL = "https://api.example.com"

# Private: leading underscore
class Config:
    def __init__(self):
        self._internal_state = {}  # Private
        self.__very_private = {}   # Name mangled
```

### Line Length
- Maximum 79 characters for code
- Maximum 72 for comments/docstrings
- Use parentheses for line continuation

```python
# Good
result = some_function(
    argument1,
    argument2,
    argument3
)

# Bad
result = some_function(argument1, argument2, argument3, argument4, argument5)
```

### Imports
```python
# Order: stdlib, third-party, local
import os
import sys
from pathlib import Path

import requests
import pandas as pd

from myproject.models import User
from myproject.utils import helpers

# One import per line (preferred)
import os
import sys

# NOT: import os, sys
```

---

## 🏗️ Design Patterns

### Decorator Pattern
```python
from functools import wraps
import time

def timer(func):
    """Measure execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"
```

### Context Manager
```python
from contextlib import contextmanager

@contextmanager
def database_connection(url):
    """Manage database connections safely."""
    conn = create_connection(url)
    try:
        yield conn
    finally:
        conn.close()

# Usage
with database_connection("sqlite:///db.sqlite") as conn:
    conn.execute("SELECT * FROM users")
```

### Singleton Pattern
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Pattern
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_factory(animal_type: str) -> Animal:
    """Create animals based on type."""
    animals = {
        "dog": Dog,
        "cat": Cat
    }
    return animals[animal_type]()
```

---

## 🔧 Type Hints

### Basic Types
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

### Optional and Union
```python
from typing import Optional, Union

def find_user(user_id: int) -> Optional[User]:
    """Return User or None."""
    return db.get(user_id) or None

def process(value: Union[int, str]) -> str:
    """Accept int or str."""
    return str(value)

# Python 3.10+
def process(value: int | str) -> str:
    return str(value)
```

### Generic Types
```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
```

---

## ⚠️ Common Pitfalls

### Mutable Default Arguments
```python
# BAD
def add_item(item, items=[]):
    items.append(item)
    return items

# GOOD
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Late Binding Closures
```python
# BAD - All functions return 3
functions = []
for i in range(3):
    functions.append(lambda: i)

# GOOD - Use default argument
functions = []
for i in range(3):
    functions.append(lambda i=i: i)
```

### Not Using `with` for Resources
```python
# BAD
f = open('file.txt')
data = f.read()
f.close()  # Might not run if exception occurs

# GOOD
with open('file.txt') as f:
    data = f.read()
```

### Catching Too Broad Exceptions
```python
# BAD
try:
    do_something()
except Exception:
    pass

# GOOD
try:
    do_something()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
except FileNotFoundError:
    logger.error("File not found")
```

---

## 🚀 Performance Tips

### Use Built-in Functions
```python
# Slow
total = 0
for num in numbers:
    total += num

# Fast
total = sum(numbers)
```

### List Comprehensions
```python
# Slow
squares = []
for x in range(10):
    squares.append(x ** 2)

# Fast
squares = [x ** 2 for x in range(10)]
```

### Sets for Membership Testing
```python
# Slow - O(n)
if item in large_list:
    pass

# Fast - O(1)
large_set = set(large_list)
if item in large_set:
    pass
```

### Generators for Large Data
```python
# Memory intensive
def get_squares(n):
    return [x ** 2 for x in range(n)]

# Memory efficient
def get_squares(n):
    for x in range(n):
        yield x ** 2
```

---

## 🧪 Testing Best Practices

### pytest Structure
```python
import pytest

class TestUser:
    @pytest.fixture
    def user(self):
        return User(name="John", email="john@example.com")
    
    def test_user_creation(self, user):
        assert user.name == "John"
        assert user.email == "john@example.com"
    
    def test_user_validation(self):
        with pytest.raises(ValueError):
            User(name="", email="invalid")
```

### Test Naming
```python
# Good: test_<what>_<condition>_<expected>
def test_calculate_total_with_empty_cart_returns_zero():
    pass

def test_login_with_invalid_password_raises_error():
    pass
```

---

## 📚 Quick Reference

### String Formatting
```python
name = "World"

# f-strings (preferred, Python 3.6+)
greeting = f"Hello, {name}!"

# .format() (older style)
greeting = "Hello, {}!".format(name)

# % formatting (legacy)
greeting = "Hello, %s!" % name
```

### Dictionary Operations
```python
# Merge (Python 3.9+)
merged = dict1 | dict2

# Get with default
value = data.get("key", "default")

# Setdefault
data.setdefault("key", []).append(item)
```

### Pathlib (Modern File Handling)
```python
from pathlib import Path

# Create path
path = Path("folder") / "file.txt"

# Read/write
content = path.read_text()
path.write_text("new content")

# Check existence
if path.exists():
    pass
```

---

**Knowledge Version**: 1.0  
**Last Updated**: March 2026