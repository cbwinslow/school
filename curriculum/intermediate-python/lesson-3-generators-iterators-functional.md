# Lesson 3: Generators and Iterators

## Overview

This lesson explores Python's powerful generators and iterators, enabling efficient, memory-conscious programming for large datasets and infinite sequences.

## Duration
2-3 hours

## Prerequisites
- Basic understanding of iteration and loops
- Familiarity with functions and classes
- Basic knowledge of memory management

## Topics Covered

### 1. Generator Functions
- Creating generators with `yield`
- Generator vs regular functions
- State preservation in generators
- Generator execution flow

### 2. Generator Expressions
- List comprehensions vs generator expressions
- Memory efficiency comparison
- Lazy evaluation benefits
- Performance considerations

### 3. Iterator Protocol
- Implementing `__iter__` and `__next__`
- Custom iterator classes
- StopIteration exception
- Iterator vs iterable distinction

### 4. Coroutines
- Basic coroutine concepts
- `async` and `await` syntax
- Coroutine execution model
- Coroutine vs generator differences

### 5. Async Generators
- Creating async generators
- Async iteration
- Async context managers
- Real-world async generator use cases

## Key Concepts

### Generator Functions
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)
```

### Generator Expressions
```python
# List comprehension (creates entire list in memory)
numbers = [x**2 for x in range(1000000)]

# Generator expression (lazy evaluation)
numbers_gen = (x**2 for x in range(1000000))

# Memory comparison
import sys
print(f"List size: {sys.getsizeof(numbers)} bytes")
print(f"Generator size: {sys.getsizeof(numbers_gen)} bytes")
```

### Custom Iterator Class
```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

for num in FibonacciIterator(10):
    print(num)
```

### Coroutine Example
```python
async def fetch_data(url):
    print(f"Fetching {url}...")
    await asyncio.sleep(1)  # Simulate network delay
    return f"Data from {url}"

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

import asyncio
asyncio.run(main())
```

### Async Generator
```python
async def generate_numbers():
    for i in range(5):
        await asyncio.sleep(0.5)
        yield i

async def main():
    async for number in generate_numbers():
        print(f"Received: {number}")

