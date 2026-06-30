<!--
module_id: exception_handling_and_files
author: Amir Kayhani
email: amir.kayhani@warwick.ac.uk
version: 1.0.0
current_version_description: Initial version introducing exception handling and file operations in Python.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Exception Handling and Files

comment: Learn how to handle exceptions and work with files in Python.

long_description: This module introduces learners to exception handling and file operations in Python. These are essential skills for building robust programs and working with external data.

estimated_time_in_minutes: 40

@pre_reqs
Learners should be familiar with [basic Python syntax](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1) and [loops and conditionals](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1).
@end

@learning_objectives

- Handle exceptions using `try`, `except`, and `finally`.
- Read from and write to files in Python.

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_loops
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

- python_basics_exercise
- working_with_files

@end

@depends_on_knowledge_available_in

- python_basics_variables_functions_methods
- python_basics_loops_conditionals

@end

@version_history

Previous versions: 

- None (initial version)
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Python Basics: Exception Handling and Files

@overview

In this module, you will learn how to handle exceptions and work with files in Python. Exception handling ensures your programs can gracefully handle errors, while file operations allow you to read, write, and manage external data. By the end of this module, you will be able to confidently manage file operations and handle common errors that may arise during execution.
 

## Lesson Preparation

@lesson_prep_python_pyodide

## Introduction

In Python, exception handling and file operations are essential skills for building robust programs. Exception handling ensures your program can gracefully handle errors, while file operations allow you to interact with external data. In this module, you'll learn how to:

1. Handle exceptions using `try`, `except`, and `finally`.
2. Open, read, write, and append to files in Python.

---

## Exception Handling in Python

Errors can occur during program execution, particularly in data science and AI applications where we deal with large datasets, complex computations, and external dependencies. Python provides a way to handle these errors gracefully using `try`, `except`, and `finally`. Exception handling ensures that your program can recover from unexpected situations without crashing.

### Common Python Exceptions

1. **ValueError**: Raised when an operation or function receives an argument with the right type but inappropriate value
2. **FileNotFoundError**: Raised when trying to access a file that doesn't exist
3. **TypeError**: Raised when an operation or function is applied to an object of inappropriate type
4. **ZeroDivisionError**: Raised when dividing by zero
5. **IndexError**: Raised when trying to access an index that is out of range

Without exception handling, your program will terminate immediately when an error occurs. For example:

```python
# This will raise an error and stop execution
# Similar to trying to access a missing feature in a dataset
missing_value = None
result = missing_value + 10  # TypeError
print("This will not be printed.")
```
@Pyodide.eval

In the example above, dividing by zero raises a `ZeroDivisionError`, which causes the program to terminate. This is problematic in real-world applications, such as AI systems, where a single error could disrupt the entire workflow. For instance, if an AI model encounters a missing value during training, the program should handle the error gracefully instead of crashing.

Using exception handling, you can gracefully handle such errors:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
print("This will be printed.")
```
@Pyodide.eval

Here, the `try` block contains the code that might raise an exception. If an exception occurs, the `except` block handles it. This ensures that the program continues execution. For example, in a data preprocessing pipeline, you might encounter missing or invalid data. Instead of stopping the entire pipeline, you can log the error and proceed with the next data point.

---

### Example: Handling Multiple Exceptions

Here's an example of handling different types of exceptions:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
```
@Pyodide.eval

In this example, the `try` block attempts to divide a number by the user-provided input. If the input is not a number, a `ValueError` is raised. If the user enters zero, a `ZeroDivisionError` is raised. The `finally` block ensures that the message "Execution completed" is printed regardless of whether an exception occurred. This is particularly useful in AI workflows where you need to ensure that resources (e.g., file handles, database connections) are released properly even if an error occurs.

**Quiz:**
What will the following code output if the user enters "0"?

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("Execution completed.")
```

[( )] Result: 0.0  
[( )] Invalid input! Please enter a number.  
[(X)] You cannot divide by zero! Execution completed.  
[( )] An unexpected error occurred.  

**Explanation:**
The user enters "0", which raises a `ZeroDivisionError`. The `except ZeroDivisionError` block handles the error, and the `finally` block ensures that "Execution completed." is printed.

---

### Raising Exceptions

You can raise exceptions intentionally using the `raise` keyword. This is useful for validating input or enforcing constraints:

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Your age is {age}.")

try:
    check_age(-5)
except ValueError as e:
    print(e)
```
@Pyodide.eval

