# Lesson 1: Advanced Object-Oriented Programming

## Overview

This lesson covers advanced object-oriented programming concepts in Python, building upon basic OOP knowledge to create sophisticated class hierarchies and design patterns.

## Duration
2-3 hours

## Prerequisites
- Basic understanding of classes and objects
- Familiarity with inheritance and basic polymorphism
- Experience with simple Python classes

## Topics Covered

### 1. Inheritance and Class Hierarchies
- Single inheritance and method overriding
- Multiple inheritance and the Method Resolution Order (MRO)
- Super() function and cooperative inheritance
- Diamond inheritance problem and its solutions

### 2. Abstract Base Classes (ABCs)
- Creating abstract base classes with `abc` module
- Abstract methods and properties
- Concrete implementations vs abstract methods
- Using `@abstractmethod` and `@abstractproperty` decorators

### 3. Polymorphism and Duck Typing
- Interface design and implementation
- Duck typing principles in Python
- Polymorphic behavior and method overriding
- Type checking vs duck typing

### 4. Mixins and Composition
- Mixin classes for reusable functionality
- Composition vs inheritance debate
- Multiple inheritance for mixins
- Designing flexible class hierarchies

### 5. Design Patterns with OOP
- Factory pattern implementation
- Singleton pattern in Python
- Observer pattern for event handling
- Strategy pattern for algorithm selection

## Key Concepts

### Inheritance
```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

### Multiple Inheritance and MRO
```python
class A:
    def method(self):
        return "A method"

class B:
    def method(self):
        return "B method"

class C(A, B):
    pass

print(C.__mro__)  # Shows method resolution order
```

### Mixins
```python
class SerializableMixin:
    def to_dict(self):
        return self.__dict__

class LoggableMixin:
    def log(self, message):
        print(f"LOG: {message}")

