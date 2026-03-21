# Lesson 9: Performance Optimization

## Lesson Overview
This lesson covers performance optimization techniques in Python, including profiling, benchmarking, and optimization strategies. Students will learn how to identify bottlenecks and improve code efficiency.

## Learning Objectives
By the end of this lesson, students will be able to:
- Use profiling tools to identify performance bottlenecks
- Understand time and space complexity
- Optimize algorithms and data structures
- Use caching and memoization techniques
- Implement concurrency and parallelism
- Use just-in-time (JIT) compilation
- Optimize memory usage
- Use appropriate data structures
- Apply performance best practices
- Measure and compare performance

## Topics Covered

### 9.1 Profiling Tools
```python
# Using cProfile for function profiling
import cProfile
import re

def calculate_sum(n):
    return sum(range(n))

def calculate_factorial(n):
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

def test_performance():
    calculate_sum(1000000)
    calculate_factorial(100)

# Basic profiling
cProfile.run('test_performance()')

# Profiling to file
cProfile.run('test_performance()', 'performance.prof')

# Analyzing profile results
import pstats
with open('profile_stats.txt', 'w') as f:
    p = pstats.Stats('performance.prof', stream=f)
    p.sort_stats('cumulative').print_stats(10)

# Using line_profiler
# Install: pip install line_profiler
# @profile decorator
@profile
def slow_function():
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

# Using memory_profiler
# Install: pip install memory_profiler
# @profile decorator
@profile
def memory_heavy():
    data = [i for i in range(1000000)]
    return data

# Using timeit for benchmarking
import timeit

time_taken = timeit.timeit('calculate_sum(1000000)', globals=globals(), number=10)
print(f"Time taken: {time_taken:.4f} seconds")

# timeit with setup
code_to_test = """
import random
numbers = [random.randint(1, 100) for _ in range(1000)]
result = sum(numbers)
"""
time_taken = timeit.timeit(code_to_test, number=1000)
print(f"Average time: {time_taken/1000:.6f} seconds")
```

# Using line_profiler for line-by-line profiling
# Install: pip install line_profiler
# Usage: @profile decorator
@profile
def slow_function():
    result = 0
    for i in range(1000000):
        result += i ** 2
    return result

slow_function()

# Using memory_profiler for memory usage
# Install: pip install memory_profiler
# Usage: @profile decorator
@profile
def memory_heavy():
    data = [i for i in range(1000000)]
    return sum(data)

memory_heavy()

# Using timeit for benchmarking
import timeit

# Simple timing
time_taken = timeit.timeit('calculate_sum(1000000)', 
                          setup='from __main__ import calculate_sum', 
                          number=10)
print(f"Time taken: {time_taken:.4f} seconds")

# Setup and timing
time_taken = timeit.timeit('calculate_factorial(100)', 
                          setup='from __main__ import calculate_factorial', 
                          number=100)
print(f"Time taken: {time_taken:.4f} seconds")

# Using %%timeit in Jupyter notebooks
# %%timeit calculate_sum(1000000)
```

### 9.2 Time Complexity Analysis
```python
# Constant time O(1)
def get_first_element(lst):
    if lst:
        return lst[0]
    return None

# Linear time O(n)
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Quadratic time O(n^2)
def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                duplicates.append(lst[i])
    return duplicates

