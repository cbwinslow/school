# Lesson 9: Performance Optimization

## Overview
This lesson covers performance optimization techniques in Python, including profiling, benchmarking, and optimization strategies to create efficient and scalable applications.

## Learning Objectives
By the end of this lesson, students will be able to:
- Profile Python code to identify bottlenecks
- Use benchmarking tools to measure performance
- Apply optimization techniques for better performance
- Understand time and space complexity
- Use appropriate data structures and algorithms
- Optimize I/O operations
- Implement caching strategies
- Use concurrency and parallelism effectively
- Apply best practices for performance
- Debug performance issues

## Topics

### 9.1 Profiling Python Code

#### Using cProfile
```python
import cProfile
import pstats
import io

def profile_code(func):
    """Decorator to profile a function."""
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        
        result = func(*args, **kwargs)
        
        pr.disable()
        
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        
        return result
    return wrapper

# Example usage
@profile_code
def slow_function():
    """Function with performance issues."""
    total = 0
    for i in range(1000):
        for j in range(1000):
            total += i * j
    return total

# Run the profiled function
slow_function()
```

#### Using line_profiler
```python
# Install: pip install line_profiler

# content.py
def slow_function():
    """Function with performance issues."""
    total = 0
    for i in range(1000):
        for j in range(1000):
            total += i * j
    return total

# test.py
import line_profiler
import content

# Profile specific functions
profiler = line_profiler.LineProfiler()
profiler.add_function(content.slow_function)

# Run the function
content.slow_function()

# Print results
profiler.print_stats()
```

#### Using memory_profiler
```python
# Install: pip install memory_profiler

from memory_profiler import profile

@profile
def memory_intensive():
    """Function that uses a lot of memory."""
    data = [i for i in range(1000000)]
    return sum(data)

# Run the memory-profiled function
memory_intensive()
```

### 9.2 Benchmarking

#### Using timeit
```python
import timeit

# Simple timing
def time_example():
    """Time a simple operation."""
    setup = "import math"
    stmt = "math.sqrt(2)")
    
    # Time it 1000 times
    time_taken = timeit.timeit(stmt, setup, number=1000)
    print(f"Time taken: {time_taken:.6f} seconds")

# Comparing implementations
def compare_implementations():
    """Compare different implementations."""
    setup = ""
    setup += "import math\n"
    setup += "import numpy as np\n"
    
    stmt1 = "sum([math.sqrt(i) for i in range(1000)])"
    stmt2 = "sum(np.sqrt(np.arange(1000)))")
    
    time1 = timeit.timeit(stmt1, setup, number=1000)
    time2 = timeit.timeit(stmt2, setup, number=1000)
    
    print(f"Pure Python: {time1:.6f} seconds")
    print(f"NumPy: {time2:.6f} seconds")
```

#### Using pytest-benchmark
```python
# Install: pip install pytest-benchmark

# test_benchmark.py
import pytest

def fibonacci(n: int) -> int:
    """Recursive Fibonacci (slow)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_iterative(n: int) -> int:
    """Iterative Fibonacci (fast)."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Benchmark tests
@pytest.mark.benchmark(group="fibonacci")
def test_fibonacci_recursive(benchmark):
    """Benchmark recursive Fibonacci."""
    result = benchmark(fibonacci, 10)
    assert result == 55

@pytest.mark.benchmark(group="fibonacci")
def test_fibonacci_iterative(benchmark):
    """Benchmark iterative Fibonacci."""
    result = benchmark(fibonacci_iterative, 10)
    assert result == 55
```

### 9.3 Time Complexity Analysis

#### Big O Notation
```python
# O(1) - Constant time
def get_first_item(items: list):
    """Get first item - constant time."""
    if items:
        return items[0]
    return None

# O(n) - Linear time
def sum_items(items: list):
    """Sum all items - linear time."""
    total = 0
    for item in items:
        total += item
    return total

# O(n^2) - Quadratic time
def bubble_sort(items: list):
    """Bubble sort - quadratic time."""
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

# O(log n) - Logarithmic time
def binary_search(items: list, target: int):
    """Binary search - logarithmic time."""
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n log n) - Linearithmic time
def merge_sort(items: list):
    """Merge sort - linearithmic time."""
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    
    return merge(left, right)

def merge(left: list, right: list) -> list:
    """Merge two sorted lists."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

#### Space Complexity
```python
# O(1) space - In-place sorting
def in_place_sort(items: list):
    """Sort in place - constant extra space."""
    items.sort()
    return items

