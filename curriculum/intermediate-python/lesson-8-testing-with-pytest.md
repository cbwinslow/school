# Lesson 8: Testing with pytest

## Lesson Overview
This lesson covers testing fundamentals in Python using pytest, the most popular testing framework. Students will learn how to write unit tests, integration tests, and use testing best practices to ensure code quality.

## Learning Objectives
By the end of this lesson, students will be able to:
- Write basic unit tests using pytest
- Use test fixtures for setup and teardown
- Create test classes and parameterized tests
- Use mocking and patching for external dependencies
- Write integration tests
- Use assertions effectively
- Generate and interpret test coverage reports
- Use pytest plugins and advanced features
- Implement test-driven development (TDD)
- Debug failing tests

## Topics Covered

### 8.1 Basic Testing with pytest
```python
# Simple test functions
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def multiply(a, b):
    return a * b

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

# Test classes
class TestMathOperations:
    def test_addition(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    
    def test_multiplication(self):
        assert multiply(2, 3) == 6
        assert multiply(-1, 5) == -5

# Running tests
# pytest test_math.py
# pytest -v test_math.py  # Verbose output
# pytest -x test_math.py  # Stop on first failure
```

### 8.2 Test Fixtures
```python
import pytest

# Simple fixture
def setup_database():
    print("Setting up database...")
    db = {}  # Simulate database connection
    yield db
    print("Tearing down database...")
    # Clean up resources

# Using fixture in test
class TestDatabaseOperations:
    def test_insert_user(self, setup_database):
        db = setup_database
        db['users'] = []
        db['users'].append({'id': 1, 'name': 'Alice'})
        assert len(db['users']) == 1
    
    def test_get_user(self, setup_database):
        db = setup_database
        db['users'] = [{'id': 1, 'name': 'Alice'}]
        user = next((u for u in db['users'] if u['id'] == 1), None)
        assert user is not None
        assert user['name'] == 'Alice'

# Fixture with parameters
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

# Using parameterized fixture
def test_number_properties(number):
    assert number > 0
    assert isinstance(number, int)

# Fixture with scope
@pytest.fixture(scope="module")
def module_database():
    print("Setting up module database...")
    db = {}
    yield db
    print("Tearing down module database...")

# Using module-scoped fixture
class TestModuleDatabase:
    def test_module_operation1(self, module_database):
        module_database['data'] = [1, 2, 3]
        assert len(module_database['data']) == 3
    
    def test_module_operation2(self, module_database):
        assert 'data' in module_database
        assert len(module_database['data']) == 3
```

def test_numeric_assertions():
    assert 5 == 5
    assert 5 != 6
    assert 10 > 5
    assert 3 <= 5

def test_list_assertions():
    assert [1, 2, 3] == [1, 2, 3]
    assert [1, 2, 3] != [1, 2, 4]
    assert 2 in [1, 2, 3]
    assert 4 not in [1, 2, 3]

def test_dict_assertions():
    data = {'name': 'Alice', 'age': 30}
    assert data['name'] == 'Alice'
    assert 'age' in data
    assert data.get('city') is None

def test_exception_assertions():
    import math
    
    # Test that function raises exception
    with pytest.raises(ValueError):
        math.sqrt(-1)
    
    # Test exception with message
    with pytest.raises(ValueError, match='math domain error'):
        math.sqrt(-1)

def test_approx_assertions():
    # For floating point comparisons
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert 1.0001 == pytest.approx(1.0, rel=1e-3)
```

### 8.3 Test Fixtures
```python
import pytest

# Simple fixture
def setup_database():
    """Setup test database"""
    print("Setting up database...")
    db = {'users': []}
    yield db
    print("Tearing down database...")
    # Cleanup code here

# Using fixture
def test_add_user(setup_database):
    db = setup_database
    db['users'].append({'name': 'Alice', 'age': 30})
    assert len(db['users']) == 1

# Fixture with decorator
@pytest.fixture
def sample_data():
    return {'name': 'Bob', 'age': 25}

