# Lesson 8: Testing with Pytest

## Overview
This lesson covers testing fundamentals using pytest, a powerful testing framework for Python that enables comprehensive test suites for robust software development.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write basic unit tests with pytest
- Use test fixtures for setup and teardown
- Create parameterized tests
- Use assertions effectively
- Organize tests in test modules
- Mock external dependencies
- Measure test coverage
- Write integration tests
- Use pytest plugins and advanced features
- Apply testing best practices

## Topics

### 8.1 Basic Testing Concepts

#### Writing Your First Test
```python
# content.py - Module to be tested
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# test_content.py - Test file
import pytest
from content import add, subtract, multiply, divide

# Basic test
def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test with multiple assertions
def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

# Test with expected exceptions
def test_divide_by_zero():
    """Test that divide raises ValueError for zero denominator."""
    with pytest.raises(ValueError):
        divide(10, 0)

# Test with floating point numbers
def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
```

#### Test Discovery and Naming
```python
# Test files should be named:
# - test_*.py
# - *_test.py

# Test functions should be named:
# - test_*

# Test classes should be named:
# - Test*

# Example structure
# project/
# ├── content.py
# ├── test_content.py
# ├── tests/
# │   ├── test_content.py
# │   └── test_other.py
```

### 8.2 Test Fixtures

#### Basic Fixtures
```python
import pytest
from datetime import datetime, timedelta

# Simple fixture
def simple_fixture():
    """Simple fixture that returns a value."""
    return 42

# Using fixture in test
def test_using_fixture(simple_fixture):
    """Test that uses the simple_fixture."""
    assert simple_fixture == 42

# Fixture with setup and teardown
def setup_teardown_fixture():
    """Fixture with setup and teardown actions."""
    print("Setting up...")
    yield "setup complete"
    print("Tearing down...")

# Using setup/teardown fixture
def test_setup_teardown(setup_teardown_fixture):
    """Test that uses the setup/teardown fixture."""
    result = setup_teardown_fixture
    assert result == "setup complete"

# Fixture with parameters
def user_fixture(name: str = "Alice", age: int = 30):
    """Fixture that creates a user dictionary."""
    return {"name": name, "age": age}

# Using fixture with different parameters
def test_user_fixture(user_fixture):
    """Test with default user fixture."""
    user = user_fixture
    assert user["name"] == "Alice"
    assert user["age"] == 30

# Fixture with custom parameters
def test_specific_user(user_fixture):
    """Test with specific user parameters."""
    user = user_fixture("Bob", 25)
    assert user["name"] == "Bob"
    assert user["age"] == 25
```

#### Fixture Scopes
```python
# Function scope (default)
@pytest.fixture
def function_scoped():
    """Fixture with function scope."""
    print("Function setup")
    yield
    print("Function teardown")

# Class scope
@pytest.fixture(scope="class")
def class_scoped():
    """Fixture with class scope."""
    print("Class setup")
    yield
    print("Class teardown")

# Module scope
@pytest.fixture(scope="module")
def module_scoped():
    """Fixture with module scope."""
    print("Module setup")
    yield
    print("Module teardown")

# Session scope
@pytest.fixture(scope="session")
def session_scoped():
    """Fixture with session scope."""
    print("Session setup")
    yield
    print("Session teardown")

# Using different scopes
class TestScopes:
    def test_function_scope(self, function_scoped):
        """Test with function-scoped fixture."""
        pass
    
    def test_class_scope(self, class_scoped):
        """Test with class-scoped fixture."""
        pass
    
    def test_module_scope(self, module_scoped):
        """Test with module-scoped fixture."""
        pass
    
    def test_session_scope(self, session_scoped):
        """Test with session-scoped fixture."""
        pass
```

### 8.3 Parameterized Tests

