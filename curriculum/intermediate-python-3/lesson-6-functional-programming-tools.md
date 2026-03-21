# Lesson 6: Functional Programming Tools

## Overview
This lesson covers functional programming concepts and tools in Python, enabling elegant, declarative, and efficient code for data processing and transformation.

## Learning Objectives
By the end of this lesson, students will be able to:
- Use functional programming tools (map, filter, reduce, etc.)
- Work with lambda functions effectively
- Apply higher-order functions
- Use the functools module for advanced functional patterns
- Implement lazy evaluation with iterators
- Use list comprehensions and generator expressions
- Apply functional patterns to real-world problems
- Understand the benefits and limitations of functional programming

## Topics

### 6.1 Core Functional Tools

#### Map, Filter, and Reduce
```python
# Map - apply function to each item
numbers = [1, 2, 3, 4, 5]

def square(x: int) -> int:
    return x ** 2

squared = map(square, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# Using lambda
lengths = map(len, ['cat', 'window', 'defenestrate'])
print(list(lengths))  # [3, 6, 12]

# Filter - select items based on condition
def is_even(x: int) -> bool:
    return x % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]

# Using lambda
long_words = filter(lambda word: len(word) > 5, ['cat', 'window', 'defenestrate'])
print(list(long_words))  # ['defenestrate']

# Reduce - combine items into single value
from functools import reduce

def multiply(x: int, y: int) -> int:
    return x * y

product = reduce(multiply, numbers, 1)
print(product)  # 120

# Using lambda
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# Sum using reduce
sum_result = reduce(lambda x, y: x + y, numbers, 0)
print(sum_result)  # 15
```

#### Zip and Enumerate
```python
# Zip - combine multiple iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

people = zip(names, ages, cities)
print(list(people))  # [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ...]

# Unzip
names_again, ages_again, cities_again = zip(*people)

# Enumerate - get index and value
indexed = enumerate(names)
print(list(indexed))  # [(0, 'Alice'), (1, 'Bob'), (2, 'Charlie')]

# With start parameter
indexed_from_one = enumerate(names, start=1)
print(list(indexed_from_one))  # [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
```

### 6.2 Lambda Functions

#### Basic Lambda Usage
```python
# Simple lambda
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# Lambda with filter
words = ['cat', 'window', 'defenestrate']
long_words = filter(lambda word: len(word) > 5, words)
print(list(long_words))  # ['defenestrate']

# Lambda with sorted
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # ['cat', 'window', 'defenestrate']

# Lambda with max/min
max_word = max(words, key=lambda word: len(word))
print(max_word)  # 'defenestrate'
```

#### When to Use Lambda
```python
# Good use cases - simple, one-time operations
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

top_student = max(students, key=lambda s: s['grade'])
print(top_student)  # {'name': 'Bob', 'grade': 92}

# Complex operations should use regular functions

def calculate_grade(student: dict) -> float:
    """Complex grade calculation."""
    base_grade = student['grade']
    extra_credit = student.get('extra_credit', 0)
    return base_grade + extra_credit * 0.1

# Better than: key=lambda s: s['grade'] + s.get('extra_credit', 0) * 0.1
```

### 6.3 Higher-Order Functions

#### Functions that Return Functions
```python
def create_multiplier(factor: int):
    """Returns a function that multiplies by the given factor."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

# Usage
time_two = create_multiplier(2)
time_three = create_multiplier(3)

print(time_two(5))   # 10
print(time_three(5))  # 15

# More complex example
def create_validator(allowed_types: tuple):
    """Returns a validation function."""
    def validator(value: Any) -> bool:
        return isinstance(value, allowed_types)
    return validator

# Usage
is_number = create_validator((int, float))
is_string = create_validator((str,))

print(is_number(5))      # True
print(is_number('5'))    # False
print(is_string('hello')) # True
```

#### Functions that Accept Functions
```python
def process_items(
    items: list,
    operation: Callable[[Any], Any]
) -> list:
    """Apply operation to each item."""
    return [operation(item) for item in items]

# Usage
numbers = [1, 2, 3, 4, 5]

def square(x: int) -> int:
    return x ** 2

def double(x: int) -> int:
    return x * 2

def to_string(x: int) -> str:
    return str(x)

print(process_items(numbers, square))     # [1, 4, 9, 16, 25]
print(process_items(numbers, double))     # [2, 4, 6, 8, 10]
print(process_items(numbers, to_string))  # ['1', '2', '3', '4', '5']
```

### 6.4 functools Module

#### Partial Functions
```python
def power(base: float, exponent: float) -> float:
    return base ** exponent

# Create partial functions
from functools import partial

time_two = partial(power, exponent=2)
time_three = partial(power, exponent=3)
time_four = partial(power, exponent=4)

print(time_two(5))    # 25
print(time_three(5))  # 125
print(time_four(5))   # 625

# Partial with multiple arguments
def greet(greeting: str, name: str) -> str:
    return f"{greeting}, {name}!"

hello_greeter = partial(greet, "Hello")
good_morning_greeter = partial(greet, "Good morning")

print(hello_greeter("Alice"))        # "Hello, Alice!"
print(good_morning_greeter("Bob"))   # "Good morning, Bob!"
```

#### reduce with Complex Operations
```python
def calculate_total(orders: list) -> float:
    """Calculate total cost of orders."""
    from functools import reduce
    
    def add_prices(total: float, order: dict) -> float:
        return total + order['price'] * order['quantity']
    
    return reduce(add_prices, orders, 0.0)

# Usage
orders = [
    {'item': 'Book', 'price': 15.99, 'quantity': 2},
    {'item': 'Pen', 'price': 2.99, 'quantity': 5},
    {'item': 'Notebook', 'price': 4.99, 'quantity': 3}
]

total = calculate_total(orders)
print(f"Total: ${total:.2f}")  # Total: $58.91
```

