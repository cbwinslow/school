# Lesson 3: Generators and Iterators

## Overview
This lesson covers generators and iterators, powerful Python features for memory-efficient data processing, along with functional programming tools that enable elegant and expressive code.

## Learning Objectives
By the end of this lesson, students will be able to:
- Create and use generator functions
- Implement custom iterator classes
- Understand lazy evaluation and memory efficiency
- Use built-in iterator functions (map, filter, zip, etc.)
- Apply functional programming concepts with functools and itertools
- Create infinite sequences and data pipelines
- Use comprehensions effectively
- Implement coroutines for asynchronous data processing

## Topics

### 3.1 Generator Functions

#### Basic Generators
```python
def count_up_to(n: int):
    """Generator that counts from 1 to n."""
    for i in range(1, n + 1):
        yield i

# Usage
for number in count_up_to(5):
    print(number)

# Generator expressions
def squares(n: int):
    return (i ** 2 for i in range(1, n + 1))

# Usage
squares_gen = squares(5)
for square in squares_gen:
    print(square)
```

#### Infinite Generators
```python
def infinite_counter(start: int = 1):
    """Infinite counter generator."""
    i = start
    while True:
        yield i
        i += 1

# Usage
counter = infinite_counter()
for _ in range(10):
    print(next(counter))

# Fibonacci generator
def fibonacci():
    """Infinite Fibonacci sequence generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### 3.2 Custom Iterator Classes

#### Implementing Iterator Protocol
```python
def Countdown:
    def __init__(self, start: int):
        self.start = start
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            result = self.current
            self.current -= 1
            return result

# Usage
countdown = Countdown(5)
for num in countdown:
    print(num)

# Multiple iterations
def RangeIterator:
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or \
           (self.step < 0 and self.current <= self.end):
            raise StopIteration
        else:
            result = self.current
            self.current += self.step
            return result

# Usage
range_iter = RangeIterator(0, 10, 2)
for num in range_iter:
    print(num)
```

### 3.3 Built-in Iterator Functions

#### Map, Filter, Zip
```python
def names = ["Alice", "Bob", "Charlie", "David"]
numbers = [1, 2, 3, 4]

# Map - apply function to each item
lengths = map(len, names)
print(list(lengths))  # [5, 3, 7, 5]

# Filter - select items based on condition
short_names = filter(lambda name: len(name) < 5, names)
print(list(short_names))  # ['Bob']

# Zip - combine multiple iterables
paired = zip(names, numbers)
print(list(paired))  # [('Alice', 1), ('Bob', 2), ...]

# Multiple iterators
def process_data(data):
    # Filter even numbers, square them, and sum
    return sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, data)))

# Usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_data(data)
print(result)  # 220
```

#### Chain and islice
```python
def chain(*iterables):
    """Chain multiple iterables together."""
    for it in iterables:
        for element in it:
            yield element

# Usage
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

chained = chain(numbers1, numbers2, numbers3)
print(list(chained))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# islice - get a slice of an iterator
def islice(iterable, start, stop=None, step=1):
    """Get a slice of an iterator."""
    it = iter(iterable)
    if stop is None:
        stop = start
        start = 0
    
    # Skip to start
    for _ in range(start):
        next(it, None)
    
    # Yield until stop
    for i in range(start, stop):
        if i % step == 0:
            yield next(it)
        else:
            next(it, None)

# Usage
fib = fibonacci()
fib_slice = islice(fib, 0, 10)
print(list(fib_slice))  # First 10 Fibonacci numbers
```

### 3.4 Functional Programming with functools

#### Reduce and Partial
```python
def reduce(function, iterable, initializer=None):
    """Reduce iterable to a single value."""
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    
    for element in it:
        value = function(value, element)
    return value

# Usage
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# Partial - create partial functions
def partial(func, *args, **keywords):
    def new_func(*f_args, **f_keywords):
        new_keywords = {**keywords, **f_keywords}
        return func(*args, *f_args, **new_keywords)
    return new_func

# Usage
def power(base, exponent):
    return base ** exponent

# Create a square function
power_of_two = partial(power, exponent=2)
print(power_of_two(5))  # 25