In this example, the `check_age` function raises a `ValueError` if the age is negative. This is useful in AI applications where input validation is critical. For example, when deploying a machine learning model as a web service, you might validate user inputs (e.g., ensuring numerical inputs for a regression model) and raise exceptions for invalid data.

**Quiz:**
What will happen if the following code is executed?

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age > 150:
        raise ValueError("Age is unrealistically high!")
    else:
        print("Age is valid.")

try:
    validate_age(200)
except ValueError as e:
    print(e)
```

[( )] Age is valid.  
[(X)] Age is unrealistically high!  
[( )] Age cannot be negative!  
[( )] An unexpected error occurred.  

**Explanation:**
The `validate_age` function raises a `ValueError` if the age is greater than 150. The `except` block catches the exception and prints the error message.

---

## File Handling in Python

Python provides built-in functions to work with files. File handling allows you to read, write, and manage external data efficiently.

### Reading Files

Reading files is a fundamental operation in Python, allowing you to access and process external data. Python provides several methods to read files efficiently, depending on the use case.

#### Reading the Entire File

You can read the entire content of a file at once using the `read()` method. This is suitable for small files:

```python
# Reading the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
@Pyodide.eval

#### Reading Line by Line

For larger files, it is more memory-efficient to read the file line by line using a loop:

```python
# Reading the file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```
@Pyodide.eval

#### Reading Specific Number of Characters

You can read a specific number of characters using the `read(size)` method:

```python
# Reading the first 10 characters
with open("example.txt", "r") as file:
    content = file.read(10)
    print(content)
```
@Pyodide.eval

#### Applications in Data Science and AI
- Reading datasets stored in text files (e.g., CSV, JSON)
- Preprocessing text data for natural language processing (NLP)
- Loading configuration files for machine learning experiments

---

### Writing to Files

You can write to a file using the `write()` method. If the file already exists, it will be overwritten:

```python
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")
```
@Pyodide.eval

In this example, the file is opened in write mode (`"w"`), and the `write` method is used to write data to the file. This is useful in AI applications where you need to save model outputs, logs, or results to a file.

To append to a file, use the `"a"` mode:

```python
with open("example.txt", "a") as file:
    file.write("Appending this line.\n")
```
@Pyodide.eval

Appending to a file is useful when you want to add new data without overwriting the existing content. For example, you might append new log entries to a log file during model training.

---

### Writing and Reading in Append Mode (`a`)

The `a` mode is used to open a file for appending. Data is added to the end of the file without modifying its existing contents. If the file does not exist, it is created.

#### Example: Appending to a File

```python
# Appending data to a file
with open("example.txt", "a") as file:
    file.write("This is appended content.\n")
```
@Pyodide.eval

In this example, the `write` method adds new content to the end of the file. If the file does not exist, it will be created.

#### Example: Reading After Appending

To verify the appended content, you can open the file in read mode:

