# Lesson 1: Advanced OOP Concepts

## Lesson Overview
This lesson covers advanced object-oriented programming concepts in Python, including inheritance patterns, polymorphism, abstract classes, and design patterns. Students will learn how to create robust, maintainable class hierarchies.

## Learning Objectives
By the end of this lesson, students will be able to:
- Implement multiple inheritance and understand method resolution order (MRO)
- Use abstract base classes and interfaces
- Apply polymorphism in practical scenarios
- Implement common design patterns (Factory, Singleton, Observer)
- Understand and use class methods, static methods, and properties
- Create custom comparison operators and rich comparison methods

## Topics Covered

### 1.1 Inheritance and Method Resolution Order
```python
class Animal:
    def speak(self):
        return "Some sound"

class Mammal(Animal):
    def speak(self):
        return "Generic mammal sound"

class Dog(Mammal):
    def speak(self):
        return "Woof!"

class Cat(Mammal):
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop"

class RobotDog(Dog, Robot):
    def speak(self):
        return f"{super().speak()} with robotic precision"
```

### 1.2 Abstract Base Classes
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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

### 1.3 Class Methods and Static Methods
```python
class Employee:
    # Class variable
    company = "TechCorp"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Instance method
    def give_raise(self, amount):
        self.salary += amount
        return self.salary
    
    # Class method
    @classmethod
    def from_string(cls, employee_str):
        name, salary = employee_str.split(',')
        return cls(name, float(salary))
    
    # Static method
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

# Usage
emp1 = Employee("Alice", 50000)
emp2 = Employee.from_string("Bob,60000")
print(Employee.is_workday(datetime.date(2023, 3, 15)))  # True
```

### 1.4 Properties and Decorators
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    @property
    def available_balance(self):
        # Could include logic for pending transactions, etc.
        return self._balance

# Usage
account = BankAccount(1000)
print(account.balance)  # 1000
account.balance = 1500
print(account.available_balance)  # 1500
```

### 1.5 Custom Comparison Operators
```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age
    
    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Usage
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1 > p2)  # True
print(p1 <= p2)  # False
print(p1 == p2)  # False
```

## Exercises

### Exercise 1.1: Animal Hierarchy
Create a class hierarchy for different types of animals with the following requirements:
- Base class `Animal` with abstract methods `speak()` and `move()`
- Derived classes: `Mammal`, `Bird`, `Fish`, `Reptile`
- Each class should implement the abstract methods appropriately
- Create a `Zoo` class that can contain multiple animals and make them all speak

### Exercise 1.2: Document Management System
Design a document management system with the following classes:
- `Document` (base class with title, author, content)
- `TextDocument` (inherits from Document, adds word count)
- `PDFDocument` (inherits from Document, adds page count)
- `Spreadsheet` (inherits from Document, adds row/column count)
- Implement a method to display document information polymorphically

### Exercise 1.3: Singleton Pattern
Implement a Singleton pattern for a database connection class:
- Ensure only one instance can be created
- Implement thread-safe initialization
- Add methods to connect, disconnect, and execute queries
- Demonstrate that multiple attempts to create instances return the same object

## Assessment Questions

1. What is the method resolution order (MRO) in Python, and how does it work with multiple inheritance?
2. Explain the difference between class methods, static methods, and instance methods.
3. How do abstract base classes enforce interface contracts in Python?
4. What are the benefits of using properties instead of direct attribute access?
5. How do the `@total_ordering` decorator and rich comparison methods work together?