#### lru_cache for Memoization
```python
def fibonacci(n: int) -> int:
    """Recursive Fibonacci with memoization."""
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    
    return fib(n)

# Usage
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765

# Cache info
# print(fibonacci.__wrapped__.cache_info())
```

#### singledispatch for Function Overloading
```python
def process_data(data: Any) -> str:
    """Process data based on its type."""
    from functools import singledispatch
    
    @singledispatch
    def process(data: Any) -> str:
        return f"Unknown type: {type(data).__name__}"
    
    @process.register
    def _(data: int) -> str:
        return f"Integer: {data}"
    
    @process.register
    def _(data: str) -> str:
        return f"String: {data}"
    
    @process.register
    def _(data: list) -> str:
        return f"List of {len(data)} items"
    
    return process(data)

# Usage
print(process_data(42))           # "Integer: 42"
print(process_data("hello"))      # "String: hello"
print(process_data([1, 2, 3]))    # "List of 3 items"
print(process_data({'a': 1}))     # "Unknown type: dict"
```

### 6.5 Comprehensions and Generator Expressions

#### List Comprehensions
```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# With condition
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16]

# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Complex example - Pythagorean triples
pythagorean = [(a, b, c) 
               for a in range(1, 30) 
               for b in range(a, 30) 
               for c in range(b, 30) 
               if a ** 2 + b ** 2 == c ** 2]
print(pythagorean)
```

#### Dictionary Comprehensions
```python
# Basic dictionary comprehension
words = ['cat', 'window', 'defenestrate']
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'cat': 3, 'window': 6, 'defenestrate': 12}

# With condition
long_words = {word: len(word) for word in words if len(word) > 5}
print(long_words)  # {'window': 6, 'defenestrate': 12}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_from_lists = {k: v for k, v in zip(keys, values)}
print(dict_from_lists)  # {'a': 1, 'b': 2, 'c': 3}

# Counting occurrences
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = {word: words.count(word) for word in set(words)}
print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

#### Set Comprehensions
```python
# Basic set comprehension
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(unique)  # {1, 2, 3, 4}

# With condition
even = {x for x in numbers if x % 2 == 0}
print(even)  # {2, 4}

# Prime numbers
primes = {x for x in range(2, 100) 
          if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))}
print(primes)
```

#### Generator Expressions
```python
# Basic generator expression
numbers = [1, 2, 3, 4, 5]
squared_gen = (x ** 2 for x in numbers)
print(list(squared_gen))  # [1, 4, 9, 16, 25]

# Memory-efficient processing
large_data = (x ** 2 for x in range(1000000))
print(sum(large_data))  # Sum without storing all squares

# Chaining generators
def even_numbers():
    return (x for x in range(100) if x % 2 == 0)

def squared():
    return (x ** 2 for x in even_numbers())

def filtered():
    return (x for x in squared() if x < 1000)

result = list(filtered())
print(result)
```

### 6.6 Advanced Functional Patterns

#### Function Composition
```python
def compose(*functions):
    """Compose multiple functions right to left."""
    def composed(arg):
        for func in reversed(functions):
            arg = func(arg)
        return arg
    return composed

# Usage
def add_one(x: int) -> int:
    return x + 1

def multiply_by_two(x: int) -> int:
    return x * 2

def subtract_three(x: int) -> int:
    return x - 3

composed_func = compose(subtract_three, multiply_by_two, add_one)
print(composed_func(5))  # ((5 + 1) * 2) - 3 = 9
```

#### Pipeline Processing
```python
def pipeline(*functions):
    """Create a processing pipeline."""
    def process(data):
        for func in functions:
            data = func(data)
        return data
    return process

# Usage
def filter_positive(numbers: list) -> list:
    return [x for x in numbers if x > 0]

def multiply_by_two(numbers: list) -> list:
    return [x * 2 for x in numbers]

def to_strings(numbers: list) -> list:
    return [str(x) for x in numbers]

process_pipeline = pipeline(
    filter_positive,
    multiply_by_two,
    to_strings
)

result = process_pipeline([-1, 2, -3, 4, -5, 6])
print(result)  # ['4', '8', '12']
```

#### Currying
```python
def curry(func):
    """Transform a function into a curried version."""
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))
    return curried

# Usage
def add_three(a: int, b: int, c: int) -> int:
    return a + b + c

curried_add = curry(add_three)

add_1 = curried_add(1)
add_1_2 = add_1(2)
result = add_1_2(3)
print(result)  # 6

# Or in one line
result = curry(add_three)(1)(2)(3)
print(result)  # 6
```

## Exercises

### Exercise 6.1: Basic Functional Tools
Use map, filter, and reduce to process a list of numbers.

### Exercise 6.2: Lambda Functions
Create a sorting function that uses lambda for custom sorting criteria.

### Exercise 6.3: Higher-Order Functions
Write a function that takes another function as an argument and applies it to a list.

### Exercise 6.4: functools Usage
Implement a memoized version of a recursive function using lru_cache.

### Exercise 6.5: Comprehensions
Create complex comprehensions for data transformation tasks.

### Exercise 6.6: Function Composition
Build a function composition utility and use it to create complex operations.

## Assessment Questions

1. What are the advantages of using functional programming tools?
2. When should you use a lambda function versus a regular function?
3. How does currying differ from partial application?
4. What are the benefits of using generator expressions over list comprehensions?
5. How can function composition improve code readability?

## Real-World Applications
- Data processing and transformation pipelines
- Event handling and callback systems
- Configuration and plugin systems
- Mathematical and scientific computing
- Web request processing
- Stream processing and data analysis