def test_sample_data(sample_data):
    assert sample_data['name'] == 'Bob'
    assert sample_data['age'] == 25

# Fixture with scope
@pytest.fixture(scope='module')
def expensive_resource():
    """Resource that's expensive to create"""
    print("Creating expensive resource...")
    resource = [1, 2, 3, 4, 5]
    yield resource
    print("Destroying expensive resource...")

def test_expensive_resource(expensive_resource):
    assert len(expensive_resource) == 5

def test_expensive_resource2(expensive_resource):
    assert sum(expensive_resource) == 15

# Fixture with autouse
@pytest.fixture(autouse=True)
def timestamp_fixture():
    """Automatically run before each test"""
    print(f"Test started at {datetime.now()}")
    yield
    print("Test completed")
```

### 8.4 Test Classes
```python
import pytest

# Test class for Calculator
class TestCalculator:
    
    def test_addition(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    
    def test_subtraction(self):
        assert subtract(5, 3) == 2
        assert subtract(3, 5) == -2
    
    def test_multiplication(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
    
    def test_division(self):
        assert divide(10, 2) == 5
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

# Test class with setup/teardown
class TestDatabaseOperations:
    
    def setup_method(self):
        """Run before each test method"""
        print("Setting up test database")
        self.db = create_test_database()
    
    def teardown_method(self):
        """Run after each test method"""
        print("Tearing down test database")
        self.db.close()
    
    def test_insert_user(self):
        user_id = self.db.insert_user('Alice', 30)
        assert user_id is not None
    
    def test_query_users(self):
        self.db.insert_user('Bob', 25)
        users = self.db.get_all_users()
        assert len(users) == 1

# Test class with fixtures
class TestWithFixtures:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.calc = Calculator()
        yield
        del self.calc
    
    def test_add(self):
        assert self.calc.add(2, 3) == 5
    
    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
```

### 8.5 Parameterized Tests
```python
import pytest

# Basic parameterization
@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (0, 0),
    (-2, 4)
])
def test_square(input, expected):
    assert square(input) == expected

# Multiple parameters
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

# Using fixtures with parameters
@pytest.fixture(params=[1, 2, 3])
def numbers(request):
    return request.param

def test_numbers(numbers):
    assert numbers in [1, 2, 3]

# Parameterized with ids
@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (0, 0),
    (-2, 4)
], ids=["positive", "positive", "zero", "negative"])
def test_square_with_ids(input, expected):
    assert square(input) == expected

# Parameterized with fixture
@pytest.fixture
def get_data():
    return [
        (2, 4),
        (3, 9),
        (0, 0),
        (-2, 4)
    ]

@pytest.mark.parametrize("input, expected", get_data())
def test_square_from_fixture(input, expected):
    assert square(input) == expected
```

### 8.6 Mocking and Patching
```python
import pytest
from unittest.mock import patch, MagicMock

# Mocking external dependencies
class ExternalAPI:
    def get_user(self, user_id):
        # Simulate API call
        if user_id == 1:
            return {'id': 1, 'name': 'Alice', 'age': 30}
        else:
            raise ValueError("User not found")

def test_get_user():
    api = ExternalAPI()
    
    # Mock the API response
    with patch.object(ExternalAPI, 'get_user', return_value={'id': 1, 'name': 'Bob', 'age': 25}):
        result = api.get_user(1)
        assert result['name'] == 'Bob'
        assert result['age'] == 25

# Mocking with side effects
@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'data': 'test'}
    
    response = make_api_call('https://api.example.com/data')
    assert response['data'] == 'test'

# Mocking with side effects (different responses)
@patch('requests.get')
def test_api_call_with_side_effect(mock_get):
    def mock_response(url):
        if 'success' in url:
            return MagicMock(status_code=200, json=lambda: {'data': 'success'})
        else:
            return MagicMock(status_code=404, json=lambda: {'error': 'not found'})
    
    mock_get.side_effect = mock_response
    
    success_response = make_api_call('https://api.example.com/success')
    assert success_response['data'] == 'success'
    
    error_response = make_api_call('https://api.example.com/failure')
    assert error_response['error'] == 'not found'

