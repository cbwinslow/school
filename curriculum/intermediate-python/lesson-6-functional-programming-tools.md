# Lesson 6: Functional Programming Tools

## Lesson Overview
This lesson covers functional programming concepts in Python, including higher-order functions, lambda expressions, and the functional tools available in the standard library. Students will learn how to write more declarative and concise code.

## Learning Objectives
By the end of this lesson, students will be able to:
- Use map, filter, and reduce functions effectively
- Write and use lambda expressions
- Apply functional programming patterns
- Use the functools module for advanced functional tools
- Implement partial functions and currying
- Use the itertools module for functional iteration
- Apply functional programming to real-world problems
- Understand the trade-offs between functional and imperative programming

## Topics Covered

### 6.1 Map, Filter, and Reduce
```python
# Map - apply function to each element
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Filter - select elements based on condition
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)  # [2, 4]

# Reduce - accumulate values
from functools import reduce
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# Map with multiple iterables
def add_pairs(a, b):
    return a + b

result = list(map(add_pairs, [1, 2, 3], [4, 5, 6]))
print(result)  # [5, 7, 9]

# Filter with complex conditions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime, range(1, 20)))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

### 6.2 Lambda Expressions
```python
# Simple lambda
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Lambda with conditional
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # 20

# Lambda with multiple operations
complex_op = lambda x: (x * 2, x ** 2, x / 2)
print(complex_op(10))  # (20, 100, 5.0)

# Lambda with default arguments
default_add = lambda x, y=10: x + y
print(default_add(5))      # 15
print(default_add(5, 3))   # 8

# Lambda with variable arguments
sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # 15

# Lambda with keyword arguments
print_info = lambda **kwargs: f"Name: {kwargs.get('name', 'Unknown')}, Age: {kwargs.get('age', 'N/A')}"
print(print_info(name="Alice", age=25))  # Name: Alice, Age: 25
```

### 6.3 Functools Module
```python
from functools import partial, reduce, wraps

# Partial functions
multiply = lambda x, y: x * y
double = partial(multiply, 2)
triple = partial(multiply, 3)
print(double(5))   # 10
print(triple(5))   # 15

# Reduce with custom operations
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15

# Function decorators with functools
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper
```

### 6.4 Itertools Module
```python
import itertools

# Infinite iterators
count = itertools.count(10, 2)  # Start at 10, step by 2
print(list(itertools.islice(count, 5)))  # [10, 12, 14, 16, 18]

# Combinations
items = ['A', 'B', 'C']
combinations = list(itertools.combinations(items, 2))
print(combinations)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Permutations
permutations = list(itertools.permutations(items, 2))
print(permutations)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Cartesian product
numbers = [1, 2, 3]
letters = ['A', 'B']
cartesian = list(itertools.product(numbers, letters))
print(cartesian)  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]

# Group by
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}]
for key, group in itertools.groupby(data, key=lambda x: x['age']):
    print(f"Age {key}: {[item['name'] for item in group]}")
```

### 6.5 Real-World Applications
```python
# Data processing pipeline
from typing import List, Dict, Any

def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process data using functional programming patterns."""
    # Filter invalid data
    valid_data = filter(lambda x: x.get('valid', True), data)
    
    # Transform data
    transformed = map(lambda x: {
        'id': x['id'],
        'processed_value': x['value'] * 2,
        'timestamp': x.get('timestamp', None)
    }, valid_data)
    
    # Sort by processed value
    sorted_data = sorted(transformed, key=lambda x: x['processed_value'])
    
    return list(sorted_data)

# Example usage
data = [
    {'id': 1, 'value': 10, 'valid': True},
    {'id': 2, 'value': 5, 'valid': False},
    {'id': 3, 'value': 15, 'valid': True},
    {'id': 4, 'value': 8, 'valid': True}
]

result = process_data(data)
print(result)
```

### 6.6 Exercises

1. **Exercise 1**: Write a function that takes a list of numbers and returns a new list containing only the even numbers, squared, using functional programming tools.

2. **Exercise 2**: Create a function that takes a list of strings and returns a dictionary where keys are the lengths of the strings and values are lists of strings with that length.

3. **Exercise 3**: Implement a function that takes a list of dictionaries representing products and returns the total cost after applying a discount to items over a certain price threshold.

4. **Exercise 4**: Write a function that takes a list of numbers and returns the sum of squares of all numbers greater than 10.

5. **Exercise 5**: Create a function that takes a list of words and returns a list of tuples containing each word and its length, sorted by length in descending order.

### 6.7 Best Practices

- Use functional programming for data transformations and filtering
- Prefer list comprehensions over map/filter when readability is important
- Use lambda expressions for simple, one-time operations
- Combine functional tools with generator expressions for memory efficiency
- Use partial functions to create reusable function variations
- Be mindful of performance when using functional tools on large datasets
- Document complex functional pipelines for maintainability

### 6.8 Common Pitfalls

- Overusing lambda expressions can make code harder to read
- Nested functional calls can become difficult to debug
- Functional programming may not be the best choice for all problems
- Performance can be slower than imperative approaches for simple operations
- Debugging functional pipelines can be challenging without proper logging

### 6.9 Assessment Questions

1. What is the difference between `map` and a list comprehension?
2. When would you use `reduce` instead of a simple loop?
3. How do you create a partial function using `functools.partial`?
4. What are the advantages of using functional programming for data processing?
5. How can you combine `filter` and `map` in a single pipeline?