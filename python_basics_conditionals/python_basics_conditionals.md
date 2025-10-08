<!--
module_id: python_basics_conditionals
author:   Meredith Lee
email:    leemc@chop.edu
version: 1.2.2
current_version_description: Replaced SageMathCells with Pyodide cells for better usability
module_type: standard
docs_version: 1.2.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Conditionals

comment: Learn how to use conditional statements in Python. 

long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about how to use conditional statements. 

estimated_time_in_minutes: 20

@pre_reqs
Learners should be familiar with using [functions and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1) and [collections](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1) at a beginner level. 
@end

@learning_objectives

- Utilize conditional statements

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_lists_dictionaries
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

- python_basics_exercise
- pandas_transform

@end

@depends_on_knowledge_available_in

- demystifying_python
- python_basics_variables_functions_methods
- python_basics_lists_dictionaries

@end


@version_history

Previous versions: 

- [1.0.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/5e1bbae6792dc5adc7cfcc99860b0f9e1447daa6/python_basics_loops_conditionals/python_basics_loops_conditionals.md#) Initial version
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Python Basics: Conditional Statements

@overview

## Attribution

@attribution

## Lesson Preparation

@sage

@lesson_prep_python_pyodide

## Introduction

In programming, it's common to want your code to make decisions or take different actions depending on certain conditions. **Conditional statements** allow you to control the flow of your program based on whether specific criteria are met. Alongside loops, which let you repeat actions, conditionals are a fundamental concept found in nearly every programming language. In this module, you'll learn how to use these tools effectively in Python.


## Conditional statements: If-else

Sometimes when you're working with Python, you might want your code to do different things in different circumstances. You handle this with an `if-else`, or **conditional**, statement.

Conditional statements often make use of **comparison operators**. Comparison operators compare values and return a `True` or `False` (also known as a [**boolean value**](https://www.geeksforgeeks.org/boolean-data-type-in-python/)), depending on the outcome of the comparison. Some important comparison operators include:

* `==`: In Python, this is used to test **equality** (be sure not to use  the single equals sign `=`, which is used for assigning values to variables). So `9 == 18` asks the questions "is 9 equal to 18?", which would evaluate to `False`.

* `!=`: not equal to.

* `<`: less than.

* `>`: greater than.

* `<=`: less than or equal to.

* `>=`: greater than or equal to.

Let's look at a simple example of some code that utilizes conditionals.

```python
name = "Pythonista"
# We're testing below to see if the value of name is a string.
# This will either evaluate to True or False.
if type(name) == str: 
    print("Welcome, "+ name+"!")
else:
    print("Please enter a name.")
```
@Pyodide.eval

**Your Turn**: Try changing the value assigned to `name` from "Pythonista" to a number, and see what happens! What happens if you remove the quotation marks?

### Multiple conditions


You also aren't confined to a single "if-else" statement! You can have multiple conditions and define multiple results. The simplest way to do this is with the keyword `elif`. Run the following code cell, and then change the number assigned to `num` and see how the output changes.

```python
num = 1
if num < 10:
    print("This number is less than 10")
elif 10 < num < 100:
    print("This number is more than 10 but less than 100")
elif num >= 100:
    print("This number is greater than or equal to 100")
else:
    print("This number equals 10")
```
@Pyodide.eval

<div class = "warning">
<b style="color: rgb(var(--color-highlight));">Warning!</b><br>

When coding in Python, it is important to remember that lines and blocks of code are run **in order**. This means that if your instructions aren't in logical order, you can get outputs that are "wrong."

</div>

**Your Turn**: Before you run the following code cell, predict what the outcome will be.

```python
num = 1
if num < 100:
    print("This number is less than 100")
elif num < 10:
    print("This number is less than 10")
elif num >= 100:
    print("This number is greater than or equal to 100.")
else:
    print("This number equals 10")
```
@Pyodide.eval

Was your prediction correct?

Because the conditional statements are run in order, and in the code above the first statement returns `True`, Python never gets to the second statement, even though it is also `True`! This behavior is important to remember when you're creating multiple conditional statements.

### Conditionals in loops

Python becomes very powerful when you start combining conditionals and loops.

Remember when we looped through a list of pieces of candy that some children started with and calculated the number they would have if we gave each child 5 more pieces? Let's suppose that the next day instead of giving all of the children more candy, only the children who have fewer than 10 pieces of candy get another piece. We can still calculate how many pieces of candy each child has now (even though we're making the very unlikely assumption that none of the children have eaten any of their candy from before!).

```python
candy1 = [8, 15, 16, 11, 12]
candy2 = []
for i in candy1:
    if i < 10: #tests to see if each student has fewer than 10 pieces of candy
        j = i + 1
    else:
        j = i
    candy2.append(j)
print(candy2)
```
@Pyodide.eval

In the case above, we've used an if-else statement within our `for` loop! These loops can actually get quite complex for some tasks, but breaking down the loop and testing out the various pieces is often a good strategy.

### Quiz: Conditional statements

Question 1
==========

What is the correct keyword to use when you want to check an additional condition after an `if` statement?

[( )] `for`  
[( )] `else`  
[(X)] `elif`  
[( )] `def`  
***
<div class="answer">
The `elif` keyword is used to check another condition if the previous `if` condition was not true.
</div>
***


Question 2
==========

What will the following code print?

```python
x = 7
if x > 10:
    print("Greater than 10")
elif x > 5:
    print("Greater than 5")
else:
    print("5 or less")
```

[( )] Greater than 10  
[(X)] Greater than 5  
[( )] 5 or less  
***
<div class="answer">
Since `x` is 7, the first condition is false, but the `elif` condition is true, so "Greater than 5" is printed.
</div>
***

Question 3
==========

Which of the following expressions will evaluate to `True` if `y = 12`?

[[X]] `y >= 10`  
[[ ]] `y < 10`  
[[X]] `y != 5`  
[[ ]] `y == 5`  
***
<div class="answer">
`y >= 10` and `y != 5` are both true when `y` is 12.
</div>
***


## Additional Resources

* There are many helpful resources on [python.org](https://www.python.org/), including a [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) and [FAQs](https://docs.python.org/3/faq/).

* The Python documentation also has [more details and examples about loops and conditional statements](https://docs.python.org/3/tutorial/controlflow.html). 

## Recap

@recap