# Patching built-in functions
@patch('builtins.open')
def test_file_operations(mock_open):
    mock_file = MagicMock()
    mock_file.read.return_value = 'test content'
    mock_open.return_value = mock_file
    
    content = read_file('test.txt')
    assert content == 'test content'
    mock_open.assert_called_once_with('test.txt', 'r')

# Patching class methods
class MyClass:
    def method(self):
        return 'original'
    
    def another_method(self):
        return self.method()

def test_patched_method():
    my_instance = MyClass()
    
    with patch.object(MyClass, 'method', return_value='mocked'):
        assert my_instance.another_method() == 'mocked'
```

### 8.7 Test Coverage
```python
# Example code to test
def calculate_grade(score):
    """Calculate letter grade based on score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test coverage examples
def test_calculate_grade():
    # Test all branches
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(75) == 'C'
    assert calculate_grade(65) == 'D'
    assert calculate_grade(55) == 'F'
    
    # Test edge cases
    assert calculate_grade(90) == 'A'
    assert calculate_grade(80) == 'B'
    assert calculate_grade(70) == 'C'
    assert calculate_grade(60) == 'D'
    assert calculate_grade(0) == 'F'

# Test coverage with pytest-cov
# Install: pip install pytest-cov
# Run: pytest --cov=module_name
# Generate HTML: pytest --cov=module_name --cov-report=html

# Example pytest.ini configuration
#[pytest]
cov_include = src/*
cov_exclude = tests/*,venv/*
cov_report = html

# Test coverage best practices
# - Aim for high coverage but focus on critical paths
# - Test edge cases and error conditions
# - Use mutation testing for advanced coverage analysis
# - Regularly check coverage reports
# - Don't sacrifice test quality for coverage percentage
```

### 8.8 Integration Tests
```python
import pytest
import requests
import time

# Integration test for a web application
@pytest.mark.integration
def test_full_workflow():
    """Test complete user workflow"""
    # Setup
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    }
    
    # Step 1: Create user
    response = requests.post('http://localhost:5000/api/users', json=user_data)
    assert response.status_code == 201
    user_id = response.json()['id']
    
    # Step 2: Login
    login_response = requests.post('http://localhost:5000/api/login', json={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert login_response.status_code == 200
    token = login_response.json()['token']
    
    # Step 3: Create post
    post_data = {
        'title': 'Test Post',
        'content': 'This is a test post.'
    }
    headers = {'Authorization': f'Bearer {token}'}
    post_response = requests.post('http://localhost:5000/api/posts', 
                                 json=post_data, headers=headers)
    assert post_response.status_code == 201
    post_id = post_response.json()['id']
    
    # Step 4: Get posts
    get_response = requests.get(f'http://localhost:5000/api/posts/{post_id}', 
                               headers=headers)
    assert get_response.status_code == 200
    assert get_response.json()['title'] == 'Test Post'
    
    # Cleanup
    delete_response = requests.delete(f'http://localhost:5000/api/posts/{post_id}', 
                                     headers=headers)
    assert delete_response.status_code == 204

# Database integration test
@pytest.mark.integration
def test_database_operations():
    """Test database operations with real database"""
    # Setup test database
    db = Database('test_db.sqlite')
    db.create_tables()
    
    # Test operations
    user_id = db.insert_user('Alice', 30)
    assert user_id is not None
    
    users = db.get_all_users()
    assert len(users) >= 1
    
    # Test query
    alice = db.get_user_by_name('Alice')
    assert alice is not None
    assert alice['age'] == 30
    
    # Cleanup
    db.delete_user(user_id)
    db.close()

# API integration test with test server
@pytest.fixture
def test_client():
    """Create test client for Flask app"""
    from app import create_app
    app = create_app(config_name='testing')
    with app.test_client() as client:
        yield client

def test_api_endpoints(test_client):
    """Test API endpoints using test client"""
    # Test GET endpoint
    response = test_client.get('/api/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'
    
    # Test POST endpoint
    data = {'name': 'Test', 'value': 123}
    response = test_client.post('/api/data', json=data)
    assert response.status_code == 201
    assert response.json['name'] == 'Test'
```

### 8.9 Test-Driven Development (TDD)
```python
# TDD example: Implementing a calculator

# Step 1: Write failing test
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Step 2: Run test (should fail)
# Step 3: Write minimal code to pass
try:
    def add(x, y):
        return x + y
except NameError:
    pass

# Step 4: Run test (should pass)
# Step 5: Refactor if needed

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

# Continue with TDD cycle...

def test_calculator_class():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 3) == 2
    assert calc.multiply(3, 4) == 12
    assert calc.divide(10, 2) == 5

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# TDD best practices
# - Write tests before implementation
# - Keep tests simple and focused
# - Run tests frequently
# - Refactor both code and tests
# - Use descriptive test names
# - Test edge cases and error conditions
```

### 8.10 pytest Plugins and Advanced Features
```python
# pytest.ini configuration
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# conftest.py for shared fixtures and hooks
import pytest
import json

def pytest_addoption(parser):
    parser.addoption(
        "--runslow",
        action="store_true",
        help="run slow tests"
    )

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: mark test as slow to run"
    )

def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)

def pytest_exception_interact(call, report):
    """Handle exceptions during test execution"""
    if report.failed:
        print(f"Test {report.nodeid} failed with exception: {call.excinfo.value}")

# Custom markers
import pytest

@pytest.mark.performance
def test_performance():
    """Test performance characteristics"""
    import time
    start = time.time()
    # Test code here
    end = time.time()
    assert end - start < 1.0  # Should complete in less than 1 second

@pytest.mark.security
def test_security():
    """Test security aspects"""
    # Security test code here
    assert is_secure() == True

# pytest-xdist for parallel testing
# Install: pip install pytest-xdist
# Run: pytest -n auto (use all cores)
# Run: pytest -n 4 (use 4 cores)

# pytest-cov for coverage
# Install: pip install pytest-cov
# Run: pytest --cov=module_name
# Run: pytest --cov=module_name --cov-report=html

# pytest-benchmark for performance testing
# Install: pip install pytest-benchmark
# Run: pytest --benchmark
```

### 8.11 Exercises

1. **Exercise 1**: Write unit tests for a function that calculates the factorial of a number, including tests for edge cases and error conditions.

2. **Exercise 2**: Create a test suite for a simple calculator class with addition, subtraction, multiplication, and division operations.

3. **Exercise 3**: Write integration tests for a REST API that includes creating, reading, updating, and deleting resources.

4. **Exercise 4**: Implement parameterized tests for a function that validates email addresses using various test cases.

5. **Exercise 5**: Create a test suite with fixtures that sets up and tears down a test database for each test.

### 8.12 Best Practices

- Write clear, descriptive test names
- Use fixtures for setup and teardown code
- Test one thing per test function
- Use appropriate assertions
- Mock external dependencies
- Test edge cases and error conditions
- Keep tests independent and isolated
- Use parameterization for similar test cases
- Maintain good test coverage
- Use continuous integration for automated testing

### 8.13 Common Pitfalls

- Testing implementation details instead of behavior
- Writing tests that are too complex
- Not testing error conditions
- Tests that depend on external state
- Slow test suites
- Tests that pass but don't actually test anything
- Not updating tests when code changes
- Over-mocking and losing integration coverage

### 8.14 Assessment Questions

1. What is the difference between a unit test and an integration test?
2. How do you use fixtures in pytest?
3. What is the purpose of mocking in tests?
4. How do you run tests in parallel using pytest?
5. What are some best practices for writing maintainable tests?