```python
# Reading the file after appending
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
@Pyodide.eval

---

### Comparison of File Modes

The table below summarizes the different file modes discussed:

| Mode  | Description                                                                 | File Created if Not Exists | Overwrites Existing Content | Allows Reading | Allows Writing |
|-------|-----------------------------------------------------------------------------|----------------------------|----------------------------|----------------|----------------|
| `r`   | Read-only mode. File must exist.                                           | No                         | No                         | Yes            | No             |
| `w`   | Write mode. Overwrites the file if it exists.                              | Yes                        | Yes                        | No             | Yes            |
| `a`   | Append mode. Adds content to the end of the file.                          | Yes                        | No                         | No             | Yes            |
| `r+`  | Read and write mode. File must exist.                                      | No                         | No                         | Yes            | Yes            |
| `w+`  | Write and read mode. Overwrites the file if it exists.                     | Yes                        | Yes                        | Yes            | Yes            |
| `a+`  | Append and read mode. Adds content to the end of the file.                 | Yes                        | No                         | Yes            | Yes            |
| `rb`  | Read-only mode for binary files. File must exist.                          | No                         | No                         | Yes            | No             |
| `wb`  | Write mode for binary files. Overwrites the file if it exists.             | Yes                        | Yes                        | No             | Yes            |
| `rb+` | Read and write mode for binary files. File must exist.                     | No                         | No                         | Yes            | Yes            |
| `wb+` | Write and read mode for binary files. Overwrites the file if it exists.    | Yes                        | Yes                        | Yes            | Yes            |

---

### Text Files vs Binary Files

Files in Python can be broadly categorized into text files and binary files. Each type has its own characteristics, advantages, disadvantages, and applications, especially in data science and AI.

#### Text Files

Text files store data in a human-readable format, using characters encoded in a specific encoding (e.g., UTF-8). They are commonly used for storing structured data, logs, and configuration files.

**Applications in Data Science and AI:**
- Storing datasets in CSV, JSON, or TXT formats
- Logging model training progress
- Saving configuration files for experiments

**Advantages:**
1. Human-readable and easy to debug
2. Can be opened and edited with any text editor
3. Portable across different systems

**Disadvantages:**
1. Larger file size compared to binary files
2. Slower read/write operations for large datasets
3. Limited to storing text-based data

**Example:**

```python
# Writing to a text file
with open("example.txt", "w") as file:
    file.write("This is a text file.\n")
```
@Pyodide.eval

```python
# Reading from a text file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
@Pyodide.eval

---

#### Binary Files

Binary files store data in a non-human-readable format, using raw bytes. They are commonly used for storing complex data structures, images, and serialized objects.

**Applications in Data Science and AI:**
- Storing trained machine learning models (e.g., `.pkl`, `.h5`)
- Saving image, audio, or video data
- Efficient storage of large numerical datasets (e.g., NumPy arrays)

**Advantages:**
1. More space-efficient than text files
2. Faster read/write operations
3. Suitable for storing complex data structures

**Disadvantages:**
1. Not human-readable, making debugging harder
2. Requires specific software or libraries to interpret
3. May not be portable across different systems due to encoding differences

**Example:**

```python
# Writing to a binary file
with open("example.bin", "wb") as file:
    file.write(b"Binary data")
```
@Pyodide.eval

```python
# Reading from a binary file
with open("example.bin", "rb") as file:
    data = file.read()
    print(data)
```
@Pyodide.eval

---

### Comparison of Text and Binary Files

| Feature                | Text Files                              | Binary Files                            |
|------------------------|-----------------------------------------|-----------------------------------------|
| **Format**             | Human-readable characters               | Raw bytes                               |
| **Readability**        | Can be opened and read by humans        | Requires specific software to interpret |
| **File Size**          | Larger due to encoding overhead         | Smaller and more space-efficient        |
| **Speed**              | Slower read/write operations            | Faster read/write operations            |
| **Applications**       | Logs, CSV, JSON, configuration files    | Models, images, audio, numerical data   |
| **Portability**        | Highly portable across systems          | May face compatibility issues           |
| **Debugging**          | Easy to debug                           | Harder to debug                         |

---

### Working with Binary Files

Binary files store data in a non-text format. You can read and write binary files using the `"rb"` and `"wb"` modes:

```python
# Writing binary data
with open("example.bin", "wb") as file:
    file.write(b"Binary data")
```
@Pyodide.eval

Try running the code above first to create the binary file, then run the code below to read it:

```python
# Reading binary data
with open("example.bin", "rb") as file:
    data = file.read()
    print(data)
```
@Pyodide.eval

Binary files are commonly used in AI applications to store model weights, serialized objects, or image data. For example, you might save a trained neural network model to a binary file and load it later for inference.

**Quiz:**
Which of the following is NOT true about binary files?

[( )] Binary files are more space-efficient than text files.  
[( )] Binary files are not human-readable.  
[(X)] Binary files are always portable across different systems.  
[( )] Binary files are faster to read and write than text files.  

**Explanation:**
Binary files may not be portable across different systems due to differences in encoding or serialization formats.

---

### Advanced File Operations

The `"a+"` mode is used to open a file for both appending and reading. Data is added to the end of the file without modifying its existing contents. If the file does not exist, it is created.

