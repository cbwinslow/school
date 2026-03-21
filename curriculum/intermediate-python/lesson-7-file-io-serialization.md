# Lesson 7: File I/O and Serialization

## Lesson Overview
This lesson covers file input/output operations and data serialization in Python. Students will learn how to read and write various file formats, handle binary data, and serialize objects for storage and transmission.

## Learning Objectives
By the end of this lesson, students will be able to:
- Read and write text files using different encodings
- Handle binary file operations
- Work with CSV files for data analysis
- Use JSON for data serialization
- Work with XML data
- Use pickle for Python object serialization
- Handle file paths and directories
- Implement file compression
- Handle file permissions and errors
- Create robust file processing pipelines

## Topics Covered

### 7.1 Text File Operations
```python
# Reading text files
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())

# Writing text files
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Appending to files
with open('output.txt', 'a', encoding='utf-8') as file:
    file.write("This line was appended.\n")

# Reading with different encodings
with open('example.txt', 'r', encoding='latin-1') as file:
    content = file.read()

# Reading large files efficiently
with open('large_file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        process_line(line)  # Process line by line

# Writing with buffering
with open('output.txt', 'w', buffering=1, encoding='utf-8') as file:
    file.write("Buffered output\n")
```

### 7.2 Binary File Operations
```python
# Writing binary data
with open('data.bin', 'wb') as file:
    # Write integers
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        file.write(num.to_bytes(4, byteorder='big', signed=True))
    
    # Write floats
    floats = [1.1, 2.2, 3.3]
    for f in floats:
        file.write(f.to_bytes(8, byteorder='big', signed=True))

# Reading binary data
with open('data.bin', 'rb') as file:
    # Read integers
    numbers = []
    for _ in range(5):
        data = file.read(4)
        if data:
            numbers.append(int.from_bytes(data, byteorder='big', signed=True))
    
    # Read floats
    floats = []
    for _ in range(3):
        data = file.read(8)
        if data:
            floats.append(float.from_bytes(data, byteorder='big', signed=True))

# Working with bytes
with open('image.png', 'rb') as file:
    header = file.read(8)
    print(f"PNG header: {header}")

# Writing bytes directly
with open('bytes.bin', 'wb') as file:
    file.write(b'Hello, World!')
    file.write(b'\x00\x01\x02')  # Binary data
```
    binary_data = b'\x00\x01\x02\x03'
    file.write(binary_data)

# Reading binary data
with open('data.bin', 'rb') as file:
    binary_data = file.read()
    print(binary_data)

# Working with images
from PIL import Image

# Save image
img = Image.new('RGB', (100, 100), color = 'red')
img.save('red_square.png')

# Load image
img = Image.open('red_square.png')
img.show()
```

### 7.3 CSV Files
```python
import csv

# Reading CSV files
with open('data.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading with DictReader
with open('data.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])

# Writing CSV files
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])

# Writing with DictWriter
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 30, 'City': 'New York'})
```

### 7.4 JSON Serialization
```python
import json

# Python object to JSON string
data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'hiking'],
    'address': {
        'street': '123 Main St',
        'city': 'New York'
    }
}

json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string to Python object
parsed_data = json.loads(json_string)
print(parsed_data['name'])

# Writing JSON to file
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)

# Reading JSON from file
with open('data.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Custom JSON encoding
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {'name': self.name, 'age': self.age}

person = Person('Bob', 25)
json_string = json.dumps(person, default=lambda o: o.to_dict())
print(json_string)
```

### 7.5 XML Processing
```python
import xml.etree.ElementTree as ET

# Creating XML
data = ET.Element('data')
person = ET.SubElement(data, 'person')
name = ET.SubElement(person, 'name')
name.text = 'Alice'
age = ET.SubElement(person, 'age')
age.text = '30'

# Convert to string
xml_string = ET.tostring(data, encoding='unicode')
print(xml_string)

# Writing to file
with open('data.xml', 'w', encoding='utf-8') as file:
    file.write(xml_string)

# Parsing XML
with open('data.xml', 'r', encoding='utf-8') as file:
    tree = ET.parse(file)
    root = tree.getroot()
    
    for person in root.findall('person'):
        name = person.find('name').text
        age = person.find('age').text
        print(f'Name: {name}, Age: {age}')

# Using lxml for more advanced XML
from lxml import etree

tree = etree.parse('data.xml')
root = tree.getroot()

# XPath queries
names = root.xpath('//person/name/text()')
print(names)
```

### 7.6 Pickle Serialization
```python
import pickle

# Simple object serialization
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 30)

# Serialize to file
with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

# Deserialize from file
with open('person.pkl', 'rb') as file:
    loaded_person = pickle.load(file)
    print(loaded_person.name, loaded_person.age)