# O(n) space - Creating new list
def create_new_list(items: list):
    """Create new list - linear extra space."""
    return [x * 2 for x in items]

# O(n^2) space - Matrix operations
def matrix_operations(matrix: list):
    """Matrix operations - quadratic space."""
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[i][j] ** 2
    
    return result
```

### 9.4 Data Structures and Algorithms

#### Choosing the Right Data Structure
```python
# List vs. Set for membership testing
import timeit

def list_vs_set():
    """Compare list vs set membership testing."""
    setup = ""
    setup += "import random\n"
    setup += "data_list = list(range(10000))\n"
    setup += "data_set = set(range(10000))\n"
    
    stmt_list = "random.choice(data_list) in data_list"
    stmt_set = "random.choice(list(data_set)) in data_set"
    
    time_list = timeit.timeit(stmt_list, setup, number=1000)
    time_set = timeit.timeit(stmt_set, setup, number=1000)
    
    print(f"List membership: {time_list:.6f} seconds")
    print(f"Set membership: {time_set:.6f} seconds")

# Dictionary for key-value lookups
def optimize_dict_usage():
    """Optimize dictionary usage."""
    # Good: Direct access
    data = {i: i ** 2 for i in range(1000)}
    result = data[500]  # Fast O(1) lookup
    
    # Bad: Linear search
    items = [(i, i ** 2) for i in range(1000)]
    result = next((v for k, v in items if k == 500), None)  # Slow O(n)

# Using collections for specialized needs
from collections import defaultdict, Counter, deque

def collections_usage():
    """Use specialized collections."""
    # defaultdict for automatic default values
    word_counts = defaultdict(int)
    for word in ['apple', 'banana', 'apple', 'cherry']:
        word_counts[word] += 1
    
    # Counter for counting hashable objects
    counter = Counter(['apple', 'banana', 'apple', 'cherry'])
    print(counter.most_common(2))  # Most common elements
    
    # deque for fast appends and pops from both ends
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.appendleft(0)
    print(queue)  # deque([0, 1, 2])
    print(queue.pop())  # 2
    print(queue.popleft())  # 0
```

#### Algorithm Optimization
```python
# Optimized Fibonacci
def fibonacci_optimized(n: int) -> int:
    """Optimized Fibonacci using dynamic programming."""
    if n <= 1:
        return n
    
    # Iterative approach - O(n) time, O(1) space
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Optimized factorial
def factorial_optimized(n: int) -> int:
    """Optimized factorial using iteration."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Optimized prime checking
def is_prime_optimized(n: int) -> bool:
    """Optimized prime checking."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True
```

### 9.5 I/O Optimization

#### Efficient File Reading
```python
# Reading large files efficiently
def read_large_file(file_path: str) -> None:
    """Read large file efficiently."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            process_line(line)

# Using buffered reading
def buffered_read(file_path: str, buffer_size: int = 8192) -> None:
    """Read file with buffer."""
    with open(file_path, 'r', encoding='utf-8') as file:
        while chunk := file.read(buffer_size):
            process_chunk(chunk)

# Writing efficiently
def write_efficiently(file_path: str, data: list[str]) -> None:
    """Write data efficiently."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(data)

# Using temporary files
def use_temporary_files():
    """Use temporary files for intermediate data."""
    import tempfile
    
    with tempfile.NamedTemporaryFile('w+', encoding='utf-8') as temp_file:
        # Write intermediate data
        temp_file.write("Intermediate data\n")
        temp_file.flush()
        
        # Read back
        temp_file.seek(0)
        content = temp_file.read()
        print(content)
```

#### Network I/O Optimization
```python
import requests
from concurrent.futures import ThreadPoolExecutor

