# Lesson 4: Context Managers and Exception Handling

## Lesson Overview
This lesson covers context managers and exception handling in Python, focusing on resource management and robust error handling patterns. Students will learn how to create custom context managers and implement comprehensive exception handling.

## Learning Objectives
By the end of this lesson, students will be able to:
- Create custom context managers using class-based and decorator approaches
- Understand the context manager protocol (__enter__, __exit__)
- Use context managers for resource management
- Implement comprehensive exception handling patterns
- Create custom exception classes
- Use exception chaining and context
- Apply the EAFP (Easier to Ask for Forgiveness than Permission) principle
- Handle multiple exceptions effectively
- Use finally blocks for cleanup
- Implement retry patterns with exception handling

## Topics Covered

### 4.1 Context Manager Protocol
```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering the context"""
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting the context"""
        if self.file:
            self.file.close()
        
        # Handle exceptions if they occurred
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
            # Return True to suppress the exception, False to propagate it
            return False

# Usage
with ManagedFile('example.txt', 'w') as file:
    file.write("Hello, World!")
    # No need to manually close the file
```

### 4.2 Contextlib and Decorator Approach
```python
import contextlib
from typing import Any, Callable

@contextlib.contextmanager
def managed_file(filename, mode):
    """Context manager as a generator"""
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Usage
with managed_file('example.txt', 'w') as file:
    file.write("Hello, World!")

# Multiple context managers
with managed_file('file1.txt', 'r') as f1, managed_file('file2.txt', 'w') as f2:
    content = f1.read()
    f2.write(content)

# Context manager for timing
@contextlib.contextmanager
def timer(name):
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"{name} took {elapsed:.4f} seconds")

# Usage
with timer('File processing'):
    process_file('large_file.txt')
```

### 4.3 Custom Exception Classes
```python
class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class ValidationError(CustomError):
    """Exception raised for validation errors"""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"Validation error in {field}: {message}")

class DatabaseError(CustomError):
    """Exception raised for database errors"""
    def __init__(self, operation: str, details: str = ""):
        self.operation = operation
        self.details = details
        super().__init__(f"Database error during {operation}: {details}")

class ResourceNotFoundError(CustomError):
    """Exception raised when a resource is not found"""
    def __init__(self, resource_type: str, resource_id: str):
        self.resource_type = resource_type
        self.resource_id = resource_id
        super().__init__(f"{resource_type} with ID {resource_id} not found")

# Usage
try:
    user = get_user_from_db(user_id)
    if user is None:
        raise ResourceNotFoundError("User", user_id)
    
    if not validate_user(user):
        raise ValidationError("user", "Invalid data format")
    
except ResourceNotFoundError as e:
    log_error(e)
    return None
except ValidationError as e:
    log_error(e)
    raise
except CustomError as e:
    log_error(e)
    raise DatabaseError("User retrieval", str(e))
```

### 4.4 Exception Handling Patterns
```python
# EAFP (Easier to Ask for Forgiveness than Permission)
def get_dict_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None

# LBYL (Look Before You Leap) - less Pythonic
def get_dict_value_lbyl(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    return None

# Multiple exceptions
try:
    result = risky_operation()
except (ValueError, TypeError) as e:
    handle_data_error(e)
except ConnectionError as e:
    handle_connection_error(e)
except Exception as e:
    handle_unexpected_error(e)

# Exception chaining
class DataProcessingError(Exception):
    pass

try:
    data = fetch_data()
    processed = process_data(data)
except DataProcessingError as e:
    raise DataProcessingError("Failed to process data") from e

# Finally block for cleanup
def process_file_safely(file_path):
    file = None
    try:
        file = open(file_path, 'r')
        data = file.read()
        return process_data(data)
    except Exception as e:
        log_error(f"Error processing {file_path}: {e}")
        raise
    finally:
        if file:
            file.close()
            print(f"Closed file: {file_path}")
```

### 4.5 Retry Patterns with Context Managers
```python
import time
from typing import Callable, Any

class RetryManager:
    def __init__(self, max_retries=3, delay=1.0, backoff=2.0):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff
        self.attempts = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.attempts += 1
            if self.attempts < self.max_retries:
                wait_time = self.delay * (self.backoff ** (self.attempts - 1))
                print(f"Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
                return True  # Suppress exception to retry
            else:
                print("Max retries reached")
                return False  # Propagate exception

# Usage with retry
def unreliable_operation():
    if random.random() < 0.7:
        raise ConnectionError("Random failure")
    return "Success"

with RetryManager(max_retries=5, delay=0.5, backoff=1.5):
    result = unreliable_operation()
    print(f"Operation result: {result}")

# Retry decorator alternative
@retry_decorator(max_retries=5, delay=0.5)
def reliable_operation():
    return unreliable_operation()
```

### 4.6 Resource Management Examples
```python
# Database connection context manager
class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
    
    def __enter__(self):
        print("Connecting to database...")
        self.connection = connect_to_database(self.connection_string)
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            print("Closing database connection...")
            self.connection.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Database operation failed: {exc_value}")
            return False  # Propagate exception

# Usage
with DatabaseConnection("postgresql://...") as conn:
    result = conn.execute("SELECT * FROM users")
    print(result)

# File locking context manager
import fcntl

class FileLock:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None
    
    def __enter__(self):
        self.file = open(self.file_path, 'r+')
        fcntl.flock(self.file, fcntl.LOCK_EX)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            fcntl.flock(self.file, fcntl.LOCK_UN)
            self.file.close()

# Usage with file locking
with FileLock('shared_file.txt'):
    with open('shared_file.txt', 'r+') as f:
        data = f.read()
        f.seek(0)
        f.write(process_data(data))
```

## Exercises

### Exercise 4.1: Custom Context Manager
Create a context manager for:
- A timer that measures execution time
- A database transaction manager
- A file backup manager
- A resource pool manager

### Exercise 4.2: Exception Handling Strategy
Create a comprehensive exception handling system:
- Custom exception hierarchy
- Error logging and reporting
- Graceful degradation
- User-friendly error messages

### Exercise 4.3: Retry Mechanism
Create a robust retry mechanism:
- Exponential backoff
- Circuit breaker pattern
- Timeout handling
- Retry statistics and monitoring

### Exercise 4.4: Resource Cleanup
Create resource cleanup utilities:
- Temporary file manager
- Cache cleanup
- Connection pool management
- Memory management

## Assessment Questions

1. What is the purpose of the `__enter__` and `__exit__` methods in context managers?
2. How does the EAFP principle differ from LBYL in Python?
3. What are the benefits of creating custom exception classes?
4. How can you implement retry logic with exponential backoff?
5. What are some common use cases for context managers?