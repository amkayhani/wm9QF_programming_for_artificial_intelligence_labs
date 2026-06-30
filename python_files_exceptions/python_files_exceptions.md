<!--
module_id: python_files_exceptions
author: 
email: 
version: 1.0.0
current_version_description: Initial version introducing file handling and exception handling in Python.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: File Handling and Exception Handling

comment: Learn how to work with files and handle exceptions in Python.

long_description: This module introduces learners to file handling and exception handling in Python. These are essential skills for working with external data and ensuring robust error handling in your programs.

estimated_time_in_minutes: 25


@learning_objectives

- Read from and write to files in Python.
- Handle exceptions using `try`, `except`, and `finally`.

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_conditionals
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

link: ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Python Basics: File Handling and Exception Handling



@overview

In this module, you will learn how to work with files in Python, including reading, writing, and appending data. Additionally, you will explore how to handle exceptions to make your programs more robust and error-resistant. By the end of this module, you will be able to confidently manage file operations and handle common errors that may arise during execution.

## Attribution

@attribution

## Lesson Preparation

@sage

@lesson_prep_python_pyodide

## Introduction

In Python, working with files and handling exceptions are essential skills for building robust programs. File handling allows you to read from and write to files, while exception handling ensures your program can gracefully handle errors that may occur during execution.

In this module, you'll learn how to:

1. Open, read, and write files in Python.
2. Handle exceptions using `try`, `except`, and `finally`.

---

## File Handling in Python

Python provides built-in functions to work with files. The most common operations are:

- **Opening a file**: Use the `open()` function.
- **Reading from a file**: Use methods like `read()`, `readline()`, or `readlines()`.
- **Writing to a file**: Use the `write()` or `writelines()` methods.
- **Closing a file**: Use the `close()` method or a `with` statement to automatically close the file.

### Example: Reading a File

<div style="display: none">
```python @Pyodide.exec
with open("example.txt", "w") as file:
    file.write("Hello World!")
```
</div>

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
@Pyodide.eval

**Your Turn**: Create a text file named `example.txt` with some content, and then run the code above to read its contents.

---

### Example: Writing to a File

```python
# Open a file in write mode
with open("example.txt", "w") as file:
    file.write("Hello, world!")
```
@Pyodide.eval

**Your Turn**: Run the code above to write to `example.txt`. Then, modify the code to append additional text using the `"a"` (append) mode.

---

### File Modes

When opening a file, you can specify the mode:

- `"r"`: Read (default).
- `"w"`: Write (overwrites the file if it exists).
- `"a"`: Append (adds content to the end of the file).
- `"b"`: Binary mode (e.g., `"rb"` for reading binary files).

---

## Exception Handling in Python

Errors can occur during file operations or other parts of your program. Python provides a way to handle these errors gracefully using `try`, `except`, and `finally`.

### Example: Handling Exceptions

```python
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
finally:
    print("Execution completed.")
```
@Pyodide.eval

**Your Turn**: Run the code above. What happens if you replace `"nonexistent_file.txt"` with the name of an existing file?

---

### Common Exceptions in File Handling

- `FileNotFoundError`: Raised when a file or directory is requested but doesn't exist.
- `PermissionError`: Raised when you don't have the required permissions to access a file.
- `IOError`: Raised for general input/output errors.

---

## Combining File Handling and Exception Handling

You can combine file handling and exception handling to create robust programs.

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

**Your Turn**: Modify the code above to handle additional exceptions, such as `IOError`.

---

## Quiz: File Handling and Exception Handling

Question 1
==========

What is the correct way to open a file for reading in Python?

[( )] `open("file.txt", "w")`  
[(X)] `open("file.txt", "r")`  
[( )] `open("file.txt", "a")`  
[( )] `open("file.txt", "rb")`  
***
<div class="answer">
The `"r"` mode is used to open a file for reading.
</div>
***

Question 2
==========

What will the following code print if `example.txt` does not exist?

```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Done.")
```

[( )] The contents of `example.txt`  
[(X)] File not found.  
[( )] Done.  
[( )] An error message  
***
<div class="answer">
The `FileNotFoundError` exception is caught, so "File not found." is printed, followed by "Done." from the `finally` block.
</div>
***

Question 3
==========

Which of the following exceptions is raised when trying to open a file that does not exist?

[[X]] `FileNotFoundError`  
[[ ]] `PermissionError`  
[[ ]] `IOError`  
[[ ]] `ValueError`  
***
<div class="answer">
`FileNotFoundError` is raised when a file does not exist.
</div>
***

---

## Additional Resources

- [Python File Handling Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)

---

## Recap

@recap