# Sequential requests (slow)
def sequential_requests(urls: list[str]) -> list[dict]:
    """Make requests sequentially."""
    results = []
    for url in urls:
        response = requests.get(url)
        results.append(response.json())
    return results

# Concurrent requests (fast)
def concurrent_requests(urls: list[str]) -> list[dict]:
    """Make requests concurrently."""
    results = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(requests.get, url) for url in urls]
        for future in futures:
            response = future.result()
            results.append(response.json())
    
    return results

# Using sessions for connection pooling
def use_sessions(urls: list[str]) -> list[dict]:
    """Use requests sessions for better performance."""
    results = []
    
    with requests.Session() as session:
        for url in urls:
            response = session.get(url)
            results.append(response.json())
    
    return results
```

### 9.6 Caching Strategies

#### Simple Caching
```python
# Manual caching
def cached_fibonacci():
    """Fibonacci with manual caching."""
    cache = {}
    
    def fib(n: int) -> int:
        if n in cache:
            return cache[n]
        
        if n <= 1:
            result = n
        else:
            result = fib(n - 1) + fib(n - 2)
        
        cache[n] = result
        return result
    
    return fib

# Using functools.lru_cache
def cached_factorial():
    """Factorial with LRU cache."""
    from functools import lru_cache
    
    @lru_cache(maxsize=128)
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    return factorial

# Time-based caching
def time_based_cache(expiration: int = 60):
    """Cache with time-based expiration."""
    import time
    from functools import wraps
    
    def decorator(func):
        cache = {}
        timestamps = {}
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()
            
            # Check cache
            if key in cache:
                if current_time - timestamps[key] < expiration:
                    return cache[key]
                else:
                    # Expired
                    del cache[key]
                    del timestamps[key]
            
            # Compute and cache
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = current_time
            return result
        
        return wrapper
    
    return decorator

# Usage
@time_based_cache(expiration=30)
def expensive_computation(x: int) -> int:
    """Expensive computation."""
    print(f"Computing for {x}...")
    return x ** 2 + x + 1
```

### 9.7 Concurrency and Parallelism

#### Threading for I/O-bound Tasks
```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# I/O-bound task
def io_bound_task(url: str) -> dict:
    """I/O-bound task (network request)."""
    import requests
    response = requests.get(url)
    return response.json()

# Sequential I/O
def sequential_io(urls: list[str]) -> list[dict]:
    """Sequential I/O operations."""
    results = []
    for url in urls:
        results.append(io_bound_task(url))
    return results

# Concurrent I/O
def concurrent_io(urls: list[str]) -> list[dict]:
    """Concurrent I/O operations."""
    results = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(io_bound_task, url) for url in urls]
        for future in futures:
            results.append(future.result())
    
    return results
```

#### Multiprocessing for CPU-bound Tasks
```python
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

# CPU-bound task
def cpu_bound_task(data: list[int]) -> int:
    """CPU-bound task (heavy computation)."""
    return sum(x ** 2 for x in data)

# Sequential CPU
def sequential_cpu(data_chunks: list[list[int]]) -> int:
    """Sequential CPU operations."""
    total = 0
    for chunk in data_chunks:
        total += cpu_bound_task(chunk)
    return total

# Parallel CPU
def parallel_cpu(data_chunks: list[list[int]]) -> int:
    """Parallel CPU operations."""
    total = 0
    
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(cpu_bound_task, chunk) for chunk in data_chunks]
        for future in futures:
            total += future.result()
    
    return total
```

#### AsyncIO for Concurrent I/O
```python
import asyncio
import aiohttp

