# Lesson 7: File I/O and Serialization

## Overview
This lesson covers file input/output operations and data serialization techniques, essential for working with persistent data, configuration files, and data exchange formats.

## Learning Objectives
By the end of this lesson, students will be able to:
- Read from and write to text files
- Work with binary files
- Handle different file encodings
- Use JSON for data serialization
- Work with CSV files
- Use pickle for Python object serialization
- Handle file paths and directories
- Implement file compression
- Work with configuration files
- Handle file errors and exceptions

## Topics

### 7.1 Basic File Operations

#### Reading Text Files
```python
def read_text_file(file_path: str) -> str:
    """Read entire text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Usage
content = read_text_file('example.txt')
print(content)

# Reading line by line
def read_lines(file_path: str) -> list[str]:
    """Read file line by line."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Reading with iteration
def process_large_file(file_path: str) -> None:
    """Process large file line by line."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            process_line(line)

# Reading with different encodings
def read_with_encoding(file_path: str, encoding: str) -> str:
    """Read file with specified encoding."""
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()
```

#### Writing Text Files
```python
def write_text_file(file_path: str, content: str) -> None:
    """Write text to file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Usage
write_text_file('output.txt', 'Hello, World!')

# Appending to file
def append_to_file(file_path: str, content: str) -> None:
    """Append text to existing file."""
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

# Writing multiple lines
def write_lines(file_path: str, lines: list[str]) -> None:
    """Write list of lines to file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
```

#### Binary File Operations
```python
def read_binary_file(file_path: str) -> bytes:
    """Read binary file."""
    with open(file_path, 'rb') as file:
        return file.read()

# Usage
binary_data = read_binary_file('image.png')

# Writing binary files
def write_binary_file(file_path: str, data: bytes) -> None:
    """Write binary data to file."""
    with open(file_path, 'rb') as file:
        file.write(data)

# Copying binary files
def copy_binary_file(src: str, dest: str) -> None:
    """Copy binary file."""
    with open(src, 'rb') as src_file, \
         open(dest, 'wb') as dest_file:
        dest_file.write(src_file.read())
```

### 7.2 JSON Serialization

#### Basic JSON Operations
```python
import json

# Python object to JSON string
def to_json_string(data: Any) -> str:
    """Convert Python object to JSON string."""
    return json.dumps(data, indent=2)

# JSON string to Python object
def from_json_string(json_str: str) -> Any:
    """Convert JSON string to Python object."""
    return json.loads(json_str)

# Writing JSON to file
def write_json_file(file_path: str, data: Any) -> None:
    """Write Python object to JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

# Reading JSON from file
def read_json_file(file_path: str) -> Any:
    """Read JSON file and convert to Python object."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Usage
data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'hiking'],
    'address': {
        'street': '123 Main St',
        'city': 'Anytown'
    }
}

json_str = to_json_string(data)
write_json_file('data.json', data)
loaded_data = read_json_file('data.json')
```

#### Custom JSON Encoding
```python
import json
from datetime import datetime
from typing import Any

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for complex types."""
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return super().default(obj)

# Usage
data = {
    'created_at': datetime.now(),
    'user': User('Alice', 30)  # Assume User class exists
}

json_str = json.dumps(data, cls=CustomJSONEncoder, indent=2)

# Custom decoding
def custom_decoder(dct: dict) -> Any:
    if 'created_at' in dct:
        dct['created_at'] = datetime.fromisoformat(dct['created_at'])
    return dct

json_str = '...'
loaded_data = json.loads(json_str, object_hook=custom_decoder)
```

### 7.3 CSV File Operations

#### Reading CSV Files
```python
import csv
from typing import List, Dict, Any

# Read CSV as list of lists
def read_csv_as_lists(file_path: str) -> List[List[str]]:
    """Read CSV file as list of rows (each row is a list of values)."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

# Read CSV as list of dictionaries
def read_csv_as_dicts(file_path: str) -> List[Dict[str, Any]]:
    """Read CSV file as list of dictionaries (header row as keys)."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Reading with different delimiters
def read_csv_with_delimiter(
    file_path: str, 
    delimiter: str = ','
) -> List[Dict[str, Any]]:
    """Read CSV with custom delimiter."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return list(reader)

# Usage
rows = read_csv_as_lists('data.csv')
headers = rows[0] if rows else []
data = rows[1:] if len(rows) > 1 else []

# Or using DictReader
data_dicts = read_csv_as_dicts('data.csv')
```

#### Writing CSV Files
```python
# Write CSV from list of lists
def write_csv_from_lists(
    file_path: str, 
    data: List[List[Any]], 
    headers: List[str] = None
) -> None:
    """Write CSV data from list of lists."""
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)

# Write CSV from list of dictionaries
def write_csv_from_dicts(
    file_path: str, 
    data: List[Dict[str, Any]], 
    headers: List[str] = None
) -> None:
    """Write CSV data from list of dictionaries."""
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        if headers is None:
            headers = data[0].keys() if data else []
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# Usage
data = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

write_csv_from_dicts('output.csv', data)
```

