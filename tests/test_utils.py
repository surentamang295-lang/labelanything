"""Tests for utility functions."""

import os
import tempfile
from pathlib import Path

import pytest

from labelanything.utils import canRead


class TestCanRead:
    """Test cases for the canRead function."""
    
    def test_canRead_existing_file(self):
        """Test that canRead returns True for an existing readable file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("test content")
            temp_path = f.name
        
        try:
            assert canRead(temp_path) is True
        finally:
            os.unlink(temp_path)
    
    def test_canRead_nonexistent_file(self):
        """Test that canRead returns False for a non-existent file."""
        assert canRead("/path/to/nonexistent/file.txt") is False
    
    def test_canRead_directory(self):
        """Test that canRead returns False for a directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            assert canRead(temp_dir) is False
    
    def test_canRead_with_path_object(self):
        """Test that canRead works with Path objects."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("test content")
            temp_path = Path(f.name)
        
        try:
            assert canRead(temp_path) is True
        finally:
            os.unlink(temp_path)
    
    def test_canRead_empty_file(self):
        """Test that canRead returns True for an empty but readable file."""
        with tempfile.NamedTemporaryFile(delete=False) as f:
            temp_path = f.name
        
        try:
            assert canRead(temp_path) is True
        finally:
            os.unlink(temp_path)
    
    def test_canRead_invalid_input(self):
        """Test that canRead returns False for invalid input."""
        assert canRead(None) is False
        assert canRead(123) is False
        assert canRead([]) is False
    
    def test_canRead_unreadable_file(self):
        """Test that canRead returns False for a file without read permissions."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("test content")
            temp_path = f.name
        
        try:
            # Remove read permissions
            os.chmod(temp_path, 0o000)
            assert canRead(temp_path) is False
        finally:
            # Restore permissions to delete the file
            os.chmod(temp_path, 0o644)
            os.unlink(temp_path)
