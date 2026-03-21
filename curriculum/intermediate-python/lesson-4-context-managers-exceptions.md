# 🔥 Lesson 4: Context Managers & Exception Handling

## Lesson Overview

**Duration**: 2 hours
**Difficulty**: Intermediate
**Prerequisites**: Basic file I/O, error handling

## Learning Objectives

By the end of this lesson, you will be able to:
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

## Key Concepts

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
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    # No need to close the file manually
```

### 4.2 Custom Exception Classes
```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Validation error in {field}: {message}")

class DatabaseError(Exception):
    def __init__(self, query, error):
        self.query = query
        self.error = error
        super().__init__(f"Database error in query '{query}': {error}")

class APIError(Exception):
    def __init__(self, endpoint, status_code, message):
        self.endpoint = endpoint
        self.status_code = status_code
        self.message = message
        super().__init__(f"API error at {endpoint}: {status_code} - {message}")

# Usage

def validate_user(user_data):
    if 'name' not in user_data:
        raise ValidationError('name', 'Name is required')
    if len(user_data['name']) < 2:
        raise ValidationError('name', 'Name must be at least 2 characters')
    if 'age' in user_data and user_data['age'] < 0:
        raise ValidationError('age', 'Age cannot be negative')


def process_user(user_data):
    try:
        validate_user(user_data)
        # Process user data
        print("User processed successfully")
    except ValidationError as e:
        print(f"Validation failed: {e}")
        raise  # Re-raise the exception
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
```

### 4.3 Exception Handling Patterns
```python
# Multiple exceptions

def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        return None
    else:
        print("Division successful")
        return result

# Finally block for cleanup

