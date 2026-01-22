"""
Unit tests for the DataReader module.
"""

import unittest
import os
import tempfile
import json
from reader import DataReader, read_file


class TestDataReader(unittest.TestCase):
    """Test cases for DataReader class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.reader = DataReader()
        self.test_dir = tempfile.mkdtemp()
        
        # Create test files
        self.txt_file = os.path.join(self.test_dir, 'test.txt')
        with open(self.txt_file, 'w') as f:
            f.write('Hello World')
        
        self.csv_file = os.path.join(self.test_dir, 'test.csv')
        with open(self.csv_file, 'w') as f:
            f.write('name,value\ntest,123\n')
        
        self.json_file = os.path.join(self.test_dir, 'test.json')
        with open(self.json_file, 'w') as f:
            json.dump({'key': 'value'}, f)
    
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_read_txt_file(self):
        """Test reading text file."""
        content = self.reader.read(self.txt_file)
        self.assertEqual(content, 'Hello World')
    
    def test_read_csv_file(self):
        """Test reading CSV file."""
        content = self.reader.read(self.csv_file)
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]['name'], 'test')
        self.assertEqual(content[0]['value'], '123')
    
    def test_read_json_file(self):
        """Test reading JSON file."""
        content = self.reader.read(self.json_file)
        self.assertEqual(content['key'], 'value')
    
    def test_read_nonexistent_file(self):
        """Test reading a file that doesn't exist."""
        with self.assertRaises(FileNotFoundError):
            self.reader.read('nonexistent.txt')
    
    def test_read_unsupported_format(self):
        """Test reading an unsupported file format."""
        unsupported_file = os.path.join(self.test_dir, 'test.pdf')
        with open(unsupported_file, 'w') as f:
            f.write('test')
        
        with self.assertRaises(ValueError):
            self.reader.read(unsupported_file)
    
    def test_can_read_existing_file(self):
        """Test can_read with existing supported file."""
        self.assertTrue(self.reader.can_read(self.txt_file))
    
    def test_can_read_nonexistent_file(self):
        """Test can_read with nonexistent file."""
        self.assertFalse(self.reader.can_read('nonexistent.txt'))
    
    def test_can_read_unsupported_format(self):
        """Test can_read with unsupported format."""
        unsupported_file = os.path.join(self.test_dir, 'test.pdf')
        with open(unsupported_file, 'w') as f:
            f.write('test')
        
        self.assertFalse(self.reader.can_read(unsupported_file))
    
    def test_convenience_function(self):
        """Test the read_file convenience function."""
        content = read_file(self.txt_file)
        self.assertEqual(content, 'Hello World')
    
    def test_supported_formats(self):
        """Test that supported formats are correctly listed."""
        expected_formats = ['.txt', '.csv', '.json']
        self.assertEqual(self.reader.supported_formats, expected_formats)


if __name__ == '__main__':
    unittest.main()
