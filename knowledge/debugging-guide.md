# 🔍 Debugging Guide Knowledge Base

## Overview
This knowledge file contains debugging strategies, common errors, and troubleshooting techniques. Reference this when helping students debug their code.

---

## 🎯 Debugging Philosophy

### Systematic Approach
1. **Reproduce** the error consistently
2. **Isolate** the problem area
3. **Hypothesize** the cause
4. **Test** your hypothesis
5. **Fix** the root cause
6. **Verify** the fix works

### Key Principles
- Read error messages carefully
- Check the simplest things first
- Change one thing at a time
- Keep notes of what you've tried
- Take breaks when frustrated

---

## 🐛 Python Debugging

### Common Errors

#### NameError
```python
# Error
print(my_variable)  # NameError: name 'my_variable' is not defined

# Fix
my_variable = 10
print(my_variable)
```

#### TypeError
```python
# Error
result = "5" + 3  # TypeError: can only concatenate str to str

# Fix
result = int("5") + 3  # 8
# or
result = "5" + str(3)  # "53"
```

#### AttributeError
```python
# Error
my_list = [1, 2, 3]
my_list.append(4)
my_list.appned(5)  # AttributeError: 'list' object has no attribute 'appned'

# Fix - check spelling
my_list.append(5)
```

#### KeyError
```python
# Error
data = {"name": "John"}
print(data["age"])  # KeyError: 'age'

# Fix
print(data.get("age", "Not found"))  # "Not found"
# or
if "age" in data:
    print(data["age"])
```

#### IndexError
```python
# Error
items = [1, 2, 3]
print(items[5])  # IndexError: list index out of range

# Fix
if len(items) > 5:
    print(items[5])
# or
print(items[-1])  # Last item: 3
```

### Debugging Techniques

#### Print Debugging
```python
def calculate_total(items):
    print(f"Input: {items}")  # Debug
    total = sum(items)
    print(f"Total: {total}")  # Debug
    return total
```

#### Using pdb
```python
import pdb

def complex_function(data):
    pdb.set_trace()  # Debugger stops here
    result = process(data)
    return result

# Commands:
# n - next line
# s - step into function
# c - continue
# p variable - print variable
# l - list source code
# q - quit
```

#### Logging
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug(f"Processing: {data}")
    try:
        result = transform(data)
        logger.info(f"Success: {result}")
        return result
    except Exception as e:
        logger.error(f"Error: {e}")
        raise
```

#### Assertions
```python
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

def process_list(items):
    assert isinstance(items, list), "Expected list"
    assert len(items) > 0, "List cannot be empty"
    return sum(items)
```

---

## 📘 TypeScript Debugging

### Common Errors

#### Type Errors
```typescript
// Error
const name: string = 123;  // Type 'number' is not assignable to type 'string'

// Fix
const name: string = "123";
// or
const value: number = 123;
```

#### Null/Undefined Errors
```typescript
// Error
const element = document.getElementById("app");
element.innerHTML = "Hello";  // Object is possibly 'null'

// Fix
const element = document.getElementById("app");
if (element) {
  element.innerHTML = "Hello";
}
// or
element!.innerHTML = "Hello";  // Only if you're sure it exists
```

#### Property Does Not Exist
```typescript
// Error
interface User {
  name: string;
}
const user: User = { name: "John" };
console.log(user.age);  // Property 'age' does not exist on type 'User'

// Fix
interface User {
  name: string;
  age?: number;  // Make optional
}
```

#### Async/Await Errors
```typescript
// Error
async function fetchData() {
  const data = fetch("/api/data");  // Missing await
  return data.json();  // Error: data is Promise, not Response
}

