# Lesson 1: Advanced Object-Oriented Programming

## Overview
This lesson covers advanced object-oriented programming concepts in Python, including inheritance patterns, polymorphism, abstract base classes, and design patterns that enable the creation of flexible and maintainable code.

## Learning Objectives
By the end of this lesson, students will be able to:
- Implement multiple inheritance and understand method resolution order (MRO)
- Create and use abstract base classes with the `abc` module
- Apply polymorphism in practical scenarios
- Design class hierarchies using composition over inheritance
- Implement the factory pattern and singleton pattern
- Use dataclasses for cleaner data structures

## Topics

### 1.1 Inheritance and Method Resolution Order

#### Multiple Inheritance
```python
from typing import List, Optional

class Animal:
    def __init__(self, name: str):
        self.name = name
        self._age = 0
    
    def speak(self) -> str:
        return f"{self.name} makes a sound"
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

class Mammal(Animal):
    def __init__(self, name: str, has_fur: bool = True):
        super().__init__(name)
        self.has_fur = has_fur
    
    def speak(self) -> str:
        return f"{self.name} the mammal makes a sound"

class Bird(Animal):
    def __init__(self, name: str, can_fly: bool = True):
        super().__init__(name)
        self.can_fly = can_fly
    
    def speak(self) -> str:
        return f"{self.name} the bird chirps"

class Platypus(Mammal, Bird):
    def __init__(self, name: str):
        Mammal.__init__(self, name, has_fur=False)
        Bird.__init__(self, name, can_fly=False)
    
    def speak(self) -> str:
        return f"{self.name} the platypus is confused"
```

#### Method Resolution Order (MRO)
```python
print(Platypus.__mro__)
# Output: (Platypus, Mammal, Bird, Animal, object)
```

### 1.2 Abstract Base Classes

#### Creating Abstract Classes
```python
from abc import ABC, abstractmethod
from typing import List

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} object"

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius
```

### 1.3 Polymorphism

#### Practical Polymorphism
```python
def draw_shapes(shapes: List[Shape]) -> None:
    for shape in shapes:
        print(f"Drawing {shape}: area={shape.area():.2f}")

# Usage
rect = Rectangle(5, 3)
circle = Circle(4)
triangle = Triangle(3, 4, 5)  # Assume Triangle class exists

shapes = [rect, circle, triangle]
draw_shapes(shapes)
```

### 1.4 Design Patterns

#### Factory Pattern
```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str, name: str, **kwargs) -> Animal:
        if animal_type == "dog":
            return Dog(name, **kwargs)
        elif animal_type == "cat":
            return Cat(name, **kwargs)
        elif animal_type == "bird":
            return Bird(name, **kwargs)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connection = None
    
    def connect(self) -> None:
        if self.connection is None:
            print(f"Connecting to {self.connection_string}")
            self.connection = "Connection object"  # Simulated connection
    
    def disconnect(self) -> None:
        if self.connection:
            print("Disconnecting")
            self.connection = None
```

### 1.5 Dataclasses

#### Using Dataclasses
```python
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Person:
    name: str
    age: int
    email: str
    address: str = ""
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    price: float
    pages: int
    published_year: int
    
    def is_expensive(self) -> bool:
        return self.price > 50.0

@dataclass
class Library:
    name: str
    books: List[Book] = field(default_factory=list)
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if book.author == author]
```

## Exercises

### Exercise 1.1: Animal Hierarchy
Create a class hierarchy for different types of vehicles (Car, Motorcycle, Truck, etc.) with common methods and specific implementations.

### Exercise 1.2: Shape Calculator
Implement a shape calculator that can compute areas and perimeters for various geometric shapes using abstract base classes.

### Exercise 1.3: Plugin System Base
Create a base plugin system using abstract classes that can be extended for different types of plugins.

### Exercise 1.4: Factory Pattern
Implement a factory pattern for creating different types of documents (PDF, Word, Text) with common interfaces.

## Assessment Questions

1. What is the difference between single and multiple inheritance?
2. How does Python's method resolution order work in multiple inheritance?
3. When would you use an abstract base class versus a regular class?
4. Explain the singleton pattern and its use cases.
5. What are the benefits of using dataclasses over regular classes?

## Real-World Applications
- Building extensible frameworks
- Creating plugin architectures
- Implementing design patterns
- Developing data models
- Creating reusable libraries