# Create a cube function
power_of_three = partial(power, exponent=3)
print(power_of_three(3))  # 27
```

#### LRU Cache
```python
def lru_cache(maxsize=128):
    """Least Recently Used cache decorator."""
    def decorator(func):
        cache = {}
        order = []
        
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            
            if key in cache:
                # Move to end (most recently used)
                order.remove(key)
                order.append(key)
                return cache[key]
            
            result = func(*args, **kwargs)
            
            # Add to cache
            cache[key] = result
            order.append(key)
            
            # Remove least recently used if cache is full
            if len(cache) > maxsize:
                oldest = order.pop(0)
                del cache[oldest]
            
            return result
        
        wrapper.cache_info = lambda: {
            'hits': 0,  # Simplified
            'misses': 0,  # Simplified
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        
        return wrapper
    return decorator

@lru_cache(maxsize=32)
def expensive_computation(x: int) -> int:
    print(f"Computing for {x}...")
    return x ** 2 + x + 1

# Usage
print(expensive_computation(5))  # Computes
print(expensive_computation(5))  # Cache hit
print(expensive_computation(10))  # Computes
```

### 3.5 itertools for Advanced Iteration

#### Combinations and Permutations
```python
def combinations(iterable, r):
    """Generate all combinations of length r."""
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        
        yield tuple(pool[i] for i in indices)

# Usage
items = ['A', 'B', 'C']
comb = combinations(items, 2)
print(list(comb))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Permutations
def permutations(iterable, r=None):
    """Generate all permutations."""
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    
    if r > n:
        return
    
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# Usage
perm = permutations(items)
print(list(perm))  # All permutations of ['A', 'B', 'C']
```

#### groupby and tee
```python
def groupby(iterable, key=None):
    """Group consecutive items with the same key."""
    if key is None:
        key = lambda x: x
    
    iterator = iter(iterable)
    try:
        current_key = key(next(iterator))
        current_group = []
        
        while True:
            try:
                item = next(iterator)
                item_key = key(item)
                
                if item_key == current_key:
                    current_group.append(item)
                else:
                    yield (current_key, current_group)
                    current_key = item_key
                    current_group = [item]
            except StopIteration:
                yield (current_key, current_group)
                break
    except StopIteration:
        return

# Usage
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('a', 5)]
grouped = groupby(data, key=lambda x: x[0])
for key, group in grouped:
    print(f"{key}: {list(group)}")

# tee - create multiple independent iterators
def tee(iterable, n=2):
    """Create n independent iterators from one iterable."""
    # For simplicity, we'll use list to store the values
    # In real implementation, this would be more memory efficient
    values = []
    iterator = iter(iterable)
    
    def create_iterator():
        index = 0
        while True:
            if index >= len(values):
                try:
                    value = next(iterator)
                    values.append(value)
                except StopIteration:
                    break
            yield values[index]
            index += 1
    
    return [create_iterator() for _ in range(n)]

# Usage
original = [1, 2, 3, 4, 5]
it1, it2 = tee(original)
print(list(it1))  # [1, 2, 3, 4, 5]
print(list(it2))  # [1, 2, 3, 4, 5]
```

### 3.6 Comprehensions and Generator Expressions

#### Advanced Comprehensions
```python
def matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested comprehensions
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conditional comprehensions
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ['cat', 'window', 'defenestrate']}
print(word_lengths)  # {'cat': 3, 'window': 6, 'defenestrate': 12}

# Set comprehensions
squares_set = {x ** 2 for x in range(10)}
print(squares_set)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Generator expressions for memory efficiency
large_data = (x ** 2 for x in range(1000000))
print(sum(large_data))  # Sum of squares without storing all values
```

### 3.7 Coroutines and Asynchronous Data Processing

#### Basic Coroutines
```python
def coroutine_example():
    print("Coroutine started")
    while True:
        value = yield
        print(f"Received: {value}")

# Usage
coro = coroutine_example()
next(coro)  # Prime the coroutine
coro.send(10)  # Received: 10
coro.send(20)  # Received: 20
```

#### Pipeline Processing
```python
def data_source():
    """Source that generates data."""
    for i in range(10):
        print(f"Source producing {i}")
        yield i


def filter_even():
    """Filter that only allows even numbers."""
    print("Filter even started")
    while True:
        value = yield
        if value % 2 == 0:
            print(f"Filter even passing {value}")
            yield value


def multiply_by_three():
    """Processor that multiplies by three."""
    print("Multiply by three started")
    while True:
        value = yield
        result = value * 3
        print(f"Multiply by three producing {result}")
        yield result


def pipeline():
    """Create a processing pipeline."""
    source = data_source()
    
    # Create processors
    filter_proc = filter_even()
    next(filter_proc)  # Prime the filter
    
    multiply_proc = multiply_by_three()
    next(multiply_proc)  # Prime the multiplier
    
    # Process data
    for data in source:
        # Send to filter
        filter_proc.send(data)
        filtered = filter_proc.send(None)
        
        if filtered is not None:
            # Send to multiplier
            multiply_proc.send(filtered)
            result = multiply_proc.send(None)
            print(f"Pipeline result: {result}")

# Usage
pipeline()
```

## Exercises

### Exercise 3.1: Simple Generator
Create a generator that yields prime numbers up to a given limit.

### Exercise 3.2: Custom Iterator
Implement an iterator that reads lines from a file one at a time.

### Exercise 3.3: Data Pipeline
Create a data processing pipeline using generators that filters, transforms, and aggregates data.

### Exercise 3.4: Fibonacci Generator
Write a generator that produces Fibonacci numbers indefinitely.

### Exercise 3.5: File Processor
Create a generator that reads a large file in chunks and processes each chunk.

### Exercise 3.6: Permutation Generator
Implement a generator that produces all permutations of a list.

## Assessment Questions

1. What is the difference between a generator function and a regular function?
2. How do generators help with memory efficiency?
3. Explain the iterator protocol in Python.
4. What are the benefits of using functional programming tools?
5. How do coroutines differ from regular generators?

## Real-World Applications
- Processing large datasets without loading everything into memory
- Creating data processing pipelines
- Implementing lazy evaluation
- Building efficient algorithms
- Creating asynchronous data processing systems
- Working with streams of data