### 7.4 Pickle Serialization

#### Basic Pickle Operations
```python
import pickle
from typing import Any

# Serialize to bytes
def to_pickle_bytes(data: Any) -> bytes:
    """Convert Python object to pickle bytes."""
    return pickle.dumps(data)

# Deserialize from bytes
def from_pickle_bytes(data: bytes) -> Any:
    """Convert pickle bytes to Python object."""
    return pickle.loads(data)

# Write pickle to file
def write_pickle_file(file_path: str, data: Any) -> None:
    """Write Python object to pickle file."""
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

# Read pickle from file
def read_pickle_file(file_path: str) -> Any:
    """Read pickle file and convert to Python object."""
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Usage
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        return f'Person(name={self.name!r}, age={self.age})'

person = Person('Alice', 30)
person_data = {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'hiking']}

pickle_bytes = to_pickle_bytes(person)
write_pickle_file('person.pkl', person)
loaded_person = read_pickle_file('person.pkl')
```

#### Advanced Pickle Features
```python
# Custom pickling
def custom_pickle():
    """Example of custom pickling behavior."""
    class CustomObject:
        def __init__(self, value: int):
            self.value = value
            self._secret = 'hidden'
        
        def __getstate__(self) -> dict:
            """Return state to be pickled."""
            state = self.__dict__.copy()
            # Don't pickle secret attribute
            state.pop('_secret', None)
            return state
        
        def __setstate__(self, state: dict) -> None:
            """Restore state from pickle."""
            self.__dict__.update(state)
            # Set default value for secret
            self._secret = 'default'
    
    obj = CustomObject(42)
    pickle_bytes = pickle.dumps(obj)
    loaded_obj = pickle.loads(pickle_bytes)
    print(loaded_obj.value)  # 42
    # loaded_obj._secret exists but was set to 'default'
```

### 7.5 File Paths and Directories

#### Path Operations
```python
import os
from pathlib import Path
from typing import List

# Using pathlib (modern approach)

def get_file_info(file_path: str) -> dict:
    """Get information about a file."""
    path = Path(file_path)
    return {
        'exists': path.exists(),
        'is_file': path.is_file(),
        'is_dir': path.is_dir(),
        'size': path.stat().st_size if path.exists() else None,
        'created': path.stat().st_ctime if path.exists() else None,
        'modified': path.stat().st_mtime if path.exists() else None,
        'suffix': path.suffix,
        'stem': path.stem,
        'parent': str(path.parent),
        'name': path.name
    }

# Directory operations
def list_directory(dir_path: str) -> List[dict]:
    """List contents of a directory."""
    path = Path(dir_path)
    if not path.exists():
        return []
    
    contents = []
    for item in path.iterdir():
        contents.append({
            'name': item.name,
            'is_file': item.is_file(),
            'is_dir': item.is_dir(),
            'size': item.stat().st_size if item.is_file() else None,
            'modified': item.stat().st_mtime
        })
    return contents

# Creating directories
def create_directory(dir_path: str, parents: bool = False) -> None:
    """Create directory (and parents if needed)."""
    path = Path(dir_path)
    path.mkdir(parents=parents, exist_ok=True)

# File pattern matching
def find_files(
    dir_path: str, 
    pattern: str = '*.txt'
) -> List[str]:
    """Find files matching pattern in directory."""
    path = Path(dir_path)
    return [str(p) for p in path.glob(pattern)]

# Recursive search
def find_files_recursive(
    dir_path: str, 
    pattern: str = '*.py'
) -> List[str]:
    """Find files matching pattern recursively."""
    path = Path(dir_path)
    return [str(p) for p in path.rglob(pattern)]
```

#### File Operations with Pathlib
```python
# Reading and writing with pathlib
def read_text_pathlib(file_path: str) -> str:
    """Read text file using pathlib."""
    path = Path(file_path)
    return path.read_text(encoding='utf-8')


def write_text_pathlib(file_path: str, content: str) -> None:
    """Write text file using pathlib."""
    path = Path(file_path)
    path.write_text(content, encoding='utf-8')

# Binary operations
def read_binary_pathlib(file_path: str) -> bytes:
    """Read binary file using pathlib."""
    path = Path(file_path)
    return path.read_bytes()


def write_binary_pathlib(file_path: str, data: bytes) -> None:
    """Write binary file using pathlib."""
    path = Path(file_path)
    path.write_bytes(data)
```

### 7.6 File Compression

