<!--
module_id: python_basics_loops
author:   Meredith Lee
email:    leemc@chop.edu
version: 1.2.2
current_version_description: Replaced SageMathCells with Pyodide cells for better usability
module_type: standard
docs_version: 1.2.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Loops

comment: Learn how to use loops in Python. 

long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about how to loop through sequences. 

estimated_time_in_minutes: 40

@pre_reqs
Learners should be familiar with using [functions and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1) and [collections](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1) at a beginner level. 
@end

@learning_objectives

- Iterate through lists using loops

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

- [1.0.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/5e1bbae6792dc5adc7cfcc99860b0f9e1447daa6/python_basics_loops/python_basics_loops.md#) Initial version
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Python Basics: Loops

@overview


## Attribution

@attribution


## Lesson Preparation

@lesson_prep_python_pyodide


## Introduction

In programming, we often need to perform a task repeatedly (or **iteratively**), or only if certain conditions are met. Iterating over an series of inputs and performing a specified task on each input is accomplished using **loops**.  Loops are not unique to Python-- they appear in almost every language! This module will discuss how these concepts work in Python. 


## For Loops

In Python, [lists and dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1) are examples of **iterable** objects, or objects whose members can be returned one at a time. This is important in **loops**, which repeat (or iterate) the same operation for each element in an iterable object like a list.

For a sense of how for loops work in Python, here is a simple example. Let's say there are five children at a party, and they each start with a certain number of pieces of candy. Next, let's say that we give each child 5 more pieces of candy. Using a simple loop, we can get a list of how many total pieces of candy each child has now using the `for` and `in` keywords.
    

```python
starting_candy = [3, 10, 11, 6, 7]
candy_day1 = [] #Here we are initiating an empty list, so that we can add elements to it later
for i in starting_candy: #In the loop, i will take on the value of each list element in turn
    j = i + 5
    candy_day1.append(j)
print(candy_day1)
```
@Pyodide.eval

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Did you notice the explanatory text in the above code cell that started with a pound sign (or hash mark)? The pound sign / hash mark ( # ) in a code cell indicates the start of a **comment**. Comments aren't recognized as code and won't be run. Each line of a comment must be marked with a new pound sign. Comments are an excellent way to add brief explanations and clarifications about your code.

</div>

This example loops through the list of numbers, adds 5 to each number one at a time, and adds the sum to a new list using the `.append()` method for lists. Finally, we printed the new list to our screen. This kind of loop is sometimes called a **for loop**; there is another kind of loop called a **while loop**, which is often used when we don't know the number of times we'll have to iterate through a block of code before we start ([check out this page for more information about while loops](https://www.geeksforgeeks.org/python-while-loop/)).


### Indentation

```python
starting_candy = [3, 10, 11, 6, 7]
candy_day1 = [] #Here we are initiating an empty list, so that we can add elements to it later
for i in starting_candy: #In the loop, i will take on the value of each list element in turn
    j = i + 5
    candy_day1.append(j)
print(candy_day1)
```
@Pyodide.eval

The code cell above is exactly the same as the one on the previous page. Notice that the two lines of code after the `for` statement are **indented**. This indentation is important in Python, and not just for readability! Indents indicate blocks of code, or lines of code that do a specific thing. In this case, the two lines after the `for` statement are in a different code block than the rest; they comprise the body of the loop. Indentation tells Python what statements to evaluate in what order. You also may have noticed a colon (:) at the end of the `for` statement. This tells Python that the following lines are a new code block and should be indented. All of the lines of a code block need to be indented the same number of spaces.

Try changing the code cell above by removing the indentation before `candy_day1.append(j)` in line 5. How does the output change? Why do you think it changes the way that it does?

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Indentation is tricky, especially for complex nested loops; experienced Python programmers sometimes struggle with this, so don't worry if it takes some trial and error to figure out! If you end up struggling with a tricky loop, try isolating the individual pieces, get those working, and then build outward. [Drawing a flowchart of the problem](https://problemsolvingwithpython.com/09-Loops/09.04-Flowcharts-Describing-Loops/) can also help!

</div>


### Range
The built-in function `range()` is frequently used in loops. The `range()` function returns a range object.

```python
print(range(1, 20))
```
@Pyodide.eval

This is not terribly interesting on its own, but is very useful if you want to loop through a sequence of numbers, such as 1 to 20, without having to manually build a list of all of those numbers. If you create a list from the range object and then print that list, you'll see what's going on behind the scenes. What do you think this code will do? Run the code cell below and find out.

```python
print(list(range(1, 20)))
```
@Pyodide.eval

Notice that the last number listed is 19, not 20. Just like in subsetting, the first number passed to `range()` is **inclusive**, and the second is **exclusive**. And don't forget that the first position is index 0!

**Your Turn**: Before running the code cell below, try to predict what number will be returned. Got a number in mind? Run the code and see if your hypothesis is correct! (**Hint**: the bracket notation below (`[ ]`) allows Python to access an element in a collection object, like a list; for a refresher take a look at this [introduction to lists in Python](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#4).)

```python
print(list(range(1, 20))[7])
```
@Pyodide.eval


### Quiz: Loops


```python
for i in range(0, 6):
    j = i*i
```
@Pyodide.eval

The loop in the code cell above is missing a `print()` statement to show us the output. How would you include a `print()` statement such that all of the squares of `i` in `range(0,6)` are displayed? Feel free to edit the code cell above and experiment to find the answer.

[( )] `print(i)`, indented so that it **inside** the loop
[(X)] `print(j)`, indented so that it **inside** the loop
[( )] `print(i)` with no indentation, so that it is **outside** of the loop
[( )] `print(j)` with no indentation, so that it is **outside** of the loop
***
<div class = "answer">

According to our code, we know that `j` is the square of `i`, so that's the number we need to print. If we put the `print(j)` statement **outside** of the loop, we only see the last number, 25, because that is the value that `j` had once the loop was completed. If we place the `print(j)` statement **inside** the loop, each value of `j` is printed before the next iteration of the loop. Therefore, the second option is correct.

</div>
***


## While loops

In addition to **for loops**, Python provides another way to repeat a block of code: the **while loop**. While loops are useful when you don't know in advance how many times you need to repeat an action, but you do know the condition that should end the loop.

A while loop continues to execute as long as a specified condition remains true.

The basic structure of a while loop looks like this:

```python
while condition:
    # code block to execute
```

The loop will keep running until the condition evaluates to `False`. Be careful: if the condition never becomes `False`, the loop will run forever (this is called an **infinite loop**).

Here's a simple example that counts from 1 to 5:

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
@Pyodide.eval

In this example, the variable `count` starts at 1. The loop checks if `count` is less than or equal to 5. If so, it prints the value and then increases `count` by 1. Once `count` becomes 6, the condition is no longer true, and the loop stops.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>
Always make sure that something inside your while loop will eventually make the condition `False`. Otherwise, you'll create an infinite loop, and your program will never stop running!

Inifinite loops are a particular problem for these learning materials as unlike on a typical computer, you can't just hit "Ctrl+C" to end the program. If you create an infinite loop, you'll need to refresh the page to kill it.
</div>

### Indentation

```python
count = 0
while count <= 5:
    count += 1
    print(count)
print("Done!")
```
@Pyodide.eval

Just like with for loops, indentation is crucial in while loops. The indented lines after the `while` statement form the body of the loop and will be executed repeatedly as long as the condition is true.

Try removing the indentation before `print(count)` in the code above. What happens? Why do you think Python requires indentation here?

### Common Pitfalls

- **Forgetting to update the condition:** If you forget to change the variable used in the condition, you might create an infinite loop.
- **Off-by-one errors:** Double-check your conditions to ensure the loop runs the correct number of times.

### Quiz: While Loops

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```
@Pyodide.eval

What will be the output of the code above?

[( )] 3 3 3
[( )] 3 2 2 1 1 0
[(X)] 3 2 1
[( )] 1 2 3
***
<div class = "answer">

The code prints the value of `n` and then subtracts 1 from `n` each time through the loop. The loop stops when `n` becomes 0, so the output is 3, 2, 1.

</div>
***

**Your Turn:** Try editing the code above to count up from 1 to 3 instead of down from 3 to 1. What changes do you need to make?

### When to Use While Loops

Use a while loop when you don't know in advance how many times you need to repeat an action, but you do know the condition that should end the loop. For example, you might use a while loop to keep asking a user for input until they provide a valid response.

For more on while loops, see the [Python documentation on control flow](https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools).


## Nested loops

A **nested loop** is a loop inside another loop. This is useful when you need to perform a repetitive action within another repetitive action, such as working with multi-dimensional data (like lists of lists).

The most common example is a nested `for` loop:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item)
```
@Pyodide.eval

In this example, the outer loop iterates over each row in the matrix, and the inner loop iterates over each item in the current row. This prints every element in the 2D list.

### How Nested Loops Work

- The **outer loop** runs once for each element in the outer collection.
- For each iteration of the outer loop, the **inner loop** runs through all its iterations.

This means the inner loop completes all its iterations for every single iteration of the outer loop.

### Example: Multiplication Table

You can use nested loops to print a multiplication table:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```
@Pyodide.eval


The key thing to understand about nested loops is that while the inner loop is only defined to iterate 3 times, it will do so for each iteration of the outer loop. So in total, the inner loop runs 3 (inner) x 3 (outer) = 9 times.

Therefore, having nested loops is a powerful tool but one that can also lead to computationally expensive operations if the loops are large or deeply nested.

```python
loops = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                loops += 1
print("Quadruple nested loops ran", loops, "times")
```
@Pyodide.eval

<div class = "important">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br




### Quiz: Nested Loops

Question 1
==========

What will the following code print?

```python
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")
```
@Pyodide.eval

[( )] i=0, j=0 i=1, j=1 i=2, j=2  
[(X)] i=0, j=0 i=0, j=1 i=0, j=2 i=1, j=0 i=1, j=1 i=1, j=2  
[( )] i=0, j=0 i=1, j=0 i=2, j=0  
[( )] i=0, j=1 i=1, j=2  
***
<div class="answer">

The outer loop runs twice (`i=0` and `i=1`), and for each value of `i`, the inner loop runs three times (`j=0`, `j=1`, `j=2`). So, the output lists all combinations of `i` and `j`.

</div>
***

**Your Turn:**  
Try modifying the multiplication table example above to print a 5x5 table instead of a 3x3 table.


### When to Use Nested Loops

Use nested loops when you need to process data with more than one dimension, such as grids, matrices, or when comparing every item in a collection to every other item.

For more details, see the [Python documentation on nested loops](https://docs.python.org/3/tutorial/controlflow.html#nested-compound-statements).


## Additional Resources

* There are many helpful resources on [python.org](https://www.python.org/), including a [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) and [FAQs](https://docs.python.org/3/faq/).

* The Python documentation also has [more details and examples about loops and conditional statements](https://docs.python.org/3/tutorial/controlflow.html). 

## Recap

@recap