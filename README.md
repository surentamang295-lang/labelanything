# labelanything

A data labeling and annotation tool with utilities for file handling.

## Installation

```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Features

### `canRead` Function

Check if a file can be read. This function verifies:
- The file exists
- The file is readable (has read permissions)
- The path points to a file (not a directory)

#### Usage

```python
from labelanything import canRead

# Check if a file can be read
if canRead("data.txt"):
    print("File is readable")
else:
    print("File cannot be read")

# Also works with Path objects
from pathlib import Path
if canRead(Path("data.txt")):
    print("File is readable")
```

#### Examples

```python
from labelanything import canRead

# Returns True for existing readable files
canRead("existing_file.txt")  # True

# Returns False for non-existent files
canRead("nonexistent.txt")  # False

# Returns False for directories
canRead("/some/directory")  # False

# Returns False for files without read permissions
canRead("no_read_permission.txt")  # False
```

## Testing

Run tests with pytest:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=labelanything --cov-report=html
```

## Development

This project uses:
- Python 3.8+
- pytest for testing

## License

TBD