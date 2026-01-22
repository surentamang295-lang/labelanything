"""Utility functions for labelanything."""

import os
from pathlib import Path
from typing import Union


def canRead(file_path: Union[str, Path]) -> bool:
    """
    Check if a file can be read.
    
    This function verifies that:
    1. The file exists
    2. The file is readable (has read permissions)
    3. The path points to a file (not a directory)
    
    Args:
        file_path: Path to the file to check (string or Path object)
        
    Returns:
        bool: True if the file exists and can be read, False otherwise
        
    Examples:
        >>> canRead("data.txt")
        True
        >>> canRead("/path/to/nonexistent.txt")
        False
    """
    try:
        path = Path(file_path)
        
        # Check if path exists
        if not path.exists():
            return False
            
        # Check if it's a file (not a directory)
        if not path.is_file():
            return False
            
        # Check if file is readable
        if not os.access(path, os.R_OK):
            return False
            
        return True
        
    except (OSError, ValueError, TypeError):
        # Handle any unexpected errors (invalid paths, permission issues, etc.)
        return False
