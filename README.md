# labelanything

A simple data reading library that supports multiple file formats.

## Features

- Read text files (.txt)
- Read CSV files (.csv)
- Read JSON files (.json)
- Check if a file can be read before attempting to read it

## Usage

### Basic Usage

```python
from reader import DataReader

# Create a reader instance
reader = DataReader()

# Read a text file
text_content = reader.read('example.txt')
print(text_content)

# Read a CSV file (returns list of dictionaries)
csv_data = reader.read('example.csv')
for row in csv_data:
    print(row)

# Read a JSON file
json_data = reader.read('example.json')
print(json_data)

# Check if a file can be read
if reader.can_read('myfile.txt'):
    content = reader.read('myfile.txt')
```

### Convenience Function

```python
from reader import read_file

# Quick one-liner to read any supported file
content = read_file('example.json')
```

## Running Examples

Run the example script to see the data reader in action:

```bash
python example_usage.py
```

## Supported Formats

- `.txt` - Plain text files
- `.csv` - Comma-separated values
- `.json` - JSON files

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)