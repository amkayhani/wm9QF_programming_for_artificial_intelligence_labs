#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script to remove checkmark symbols from a file."""

import sys
import codecs

def remove_checkmarks(filepath):
    """Remove all checkmark symbols from the specified file."""
    try:
        # Read the file with proper encoding
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # The checkmark character (U+2713)
        checkmark = '\u2713'
        
        # Count checkmarks before removal
        count = content.count(checkmark)
        print(f"Found {count} checkmark symbols (U+2713)")
        
        # Remove checkmarks
        new_content = content.replace(checkmark, '')
        
        # Write back to file
        with codecs.open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Successfully removed {count} checkmark symbols from {filepath}")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    filepath = r"c:\Users\kayhan_a\Downloads\wm9QF_programming_for_artificial_intelligence_labs\object_oriented_programming\object_oriented_programming.md"
    remove_checkmarks(filepath)
