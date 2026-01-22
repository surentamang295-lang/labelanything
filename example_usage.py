#!/usr/bin/env python3
"""
Example script demonstrating the data reading functionality.
"""

from reader import DataReader, read_file


def main():
    """Demonstrate reading different file formats."""
    reader = DataReader()
    
    print("=" * 50)
    print("DataReader Example - Testing File Reading")
    print("=" * 50)
    
    # Test reading text file
    print("\n1. Reading text file (example.txt):")
    print("-" * 50)
    txt_content = reader.read('example.txt')
    print(txt_content)
    
    # Test reading CSV file
    print("\n2. Reading CSV file (example.csv):")
    print("-" * 50)
    csv_content = reader.read('example.csv')
    for row in csv_content:
        print(f"  {row}")
    
    # Test reading JSON file
    print("\n3. Reading JSON file (example.json):")
    print("-" * 50)
    json_content = reader.read('example.json')
    print(f"  Count: {json_content['count']}")
    print(f"  Users:")
    for user in json_content['users']:
        print(f"    - {user['name']}, {user['age']}, {user['city']}")
    
    # Test can_read method
    print("\n4. Testing can_read method:")
    print("-" * 50)
    test_files = ['example.txt', 'example.csv', 'example.json', 'nonexistent.txt', 'file.pdf']
    for file in test_files:
        result = reader.can_read(file)
        print(f"  can_read('{file}'): {result}")
    
    # Test convenience function
    print("\n5. Using convenience function read_file:")
    print("-" * 50)
    content = read_file('example.txt')
    print(f"  First 50 chars: {content[:50]}...")
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")
    print("=" * 50)


if __name__ == '__main__':
    main()