# Logarithmic time O(log n)
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Linearithmic time O(n log n)
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Exponential time O(2^n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Optimized with memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Comparing performance
import time

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

# Test different implementations
result1, time1 = measure_time(fibonacci_recursive, 35)
result2, time2 = measure_time(fibonacci_memo, 35)
print(f"Recursive: {time1:.4f}s, Memoized: {time2:.4f}s")
```

### 9.3 Algorithm Optimization
```python
# Optimizing nested loops
# Before: O(n^2)
def find_pairs_brute_force(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

# After: O(n) using hash table
ndef find_pairs_optimized(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

# Optimizing string operations
# Before: O(n^2)
def has_duplicate_characters(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return True
    return False

# After: O(n) using set
def has_duplicate_characters_optimized(s):
    return len(s) != len(set(s))

# Optimizing list operations
# Before: O(n^2)
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# After: O(n) using set
def remove_duplicates_optimized(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Optimizing search operations
# Before: O(n)
def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# After: Using built-in (often optimized in C)
def find_max_optimized(lst):
    return max(lst) if lst else None

# Optimizing mathematical operations
# Before: O(n)
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# After: Using formula O(1)
def sum_of_squares_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6
```

### 9.4 Data Structure Optimization
```python
# Choosing appropriate data structures
import timeit
import random

# List vs Set for membership testing
lst = list(range(10000))
set_data = set(lst)

# List membership: O(n)
list_time = timeit.timeit('1000 in lst', 
                         setup='lst = list(range(10000))', 
                         number=1000)

# Set membership: O(1)
set_time = timeit.timeit('1000 in set_data', 
                        setup='set_data = set(range(10000))', 
                        number=1000)

print(f"List membership: {list_time:.6f}s")
print(f"Set membership: {set_time:.6f}s")

# Dictionary for key-value lookups
# Before: O(n) with list of tuples
pairs = [(i, i ** 2) for i in range(10000)]
def get_value_brute(key):
    for k, v in pairs:
        if k == key:
            return v
    return None

# After: O(1) with dictionary
dict_data = {i: i ** 2 for i in range(10000)}
def get_value_dict(key):
    return dict_data.get(key)

# Performance comparison
dict_time = timeit.timeit('get_value_dict(5000)', 
                         setup='from __main__ import get_value_dict', 
                         number=10000)
list_time = timeit.timeit('get_value_brute(5000)', 
                         setup='from __main__ import get_value_brute', 
                         number=10000)

print(f"Dict lookup: {dict_time:.6f}s")
print(f"List lookup: {list_time:.6f}s")

# Using deque for queue operations
from collections import deque

# List as queue (inefficient)
queue = []
for i in range(10000):
    queue.append(i)  # O(1)
for _ in range(5000):
    queue.pop(0)  # O(n) - inefficient

# Deque as queue (efficient)
queue = deque()
for i in range(10000):
    queue.append(i)  # O(1)
for _ in range(5000):
    queue.popleft()  # O(1) - efficient

# Using heapq for priority queue
import heapq

# Priority queue operations
heap = []
for i in range(10000):
    heapq.heappush(heap, random.randint(1, 100000))  # O(log n)

# Get smallest element
smallest = heapq.heappop(heap)  # O(log n)

# Using bisect for sorted lists
import bisect

# Binary search insertion
lst = []
for i in range(1000):
    num = random.randint(1, 10000)
    bisect.insort(lst, num)  # O(n) for insertion, but keeps sorted

# Finding insertion point
pos = bisect.bisect_left(lst, 5000)  # O(log n)
```

### 9.5 Caching and Memoization
```python
# Simple memoization with decorator
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Using functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Testing cache effectiveness
import time

def measure_cached(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

# First call (computes)
result1, time1 = measure_cached(factorial, 100)
print(f"First call: {time1:.6f}s")

# Second call (cache hit)
result2, time2 = measure_cached(factorial, 100)
print(f"Second call: {time2:.6f}s")

# Using cache_info
print(f"Cache info: {factorial.cache_info()}")

# Clearing cache
factorial.cache_clear()

# Manual caching with dictionary
class ExpensiveOperation:
    def __init__(self):
        self.cache = {}
    
    def compute(self, x):
        if x in self.cache:
            return self.cache[x]
        
        # Simulate expensive computation
        import time
        time.sleep(0.1)
        result = x ** 2 + x + 41  # Example computation
        self.cache[x] = result
        return result

# Caching with TTL (time-to-live)
import time
from threading import Lock

class TTLCache:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.cache = {}
        self.lock = Lock()
    
    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, timestamp = self.cache[key]
                if time.time() - timestamp < self.ttl:
                    return value
                else:
                    del self.cache[key]
            return None
    
    def set(self, key, value):
        with self.lock:
            self.cache[key] = (value, time.time())

# Using caching in web applications
from flask import Flask, request
from functools import wraps

app = Flask(__name__)

def cache_response(timeout=60):
    def decorator(f):
        cache = {}
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = request.path + str(request.args)
            if cache_key in cache:
                return cache[cache_key]
            
            response = f(*args, **kwargs)
            cache[cache_key] = response
            return response
        return decorated_function
    return decorator

@app.route('/api/data')
@cache_response(timeout=60)
def get_data():
    # Simulate expensive API call
    import time
    time.sleep(0.5)
    return {'data': 'cached result'}
```

### 9.6 Concurrency and Parallelism
```python
# Using threading for I/O-bound tasks
import threading
import time

def io_bound_task(task_id, delay):
    print(f"Task {task_id} started")
    time.sleep(delay)
    print(f"Task {task_id} completed")

# Sequential execution
start_time = time.time()
for i in range(5):
    io_bound_task(i, 1)
print(f"Sequential time: {time.time() - start_time:.2f}s")

# Parallel execution
start_time = time.time()
threads = []
for i in range(5):
    t = threading.Thread(target=io_bound_task, args=(i, 1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print(f"Parallel time: {time.time() - start_time:.2f}s")

# Using multiprocessing for CPU-bound tasks
import multiprocessing

def cpu_bound_task(n):
    # Simulate CPU-intensive work
    return sum(i * i for i in range(n))

# Sequential
start_time = time.time()
results = [cpu_bound_task(1000000) for _ in range(4)]
print(f"Sequential CPU time: {time.time() - start_time:.2f}s")

# Parallel
start_time = time.time()
with multiprocessing.Pool(4) as pool:
    results = pool.map(cpu_bound_task, [1000000] * 4)
print(f"Parallel CPU time: {time.time() - start_time:.2f}s")

# Using concurrent.futures for high-level concurrency
from concurrent.futures import ThreadPoolExecutor, as_completed

# ThreadPoolExecutor for I/O-bound tasks
def fetch_url(url):
    import requests
    try:
        response = requests.get(url, timeout=5)
        return url, response.status_code
    except Exception as e:
        return url, str(e)

urls = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.python.org',
    'https://www.example.com'
]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(fetch_url, url) for url in urls]
    for future in as_completed(futures):
        url, result = future.result()
        print(f"{url}: {result}")

# ProcessPoolExecutor for CPU-bound tasks
def process_data(data):
    # Simulate data processing
    return sum(x ** 2 for x in data)

data_chunks = [list(range(1000000)) for _ in range(4)]

with multiprocessing.Pool(4) as pool:
    results = pool.map(process_data, data_chunks)
    print(f"Results: {results}")

# Using asyncio for asynchronous I/O
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        
        results = await asyncio.gather(*tasks)
        for url, content in zip(urls, results):
            print(f"{url}: {len(content)} characters")

# Run asyncio event loop
import time
start_time = time.time()
asyncio.run(main())
print(f"Async time: {time.time() - start_time:.2f}s")

# Using queues for thread-safe communication
from queue import Queue

def producer(queue, items):
    for item in items:
        queue.put(item)
        print(f"Produced: {item}")
    queue.put(None)  # Sentinel to indicate end

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        queue.task_done()

# Using queue with threads
queue = Queue()
producer_thread = threading.Thread(target=producer, args=(queue, range(10)))
consumer_thread = threading.Thread(target=consumer, args=(queue,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
```

### 9.7 Just-In-Time (JIT) Compilation
```python
# Using Numba for JIT compilation
# Install: pip install numba
from numba import jit
import numpy as np

# Regular Python function
def slow_function(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# JIT-compiled version
@jit(nopython=True)
def fast_function(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# Performance comparison
a = np.random.rand(1000000)
b = np.random.rand(1000000)

# First run (compilation + execution)
start = time.perf_counter()
slow_function(a, b)
print(f"Slow function first run: {time.perf_counter() - start:.4f}s")

# Subsequent runs
start = time.perf_counter()
slow_function(a, b)
print(f"Slow function subsequent: {time.perf_counter() - start:.4f}s")

# JIT-compiled
start = time.perf_counter()
fast_function(a, b)
print(f"JIT function first run: {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
fast_function(a, b)
print(f"JIT function subsequent: {time.perf_counter() - start:.4f}s")

# Using Cython for compiled Python
# Install: pip install cython
# Create .pyx file and setup.py
# Run: python setup.py build_ext --inplace

# Example Cython function (in .pyx file)
# def fast_sum(double[:] a, double[:] b):
#     cdef int i
#     cdef double result = 0
#     for i in range(len(a)):
#         result += a[i] * b[i]
#     return result

# Using PyPy for alternative Python implementation
# Install: Download PyPy from https://www.pypy.org/
# Run: pypy script.py

# PyPy often provides 4-7x speedup for pure Python code

# Using Numba vectorization
@jit(nopython=True)
def vectorized_add(a, b):
    return a + b

# Performance comparison
import numpy as np

a = np.random.rand(1000000)
b = np.random.rand(1000000)

# Python loop
start = time.perf_counter()
result1 = np.zeros_like(a)
for i in range(len(a)):
    result1[i] = a[i] + b[i]
print(f"Python loop: {time.perf_counter() - start:.4f}s")

# NumPy (already optimized)
start = time.perf_counter()
result2 = a + b
print(f"NumPy: {time.perf_counter() - start:.4f}s")

# Numba JIT
start = time.perf_counter()
result3 = vectorized_add(a, b)
print(f"Numba JIT: {time.perf_counter() - start:.4f}s")

# Using Numba for different data types
@jit(nopython=True)
def process_integers(a):
    result = 0
    for i in range(len(a)):
        result += a[i] * i
    return result

@jit(nopython=True)
def process_floats(a):
    result = 0.0
    for i in range(len(a)):
        result += a[i] * i
    return result

# Performance with different types
import array

int_array = array.array('i', range(1000000))
float_array = array.array('d', (float(i) for i in range(1000000)))

start = time.perf_counter()
process_integers(int_array)
print(f"Integers: {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
process_floats(float_array)
print(f"Floats: {time.perf_counter() - start:.4f}s")
```

### 9.8 Memory Optimization
```python
# Using generators for memory efficiency
# Before: O(n) memory
def create_large_list(n):
    return [i ** 2 for i in range(n)]

# After: O(1) memory with generator
def create_large_generator(n):
    for i in range(n):
        yield i ** 2

# Memory comparison
import sys

# List
large_list = create_large_list(1000000)
print(f"List memory: {sys.getsizeof(large_list)} bytes")

# Generator
large_gen = create_large_generator(1000000)
print(f"Generator memory: {sys.getsizeof(large_gen)} bytes")

# Using array for homogeneous numeric data
import array

# List of numbers
lst = list(range(1000000))
print(f"List memory: {sys.getsizeof(lst)} bytes")

# Array of integers
arr = array.array('i', range(1000000))
print(f"Array memory: {sys.getsizeof(arr)} bytes")

# Using bytes for binary data
# Before: List of integers
binary_data = [255, 128, 64, 32, 16, 8, 4, 2, 1]
print(f"List memory: {sys.getsizeof(binary_data)} bytes")

# After: Bytes object
binary_data = bytes([255, 128, 64, 32, 16, 8, 4, 2, 1])
print(f"Bytes memory: {sys.getsizeof(binary_data)} bytes")

# Using __slots__ for memory-efficient classes
# Before: Regular class
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# After: Slots class
class SlotPoint:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
import sys

regular = [RegularPoint(i, i) for i in range(10000)]
slots = [SlotPoint(i, i) for i in range(10000)]

print(f"Regular class memory: {sys.getsizeof(regular)} bytes")
print(f"Slots class memory: {sys.getsizeof(slots)} bytes")

# Using weakref for caching without memory leaks
import weakref

class ExpensiveObject:
    def __init__(self, value):
        self.value = value
    
    def compute(self):
        # Simulate expensive computation
        return self.value ** 2

class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def get(self, key):
        return self._cache.get(key)
    
    def set(self, key, value):
        self._cache[key] = value

# Using the cache
cache = Cache()
obj1 = ExpensiveObject(10)
cache.set('obj1', obj1)

# obj1 can be garbage collected if no other references exist
obj1 = None
import gc

gc.collect()
print(f"Cache after GC: {list(cache._cache.keys())}")

# Using context managers for resource management
class ManagedResource:
    def __init__(self):
        self.data = [0] * 1000000  # Large resource
    
    def __enter__(self):
        print("Acquiring resource")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        self.data = None  # Release memory

def use_resource():
    with ManagedResource() as resource:
        # Use resource
        result = sum(resource.data)
    # Resource is released here
    return result

# Using memoryview for efficient buffer access
data = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09')
view = memoryview(data)

# Slice without copying
slice_view = view[1:5]
print(f"Slice view: {slice_view.tobytes()}")

# Modifying through view
slice_view[0] = 255
print(f"Modified data: {data}")
```

### 9.9 Performance Best Practices
```python
# Use built-in functions and libraries
# They're implemented in C and highly optimized
import operator

def sum_with_builtin(lst):
    return sum(lst)

def sum_with_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total

def sum_with_reduce(lst):
    from functools import reduce
    return reduce(operator.add, lst, 0)

# Performance comparison
lst = list(range(100000))

# Built-in sum (usually fastest)
builtin_time = timeit.timeit('sum_with_builtin(lst)', 
                            setup='from __main__ import sum_with_builtin, lst', 
                            number=1000)

# Manual loop
loop_time = timeit.timeit('sum_with_loop(lst)', 
                         setup='from __main__ import sum_with_loop, lst', 
                         number=1000)

# Reduce
reduce_time = timeit.timeit('sum_with_reduce(lst)', 
                           setup='from __main__ import sum_with_reduce, lst', 
                           number=1000)

print(f"Built-in: {builtin_time:.6f}s")
print(f"Loop: {loop_time:.6f}s")
print(f"Reduce: {reduce_time:.6f}s")

# Avoid unnecessary computations
# Before: Computing same value multiple times
def inefficient_function(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += expensive_computation(i, j)
    return result

# After: Cache repeated computations
def efficient_function(n):
    result = 0
    cache = {}
    for i in range(n):
        for j in range(n):
            if (i, j) not in cache:
                cache[(i, j)] = expensive_computation(i, j)
            result += cache[(i, j)]
    return result

# Use appropriate algorithms
# Before: O(n^2) bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# After: O(n log n) Timsort (Python's default)
def optimized_sort(lst):
    return sorted(lst)

# Minimize I/O operations
# Before: Multiple small writes
with open('output.txt', 'w') as f:
    for i in range(1000):
        f.write(f"Line {i}\n")  # Many I/O operations

# After: Single large write
with open('output.txt', 'w') as f:
    lines = [f"Line {i}\n" for i in range(1000)]
    f.writelines(lines)  # Single I/O operation

# Use local variables
# Local variable access is faster than global
import math

def use_global():
    result = 0
    for i in range(1000000):
        result += math.sqrt(i)
    return result

def use_local():
    sqrt = math.sqrt
    result = 0
    for i in range(1000000):
        result += sqrt(i)
    return result

# Avoid creating unnecessary objects
# Before: Creating many temporary lists
result = []
for i in range(1000):
    temp = [i * j for j in range(100)]  # Creates 1000 temporary lists
    result.append(sum(temp))

# After: Using generator expressions
result = []
for i in range(1000):
    total = sum(i * j for j in range(100))  # No temporary list
    result.append(total)

# Use early returns and breaks
# Before: Checking all conditions
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            if item % 2 == 0:
                if item < 100:
                    result.append(item)
    return result

# After: Early returns and breaks
def process_data_optimized(data):
    result = []
    for item in data:
        if item <= 0:
            continue
        if item >= 100:
            continue
        if item % 2 != 0:
            continue
        result.append(item)
    return result

# Use appropriate data structures
# For counting: collections.Counter
from collections import Counter

def count_items(lst):
    return Counter(lst)

# For grouping: defaultdict
from collections import defaultdict

def group_by_key(data):
    groups = defaultdict(list)
    for item in data:
        groups[item['key']].append(item)
    return groups

# For memoization: functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    # Simulate expensive computation
    import time
    time.sleep(0.1)
    return x ** 2
```

### 9.10 Exercises

1. **Exercise 1**: Profile a given function and identify the top 3 performance bottlenecks. Optimize the function and measure the improvement.

2. **Exercise 2**: Implement a memoized version of the Fibonacci function and compare its performance with the naive recursive implementation.

3. **Exercise 3**: Write a program that processes a large CSV file (1GB+) using memory-efficient techniques and measures memory usage.

4. **Exercise 4**: Create a concurrent web scraper that fetches multiple URLs simultaneously and compare its performance with a sequential version.

5. **Exercise 5**: Optimize a nested loop algorithm from O(n^2) to O(n) using appropriate data structures.

### 9.11 Real-World Applications

- Data processing pipelines for big data
- Web application performance optimization
- Scientific computing and simulations
- Machine learning model training
- Game development and real-time systems
- Financial modeling and analysis
- Database query optimization
- API response time optimization

### 9.12 Best Practices

- Profile before optimizing
- Focus on bottlenecks, not micro-optimizations
- Use appropriate data structures
- Consider time-space tradeoffs
- Write readable code first, optimize later
- Use caching strategically
- Test performance improvements
- Monitor production performance
- Document performance characteristics
- Consider scalability from the start

### 9.13 Common Pitfalls

- Premature optimization
- Over-engineering solutions
- Ignoring algorithmic complexity
- Not measuring performance
- Optimizing the wrong parts of code
- Sacrificing code readability
- Not considering memory usage
- Ignoring concurrency issues
- Not testing with realistic data
- Failing to monitor production performance