// Fix
async function fetchData() {
  const response = await fetch("/api/data");
  return response.json();
}
```

### Debugging Techniques

#### Console Debugging
```typescript
console.log("Value:", value);
console.table([{ name: "John", age: 30 }]);
console.time("operation");
// ... code ...
console.timeEnd("operation");
```

#### Debugger Statement
```typescript
function complexLogic(data: any) {
  debugger;  // Browser/dev tools will pause here
  const result = process(data);
  return result;
}
```

#### Chrome DevTools
- Sources tab: Set breakpoints
- Console: Evaluate expressions
- Network: Check API calls
- Performance: Profile code

---

## 🔧 General Debugging Strategies

### Binary Search Debugging
```
Problem in large codebase?

1. Add print/log at MIDDLE of code
2. If problem occurs before middle → search first half
3. If problem occurs after middle → search second half
4. Repeat until isolated
```

### Rubber Duck Debugging
- Explain your code line by line
- To a colleague, pet, or rubber duck
- Often reveals the issue while explaining

### Git Bisect
```bash
# Find which commit introduced a bug
git bisect start
git bisect bad  # Current commit is broken
git bisect good abc123  # This commit worked

# Git will checkout commits for you to test
# Mark each as good or bad
git bisect good  # or git bisect bad

# When done
git bisect reset
```

### Check Recent Changes
```bash
# See recent commits
git log --oneline -10

# See what changed in last commit
git diff HEAD~1

# See changes in specific file
git log -p -- path/to/file.py
```

---

## ⚠️ Common Pitfalls

### Off-by-One Errors
```python
# Error
for i in range(len(items)):  # Should be range(len(items))
    if items[i] == target:
        return i

# Common mistake
for i in range(len(items) + 1):  # Out of bounds!
    print(items[i])
```

### Mutable Default Arguments
```python
# Error
def add_item(item, items=[]):
    items.append(item)
    return items

# Problem: list persists between calls
result1 = add_item(1)  # [1]
result2 = add_item(2)  # [1, 2] - not [2]!

# Fix
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Floating Point Comparison
```python
# Error
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False! (0.30000000000000004)

# Fix
import math
print(math.isclose(a, b))  # True
# or
print(abs(a - b) < 1e-9)  # True
```

### Race Conditions
```python
# Error in async code
async def increment_counter():
    global counter
    current = counter  # Read
    await asyncio.sleep(0.1)  # Other tasks might run
    counter = current + 1  # Write - might be stale!

# Fix with locks
import asyncio

lock = asyncio.Lock()

async def increment_counter():
    async with lock:
        global counter
        counter += 1
```

---

## 🛠️ Debugging Tools

### Python
- `pdb` - Built-in debugger
- `ipdb` - Enhanced pdb with IPython
- `pytest` - Testing framework with debugging
- `pylint` - Static analysis
- `mypy` - Type checking

### TypeScript
- Chrome DevTools - Browser debugging
- VS Code Debugger - Integrated debugging
- `ts-node` - Run TypeScript directly
- ESLint - Static analysis
- TypeScript Compiler - Type checking

### General
- `git` - Version control and history
- `grep`/`ripgrep` - Search code
- `strace`/`ltrace` - System call tracing
- Wireshark - Network debugging

---

## 📚 Quick Reference

### Python Error Types
- `SyntaxError` - Invalid syntax
- `NameError` - Undefined variable
- `TypeError` - Wrong type
- `ValueError` - Wrong value
- `KeyError` - Missing dictionary key
- `IndexError` - List index out of range
- `AttributeError` - Missing attribute
- `FileNotFoundError` - File doesn't exist
- `ImportError` - Module not found

### TypeScript Error Types
- Type mismatch
- Property not found
- Possibly null/undefined
- Not assignable
- Cannot find module
- Unexpected token

### Debugging Checklist
- [ ] Read error message completely
- [ ] Check line number in error
- [ ] Verify variable names/spelling
- [ ] Check data types
- [ ] Look for null/undefined
- [ ] Check array bounds
- [ ] Verify function arguments
- [ ] Test with simple input
- [ ] Add print statements
- [ ] Use debugger

---

**Knowledge Version**: 1.0  
**Last Updated**: March 2026