def read_file_safely(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    finally:
        if file:
            file.close()
            print("File closed")

# Try-except-else-finally

def process_data(data):
    try:
        # Try block
        result = complex_operation(data)
    except ValueError as e:
        # Except block
        print(f"Value error: {e}")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        # Else block (only if no exception)
        print("Operation completed successfully")
        return result
    finally:
        # Finally block (always executed)
        print("Cleaning up resources")

# Exception chaining

def outer_function():
    try:
        inner_function()
    except Exception as e:
        print(f"Outer caught: {e}")
        raise Exception("Outer error occurred") from e


def inner_function():
    try:
        risky_operation()
    except Exception as e:
        print(f"Inner caught: {e}")
        raise Exception("Inner error occurred") from e
```

### 4.4 EAFP vs LBYL
```python
# EAFP (Easier to Ask for Forgiveness than Permission)

def get_dict_value_eafp(d, key):
    try:
        return d[key]
    except KeyError:
        return None

# LBYL (Look Before You Leap)

def get_dict_value_lbyl(d, key):
    if key in d:
        return d[key]
    return None

# EAFP is generally preferred in Python

def process_file_eafp(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None

# LBYL alternative (less Pythonic)

def process_file_lbyl(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        print(f"File {filename} not found")
        return None
```

### 4.5 Retry Patterns
```python
import time
import random
from functools import wraps


def retry(max_attempts=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    print(f"Attempt {attempts} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= backoff
            return None
        return wrapper
    return decorator

@retry(max_attempts=5, delay=1, backoff=2)
def unreliable_operation():
    if random.random() < 0.7:
        raise ConnectionError("Random failure")
    return "Success"

# Usage
result = unreliable_operation()
print(f"Result: {result}")
```
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file {self.filename}...")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing file {self.filename}...")
        if self.file:
            self.file.close()
        return False

# Using both context managers
try:
    with DatabaseConnection("db://localhost") as db, FileHandler("data.txt", "r") as file:
        # Perform operations
        data = file.read()
        print(f"Data read: {data}")
        print(f"Database: {db}")
except Exception as e:
    print(f"Error occurred: {e}")
```

### 4. Exception Handling Patterns

```python
# Basic try-except

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("This always executes")

# Multiple exceptions

def process_data(data):
    try:
        result = int(data) / 2
    except (ValueError, TypeError):
        print("Invalid data type")
        return None
    except ZeroDivisionError:
        print("Division by zero")
        return None
    else:
        return result

# Catching specific exceptions

def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"No permission to read {filename}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### 5. Custom Exception Classes

```python
# Custom exception hierarchy
class ApplicationError(Exception):
    """Base class for application-specific exceptions"""
    pass

class ValidationError(ApplicationError):
    """Raised when data validation fails"""
    def __init__(self, field, message="Invalid value"):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class DatabaseError(ApplicationError):
    """Raised when database operations fail"""
    def __init__(self, operation, message="Database operation failed"):
        self.operation = operation
        self.message = message
        super().__init__(f"{operation}: {message}")

# Usage

def validate_user(user_data):
    if not user_data.get("name"):
        raise ValidationError("name", "Name is required")
    
    if not isinstance(user_data.get("age"), int):
        raise ValidationError("age", "Age must be an integer")
    
    if user_data["age"] < 0:
        raise ValidationError("age", "Age cannot be negative")


def save_user(user_data):
    try:
        validate_user(user_data)
        # Simulate database operation
        if user_data["age"] > 120:
            raise DatabaseError("insert", "Age out of range")
        print("User saved successfully")
    except ValidationError as ve:
        print(f"Validation error: {ve}")
        raise  # Re-raise for caller to handle
    except DatabaseError as de:
        print(f"Database error: {de}")
        # Handle database-specific logic
    except Exception as e:
        print(f"Unexpected error: {e}")
        # Log and handle unexpected errors
```

### 6. Exception Chaining and Context

```python
# Exception chaining

def read_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise ConfigError("config.json not found") from e
    except json.JSONDecodeError as e:
        raise ConfigError("Invalid JSON format") from e

class ConfigError(Exception):
    pass

# Using exception context

def process_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
            # Process data
            result = int(data) / 2
            return result
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        # Preserve original exception context
        raise ProcessingError(f"Failed to process {filename}") from e

class ProcessingError(Exception):
    pass
```

### 7. EAFP vs LBYL

```python
# EAFP (Easier to Ask for Forgiveness than Permission)

def get_dict_value_eafp(data, key):
    try:
        return data[key]
    except KeyError:
        return None

# LBYL (Look Before You Leap)

def get_dict_value_lbyl(data, key):
    if key in data:
        return data[key]
    return None

# EAFP is generally preferred in Python

def process_file_eafp(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

# LBYL alternative (less Pythonic)

def process_file_lbyl(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    return None
```

### 8. Retry Patterns with Exception Handling

```python
import time
import random
from functools import wraps


def retry(max_attempts=3, delay=1, backoff=2):
    """Decorator for retrying failed operations"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise
                    
                    print(f"Attempt {attempts} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= backoff
            return None
        return wrapper
    return decorator

@retry(max_attempts=5, delay=1, backoff=2)
def unreliable_operation():
    """Operation that fails randomly"""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Operation failed")
    return "Operation succeeded"

# Usage

def robust_data_processing():
    try:
        result = unreliable_operation()
        print(f"Result: {result}")
    except ConnectionError as e:
        print(f"All attempts failed: {e}")
        # Handle final failure
```

### 9. Context Managers for Resource Management

```python
# Database transaction context manager
class Transaction:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None
    
    def __enter__(self):
        print("Starting transaction...")
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Committing transaction...")
            self.connection.commit()
        else:
            print("Rolling back transaction...")
            self.connection.rollback()
        
        if self.cursor:
            self.cursor.close()
        return False

# Usage

def perform_database_operations():
    connection = get_database_connection()
    try:
        with Transaction(connection) as cursor:
            cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
            cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
            # If any exception occurs, transaction will be rolled back
    finally:
        connection.close()
```

## Exercises

### Exercise 1: Create a File Processing Context Manager

Build a context manager for file processing:
- Handle file opening and closing
- Support different file modes
- Include error handling
- Add progress tracking
- Support multiple files

### Exercise 2: Implement a Database Transaction Manager

Create a database transaction context manager:
- Handle connection management
- Support commit/rollback
- Include error handling
- Add retry logic
- Support nested transactions

### Exercise 3: Build a Resource Pool Manager

Create a resource pool context manager:
- Manage limited resources
- Handle resource allocation
- Support timeout
- Include cleanup
- Add monitoring

### Exercise 4: Create a Validation Framework

Build a comprehensive validation framework:
- Custom validation exceptions
- Validation decorators
- Error aggregation
- Internationalization support
- Integration with data classes

## Assessment Questions

1. What is the difference between EAFP and LBYL?
2. How do context managers improve resource management?
3. When would you create a custom exception class?
4. What is exception chaining and why is it useful?
5. How do you handle multiple exceptions in a single try block?