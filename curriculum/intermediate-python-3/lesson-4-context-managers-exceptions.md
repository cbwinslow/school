# Lesson 4: Context Managers and Exception Handling

## Overview
This lesson covers context managers for resource management and comprehensive exception handling patterns for building robust Python applications.

## Learning Objectives
By the end of this lesson, students will be able to:
- Create custom context managers using class-based and decorator approaches
- Use the `with` statement for resource management
- Implement comprehensive exception handling strategies
- Create custom exception hierarchies
- Use context managers for database connections, file operations, and network resources
- Implement retry logic and timeout handling
- Use context managers for transaction management
- Apply best practices for error handling and logging

## Topics

### 4.1 Context Managers Basics

#### Using Built-in Context Managers
```python
# File operations
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    print("File written successfully")

# Network connections
import socket

def create_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('example.com', 80))
    return sock

with create_connection() as sock:
    sock.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = sock.recv(4096)
    print("Response received")

# Database connections
import sqlite3

def create_database_connection():
    conn = sqlite3.connect('example.db')
    return conn

with create_database_connection() as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    print("Database operations completed")
```

#### Class-based Context Managers
```python
def DatabaseConnection:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to database {self.db_path}")
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        
        print("Closing database connection")
        if self.connection:
            self.connection.close()
        
        # Return False to propagate exceptions, True to suppress
        return False

# Usage
with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(f"Found {len(users)} users")
```

#### Context Manager Decorator
```python
def context_manager_decorator(func):
    """Decorator to create context managers from generator functions."""
    from contextlib import contextmanager
    
    @contextmanager
    def wrapper(*args, **kwargs):
        try:
            # Setup
            setup_result = func(*args, **kwargs)
            yield setup_result
        finally:
            # Cleanup
            pass
    
    return wrapper

@context_manager_decorator
def file_handler(file_path: str, mode: str):
    """Context manager for file operations."""
    file = open(file_path, mode)
    try:
        yield file
    finally:
        file.close()

# Usage
with file_handler('example.txt', 'w') as f:
    f.write('Hello, World!')
```

### 4.2 Custom Context Managers

#### Resource Management
```python
def Resource:
    def __init__(self, resource_id: str):
        self.resource_id = resource_id
        self.is_acquired = False
    
    def acquire(self):
        if self.is_acquired:
            raise RuntimeError(f"Resource {self.resource_id} already acquired")
        print(f"Acquiring resource {self.resource_id}")
        self.is_acquired = True
    
    def release(self):
        if not self.is_acquired:
            raise RuntimeError(f"Resource {self.resource_id} not acquired")
        print(f"Releasing resource {self.resource_id}")
        self.is_acquired = False
    
    def __enter__(self):
        self.acquire()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return False  # Don't suppress exceptions

# Usage
with Resource('database_connection') as res:
    print("Using resource")
    # If an exception occurs here, release is still called
```

#### Transaction Management
```python
def Transaction:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None
        self.in_transaction = False
    
    def __enter__(self):
        print("Starting transaction")
        self.connection.execute('BEGIN')
        self.in_transaction = True
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("Rolling back transaction due to error")
            self.connection.execute('ROLLBACK')
        else:
            print("Committing transaction")
            self.connection.execute('COMMIT')
        
        self.in_transaction = False
        return False  # Don't suppress exceptions

# Usage
with DatabaseConnection('example.db') as conn:
    with Transaction(conn) as cursor:
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('Bob',))
        # If any error occurs, both inserts are rolled back
```

#### Timeout Context Manager
```python
def timeout(seconds: int):
    """Context manager that raises TimeoutError if block takes too long."""
    import signal
    
    class TimeoutException(Exception):
        pass
    
    def handler(signum, frame):
        raise TimeoutException(f"Operation timed out after {seconds} seconds")
    
    def __enter__(self):
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(seconds)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)  # Cancel the alarm
        return False

# Usage
with timeout(5):
    # This block must complete within 5 seconds
    import time
    time.sleep(3)  # OK
    # time.sleep(6)  # This would raise TimeoutException
```

### 4.3 Exception Handling Patterns

#### Exception Hierarchy
```python
def create_exception_hierarchy():
    """Create a hierarchy of custom exceptions."""
    class ApplicationError(Exception):
        """Base class for application-specific exceptions."""
        def __init__(self, message: str, code: int = 500):
            super().__init__(message)
            self.code = code
        
        def __str__(self):
            return f"[{self.code}] {super().__str__()}"
    
    class ValidationError(ApplicationError):
        """Raised when data validation fails."""
        def __init__(self, message: str, field: str = None):
            super().__init__(message, code=400)
            self.field = field
    
    class DatabaseError(ApplicationError):
        """Raised for database-related errors."""
        def __init__(self, message: str, operation: str = None):
            super().__init__(message, code=503)
            self.operation = operation
    
    class NetworkError(ApplicationError):
        """Raised for network-related errors."""
        def __init__(self, message: str, endpoint: str = None):
            super().__init__(message, code=503)
            self.endpoint = endpoint
    
    class BusinessLogicError(ApplicationError):
        """Raised for business logic violations."""
        def __init__(self, message: str, context: str = None):
            super().__init__(message, code=422)
            self.context = context
    
    return ApplicationError, ValidationError, DatabaseError, NetworkError, BusinessLogicError

# Usage
ApplicationError, ValidationError, DatabaseError, NetworkError, BusinessLogicError = create_exception_hierarchy()

try:
    # Some operation that might fail
    raise ValidationError("Invalid email format", field="email")
except ValidationError as e:
    print(f"Validation error: {e}")
    print(f"Field: {e.field}")
except DatabaseError as e:
    print(f"Database error during {e.operation}: {e}")
except NetworkError as e:
    print(f"Network error connecting to {e.endpoint}: {e}")
except ApplicationError as e:
    print(f"Application error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

#### Retry Logic
```python
def retry(max_attempts: int, delay: float = 1.0, backoff: float = 2.0):
    """Decorator to retry a function on failure."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1}/{max_attempts} failed: {e}")
                    
                    if attempt < max_attempts - 1:
                        print(f"Retrying in {current_delay} seconds...")
                        time.sleep(current_delay)
                        current_delay *= backoff
            
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1, backoff=2)
def unreliable_operation():
    """Operation that sometimes fails."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise RuntimeError("Random failure")
    return "Success"

