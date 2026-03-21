# Lesson 3: Generators and Iterators

## Lesson Overview
This lesson covers generators and iterators in Python, focusing on memory-efficient programming techniques. Students will learn how to create custom iterators, use generator expressions, and implement lazy evaluation patterns.

## Learning Objectives
By the end of this lesson, students will be able to:
- Understand the difference between iterators and iterables
- Create generator functions using `yield`
- Use generator expressions for memory-efficient operations
- Implement custom iterator classes
- Use the `itertools` module effectively
- Apply lazy evaluation patterns
- Create infinite generators
- Use coroutines and async generators

## Topics Covered

### 3.1 Iterators and Iterables
```python
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# Usage
for num in MyRange(0, 5):
    print(num)

# Iterable vs Iterator
numbers = [1, 2, 3, 4, 5]  # Iterable
iterator = iter(numbers)    # Iterator

print(next(iterator))  # 1
print(next(iterator))  # 2
```

### 3.2 Generator Functions
```python
def count_up_to(n):
    current = 0
    while current < n:
        yield current
        current += 1

# Usage
gen = count_up_to(5)
print(next(gen))  # 0
print(next(gen))  # 1

for num in count_up_to(3):
    print(num)

# Generator with multiple yields
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage
for line in read_large_file('large_file.txt'):
    process(line)  # Process line by line without loading entire file
```

### 3.3 Generator Expressions
```python
# Generator expression vs list comprehension
numbers = [1, 2, 3, 4, 5]

doubled_list = [x * 2 for x in numbers]  # List comprehension
print(doubled_list)  # [2, 4, 6, 8, 10]

doubled_gen = (x * 2 for x in numbers)  # Generator expression
print(doubled_gen)  # <generator object>
print(next(doubled_gen))  # 2

# Memory comparison
import sys

large_list = [x for x in range(1000000)]
print(f"List size: {sys.getsizeof(large_list)} bytes")

large_gen = (x for x in range(1000000))
print(f"Generator size: {sys.getsizeof(large_gen)} bytes")

# Chaining generators
def even_numbers(numbers):
    return (x for x in numbers if x % 2 == 0)

def squared(numbers):
    return (x ** 2 for x in numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = squared(even_numbers(numbers))
for val in result:
    print(val)  # 4, 16, 36, 64, 100
```

### 3.4 Infinite Generators
```python
def infinite_counter(start=0):
    current = start
    while True:
        yield current
        current += 1

# Usage
counter = infinite_counter()
for _ in range(10):
    print(next(counter))

# Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci()
for _ in range(10):
    print(next(fib))

# Prime numbers generator
def prime_numbers():
    yield 2
    primes = [2]
    candidate = 3
    while True:
        is_prime = all(candidate % p != 0 for p in primes if p * p <= candidate)
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2
```

### 3.5 itertools Module
```python
import itertools

# Combinations and permutations
numbers = [1, 2, 3]
print(list(itertools.combinations(numbers, 2)))
# [(1, 2), (1, 3), (2, 3)]

print(list(itertools.permutations(numbers, 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
print(list(itertools.product(colors, sizes)))
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ...]

# Accumulate
numbers = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(numbers)))
# [1, 3, 6, 10, 15]

# Group by
data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}, 
        {'name': 'Charlie', 'age': 30}]

for age, group in itertools.groupby(data, key=lambda x: x['age']):
    print(f"Age {age}: {[person['name'] for person in group]}")

# Chain multiple iterables
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(list(itertools.chain(numbers, letters)))
# [1, 2, 3, 'a', 'b', 'c']
```

### 3.6 Coroutines and Async Generators
```python
import asyncio

# Coroutine
async def producer():
    for i in range(5):
        print(f"Producing {i}")
        await asyncio.sleep(0.5)
        yield i

# Consumer
async def consumer():
    async for value in producer():
        print(f"Consuming {value}")

# Run the coroutine
asyncio.run(consumer())

# Async generator
class AsyncFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    async def read_lines(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                await asyncio.sleep(0.1)  # Simulate async I/O
                yield line.strip()

# Usage
async def process_file_async():
    async for line in AsyncFileReader('large_file.txt').read_lines():
        process(line)
```

## Exercises

### Exercise 3.1: Custom Iterator
Create a custom iterator for a range-like class:
- Should support start, stop, and step parameters
- Should work with negative steps
- Should support the `len()` function
- Should be memory efficient for large ranges

### Exercise 3.2: File Processing Pipeline
Create a file processing pipeline using generators:
- Should read a large CSV file line by line
- Should filter rows based on conditions
- Should transform data (e.g., convert types, calculate new columns)
- Should write results to a new file

### Exercise 3.3: Data Streaming
Create a data streaming system:
- Should generate data points continuously
- Should allow multiple consumers
- Should support backpressure (consumers can slow down producers)
- Should handle errors gracefully

### Exercise 3.4: Lazy Evaluation Library
Create a library for lazy evaluation:
- Should support map, filter, and reduce operations
- Should be chainable
- Should evaluate only when needed
- Should support infinite sequences

## Assessment Questions

1. What is the difference between an iterator and an iterable in Python?
2. How do generators help with memory efficiency compared to lists?
3. What is the purpose of the `yield` keyword in Python?
4. How can you create an infinite sequence using generators?
5. What are some common use cases for the `itertools` module?