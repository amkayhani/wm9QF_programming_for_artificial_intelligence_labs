<!--
module_id: decorators_in_python
author: Amir Kayhani
email: amir.kayhani@warwick.ac.uk
version: 1.0.0
current_version_description: Initial version introducing decorators in Python with practical examples and exercises.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Advanced: Decorators

comment: Learn how to write, use, and reason about decorators in Python.

long_description: This module explains how decorators work in Python, from basic wrappers to parameterized and class-based decorators. You will see practical AI-inspired examples, quizzes, and exercises to practice creating reusable behavior around functions and methods.

estimated_time_in_minutes: 50

@pre_reqs
Learners should be comfortable with [functions and parameters](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/functions_in_python/functions_in_python.md#1) and [loops and conditionals](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops/python_basics_loops.md#1).
@end

@learning_objectives

- Explain what decorators are and when to use them.
- Build and apply simple and parameterized decorators.
- Preserve function metadata with `functools.wraps`.
- Combine multiple decorators safely for functions and methods.
- Apply decorators to practical tasks such as logging, timing, and caching.

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: exception_handling_and_files
coding_required: true
coding_level: intermediate
coding_language: python

@sets_you_up_for

- object_oriented_programming
- python_unit_testing
- designing_reusable_components

@end

@depends_on_knowledge_available_in

- functions_in_python
- python_basics_loops

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

# Python Advanced: Decorators

@overview

Decorators let you wrap existing functions and methods with extra behavior without changing their code. They are a core tool for building reusable logging, timing, validation, and caching in Python. By the end of this module, you will know how to write decorators confidently and apply them to realistic AI and data tasks.

## Lesson Preparation

@lesson_prep_python_pyodide

## Introduction to Decorators

Decorators are callable objects that take a function (or method) and return a new callable with added behavior. They are written as higher-order functions and are applied with the `@decorator_name` syntax placed directly above a function definition.

At a high level, decorators help you:

1. Separate reusable concerns (logging, caching, validation) from business logic.
2. Keep functions small while still adding cross-cutting features.
3. Apply the same behavior consistently across many functions.

---

## Functions as First-Class Objects

In Python, functions are first-class: they can be stored in variables, passed to other functions, and returned as values. This is the foundation of decorators.

```python
def greet(name):
    return f"Hello, {name}!"

def apply_twice(func, value):
    first = func(value)
    second = func(first)
    return second

result = apply_twice(greet, "Ada")
print(result)
```
@Pyodide.eval

Because functions can be passed around like data, we can write functions that return new functions. Decorators rely on this idea.

---

## Building a Simple Decorator

A decorator is a function that accepts another function, defines a wrapper, and returns that wrapper. The wrapper is what actually runs when you call the decorated function.

```python
def announce(func):
    def wrapper():
        print("Starting...")
        output = func()
        print("Finished.")
        return output
    return wrapper

@announce
def say_hello():
    print("Hello!")

say_hello()
```
@Pyodide.eval

Here, `@announce` wraps `say_hello`. When `say_hello()` is called, Python actually calls `wrapper()`. This pattern lets you insert behavior before or after the original function runs.

**Quiz:** Why does the wrapper need to call `func()` inside it?

[( )] To rename the function.  
[(X)] To ensure the original function still executes.  
[( )] To prevent recursion.  
[( )] To silence errors.  

**Explanation:** Without calling `func()`, the decorated function would never execute; the decorator would only print messages.

---

## Handling Arguments with `*args` and `**kwargs`

Most real functions have parameters. Use `*args` and `**kwargs` in the wrapper so your decorator works with any signature.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

@debug
def power(base, exponent=2):
    return base ** exponent

add(3, 5)
power(4, exponent=3)
```
@Pyodide.eval

`*args` captures positional arguments and `**kwargs` captures keyword arguments, allowing the decorator to forward them unchanged to the original function.

---

## Preserving Metadata with `functools.wraps`

Decorators can hide useful metadata like the original function name and docstring. Use `functools.wraps` to copy metadata from the wrapped function to the wrapper.

```python
import functools

def safe_division(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Cannot divide by zero, returning None.")
            return None
    return wrapper

@safe_division
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b

print(divide.__name__)   # divide
print(divide.__doc__)    # Divide two numbers.
print(divide(10, 2))
print(divide(5, 0))
```
@Pyodide.eval

Without `@functools.wraps`, `divide.__name__` would show `wrapper`, which can confuse debugging tools, documentation, and test output.

---

## Stacking Multiple Decorators

You can apply several decorators to the same function. The closest decorator to the function runs first.

```python
import time
import functools

def measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} took {duration:.2f} ms")
        return result
    return wrapper

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        return output.upper()
    return wrapper

@measure
@uppercase
def greet(name):
    time.sleep(0.01)
    return f"Hello, {name}"

print(greet("Grace"))
```
@Pyodide.eval

Order matters: here `uppercase` runs first, then `measure` times the uppercased function. Reverse the order and you will time the original string creation instead.

---

## Parameterized Decorators

Sometimes you need a decorator that accepts its own arguments. This requires a decorator factory: a function that returns a decorator.

```python
import functools

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def wave(name):
    print(f"Hello, {name}")

wave("Ada")
```
@Pyodide.eval

Here `repeat(3)` returns a decorator configured to run the function three times. This pattern is common for configurable validation or access control.

**Your Turn:** Modify `repeat` so it prints the iteration number each time it calls the function.

---

## Decorators for Validation

Decorators are ideal for input validation, keeping function bodies focused on core logic.

```python
import functools

def require_positive(func):
    @functools.wraps(func)
    def wrapper(value):
        if value <= 0:
            raise ValueError("Value must be positive.")
        return func(value)
    return wrapper

@require_positive
def square_root(value):
    return value ** 0.5

print(square_root(9))
try:
    square_root(-4)
except ValueError as e:
    print("Validation failed:", e)
```
@Pyodide.eval

Validation decorators are especially useful in AI pipelines where data quality checks should be shared across many preprocessing functions.

---

## Decorators for Logging and Timing

Logging and timing are common cross-cutting concerns. Decorators make them reusable across different functions.

```python
import functools
import time

def log_and_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[LOG] {func.__name__} finished in {elapsed*1000:.2f} ms")
        return result
    return wrapper

@log_and_time
def simulate_inference(x):
    time.sleep(0.02)
    return x * 2

simulate_inference(21)
```
@Pyodide.eval

This pattern mirrors how production ML services measure latency and log performance for monitoring dashboards.

---

## Caching with `functools.lru_cache`

The standard library provides ready-made decorators too. `functools.lru_cache` memoizes results to speed up repeated calls.

```python
import functools
import time

@functools.lru_cache(maxsize=128)
def slow_square(n):
    time.sleep(0.01)  # pretend this is expensive
    return n * n

start = time.perf_counter()
slow_square(10)
slow_square(10)
duration = (time.perf_counter() - start) * 1000
print(f"Two calls took {duration:.2f} ms with caching enabled")
```
@Pyodide.eval

Memoization is useful in AI for repeated feature calculations or expensive model calls that reuse the same inputs.

---

## Decorators on Methods

Decorators work on methods too. The wrapper still receives `self` as the first argument for instance methods.

```python
import functools

def ensure_authenticated(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.authenticated:
            raise PermissionError("User is not authenticated.")
        return func(self, *args, **kwargs)
    return wrapper

class ModelService:
    def __init__(self):
        self.authenticated = False

    def login(self):
        self.authenticated = True

    @ensure_authenticated
    def predict(self, x):
        return x * 3

service = ModelService()
try:
    service.predict(2)
except PermissionError as e:
    print(e)

service.login()
print("Prediction:", service.predict(2))
```
@Pyodide.eval

The decorator checks authentication before allowing the method to run, similar to access control in deployed ML APIs.

---

## Class-Based Decorators

You can use a class with `__call__` defined as a decorator. This is handy when you need stateful behavior.

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"{self.func.__name__} called {self.calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def classify(sample):
    return f"Classified sample: {sample}"

classify("image_01")
classify("image_02")
```
@Pyodide.eval

Class-based decorators allow you to track state across calls (e.g., counting requests or storing a cache) without global variables.

---

## Common Pitfalls

1. **Forgetting `*args` and `**kwargs`**: This makes your decorator fail on functions with different signatures.
2. **Missing `functools.wraps`**: Debugging and documentation become harder because metadata is lost.
3. **Changing return types unexpectedly**: Ensure the wrapper returns what callers expect.
4. **Decorating functions with side effects**: Understand when additional behavior might change order-sensitive logic.

---

## Practice: Build Your Own Decorators

### Exercise 1: Retry Decorator

**Objective:** Write a decorator `retry(times)` that retries a function up to `times` times when it raises an exception, then re-raises the last error.

**Detailed Guide:**

1. **Create a decorator factory**: The outer function `retry` should accept a `times` parameter (number of retry attempts).
2. **Return a decorator**: This decorator will accept the function to be wrapped.
3. **Create a wrapper**: Inside the decorator, create a wrapper function that:
   - Loops up to `times` iterations
   - Attempts to call the original function inside a try-except block
   - If the function succeeds, return the result immediately
   - If an exception occurs and there are retries left, continue to the next iteration
   - If all retries are exhausted, re-raise the last exception
4. **Use `functools.wraps`**: Preserve the original function's metadata.
5. **Test the decorator**: Create a function that randomly fails (use `random.random()` to simulate failures) and apply your decorator to it.

**Implementation Steps:**

```python
import functools
import random

# Step 1: Create the retry decorator factory
def retry(times):
    """
    Decorator that retries a function up to 'times' times if it raises an exception.
    
    Args:
        times (int): Maximum number of retry attempts
    
    Returns:
        decorator: A decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            # Try executing the function 'times' times
            for attempt in range(times):
                try:
                    print(f"Attempt {attempt + 1} of {times}")
                    result = func(*args, **kwargs)
                    print(f"Success on attempt {attempt + 1}")
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    
            # If all attempts failed, raise the last exception
            print(f"All {times} attempts failed")
            raise last_exception
            
        return wrapper
    return decorator

# Step 2: Test function that randomly fails
@retry(times=5)
def unstable_api_call(data):
    """Simulates an unstable API call that randomly fails."""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network timeout")
    return f"Successfully processed: {data}"

# Step 3: Test the decorator
try:
    result = unstable_api_call("test_data")
    print(f"Final result: {result}")
except ConnectionError as e:
    print(f"Failed after all retries: {e}")
```
@Pyodide.eval

**Your Turn:** Modify the decorator to add exponential backoff (wait 1s, 2s, 4s between retries) using `time.sleep()`.

---

### Exercise 2: Type Checker

**Objective:** Create a decorator `enforce_types` that reads type hints from a function and raises `TypeError` if an argument does not match the annotated type.

**Detailed Guide:**

1. **Access type annotations**: Use `func.__annotations__` to get a dictionary of parameter names and their type hints.
2. **Match arguments to annotations**: In the wrapper, compare actual arguments against their expected types.
3. **Handle both positional and keyword arguments**: 
   - Use `inspect.signature()` to map positional args to parameter names
   - Check both `*args` and `**kwargs` against their expected types
4. **Raise TypeError**: If a type mismatch is detected, raise a descriptive `TypeError`.
5. **Skip return type**: Focus on checking input parameters (return type is `'return'` in annotations).
6. **Use `isinstance()`**: Check types using `isinstance(value, expected_type)`.

**Implementation Steps:**

```python
import functools
import inspect

def enforce_types(func):
    """
    Decorator that enforces type hints on function arguments.
    Raises TypeError if an argument doesn't match its annotated type.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the function's signature and annotations
        sig = inspect.signature(func)
        annotations = func.__annotations__
        
        # Bind the arguments to parameter names
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Check each argument against its type annotation
        for param_name, param_value in bound_args.arguments.items():
            # Skip if no annotation for this parameter
            if param_name not in annotations:
                continue
                
            # Skip the 'return' annotation
            if param_name == 'return':
                continue
            
            expected_type = annotations[param_name]
            
            # Check the type
            if not isinstance(param_value, expected_type):
                raise TypeError(
                    f"Argument '{param_name}' must be {expected_type.__name__}, "
                    f"got {type(param_value).__name__}"
                )
        
        # If all checks pass, call the function
        return func(*args, **kwargs)
    
    return wrapper

# Test the decorator
@enforce_types
def calculate_bmi(weight: float, height: float) -> float:
    """Calculate Body Mass Index."""
    return weight / (height ** 2)

@enforce_types
def greet_user(name: str, age: int) -> str:
    """Generate a greeting message."""
    return f"Hello {name}, you are {age} years old"

# Test cases
print("Test 1: Valid types")
print(calculate_bmi(70.5, 1.75))

print("\nTest 2: Valid types")
print(greet_user("Alice", 25))

print("\nTest 3: Invalid type for weight (should fail)")
try:
    calculate_bmi("70", 1.75)
except TypeError as e:
    print(f"Error caught: {e}")

print("\nTest 4: Invalid type for age (should fail)")
try:
    greet_user("Bob", "30")
except TypeError as e:
    print(f"Error caught: {e}")
```
@Pyodide.eval

**Your Turn:** Extend the decorator to also check the return type of the function.

---

### Exercise 3: Input Normalizer

**Objective:** Build a decorator that lowercases all string arguments before calling the function. Apply it to a simple text preprocessing function.

**Detailed Guide:**

1. **Create a decorator**: The decorator should accept a function and return a wrapper.
2. **Inspect arguments**: In the wrapper, examine both `*args` and `**kwargs`.
3. **Normalize strings**: Convert any string argument to lowercase using `.lower()`.
4. **Preserve non-strings**: Leave non-string arguments unchanged.
5. **Reconstruct arguments**: Build new tuples/dicts with normalized values.
6. **Call the original function**: Pass the normalized arguments to the wrapped function.

**Implementation Steps:**

```python
import functools

def normalize_strings(func):
    """
    Decorator that converts all string arguments to lowercase
    before passing them to the function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Normalize positional arguments
        normalized_args = tuple(
            arg.lower() if isinstance(arg, str) else arg
            for arg in args
        )
        
        # Normalize keyword arguments
        normalized_kwargs = {
            key: value.lower() if isinstance(value, str) else value
            for key, value in kwargs.items()
        }
        
        # Call the original function with normalized arguments
        return func(*normalized_args, **normalized_kwargs)
    
    return wrapper

# Example 1: Simple text processing
@normalize_strings
def create_username(first_name, last_name):
    """Create a username from first and last name."""
    return f"{first_name}_{last_name}"

# Example 2: Text analysis function
@normalize_strings
def analyze_text(text, min_length=3):
    """Analyze text and return words longer than min_length."""
    words = text.split()
    long_words = [word for word in words if len(word) >= min_length]
    return {
        'total_words': len(words),
        'long_words': long_words,
        'text_length': len(text)
    }

# Example 3: Search function
@normalize_strings
def search_keyword(content, keyword):
    """Search for a keyword in content (case-insensitive)."""
    return keyword in content

# Test the decorator
print("Test 1: Username creation")
print(create_username("JOHN", "DOE"))
print(create_username("Alice", "Smith"))

print("\nTest 2: Text analysis")
result = analyze_text("The QUICK Brown FOX jumps over the LAZY dog")
print(f"Total words: {result['total_words']}")
print(f"Long words: {result['long_words']}")

print("\nTest 3: Keyword search")
print(f"Found 'python': {search_keyword('I love PYTHON programming', 'python')}")
print(f"Found 'java': {search_keyword('I love PYTHON programming', 'java')}")

print("\nTest 4: Mixed argument types")
@normalize_strings
def format_message(name, count, prefix="User"):
    """Format a message with name and count."""
    return f"{prefix}: {name} has {count} items"

print(format_message("ALICE", 5, prefix="CUSTOMER"))
```
@Pyodide.eval

**Your Turn:** Extend the decorator to also strip whitespace from string arguments using `.strip()`.

---

### Bonus Exercise: Rate Limiter Decorator

**Challenge:** Create a decorator that limits how often a function can be called (e.g., max 3 calls per 10 seconds).

**Hint:** Use `time.time()` to track timestamps of function calls and store them in a list. Check if too many recent calls have been made before allowing the function to execute.

```python
import functools
import time

def rate_limit(max_calls, time_window):
    """
    Decorator that limits function calls to max_calls within time_window seconds.
    
    Args:
        max_calls (int): Maximum number of allowed calls
        time_window (float): Time window in seconds
    """
    def decorator(func):
        call_times = []
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_times
            current_time = time.time()
            
            # Remove calls outside the time window
            call_times = [t for t in call_times if current_time - t < time_window]
            
            # Check if we've exceeded the rate limit
            if len(call_times) >= max_calls:
                oldest_call = call_times[0]
                wait_time = time_window - (current_time - oldest_call)
                raise RuntimeError(
                    f"Rate limit exceeded. Try again in {wait_time:.1f} seconds."
                )
            
            # Record this call
            call_times.append(current_time)
            
            # Execute the function
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# Test the rate limiter
@rate_limit(max_calls=3, time_window=5)
def api_request(endpoint):
    """Simulate an API request."""
    return f"Response from {endpoint}"

# Make several rapid calls
print("Making rapid API calls...")
for i in range(5):
    try:
        result = api_request(f"/api/data/{i}")
        print(f"Call {i+1}: {result}")
    except RuntimeError as e:
        print(f"Call {i+1}: {e}")
```
@Pyodide.eval

---

## Additional Resources

- [Python Decorators Documentation](https://docs.python.org/3/glossary.html#term-decorator)
- [functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps)
- [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)
- [PEP 318: Decorators for Functions and Methods](https://peps.python.org/pep-0318/)

---

## Recap

@recap
