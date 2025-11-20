<!--
module_id: functions_in_python
version: 1.1.0
current_version_description: Added run buttons, more explanations, examples, difficult questions, and coding challenges.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Functions

comment: Learn how to define and use functions in Python.

long_description: This module introduces learners to functions in Python. Functions are essential for structuring code, improving reusability, and simplifying complex programs.

estimated_time_in_minutes: 30

@pre_reqs
Learners should be familiar with [basic Python syntax](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1).
@end

@learning_objectives

- Define and call functions in Python.
- Understand the difference between parameters and arguments.
- Use default arguments and keyword arguments.
- Explore variable scope and return values.

@end

@sets_you_up_for

- python_basics_exercise
- working_with_functions

@end

@version_history
Previous versions: None (initial version)
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Python Basics: Functions

@overview

In this module, you will learn how to define and use functions in Python. Functions are essential for structuring code, improving reusability, and simplifying complex programs. By the end of this module, you will be able to confidently create and use functions in your Python programs.

## Defining and Calling Functions

### What is a Function?

A function is a block of code that performs a specific task. Functions are defined using the `def` keyword:

```python
# Defining a function
def greet(name):
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
```
@Pyodide.eval

**Run the Code:**

```python
# Defining a function
def greet(name):
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
```

**Explanation:** Functions allow you to encapsulate logic and reuse it multiple times. In the example above, the `greet` function takes a `name` parameter and prints a greeting message.

---

### Parameters and Arguments

Functions can accept inputs, called parameters, and use them to perform operations. When calling a function, you provide values, called arguments, for these parameters:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)  # Output: 12
```
@Pyodide.eval

**Run the Code:**

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)  # Output: 12
```

**Explanation:** Parameters are placeholders in the function definition, while arguments are the actual values passed to the function when it is called.

---

## Advanced Examples

### Nested Functions

Functions can be defined inside other functions. This is useful for encapsulating logic that is only relevant within the outer function:

```python
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + x

print(outer_function(3))  # Output: 12
```
@Pyodide.eval

**Run the Code:**

```python
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + x

print(outer_function(3))  # Output: 12
```

**Explanation:** The `inner_function` is only accessible within `outer_function`. This is useful for creating helper functions that should not be exposed globally.

---

## Difficult Multiple-Choice Questions

### Question 1
What will the following code output?

```python
def tricky_function(a, b=[]):
    b.append(a)
    return b

print(tricky_function(1))
print(tricky_function(2))
```

[( )] [1], [2]  
[(X)] [1], [1, 2]  
[( )] Error  
[( )] None  

**Explanation:** The default value for `b` is a mutable list. It retains its state between function calls, leading to unexpected behavior.

---

### Question 2
Which of the following statements about Python functions is true?

[( )] Functions cannot return multiple values.  
[(X)] Functions can be passed as arguments to other functions.  
[( )] Functions must always have a `return` statement.  
[( )] Functions cannot have default arguments.  

**Explanation:** Python functions are first-class objects, meaning they can be passed as arguments, returned from other functions, and assigned to variables.

---

## Coding Challenges

### Challenge 1: Fibonacci Sequence
Write a function to generate the first `n` numbers in the Fibonacci sequence:

```python
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
@Pyodide.eval

### Challenge 2: Prime Numbers
Write a function to check if a number is prime:

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))  # Output: True
```
@Pyodide.eval

---

## Additional Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

---

## Recap

@recap

In this module, you learned how to define and use functions in Python. Functions are essential for structuring code, improving reusability, and simplifying complex programs. You explored parameters, arguments, default values, variable scope, and return values. Practice these concepts to become proficient in using functions in Python.