class User(SerializableMixin, LoggableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

## Project Integration

### Plugin System Architecture

The CLI tool project uses abstract base classes to define plugin interfaces:

```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def name(self) -> str:
        """Return the plugin name"""
    
    @abstractmethod
    def execute(self, args: dict) -> dict:
        """Execute the plugin with given arguments"""
    
    @abstractmethod
    def description(self) -> str:
        """Return plugin description"""
```

### Design Patterns in CLI Tool

**Factory Pattern for Command Creation**:
```python
class CommandFactory:
    @staticmethod
    def create_command(command_type: str, **kwargs):
        if command_type == "file":
            return FileCommand(**kwargs)
        elif command_type == "network":
            return NetworkCommand(**kwargs)
        else:
            raise ValueError(f"Unknown command type: {command_type}")
```

**Strategy Pattern for Different Operations**:
```python
class OperationStrategy:
    def execute(self, data):
        raise NotImplementedError

class AddOperation(OperationStrategy):
    def execute(self, data):
        return sum(data)

class MultiplyOperation(OperationStrategy):
    def execute(self, data):
        result = 1
        for item in data:
            result *= item
        return result
```

## Exercises

### Exercise 1: Abstract Base Class Implementation
Create an abstract base class `Vehicle` with abstract methods `start_engine()`, `stop_engine()`, and `move()`. Implement concrete classes `Car`, `Motorcycle`, and `Truck` with specific behaviors.

### Exercise 2: Multiple Inheritance Mixin
Create a mixin class `TimerMixin` that adds timing functionality to any class. Create a class that inherits from both a base class and `TimerMixin` to demonstrate the functionality.

### Exercise 3: Plugin Interface Design
Design an abstract base class for a plugin system that includes methods for initialization, execution, and cleanup. Implement at least two different plugins that follow this interface.

### Exercise 4: Factory Pattern Implementation
Create a factory class that generates different types of shapes (circle, square, triangle) based on input parameters. Each shape should have methods to calculate area and perimeter.

## Real-World Applications

- **Plugin architectures** for extensible applications
- **Game development** with complex object hierarchies
- **Web frameworks** using mixin classes for functionality
- **Database ORMs** with abstract base classes for models
- **API clients** with strategy patterns for different endpoints

## Common Pitfalls

- **Deep inheritance hierarchies** that become difficult to maintain
- **Diamond inheritance** problems without proper MRO understanding
- **Overuse of inheritance** when composition would be better
- **Tight coupling** between base and derived classes
- **Ignoring the Liskov Substitution Principle**

## Assessment Criteria

Students will be evaluated on:
- **Design Quality** (30%): Proper use of inheritance, abstraction, and design patterns
- **Implementation Correctness** (25%): Working code that follows the specifications
- **Code Organization** (20%): Clean, maintainable class structures
- **Documentation** (15%): Clear docstrings and comments
- **Testing** (10%): Basic unit tests for implemented classes

## Additional Resources

- [Python Documentation: Classes](https://docs.python.org/3/tutorial/classes.html)
- [Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Effective Python: Inheritance](https://effectivepython.com/)
- [Design Patterns in Python](https://python-patterns.guide/)
- [Python MRO Documentation](https://www.python.org/download/releases/2.3/mro/)
```

### 1.4 Properties and Descriptors
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```
    
    # Class method
    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split(",")
        return cls(name, int(salary))
    
    # Static method
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

# Usage
emp1 = Employee("Alice", 5000)
emp2 = Employee.from_string("Bob,6000")
print(emp1.get_annual_salary())
print(Employee.is_workday(datetime.date(2023, 3, 15)))
```

### 1.4 Properties and Decorators
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @property
    def is_adult(self):
        return self._age >= 18

# Usage
person = Person("Charlie", 25)
print(person.name)
print(person.is_adult)
person.age = 30
```

### 1.5 Rich Comparison Methods
```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade == other.grade
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.grade < other.grade
    
    def __repr__(self):
        return f"Student(name='{self.name}', grade={self.grade})"

# Usage
students = [
    Student("Alice", 85),
    Student("Bob", 92),
    Student("Charlie", 78)
]
students.sort()
print(students)
```

### 1.3 Design Patterns
```python
# Singleton Pattern
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = None
        print("Initializing database connection...")
    
    def connect(self):
        if not self.connection:
            print("Connecting to database...")
            self.connection = "Database connection established"
        return self.connection

# Factory Pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "dog":
            return Dog(*args, **kwargs)
        elif animal_type == "cat":
            return Cat(*args, **kwargs)
        elif animal_type == "robot_dog":
            return RobotDog(*args, **kwargs)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
```

### 1.4 Properties and Descriptors
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    def __str__(self):
        return f"{self._name} ({self._age} years old)"

# Custom Descriptor
class TypedAttribute:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"{self.name} must be of type {self.type.__name__}")
        instance.__dict__[self.name] = value

class Product:
    name = TypedAttribute('name', str)
    price = TypedAttribute('price', float)
    quantity = TypedAttribute('quantity', int)
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```
        elif vehicle_type == "motorcycle":
            return Motorcycle(**kwargs)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
```

#### Singleton Pattern
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
        self.connection = self.connect_to_database()
    
    def connect_to_database(self):
        # Simulate database connection
        return "Database connection established"
```

### 1.5 Special Methods and Rich Comparisons
```python
from functools import total_ordering

@total_ordering
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
```

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# This will raise TypeError if uncommented:
# shape = Shape()  # Cannot instantiate abstract class
```

### 3. Properties and Descriptors

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Usage
person = Person("Alice", 30)
print(person.name)  # Alice
person.age = 31
```

### 4. Class Methods and Static Methods

```python
class Employee:
    # Class variable
    company = "TechCorp"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split(",")
        return cls(name, int(salary))
    
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

# Usage
emp1 = Employee.from_string("Bob,50000")
print(emp1.name)  # Bob
print(Employee.is_workday(datetime.date(2024, 3, 20)))  # True
```

### 5. Dataclasses

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []

# Usage
book = Book("Python 101", "John Doe", 350, 29.99, ["programming", "python"])
print(book)
```

### 6. Special Methods (Dunder Methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)  # Vector(4, 6)
print(len(v1))  # 5
```

## Design Patterns

### Factory Pattern

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "dog":
            return Dog(*args, **kwargs)
        elif animal_type == "cat":
            return Cat(*args, **kwargs)
        elif animal_type == "bird":
            return Bird(*args, **kwargs)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog", "Buddy", 3)
```

### Singleton Pattern

```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_once(*args, **kwargs)
        return cls._instance
    
    def _init_once(self, connection_string):
        self.connection_string = connection_string
        self.connected = False
    
    def connect(self):
        if not self.connected:
            print(f"Connecting to {self.connection_string}")
            self.connected = True

# Usage
db1 = DatabaseConnection("localhost")
db2 = DatabaseConnection("localhost")
print(db1 is db2)  # True
```

## Exercises

### Exercise 1: Implement a Banking System

Create a banking system with the following classes:
- `Account` (abstract base class)
- `SavingsAccount` and `CheckingAccount` (concrete implementations)
- `Customer` class that can have multiple accounts
- Implement proper error handling for insufficient funds

### Exercise 2: Build a Game Character System

Create a game character system with:
- `Character` abstract base class
- `Warrior`, `Mage`, and `Rogue` subclasses
- Implement polymorphism for attack methods
- Use properties for character stats

### Exercise 3: Create a Data Processing Pipeline

Build a data processing pipeline with:
- `DataProcessor` abstract base class
- `CSVProcessor`, `JSONProcessor`, and `XMLProcessor` implementations
- Factory pattern for processor creation
- Use dataclasses for data representation

## Assessment Questions

1. What is the difference between class methods and static methods?
2. Explain method resolution order in multiple inheritance.
3. When would you use an abstract base class vs a regular class?
4. What are the benefits of using dataclasses?
5. How do special methods enhance Python classes?