# Serialize to bytes
data = {'key': 'value', 'numbers': [1, 2, 3]}
pickled_data = pickle.dumps(data)
print(pickled_data)

# Deserialize from bytes
unpickled_data = pickle.loads(pickled_data)
print(unpickled_data)

# Note: pickle is not secure for untrusted data
```

### 7.7 File Paths and Directories
```python
import os
import pathlib

# Using os.path
file_path = 'data/example.txt'
print(f'Directory: {os.path.dirname(file_path)}')
print(f'Filename: {os.path.basename(file_path)}')
print(f'Extension: {os.path.splitext(file_path)[1]}')

# Using pathlib (modern approach)
path = pathlib.Path('data/example.txt')
print(f'Directory: {path.parent}')
print(f'Filename: {path.name}')
print(f'Extension: {path.suffix}')
print(f'Stem: {path.stem}')

# Creating directories
output_dir = pathlib.Path('output/data')
output_dir.mkdir(parents=True, exist_ok=True)

# Listing files
for file in pathlib.Path('.').glob('*.txt'):
    print(file)

# Recursive glob
for file in pathlib.Path('.').rglob('*.py'):
    print(file)

# Checking file properties
path = pathlib.Path('data/example.txt')
print(f'Exists: {path.exists()}')
print(f'Is file: {path.is_file()}')
print(f'Is directory: {path.is_dir()}')
print(f'Size: {path.stat().st_size} bytes')
```

### 7.8 File Compression
```python
import gzip
import zipfile

# Gzip compression
with open('data.txt', 'rb') as f_in:
    with gzip.open('data.txt.gz', 'wb') as f_out:
        f_out.writelines(f_in)

# Gzip decompression
with gzip.open('data.txt.gz', 'rb') as f_in:
    with open('data_decompressed.txt', 'wb') as f_out:
        f_out.writelines(f_in)

# Zip compression
with zipfile.ZipFile('archive.zip', 'w') as zipf:
    zipf.write('data.txt')
    zipf.write('example.txt')

# Zip decompression
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted')

# Creating zip with compression
with zipfile.ZipFile('archive_compressed.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('data.txt')
```

### 7.9 Error Handling and Best Practices
```python
# Robust file reading
def read_file_safely(filepath: str) -> str:
    """Read file content with comprehensive error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return ''
    except PermissionError:
        print(f"Error: Permission denied for '{filepath}'")
        return ''
    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{filepath}' with UTF-8")
        return ''
    except Exception as e:
        print(f"Error reading '{filepath}': {e}")
        return ''

# Writing with error handling
def write_file_safely(filepath: str, content: str) -> bool:
    """Write content to file with error handling."""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: Cannot write to '{filepath}' - permission denied")
        return False
    except OSError as e:
        print(f"Error writing to '{filepath}': {e}")
        return False
    except Exception as e:
        print(f"Unexpected error writing to '{filepath}': {e}")
        return False

# File processing pipeline
def process_csv_file(input_path: str, output_path: str) -> None:
    """Process CSV file: read, transform, and write."""
    try:
        # Read CSV
        with open(input_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            rows = list(reader)
            
        # Transform data
        transformed = []
        for row in rows:
            try:
                row['age'] = int(row['age'])
                row['name'] = row['name'].title()
                transformed.append(row)
            except (ValueError, KeyError) as e:
                print(f"Skipping row due to error: {e}")
                continue
        
        # Write transformed data
        with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(transformed)
            
        print(f"Successfully processed {len(transformed)} rows")
        
    except FileNotFoundError:
        print(f"Input file '{input_path}' not found")
    except Exception as e:
        print(f"Error processing file: {e}")
```

### 7.10 Exercises

1. **Exercise 1**: Write a function that reads a text file and counts the frequency of each word, ignoring case and punctuation.

2. **Exercise 2**: Create a program that reads a CSV file containing student grades and calculates the average grade for each student.

3. **Exercise 3**: Implement a function that serializes a complex Python object (with nested objects and lists) to JSON and then deserializes it back.

4. **Exercise 4**: Write a script that compresses multiple files into a single zip archive and then extracts them to a different directory.

5. **Exercise 5**: Create a program that reads an XML file, modifies some elements, and writes the modified XML back to a new file.

### 7.11 Real-World Applications

- Data analysis pipelines that read CSV/JSON files
- Configuration management using JSON/YAML files
- Log file processing and analysis
- Data import/export between different systems
- File backup and archival systems
- Content management systems
- Data migration tools
- API response handling and storage

### 7.12 Best Practices

- Always use context managers (`with` statements) for file operations
- Handle different encodings appropriately
- Use pathlib for modern, object-oriented file path handling
- Implement comprehensive error handling
- Validate file formats before processing
- Use appropriate file modes (text vs binary)
- Consider memory usage for large files
- Use compression for large datasets
- Secure file operations with proper permissions
- Document file format expectations