# Usage
try:
    result = unreliable_operation()
    print(f"Operation succeeded: {result}")
except Exception as e:
    print(f"Operation failed after retries: {e}")
```

#### Context Manager for Error Handling
```python
def error_handling_context(operation_name: str):
    """Context manager for standardized error handling."""
    import logging
    
    logger = logging.getLogger(__name__)
    
    def __enter__(self):
        logger.info(f"Starting operation: {operation_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logger.error(f"Operation {operation_name} failed: {exc_val}")
            # Handle specific exception types
            if issubclass(exc_type, ValidationError):
                logger.warning("Validation error occurred")
            elif issubclass(exc_type, DatabaseError):
                logger.critical("Database error occurred")
            
            # Return False to propagate exception, True to suppress
            return False
        else:
            logger.info(f"Operation {operation_name} completed successfully")
            return True

# Usage
with error_handling_context("User Registration"):
    # Registration logic
    if not validate_email(email):
        raise ValidationError("Invalid email format")
    
    try:
        save_user_to_database(user_data)
    except DatabaseError as e:
        raise DatabaseError(f"Failed to save user: {e}")
```

### 4.4 Advanced Context Manager Patterns

#### Multiple Context Managers
```python
def process_files(input_path: str, output_path: str):
    """Process files with proper resource management."""
    with open(input_path, 'r') as input_file, \
         open(output_path, 'w') as output_file:
        
        for line in input_file:
            # Process line
            processed_line = line.strip().upper()
            output_file.write(processed_line + '\n')
    
    print(f"Processing complete: {input_path} -> {output_path}")

# Usage
process_files('input.txt', 'output.txt')
```

#### Context Manager with Return Values
```python
def resource_with_result():
    """Context manager that returns a result."""
    class ResultContext:
        def __enter__(self):
            print("Acquiring resource")
            self.resource = "Resource object"
            self.result = "Computation result"
            return self.resource, self.result
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Releasing resource")
            return False
    
    return ResultContext()

# Usage
with resource_with_result() as (resource, result):
    print(f"Resource: {resource}")
    print(f"Result: {result}")
```

#### Context Manager for Temporary Directories
```python
def temporary_directory():
    """Context manager for creating temporary directories."""
    import tempfile
    import shutil
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)
        print(f"Deleted temporary directory: {temp_dir}")

# Usage
with temporary_directory() as tmpdir:
    temp_file = os.path.join(tmpdir, 'example.txt')
    with open(temp_file, 'w') as f:
        f.write('Temporary content')
    
    print(f"Created file in temporary directory: {temp_file}")
```

### 4.5 Best Practices for Exception Handling

#### Logging and Error Reporting
```python
def setup_logging():
    """Configure logging for error handling."""
    import logging
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('application.log'),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

logger = setup_logging()

def safe_operation():
    """Operation with comprehensive error handling."""
    try:
        # Main operation
        result = perform_risky_operation()
        logger.info("Operation completed successfully")
        return result
    except ValidationError as e:
        logger.warning(f"Validation error: {e}")
        raise
    except DatabaseError as e:
        logger.error(f"Database error: {e}")
        report_error_to_monitoring(e)
        raise
    except NetworkError as e:
        logger.error(f"Network error: {e}")
        retry_operation()
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        report_error_to_monitoring(e)
        raise ApplicationError(f"Unexpected error occurred: {e}")
```

#### Graceful Degradation
```python
def graceful_operation():
    """Operation that degrades gracefully on failure."""
    try:
        # Primary operation
        return primary_operation()
    except NetworkError:
        # Fallback to local cache
        logger.info("Network unavailable, using cached data")
        return get_cached_data()
    except DatabaseError:
        # Fallback to in-memory data
        logger.info("Database unavailable, using in-memory data")
        return get_in_memory_data()
    except Exception:
        # Last resort fallback
        logger.warning("Primary operation failed, using default values")
        return get_default_values()
```

## Exercises

### Exercise 4.1: Simple Context Manager
Create a context manager that measures the execution time of a code block.

### Exercise 4.2: File Processor
Implement a context manager for processing files that handles opening, reading, and closing automatically.

### Exercise 4.3: Database Transaction
Create a context manager for database transactions that commits on success and rolls back on failure.

### Exercise 4.4: Retry Decorator
Implement a retry decorator that retries failed operations with exponential backoff.

### Exercise 4.5: Custom Exception Hierarchy
Design a custom exception hierarchy for a specific application domain.

### Exercise 4.6: Resource Pool
Create a context manager that manages a pool of reusable resources.

## Assessment Questions

1. What is the purpose of the `__exit__` method in a context manager?
2. How do you handle exceptions within a context manager?
3. What is the difference between checked and unchecked exceptions in Python?
4. When would you use a retry decorator versus handling retries manually?
5. How can context managers help prevent resource leaks?

## Real-World Applications
- Database transaction management
- File and network resource handling
- API error handling and retry logic
- Resource pooling and management
- Graceful degradation in distributed systems
- Transaction rollback and commit patterns