#### Basic Parameterization
```python
import pytest

# Parameterized test with multiple sets of data
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300)
    ]
)
def test_add_parametrized(a, b, expected):
    """Test add function with multiple parameter sets."""
    from content import add
    assert add(a, b) == expected

# Parameterized test with different types
@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello", "hello"),
        (123, "123"),
        ([1, 2, 3], "[1, 2, 3]")
    ]
)
def test_str_conversion(input, expected):
    """Test string conversion with different input types."""
    assert str(input) == expected

# Parameterized test with ids
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0)
    ],
    ids=["positive", "zero", "negative"]
)
def test_add_with_ids(a, b, expected):
    """Test add function with custom ids."""
    from content import add
    assert add(a, b) == expected
```

#### Parameterized Fixtures
```python
# Parameterized fixture
def user_fixture(request):
    """Fixture that creates different users based on parameters."""
    users = {
        "admin": {"name": "Admin", "role": "admin", "permissions": ["read", "write", "delete"]},
        "user": {"name": "User", "role": "user", "permissions": ["read"]}, 
        "guest": {"name": "Guest", "role": "guest", "permissions": []}
    }
    
    user_type = request.param
    return users[user_type]

# Using parameterized fixture
@pytest.mark.parametrize("user_fixture", ["admin", "user", "guest"], indirect=True)
def test_user_permissions(user_fixture):
    """Test user permissions for different user types."""
    assert "name" in user_fixture
    assert "role" in user_fixture
    assert "permissions" in user_fixture
    
    if user_fixture["role"] == "admin":
        assert len(user_fixture["permissions"]) == 3
    elif user_fixture["role"] == "user":
        assert len(user_fixture["permissions"]) == 1
    else:
        assert len(user_fixture["permissions"]) == 0
```

### 8.4 Advanced Assertions

#### Using pytest Assertions
```python
import pytest
from content import divide

# Basic assertions
def test_basic_assertions():
    """Test various assertion types."""
    assert 2 + 2 == 4
    assert 2 + 2 != 5
    assert 3 > 2
    assert 2 < 3
    assert 3 >= 2
    assert 2 <= 3

# Assertions with messages
def test_assertions_with_messages():
    """Test assertions with custom messages."""
    assert 2 + 2 == 4, "2 + 2 should equal 4"
    assert 10 > 5, "10 should be greater than 5"

# Assertions with floating point numbers
def test_floating_point():
    """Test floating point assertions."""
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 1.0 / 3.0 == pytest.approx(0.333, rel=1e-3)

# Assertions with containers
def test_container_assertions():
    """Test assertions with lists, dicts, etc."""
    assert [1, 2, 3] == [1, 2, 3]
    assert {"a": 1, "b": 2} == {"a": 1, "b": 2}
    assert (1, 2, 3) == (1, 2, 3)
    
    # Subset assertions
    assert {"a": 1, "b": 2}.keys() == {"a", "b"}
    assert [1, 2, 3].count(2) == 1

# Assertions with None
def test_none_assertions():
    """Test assertions with None."""
    value = None
    assert value is None
    assert not value
    
    value = 42
    assert value is not None
    assert value
```

#### Custom Assertions
```python
# Custom assertion helper
def assert_user_equal(actual, expected):
    """Custom assertion for comparing user objects."""
    assert actual["name"] == expected["name"]
    assert actual["age"] == expected["age"]
    assert actual["email"] == expected["email"]

# Using custom assertion
def test_user_comparison():
    """Test user comparison with custom assertion."""
    actual = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    expected = {"name": "Alice", "age": 30, "email": "alice@example.com"}
    
    assert_user_equal(actual, expected)

# Assertion introspection
def test_introspection():
    """Test that shows pytest's assertion introspection."""
    data = [1, 2, 3]
    assert data == [1, 2, 4]  # pytest will show the difference
```

### 8.5 Mocking and Monkeypatch