```python
# Example: Appending and reading a file
with open("example.txt", "a+") as file:
    file.write("Appending new content.\n")
    file.seek(0)  # Move the cursor to the beginning of the file
    content = file.read()
    print("File Content:", content)
```
@Pyodide.eval

**Quiz:**
What will the following code do?

```python
with open("example.txt", "a+") as file:
    file.write("Appending new content.\n")
    file.seek(0)
    content = file.read()
    print(content)
```

[( )] Overwrite the file and print the new content.  
[( )] Raise a `FileNotFoundError` if the file does not exist.  
[(X)] Append new content to the file and print all its contents.  
[( )] Only print the newly appended content.  

**Explanation:**
The `a+` mode appends new content to the file and allows reading from the beginning of the file. The `seek(0)` moves the cursor to the start of the file, so all contents are printed.

---

## Combining File Handling and Exception Handling

You can combine file handling and exception handling to create robust programs that handle errors gracefully.

### Example: Reading a File with Error Handling

```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operation completed.")
```
@Pyodide.eval

In this example, the `try` block attempts to read a file. If the file does not exist, a `FileNotFoundError` is raised. If the program does not have permission to access the file, a `PermissionError` is raised. The `finally` block ensures that the message "File operation completed" is printed regardless of whether an exception occurred. This is useful in AI workflows where you need to ensure that resources are released properly even if an error occurs.

---

### Example: File Search Utility

Write a program that searches for a specific word in a file and handles errors gracefully:

```python
def search_word_in_file(file_name, word):
    try:
        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                if word in line:
                    print(f"Found '{word}' on line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

search_word_in_file("example.txt", "Python")
```
@Pyodide.eval

This program demonstrates how to search for a specific word in a file while handling potential errors, such as missing files. This is useful in AI applications, such as searching for specific keywords in log files generated during model training or deployment.

**Your Turn**: Extend the program to count the total occurrences of the word in the file.

---

## Advanced Activities

### Activity 1: Error Logging System

Write a program that logs all errors to a separate log file:

```python
import logging

# Configure logging
logging.basicConfig(filename="error.log", level=logging.ERROR)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError: {e}")
        print("Cannot divide by zero!")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

divide(10, 0)
divide(10, "five")
```
@Pyodide.eval

Logging is essential in AI systems to track errors and debug issues. For example, during model training, you can log errors related to data loading, model convergence, or hardware failures. These logs can be analyzed later to improve the system's reliability.

**Your Turn**: Modify the program to log additional details, such as timestamps and function names.

---

### Activity 2: File Compression Utility

Write a program that compresses a text file using the `gzip` module:

```python
import gzip

# Compressing a file
with open("example.txt", "rb") as src:
    with gzip.open("example.txt.gz", "wb") as dest:
        dest.writelines(src)

# Decompressing a file
with gzip.open("example.txt.gz", "rb") as src:
    with open("decompressed_example.txt", "wb") as dest:
        dest.writelines(src)
```
@Pyodide.eval

File compression is useful in AI workflows to save storage space and reduce data transfer times. For instance, you might compress large datasets before transferring them to a remote server for training. The `gzip` module provides an easy way to compress and decompress files in Python.

**Your Turn**: Extend the program to handle errors, such as missing files or permission issues.

---

### Activity 3: Data Backup System

Write a program that creates a backup of all `.txt` files in a directory:

```python
import os
import shutil

def backup_txt_files(source_dir, backup_dir):
    try:
        os.makedirs(backup_dir, exist_ok=True)
        for file_name in os.listdir(source_dir):
            if file_name.endswith(".txt"):
                full_source_path = os.path.join(source_dir, file_name)
                full_backup_path = os.path.join(backup_dir, file_name)
                shutil.copy(full_source_path, full_backup_path)
        print("Backup completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

backup_txt_files("./source", "./backup")
```
@Pyodide.eval

Data backup is a critical task in AI and data science to prevent data loss. For example, you might back up preprocessed datasets, trained models, or experiment results to ensure they are not lost due to hardware failures or accidental deletions.

**Your Turn**: Modify the program to log the names of all files that were backed up.

---

## Additional Resources

- [Python File Handling Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Python Logging Module](https://docs.python.org/3/library/logging.html)
- [Python Gzip Module](https://docs.python.org/3/library/gzip.html)

---

## Recap

@recap

---
