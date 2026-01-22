"""
Data Reader Module for LabelAnything

This module provides functionality to read various data formats.
"""

import json
import csv
import os
from typing import Union, List, Dict, Any


class DataReader:
    """A simple data reader that supports multiple file formats."""
    
    def __init__(self):
        """Initialize the DataReader."""
        self.supported_formats = ['.txt', '.csv', '.json']
    
    def read(self, filepath: str) -> Union[str, List, Dict]:
        """
        Read data from a file.
        
        Args:
            filepath: Path to the file to read
            
        Returns:
            The file contents in an appropriate format based on file type
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is not supported
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        
        if ext not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {ext}. Supported formats: {self.supported_formats}")
        
        if ext == '.txt':
            return self._read_txt(filepath)
        elif ext == '.csv':
            return self._read_csv(filepath)
        elif ext == '.json':
            return self._read_json(filepath)
    
    def _read_txt(self, filepath: str) -> str:
        """Read a text file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _read_csv(self, filepath: str) -> List[Dict[str, Any]]:
        """Read a CSV file and return as list of dictionaries."""
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _read_json(self, filepath: str) -> Union[Dict, List]:
        """Read a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def can_read(self, filepath: str) -> bool:
        """
        Check if a file can be read.
        
        Args:
            filepath: Path to the file to check
            
        Returns:
            True if the file exists and has a supported format, False otherwise
        """
        if not os.path.exists(filepath):
            return False
        
        _, ext = os.path.splitext(filepath)
        return ext.lower() in self.supported_formats


def read_file(filepath: str) -> Union[str, List, Dict]:
    """
    Convenience function to read a file.
    
    Args:
        filepath: Path to the file to read
        
    Returns:
        The file contents in an appropriate format based on file type
    """
    reader = DataReader()
    return reader.read(filepath)