asyncio.run(main())
```

## Project Integration

### Plugin Discovery and Loading

The CLI tool uses generators for efficient plugin discovery:

```python
def discover_plugins(directory):
    """Generator that discovers plugin files"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and not file.startswith('_'):
                yield os.path.join(root, file)

class PluginLoader:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
    
    def load_plugins(self):
        """Generator that loads and yields plugin classes"""
        for plugin_path in discover_plugins(self.plugin_dir):
            module_name = os.path.splitext(os.path.basename(plugin_path))[0]
            try:
                module = importlib.import_module(f'plugins.{module_name}')
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if hasattr(attr, '_plugin_category'):
                        yield attr
            except ImportError:
                continue
```

### Data Processing Pipelines
```python
def read_large_file(file_path):
    """Generator that reads a large file line by line"""
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

class DataProcessor:
    def __init__(self, source):
        self.source = source
    
    def process(self):
        """Generator that processes data from source"""
        for item in self.source:
            # Process item (filter, transform, etc.)
            if item and not item.startswith('#'):
                yield item.upper()

# Usage
file_path = 'large_data.txt'
processor = DataProcessor(read_large_file(file_path))
for processed_item in processor.process():
    print(processed_item)
```

### Infinite Sequence Generator
```python
def infinite_counter(start=0, step=1):
    """Generator for infinite counting sequence"""
    current = start
    while True:
        yield current
        current += step

# Example usage
counter = infinite_counter()
for _ in range(10):
    print(next(counter))
```

## Exercises

### Exercise 1: Basic Generator
Create a generator function that yields Fibonacci numbers up to a given count.

### Exercise 2: Generator Expression
Create a generator expression that filters even numbers from a range and squares them.

### Exercise 3: Custom Iterator
Create a custom iterator class that iterates over a custom data structure (e.g., a tree or graph).

### Exercise 4: Coroutine
Create a coroutine that simulates a simple chat server, receiving and responding to messages.

### Exercise 5: Async Generator
Create an async generator that simulates reading data from a sensor at regular intervals.

### Exercise 6: Data Pipeline
Create a data processing pipeline using generators that reads from a file, filters data, transforms it, and writes to another file.

## Real-World Applications

- **Data processing** for large files and streams
- **Web scraping** with lazy loading of pages
- **Machine learning** for batch processing of datasets
- **Network programming** with async generators for I/O
- **Game development** for procedural content generation
- **Database operations** for efficient query result handling
- **API clients** for streaming responses
- **File processing** for log analysis and parsing

## Common Pitfalls

- **Forgetting to handle StopIteration** in custom iterators
- **Mixing up iterators and iterables**
- **Performance issues** with complex generator logic
- **Memory leaks** from holding references in generators
- **Debugging difficulties** with generator state
- **Overusing generators** when simple lists would suffice
- **Not understanding coroutine vs generator differences**

## Assessment Criteria

Students will be evaluated on:
- **Generator Implementation** (30%): Correct use of yield and generator patterns
- **Iterator Protocol** (25%): Proper implementation of __iter__ and __next__
- **Memory Efficiency** (20%): Understanding of lazy evaluation benefits
- **Project Integration** (15%): Effective use in CLI tool context
- **Testing** (10%): Unit tests for generator functions and classes

## Additional Resources

- [Python Generators Documentation](https://docs.python.org/3/tutorial/classes.html#generators)
- [Iterator Protocol](https://docs.python.org/3/library/stdtypes.html#iterator-types)
- [Async Generators](https://docs.python.org/3/library/asyncio.html#async-generator-functions)
- [Effective Python: Generators](https://effectivepython.com/)
- [PEP 342: Coroutines](https://www.python.org/dev/peps/pep-0342/)
- [Real Python: Generators](https://realpython.com/introduction-to-python-generators/)
```

### 3.4 itertools Module
```python
import itertools

# count - infinite counter
counter = itertools.count(10, 2)  # start at 10, step by 2
print(list(itertools.islice(counter, 5)))  # [10, 12, 14, 16, 18]

# cycle - cycle through iterable
cycle_iter = itertools.cycle(['red', 'green', 'blue'])
print(list(itertools.islice(cycle_iter, 6)))  # ['red', 'green', 'blue', 'red', 'green', 'blue']

# accumulate - running total
numbers = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(numbers)))  # [1, 3, 6, 10, 15]

# chain - combine iterables
combined = itertools.chain('ABC', '123', 'XYZ')
print(list(combined))  # ['A', 'B', 'C', '1', '2', '3', 'X', 'Y', 'Z']

# groupby - group consecutive items
data = [1, 1, 2, 2, 2, 3, 3, 1, 1]
for key, group in itertools.groupby(data):
    print(f"{key}: {list(group)}")
```

### 3.5 Coroutines and Async Generators
```python
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.5)
        yield i

async def main():
    async for value in async_generator():
        print(f"Received: {value}")

# Run the async generator
asyncio.run(main())

# Coroutine example
def coroutine_example():
    print("Coroutine started")
    result = yield
    print(f"Coroutine received: {result}")
    return "Done"

coro = coroutine_example()
next(coro)  # Start coroutine
coro.send("Hello")  # Send value to coroutine
```
        current += 1

# Usage
gen = count_up_to(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

for num in count_up_to(3):
    print(num)

# Generator expressions
def squares(n):
    return (x**2 for x in range(n))

# Usage
squares_gen = squares(5)
print(list(squares_gen))  # [0, 1, 4, 9, 16]
```

### 3.3 Infinite Generators
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci()
for _ in range(10):
    print(next(fib))

# Take first n elements
def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(itertools.islice(iterable, n))

print(take(10, fibonacci()))
```

### 3.4 Generator Pipelines
```python
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Pipeline: read -> filter -> transform -> aggregate
def process_data(file_path):
    lines = read_large_file(file_path)
    non_empty = (line for line in lines if line)
    words = (line.split() for line in non_empty)
    all_words = itertools.chain.from_iterable(words)
    word_counts = collections.Counter(all_words)
    return word_counts

# Usage
result = process_data('large_text_file.txt')
print(result.most_common(10))
```

### 3.5 `itertools` Module
```python
import itertools

# Infinite iterators
count = itertools.count(10, 2)  # 10, 12, 14, 16, ...
cycle = itertools.cycle('ABC')  # A, B, C, A, B, C, ...
repeat = itertools.repeat(5, 3)  # 5, 5, 5

# Combinatoric iterators
permutations = itertools.permutations('ABC', 2)  # ('A','B'), ('A','C'), ...
combinations = itertools.combinations('ABC', 2)  # ('A','B'), ('A','C'), ('B','C')
product = itertools.product('ABC', '123')  # ('A','1'), ('A','2'), ...

# Terminating iterators
accumulate = itertools.accumulate([1, 2, 3, 4])  # 1, 3, 6, 10
chain = itertools.chain('ABC', '123')  # A, B, C, 1, 2, 3
compress = itertools.compress('ABCDEF', [1,0,1,0,1,0])  # A, C, E

# Grouping iterators
groupby = itertools.groupby('AAAABBBCCDAA', key=lambda x: x)
for key, group in groupby:
    print(f"{key}: {list(group)}")
```

### 3.6 Coroutines and Async Generators
```python
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.5)
        yield i

async def main():
    async for value in async_generator():
        print(f"Received: {value}")

# Usage
asyncio.run(main())

# Coroutine-based generator
def coroutine():
    print("Coroutine started")
    while True:
        value = yield
        print(f"Received: {value}")

# Usage
coro = coroutine()
next(coro)  # Prime the coroutine
coro.send(42)  # Received: 42
coro.send('hello')  # Received: hello
```

### 3.7 Practical Applications
```python
# Database query streaming
def stream_database_results(query, batch_size=1000):
    cursor = db_connection.cursor()
    cursor.execute(query)
    
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        for row in batch:
            yield row

# File processing pipeline
def process_large_csv(file_path):
    lines = read_large_file(file_path)
    header = next(lines).split(',')
    
    for line in lines:
        values = line.split(',')
        record = dict(zip(header, values))
        yield record

# Real-time data processing
def real_time_data_source():
    while True:
        data = get_sensor_data()  # Simulate sensor reading
        yield data
        time.sleep(1)
```

```python
# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in range(10)]
print(squares_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(10))
print(squares_gen)  # <generator object <genexpr> at 0x...>
print(next(squares_gen))  # 0
print(list(squares_gen))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Memory comparison
import sys
print(f"List size: {sys.getsizeof(squares_list)} bytes")
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")
```

### 3. Custom Iterators

```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

# Usage
fib = FibonacciIterator(10)
for number in fib:
    print(number)

# Alternative: Using generator function
class FibonacciGenerator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self._generator()
    
    def _generator(self):
        count = 0
        a, b = 0, 1
        while count < self.max_count:
            yield a
            a, b = b, a + b
            count += 1
```

### 4. Built-in Functional Tools

```python
# map: Apply function to each item
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # [2, 4, 6, 8, 10]

# filter: Select items based on condition
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4]

# reduce: Accumulate values (needs import)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# Combining tools
result = reduce(lambda acc, x: acc + x**2, numbers, 0)
print(result)  # 55
```

### 5. Lambda Functions

```python
# Simple lambda
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Lambda with conditional
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # 20

# Lambda with multiple operations
complex_op = lambda x: (x**2, x**3, x**0.5)
print(complex_op(4))  # (16, 64, 2.0)

# Using lambda with map/filter
names = ["Alice", "Bob", "Charlie"]
lengths = list(map(lambda name: len(name), names))
print(lengths)  # [5, 3, 7]
```

### 6. Advanced itertools

```python
import itertools

# Infinite sequences
count_gen = itertools.count(10, 2)  # Start at 10, step by 2
print([next(count_gen) for _ in range(5)])  # [10, 12, 14, 16, 18]

# Cycle through values
cycle_gen = itertools.cycle(['A', 'B', 'C'])
print([next(cycle_gen) for _ in range(6)])  # ['A', 'B', 'C', 'A', 'B', 'C']

# Repeat value
repeat_gen = itertools.repeat(42, 3)
print(list(repeat_gen))  # [42, 42, 42]

# Combinations
items = ['A', 'B', 'C']
comb = itertools.combinations(items, 2)
print(list(comb))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Permutations
perm = itertools.permutations(items, 2)
print(list(perm))  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Chain multiple iterables
chain = itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(list(chain))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 7. Coroutines and Async Generators

```python
import asyncio

# Async generator
async def async_counter():
    count = 0
    while True:
        await asyncio.sleep(1)
        count += 1
        yield count

# Using async generator
async def use_counter():
    async for count in async_counter():
        print(f"Count: {count}")
        if count >= 5:
            break

# Run the async function
# asyncio.run(use_counter())

# Coroutine as generator
def coroutine_counter():
    count = 0
    while True:
        response = yield
        if response == 'increment':
            count += 1
            print(f"Count: {count}")
        elif response == 'reset':
            count = 0
            print("Counter reset")

# Usage
coro = coroutine_counter()
next(coro)  # Prime the coroutine
coro.send('increment')
coro.send('increment')
coro.send('reset')
coro.send('increment')
```

### 8. Infinite Sequences and Memory Efficiency

```python
def natural_numbers():
    """Infinite sequence of natural numbers"""
    n = 1
    while True:
        yield n
        n += 1

# Using infinite sequence safely
def first_n_natural_numbers(n):
    gen = natural_numbers()
    return [next(gen) for _ in range(n)]

print(first_n_natural_numbers(10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Memory-efficient processing
def process_large_file(file_path):
    """Process a large file line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            # Process each line without loading entire file
            process_line(line)