async def async_io_task(url: str) -> dict:
    """Async I/O task."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def async_concurrent_io(urls: list[str]) -> list[dict]:
    """Concurrent async I/O operations."""
    tasks = [async_io_task(url) for url in urls]
    return await asyncio.gather(*tasks)

# Run async function
def run_async_io(urls: list[str]) -> list[dict]:
    """Run async I/O operations."""
    return asyncio.run(async_concurrent_io(urls))
```

### 9.8 Best Practices and Common Pitfalls

#### Optimization Best Practices
```python
# 1. Profile before optimizing
@profile_code
def optimize_only_if_needed():
    """Only optimize after profiling."""
    # Don't optimize prematurely
    pass

# 2. Choose the right algorithm
def choose_algorithm():
    """Choose efficient algorithms."""
    # O(n log n) vs O(n^2)
    data = [5, 2, 8, 1, 9]
    sorted_data = sorted(data)  # Timsort - O(n log n)
    
    # Use built-in functions (optimized in C)
    total = sum(data)  # Faster than manual loop
    max_value = max(data)  # Faster than manual comparison

# 3. Use appropriate data structures
def use_right_data_structures():
    """Use efficient data structures."""
    # Set for membership testing (O(1) vs O(n))
    data_set = set(range(10000))
    result = 5000 in data_set  # Fast
    
    # Dictionary for key-value pairs
    data_dict = {i: i ** 2 for i in range(1000)}
    result = data_dict[500]  # Fast lookup

# 4. Avoid unnecessary work
def avoid_unnecessary_work():
    """Avoid redundant computations."""
    # Cache results
    @lru_cache(maxsize=None)
    def expensive_function(x: int) -> int:
        return x ** 2 + x + 1
    
    # Short-circuit evaluation
    def safe_division(a: int, b: int) -> Optional[float]:
        if b == 0:
            return None  # Avoid division by zero
        return a / b

# 5. Minimize I/O operations
def minimize_io():
    """Minimize I/O operations."""
    # Read/write in chunks
    with open('large_file.txt', 'r') as file:
        while chunk := file.read(8192):
            process_chunk(chunk)
    
    # Use buffering
    with open('output.txt', 'w', buffering=8192) as file:
        file.write("Data")
```

#### Common Performance Pitfalls
```python
# 1. Premature optimization
@profile_code
def avoid_premature_optimization():
    """Don't optimize before knowing it's needed."""
    # Focus on readability first
    data = [x ** 2 for x in range(100)]  # Clear and fast enough

# 2. Using the wrong data structure
def avoid_wrong_data_structures():
    """Use appropriate data structures."""
    # Bad: List for membership testing
    data = list(range(10000))
    result = 5000 in data  # O(n) - slow
    
    # Good: Set for membership testing
    data_set = set(range(10000))
    result = 5000 in data_set  # O(1) - fast

# 3. Unnecessary object creation
def avoid_unnecessary_objects():
    """Avoid creating unnecessary objects."""
    # Bad: Creating new strings in loop
    result = ""
    for i in range(1000):
        result += str(i)  # Creates new string each time
    
    # Good: Using list and join
    parts = []
    for i in range(1000):
        parts.append(str(i))
    result = "".join(parts)  # Efficient

# 4. Not using built-in functions
def use_builtins():
    """Use built-in functions."""
    data = [1, 2, 3, 4, 5]
    
    # Bad: Manual sum
    total = 0
    for x in data:
        total += x
    
    # Good: Built-in sum
    total = sum(data)  # Faster (implemented in C)
```

## Exercises

### Exercise 9.1: Profiling
Profile a given function and identify performance bottlenecks.

### Exercise 9.2: Algorithm Optimization
Optimize a slow algorithm and measure the improvement.

### Exercise 9.3: Data Structure Selection
Choose the right data structure for different scenarios.

### Exercise 9.4: Caching
Implement caching for an expensive computation.

### Exercise 9.5: Concurrency
Use threading or multiprocessing to speed up I/O-bound or CPU-bound tasks.

### Exercise 9.6: Benchmarking
Compare different implementations using benchmarking tools.

## Assessment Questions

1. What is the difference between time complexity and space complexity?
2. When would you use threading versus multiprocessing?
3. How does caching improve performance?
4. What are the benefits of using built-in functions?
5. How do you measure performance improvements?

## Real-World Applications
- Optimizing web applications for better response times
- Processing large datasets efficiently
- Building high-performance APIs
- Creating responsive user interfaces
- Scaling applications to handle more users
- Reducing infrastructure costs through optimization