#### Using monkeypatch
```python
import pytest
import requests
from unittest.mock import patch

# Function that makes HTTP requests
def get_user_data(user_id: int) -> dict:
    """Get user data from API."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()

# Test with monkeypatch
def test_get_user_data(monkeypatch):
    """Test get_user_data with mocked requests."""
    # Mock the requests.get function
    def mock_get(url):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            
            def json(self):
                return self.json_data
            
            def raise_for_status(self):
                if self.status_code != 200:
                    raise requests.HTTPError(f"Status code: {self.status_code}")
        
        if "404" in url:
            return MockResponse({}, 404)
        elif "500" in url:
            return MockResponse({}, 500)
        else:
            return MockResponse({"id": 1, "name": "Alice"}, 200)
    
    monkeypatch.setattr(requests, "get", mock_get)
    
    # Test successful response
    user_data = get_user_data(1)
    assert user_data["id"] == 1
    assert user_data["name"] == "Alice"
    
    # Test 404 error
    with pytest.raises(requests.HTTPError):
        get_user_data(404)
    
    # Test 500 error
    with pytest.raises(requests.HTTPError):
        get_user_data(500)
```

#### Using unittest.mock
```python
from unittest.mock import Mock, MagicMock, patch

# Test with MagicMock
def test_magicmock():
    """Test using MagicMock."""
    mock_obj = MagicMock()
    
    # Set return values
    mock_obj.add.return_value = 5
    assert mock_obj.add(2, 3) == 5
    
    # Check call history
    mock_obj.add.assert_called_once_with(2, 3)
    
    # Set side effects
    mock_obj.divide.side_effect = lambda x, y: x / y
    assert mock_obj.divide(10, 2) == 5
    
    # Test exception side effect
    mock_obj.divide.side_effect = ValueError("Division error")
    with pytest.raises(ValueError):
        mock_obj.divide(10, 0)

# Test with patch
@patch('content.requests')
def test_patch(requests_mock):
    """Test using patch decorator."""
    # Configure mock
    requests_mock.get.return_value.status_code = 200
    requests_mock.get.return_value.json.return_value = {"id": 1, "name": "Alice"}
    
    # Call the function
    from content import get_user_data
    user_data = get_user_data(1)
    
    # Assertions
    assert user_data["id"] == 1
    assert user_data["name"] == "Alice"
    
    # Verify calls
    requests_mock.get.assert_called_once_with("https://api.example.com/users/1")
```

### 8.6 Test Organization

#### Test Modules and Classes
```python
# content.py - Module to be tested
class Calculator:
    """Simple calculator class."""
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        return a - b
    
    def multiply(self, a: int, b: int) -> int:
        return a * b
    
    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# test_calculator.py - Test module
import pytest
from content import Calculator

# Test class for Calculator
class TestCalculator:
    """Test class for Calculator."""
    
    def setup_method(self):
        """Setup method called before each test."""
        self.calc = Calculator()
    
    def teardown_method(self):
        """Teardown method called after each test."""
        del self.calc
    
    def test_add(self):
        """Test add method."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtract method."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 5) == -2
        assert self.calc.subtract(0, 0) == 0
    
    def test_multiply(self):
        """Test multiply method."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide(self):
        """Test divide method."""
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test divide by zero raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
```

#### Test Fixtures for Setup/Teardown
```python
# conftest.py - Shared fixtures
import pytest
import tempfile
import os

# Database fixture
def database_fixture():
    """Fixture that creates a temporary database."""
    import sqlite3
    
    # Create temporary database
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY, user_id INTEGER, content TEXT)")
    
    # Insert test data
    cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie')")
    conn.commit()
    
    yield conn
    
    # Cleanup
    conn.close()

# Temporary directory fixture
def temp_dir_fixture():
    """Fixture that creates a temporary directory."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Cleanup
    shutil.rmtree(temp_dir)

# File fixture
def file_fixture(temp_dir_fixture):
    """Fixture that creates a test file."""
    file_path = os.path.join(temp_dir_fixture, "test.txt")
    with open(file_path, "w") as f:
        f.write("This is a test file.\nSecond line.")
    return file_path
```

### 8.7 Advanced pytest Features