# Example: Find prime numbers using generator
def prime_numbers():
    """Generate prime numbers indefinitely"""
    yield 2
    primes = [2]
    candidate = 3
    
    while True:
        is_prime = all(candidate % p != 0 for p in primes if p * p <= candidate)
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 2

# Get first 10 primes
prime_gen = prime_numbers()
print([next(prime_gen) for _ in range(10)])
```

### 9. Functional Programming Patterns

```python
# Pipeline pattern
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
print(result)  # [4, 16, 36, 64, 100]

# Using functools.reduce for complex operations
def calculate_statistics(numbers):
    total = reduce(lambda acc, x: acc + x, numbers, 0)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return {"total": total, "count": count, "average": average}

print(calculate_statistics([10, 20, 30, 40, 50]))

# Composing functions
from functools import partial

def compose(*functions):
    def composed(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return composed

# Usage
double = lambda x: x * 2
increment = lambda x: x + 1

composed_func = compose(double, increment)
print(composed_func(5))  # (5 + 1) * 2 = 12
```

## Exercises

### Exercise 1: Create a Data Processing Pipeline

Build a data processing pipeline using generators:
- Read data from a CSV file
- Filter rows based on conditions
- Transform data
- Write results to a new file
- Use lazy evaluation for memory efficiency

### Exercise 2: Implement an Infinite Sequence Processor

Create a system that processes infinite sequences:
- Generate prime numbers
- Find Fibonacci numbers
- Process mathematical sequences
- Implement safe termination

### Exercise 3: Build a Streaming Data Processor

Create a streaming data processor:
- Read from a network stream
- Process data in chunks
- Handle backpressure
- Use async generators

### Exercise 4: Create a Functional Utility Library

Build a functional utility library:
- Implement common functional patterns
- Add error handling
- Create composable functions
- Add type hints

## Assessment Questions

1. What are the advantages of using generators over lists?
2. How does lazy evaluation improve performance?
3. What is the difference between a generator function and a generator expression?
4. When would you use itertools vs custom iterators?
5. How do coroutines differ from regular generators?