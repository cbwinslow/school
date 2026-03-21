# Lesson 2: Decorators and Metaprogramming

## Overview
This lesson explores decorators, a powerful Python feature for modifying function and class behavior, and metaprogramming techniques for dynamic code generation and manipulation.

## Learning Objectives
By the end of this lesson, students will be able to:
- Create and use function decorators
- Implement class decorators
- Understand and use metaclasses
- Create decorators with arguments
- Use decorators for logging, caching, and validation
- Apply metaprogramming techniques for dynamic code generation
- Understand the descriptor protocol
- Create context managers using decorators

## Topics

### 2.1 Function Decorators

#### Basic Decorators
```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' finished")
        return result
    return wrapper

@simple_decorator
def greet(name: str) -> str:
    return f"Hello, {name}!"

@simple_decorator
def add(a: int, b: int) -> int:
    return a + b
```

#### Decorators with Arguments
```python
def repeat(times: int):
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
def calculate_sum(a: int, b: int) -> int:
    return a + b
```

### 2.2 Class Decorators

#### Basic Class Decorators
```python
def add_methods(cls):
    def new_method(self):
        return f"Instance of {self.__class__.__name__}"
    
    cls.new_method = new_method
    return cls

@add_methods
def MyClass:
    pass

@add_methods
def AnotherClass:
    pass

# Usage
obj1 = MyClass()
print(obj1.new_method())

obj2 = AnotherClass()
print(obj2.new_method())
```

#### Class Decorators for Validation
```python
def validate_attributes(cls):
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        
        # Validate attributes
        for attr_name, attr_value in self.__dict__.items():
            if attr_name.startswith('_') and attr_value is None:
                raise ValueError(f"Attribute '{attr_name}' cannot be None")
    
    cls.__init__ = new_init
    return cls

@validate_attributes
def Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

# Usage
# This will raise ValueError if any attribute is None
person = Person("Alice", 30)
```

### 2.3 Metaclasses

#### Basic Metaclass
```python
def LoggingMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"Creating class {name}")
        print(f"Bases: {bases}")
        print(f"Namespace: {list(namespace.keys())}")
        
        # Create the class
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class MyClass(metaclass=LoggingMeta):
    class_attribute = "value"
    
    def method(self):
        pass

class AnotherClass(MyClass, metaclass=LoggingMeta):
    def another_method(self):
        pass
```

#### Metaclass for Registration
```python
def RegistryMeta(type):
    registry = {}
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        
        # Register the class
        if name != "BaseClass":  # Don't register the base class
            mcs.registry[name] = cls
        
        return cls
    
    @classmethod
    def get_registered_classes(mcs):
        return list(mcs.registry.values())

class BaseClass(metaclass=RegistryMeta):
    pass

class ConcreteClass1(BaseClass):
    pass

class ConcreteClass2(BaseClass):
    pass

# Usage
registered_classes = RegistryMeta.get_registered_classes()
print(f"Registered classes: {registered_classes}")
```

### 2.4 Decorators for Common Use Cases

#### Timing Decorator
```python
def timing_decorator(func):
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds")
        
        return result
    return wrapper

@timing_decorator
def compute_heavy_task(n: int) -> int:
    result = 0
    for i in range(n):
        result += i ** 2
    return result
```

#### Caching Decorator
```python
def cache_decorator(func):
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create a key based on arguments
        key = (args, frozenset(kwargs.items()))
        
        if key in cache:
            print(f"Cache hit for {func.__name__}")
            return cache[key]
        
        print(f"Cache miss for {func.__name__}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@cache_decorator
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### Validation Decorator
```python
def validate_types(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate positional arguments
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument {i} must be {expected_type.__name__}, "
                        f"got {type(arg).__name__} instead"
                    )
            
            # Validate keyword arguments
            for name, value in kwargs.items():
                if name in func.__annotations__:
                    expected_type = func.__annotations__[name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Argument '{name}' must be {expected_type.__name__}, "
                            f"got {type(value).__name__} instead"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 2.5 Descriptor Protocol

#### Creating Custom Descriptors
```python
def TypedDescriptor(dtype):
    class Descriptor:
        def __init__(self, default=None):
            self.default = default
            self.value = None
        
        def __get__(self, instance, owner):
            return self.value if instance is not None else self
        
        def __set__(self, instance, value):
            if not isinstance(value, dtype):
                raise TypeError(f"Expected {dtype.__name__}, got {type(value).__name__}")
            self.value = value
        
        def __delete__(self, instance):
            self.value = None
    return Descriptor

class Person:
    name = TypedDescriptor(str)
    age = TypedDescriptor(int, default=0)
    email = TypedDescriptor(str)

# Usage
person = Person()
person.name = "Alice"
person.age = 30
# person.age = "30"  # This will raise TypeError
```

## Exercises

### Exercise 2.1: Simple Decorator
Create a decorator that logs function calls with arguments and return values.

### Exercise 2.2: Timing Decorator
Implement a decorator that measures and prints the execution time of functions.

### Exercise 2.3: Caching Decorator
Create a decorator that caches function results based on arguments.

### Exercise 2.4: Class Decorator
Write a class decorator that adds validation to all methods of a class.

### Exercise 2.5: Metaclass Registry
Create a metaclass that automatically registers all subclasses of a base class.

### Exercise 2.6: Plugin System
Design a plugin system using decorators and metaclasses for automatic plugin discovery.

## Assessment Questions

1. What is the difference between a function decorator and a class decorator?
2. How do decorators with arguments work internally?
3. What is a metaclass and when would you use one?
4. Explain the descriptor protocol and its use cases.
5. How does the method resolution order affect decorator behavior?

## Real-World Applications
- Creating reusable utility functions
- Implementing authentication and authorization
- Building plugin architectures
- Adding logging and monitoring
- Creating domain-specific languages (DSLs)
- Implementing design patterns