#### Working with Compressed Files
```python
import gzip
import zipfile
import shutil
from typing import Any

# Gzip compression
def compress_gzip(file_path: str) -> str:
    """Compress file using gzip."""
    compressed_path = f'{file_path}.gz'
    with open(file_path, 'rb') as f_in, \
         gzip.open(compressed_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    return compressed_path

# Gzip decompression
def decompress_gzip(compressed_path: str) -> str:
    """Decompress gzip file."""
    decompressed_path = compressed_path.replace('.gz', '')
    with gzip.open(compressed_path, 'rb') as f_in, \
         open(decompressed_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    return decompressed_path

# Zip archive creation
def create_zip(
    zip_path: str, 
    files: List[str], 
    base_dir: str = None
) -> None:
    """Create zip archive from files."""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            if base_dir:
                arcname = os.path.relpath(file, base_dir)
            else:
                arcname = os.path.basename(file)
            zipf.write(file, arcname)

# Zip archive extraction
def extract_zip(zip_path: str, extract_dir: str) -> None:
    """Extract zip archive."""
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_dir)

# Reading zip contents
def read_zip_file(zip_path: str, file_name: str) -> Any:
    """Read specific file from zip archive."""
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        with zipf.open(file_name) as file:
            return file.read()
```

### 7.7 Configuration Files

#### INI Configuration Files
```python
import configparser
from typing import Dict, Any

# Reading INI files
def read_ini_file(file_path: str) -> configparser.ConfigParser:
    """Read INI configuration file."""
    config = configparser.ConfigParser()
    config.read(file_path, encoding='utf-8')
    return config

# Writing INI files
def write_ini_file(
    file_path: str, 
    config: configparser.ConfigParser
) -> None:
    """Write INI configuration to file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        config.write(file)

# Usage
config = configparser.ConfigParser()
config['DEFAULT'] = {'host': 'localhost', 'port': '3306'}
config['database'] = {'user': 'admin', 'password': 'secret'}

write_ini_file('config.ini', config)
loaded_config = read_ini_file('config.ini')
```

#### YAML Configuration Files
```python
import yaml
from typing import Any

# Reading YAML files
def read_yaml_file(file_path: str) -> Any:
    """Read YAML configuration file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Writing YAML files
def write_yaml_file(file_path: str, data: Any) -> None:
    """Write data to YAML file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.safe_dump(data, file, default_flow_style=False)

# Usage
config = {
    'database': {
        'host': 'localhost',
        'port': 3306,
        'user': 'admin',
        'password': 'secret'
    },
    'features': {
        'debug': True,
        'logging': {
            'level': 'INFO',
            'file': 'app.log'
        }
    }
}

write_yaml_file('config.yaml', config)
loaded_config = read_yaml_file('config.yaml')
```

### 7.8 Error Handling and Best Practices

#### File Operation Error Handling
```python
from typing import Optional
import logging

logger = logging.getLogger(__name__)

def safe_read_file(
    file_path: str, 
    encoding: str = 'utf-8'
) -> Optional[str]:
    """Read file with comprehensive error handling."""
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except PermissionError:
        logger.error(f"Permission denied: {file_path}")
        return None
    except UnicodeDecodeError:
        logger.error(f"Encoding error in file: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None


def safe_write_file(
    file_path: str, 
    content: str, 
    encoding: str = 'utf-8'
) -> bool:
    """Write file with error handling."""
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            file.write(content)
        return True
    except PermissionError:
        logger.error(f"Permission denied: {file_path}")
        return False
    except OSError as e:
        logger.error(f"OS error writing file {file_path}: {e}")
        return False
    except Exception as e:
        logger.error(f"Error writing file {file_path}: {e}")
        return False
```

#### Context Manager for File Operations
```python
def file_operation_context(
    file_path: str, 
    mode: str = 'r', 
    encoding: str = 'utf-8'
):
    """Context manager for file operations with error handling."""
    class FileOperation:
        def __init__(self):
            self.file = None
        
        def __enter__(self):
            try:
                self.file = open(file_path, mode, encoding=encoding)
                return self.file
            except Exception as e:
                raise RuntimeError(f"Failed to open file: {e}")
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                try:
                    self.file.close()
                except Exception as e:
                    logger.error(f"Error closing file: {e}")
            
            # Don't suppress exceptions
            return False
    
    return FileOperation()

# Usage
with file_operation_context('example.txt', 'w') as file:
    file.write('Hello, World!')
```

## Exercises

### Exercise 7.1: Basic File I/O
Create functions to read and write text files with proper error handling.

### Exercise 7.2: JSON Serialization
Implement a system to save and load Python objects using JSON.

### Exercise 7.3: CSV Processing
Write functions to read and write CSV files for data analysis.

### Exercise 7.4: Configuration Management
Create a configuration system that supports multiple file formats (INI, JSON, YAML).

### Exercise 7.5: File Compression
Implement functions to compress and decompress files using gzip and zip.

### Exercise 7.6: File System Operations
Create a utility module for common file system operations with error handling.

## Assessment Questions

1. What is the difference between text and binary file modes?
2. How does JSON serialization handle complex Python objects?
3. What are the advantages of using pathlib over os.path?
4. How do you handle file encoding issues?
5. What are the security considerations when working with file I/O?

## Real-World Applications
- Data persistence and storage
- Configuration management
- Data exchange between systems
- Log file processing
- File backup and compression
- Data analysis and reporting