#### Custom Markers
```python
# pytest.ini configuration
# [pytest]
# markers =
#     slow: marks tests as slow (deselect with '-m \"not slow\"')
#     integration: marks integration tests
#     smoke: marks smoke tests

# test_module.py
import pytest
import time

@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow."""
    time.sleep(2)
    assert True

@pytest.mark.integration
def test_integration():
    """Integration test."""
    assert True

@pytest.mark.smoke
def test_smoke():
    """Smoke test."""
    assert True

# Running specific markers
# pytest -m "slow"          # Only slow tests
# pytest -m "not slow"      # All except slow tests
# pytest -m "smoke or integration"  # Smoke or integration tests
```

#### pytest Plugins
```python
# Example: pytest-cov for coverage
# Install: pip install pytest-cov
# Run: pytest --cov=content

# Example: pytest-xdist for parallel execution
# Install: pip install pytest-xdist
# Run: pytest -n auto

# Example: pytest-mock for simplified mocking
# Install: pip install pytest-mock
# Usage: def test_example(mocker):

# Example: pytest-benchmark for performance testing
# Install: pip install pytest-benchmark
# Usage: @pytest.mark.benchmark(group="example")
```

#### Test Configuration
```ini
# pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q --tb=short
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*

# Coverage configuration
[tool:pytest.ini]
addopts = --cov=content --cov-report=html --cov-report=term-missing
```

### 8.8 Best Practices

#### Writing Good Tests
```python
# Good practices

def test_good_practices():
    """Examples of good testing practices."""
    # 1. Test one thing per test
    assert add(2, 3) == 5
    
    # 2. Use descriptive test names
    # test_add_positive_numbers() is better than test_1()
    
    # 3. Keep tests simple and focused
    # Don't test multiple scenarios in one test
    
    # 4. Use fixtures for setup/teardown
    # Don't repeat setup code in multiple tests
    
    # 5. Test edge cases and error conditions
    with pytest.raises(ValueError):
        divide(10, 0)
    
    # 6. Use parameterization for similar tests
    # Instead of writing multiple similar tests
    
    # 7. Mock external dependencies
    # Don't make real API calls in unit tests
    
    # 8. Keep tests independent
    # Tests should not depend on each other
    
    # 9. Use appropriate assertions
    # Don't just assert True/False
    
    # 10. Test both success and failure cases
    # Don't only test the happy path
```

#### Test Structure Guidelines
```python
# Recommended test structure
# project/
# ├── content/
# │   ├── __init__.py
# │   ├── module1.py
# │   └── module2.py
# ├── tests/
# │   ├── __init__.py
# │   ├── conftest.py
# │   ├── test_module1.py
# │   └── test_module2.py
# ├── pytest.ini
# └── setup.py

# Test file organization
def test_module():
    """Test module-level functions."""
    pass

class TestClass:
    """Test class for class-level testing."""
    
    def test_method(self):
        """Test instance method."""
        pass
    
    @classmethod
    def test_class_method(cls):
        """Test class method."""
        pass
```

## Exercises

### Exercise 8.1: Basic Tests
Write tests for a simple calculator module using pytest.

### Exercise 8.2: Test Fixtures
Create fixtures for setting up test data and resources.

### Exercise 8.3: Parameterized Tests
Write parameterized tests for a function with multiple input scenarios.

### Exercise 8.4: Mocking
Use mocking to test functions that make external API calls.

### Exercise 8.5: Test Organization
Organize tests in a project structure with shared fixtures.

### Exercise 8.6: Integration Tests
Write integration tests that test multiple components together.

## Assessment Questions

1. What is the difference between unit tests and integration tests?
2. How do fixtures help in test organization?
3. When would you use monkeypatch versus unittest.mock?
4. What are the benefits of parameterized tests?
5. How can you measure test coverage?

## Real-World Applications
- Building comprehensive test suites for applications
- Ensuring code quality and reliability
- Facilitating refactoring and maintenance
- Supporting continuous integration/continuous deployment (CI/CD)
- Documenting expected behavior through tests
- Catching bugs early in development