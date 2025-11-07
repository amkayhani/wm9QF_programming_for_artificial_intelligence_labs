<!--
module_id: searching_algorithms
author:   David Croft
email:    david.croft@warwick.ac.uk
version: 1.0.0
current_version_description: Comprehensive introduction to searching algorithms with Python implementation and interactive visualizations
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook
title: Searching Algorithms
comment: Learn fundamental searching algorithms including linear and binary search, with hands-on Python implementation and interactive visualizations.
long_description: This module introduces searching algorithms, fundamental techniques for finding specific elements in data collections. Students will learn to implement linear search and binary search in Python, understand their time complexities, and explore real-world applications through interactive visualizations and practical coding exercises.
estimated_time_in_minutes: 35

@pre_reqs
Learners should be familiar with [Python basics including variables, functions, and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [lists and basic data structures](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), and [loops and conditional statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1).
@end

@learning_objectives  
- Understand the fundamental concept of searching and its importance in computer science
- Implement linear search algorithm in Python and analyze its time complexity
- Implement binary search algorithm in Python and understand its prerequisites
- Compare the efficiency of different searching algorithms
- Apply searching algorithms to solve real-world problems
- Use interactive visualizations to understand algorithm behavior

@end

good_first_module: false
collection: programming_for_ai
sequence_name: algorithms
coding_required: true
coding_level: intermediate
coding_language: python

@sets_you_up_for
- sorting_algorithms
- data_structures
- algorithm_analysis
@end

@depends_on_knowledge_available_in
- python_basics_variables_functions_methods
- python_basics_lists_dictionaries
- python_basics_loops_conditionals
@end

@style
.flex-container {
    display: flex;
    flex-wrap: wrap; /* Allows the items to wrap as needed */
    align-items: stretch;
    gap: 20px; /* Adds both horizontal and vertical spacing between items */
}

.flex-child { 
    flex: 1;
    margin-right: 20px; /* Adds space between the columns */
}

@media (max-width: 600px) {
    .flex-child {
        flex: 100%; /* Makes the child divs take up the full width on slim devices */
        margin-right: 0; /* Removes the right margin */
    }
}
@end

@version_history 
Previous versions: 
- [0.0.1](https://github.com/dscroft/wm9QF_programming_for_artificial_intelligence_labs/blob/main/searching_algorithms/searching_algorithms.md) Initial framework
@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: ../module_templates/macros_algo_visualisations.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Searching Algorithms

@overview

## Attribution

@algo_attribution

## Introduction

Imagine you're looking for a specific book in a library with thousands of volumes, or trying to find a particular contact in your phone with hundreds of entries. How would you approach this task? Would you start from the beginning and check each item one by one, or would you use some strategy to find it more efficiently?

This is exactly the problem that **searching algorithms** solve in computer science. Searching algorithms are systematic methods for finding specific elements within a collection of data. They are fundamental to virtually every computer application you use - from web search engines like Google, to the autocomplete feature in your messaging app, to finding files on your computer.

In this module, we'll explore two fundamental searching algorithms: **linear search** and **binary search**. We'll learn how to implement them in Python, understand when to use each one, and discover why choosing the right algorithm can make the difference between a program that responds instantly and one that takes hours to complete.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Why Searching Algorithms Matter</b><br>

Searching is one of the most common operations in computing. Every time you:
- Search for a file on your computer
- Look up a word in a digital dictionary
- Find a product on an e-commerce website
- Use GPS navigation to find a route

You're relying on searching algorithms working efficiently behind the scenes. Understanding these algorithms helps you write better programs and makes you a more effective programmer.

</div>

## What Makes a Good Searching Algorithm?

Before we dive into specific algorithms, let's think about what makes one searching method better than another. The main factors we consider are:

**Time Complexity**: How much time does the algorithm take as the size of the data grows? An algorithm that works well for 100 items might be too slow for 100,000 items.

**Space Complexity**: How much additional memory does the algorithm need? Some algorithms trade memory for speed.

**Prerequisites**: Does the data need to be organized in a particular way before we can search it? Some algorithms require sorted data, while others work on any collection.

**Simplicity**: How easy is the algorithm to understand, implement, and debug? Sometimes a simpler algorithm is better even if it's not the fastest.

Let's explore these concepts through our two main searching algorithms.


## Linear Search

Linear search is the most straightforward searching algorithm. It's like looking for a book by checking every single book on the shelf, one by one, from the beginning until you find what you're looking for (or reach the end).

### How Linear Search Works

Linear search examines each element in a collection sequentially until it finds the target element or reaches the end of the collection. Here's the step-by-step process:

1. Start at the beginning of the list
2. Check if the current element matches what we're looking for
3. If it matches, we're done! Return the position where we found it
4. If it doesn't match, move to the next element
5. Repeat steps 2-4 until we find the element or reach the end
6. If we reach the end without finding the element, it's not in the list

### Linear Search Visualization

Let's see how linear search works with an interactive visualization:

@algo_vis(LiaSearchLinear)

### Implementing Linear Search in Python

Here's how we can implement linear search in Python:

```python
def linear_search(data_list, target):
    """
    Search for target in data_list using linear search.
    
    Args:
        data_list: List of elements to search through
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    for index in range(len(data_list)):
        if data_list[index] == target:
            return index  # Found it! Return the position
    
    return None  # Not found

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
target = 22

result = linear_search(numbers, target)
if result is not None:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
```
@Pyodide.eval

Try changing the `target` value in the code above to see how the search behaves with different values!

------------------------------------

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

Although we are implementing linear search ourselves for educational purposes, in 99.99% of real-world applications you would typically use built-in functions or libraries rather than implementing your own search algorithms from scratch.

For example, in Python Python's `in` keyword or the `index()` method of lists will linearly search for an element.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print( "cherry" in fruits )  
print( fruits.index("cherry") ) 
```
@Pyodide.eval

</div>



### Let's Try It Step by Step

Let's trace through the algorithm manually to understand what's happening:

```python
def linear_search_verbose(data_list, target):
    """
    Linear search with detailed output to show each step
    """
    print(f"Searching for {target} in list: {data_list}")
    print("Steps:")
    
    for index in range(len(data_list)):
        current_element = data_list[index]
        print(f"  Step {index + 1}: Checking index {index}, value = {current_element}")
        
        if current_element == target:
            print(f"  ✓ Found {target} at index {index}!")
            return index
    
    print(f"  ✗ {target} not found in the list")
    return None

# Let's see it in action
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
linear_search_verbose(fruits, "cherry")
```
@Pyodide.eval


### Time Complexity of Linear Search

Linear search has a **time complexity of O(n)**, which means the time it takes grows linearly with the size of the input. Here's why:

- **Best case**: The element we're looking for is at the beginning of the list - we find it in 1 step
- **Worst case**: The element is at the end of the list or not in the list at all - we check all n elements
- **Average case**: On average, we'll find the element halfway through the list - about n/2 steps

Let's demonstrate this with different sized lists:

```python @Pyodide.exec
def linear_search(data_list, target):
    """
    Search for target in data_list using linear search.
    
    Args:
        data_list: List of elements to search through
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    for index in range(len(data_list)):
        if data_list[index] == target:
            return index  # Found it! Return the position
    
    return None  # Not found
```

```python
import time

def time_linear_search(size):
    """
    Create a list of given size and time how long linear search takes
    """
    # Create a list of numbers from 0 to size-1
    test_list = list(range(size))
    target = size - 1  # Look for the last element (worst case)
    
    start_time = time.time()
    result = linear_search(test_list, target)
    end_time = time.time()
    
    duration = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"List size: {size:6d}, Time: {duration:.4f} ms")

# Test with different sizes
for size in [100, 1000, 10000, 100000]:
    time_linear_search(size)
```
@Pyodide.eval

### When to Use Linear Search

Linear search is ideal when:

- **The data is not sorted** - Linear search works on any collection, regardless of order
- **The dataset is small** - For small lists (< 100 elements), the simplicity often outweighs any efficiency concerns
- **You need to find all occurrences** - Linear search can easily be modified to find every occurrence of an element
- **Simplicity is important** - It's easy to understand, implement, and debug



### Quiz: Linear Search

**Your Turn**: Before running the code below, predict what the output will be. What index will be returned?

```python
animals = ["cat", "dog", "elephant", "fish", "giraffe"]
result = linear_search(animals, "zebra")
print(f"Result: {result}")
```
@Pyodide.eval

1. What would happen if we searched for "zebra" in the animals list above?

   [( )] The function would return 0
   [( )] The function would return 5
   [(X)] The function would return None
   [( )] The function throw an exception
   ***
   <div class = "answer">

   Since "zebra" is not in the list, the linear search function would check all elements and not find a match, so it would return None to indicate "not found".

   The function is unlikely to throw an exception since not finding an element is a normal case that the function should be able to handle gracefully.
   An exception would be a more suitable response if, for example, the input values were of the wrong type. E.g. `linear_search(123, "zebra")` would throw an exception because the first argument is not a list.

   </div>
   ***

2. In the worst case, how many comparisons would linear search make on a list of 1000 elements?

   [( )] 1
   [( )] 500
   [(X)] 1000
   [( )] 999
   ***
   <div class = "answer">

   In the worst case (element not found or at the end), linear search would need to check every single element in the list, which means 1000 comparisons for a list of 1000 elements.

   </div>
   ***


## Binary Search

Binary search is a much more efficient searching algorithm, but it comes with an important requirement: **the data must be sorted**. Think of it like looking up a word in a dictionary - you don't start from the beginning and check every word. Instead, you open the dictionary in the middle and decide whether to look in the first half or the second half based on alphabetical order.


### The Power of "Divide and Conquer"

Binary search uses a "divide and conquer" strategy. Here's how it works:

1. Look at the middle element of the sorted list
2. If it's the element we're looking for, we're done!
3. If our target is smaller than the middle element, we know it must be in the left half
4. If our target is larger than the middle element, it must be in the right half
5. Repeat the process with the appropriate half, ignoring the other half completely
6. Continue until we find the element or determine it's not in the list


### Binary Search Visualization

Let's see binary search in action:

@algo_vis(LiaSearchBinary)

Notice how binary search eliminates half of the remaining possibilities with each comparison!


### Implementing Binary Search in Python

Here's an implementation of binary search:

```python
def binary_search(sorted_list, target):
    """
    Search for target in sorted_list using binary search.
    
    Args:
        sorted_list: A sorted list of elements
        target: Element we're looking for
    
    Returns:
        Index of target if found, -1 if not found
    """
    left = 0                    # Start of search range
    right = len(sorted_list) - 1  # End of search range
    
    while left <= right:
        # Calculate middle index
        middle = (left + right) // 2
        middle_value = sorted_list[middle]
        
        if middle_value == target:
            return middle  # Found it!
        elif middle_value < target:
            # Target is in the right half
            left = middle + 1
        else:
            # Target is in the left half
            right = middle - 1
    
    return None  # Not found

# Example with a sorted list
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

result = binary_search(sorted_numbers, target)
if result is not None:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
```
@Pyodide.eval

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Critical Requirement</b><br>

Binary search **only works on sorted data**. 
If you try to use binary search on an unsorted list, you'll get incorrect results. 
Always make sure your data is sorted first!

</div>


### Binary Search Step by Step

Let's trace through binary search to see exactly how it works:

```python
def binary_search_verbose(sorted_list, target):
    """
    Binary search with detailed output showing each step
    """
    print(f"Searching for {target} in sorted list: {sorted_list}")
    print("Steps:")
    
    left = 0
    right = len(sorted_list) - 1
    step = 1
    
    while left <= right:
        middle = (left + right) // 2
        middle_value = sorted_list[middle]
        
        print(f"  Step {step}: Range[{left}:{right}], Middle index={middle}, Value={middle_value}")
        
        if middle_value == target:
            print(f"  ✓ Found {target} at index {middle}!")
            return middle
        elif middle_value < target:
            print(f"    {middle_value} < {target}, search right half")
            left = middle + 1
        else:
            print(f"    {middle_value} > {target}, search left half")
            right = middle - 1
        
        step += 1
    
    print(f"  ✗ {target} not found in the list")
    return -1

# Let's see it in action
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
binary_search_verbose(numbers, 12)
```
@Pyodide.eval

### Time Complexity: The Magic of O(log n)

Binary search has a time complexity of **O(log n)**, which is dramatically faster than linear search's O(n). Here's why this is so powerful:

- Each comparison eliminates half of the remaining possibilities
- For a list of 1,000 elements, linear search might need 1,000 comparisons
- Binary search would need at most 10 comparisons (since 2^10 = 1,024)
- For a list of 1,000,000 elements, binary search needs at most 20 comparisons!

Let's compare the performance:

```python @Pyodide.exec
import numpy as np
import matplotlib.pyplot as plt

n = np.array(list(range(0,50))+list(range(100,1000000,10000)))
bo = np.log2(n, where=n>0)
lo = n

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))

# Full range plot
ax1.plot(n, lo, label='Linear Search')
ax1.plot(n, bo, label='Binary Search')
ax1.set_xlabel('Input Size (n)')
ax1.set_ylabel('Comparisons')
ax1.set_title('Full Range: Linear vs Binary Search')
ax1.legend()
ax1.grid(True, linestyle='-.')

# Zoomed-in plot for small n
ax2.plot(n, lo, label='Linear Search')
ax2.plot(n, bo, label='Binary Search')
ax2.set_xlim(0, 50)
ax2.set_ylim(0, 50)
ax2.set_xlabel('Input Size (n)')
ax2.set_ylabel('Comparisons')
ax2.set_title('Zoomed In (n = 0 to 50)')
ax2.legend()
ax2.grid(True, linestyle='-.')

plt.tight_layout()
plt.show()
```





### Sorting First: The Tradeoff

Remember, binary search requires sorted data. If your data isn't sorted, you need to sort it first:

This is *the* tradeoff of binary search vs linear search. Sorting can be an expensive operation, efficient algorithms like quicksort or mergesort run in O(n log n) time.

If you are only searching once, then linear search's O(n) time might be faster overall than sorting & binary search with O(n log n) + O(log n).

However, if you are doing multiple searches on the same data, then the up front cost of sorting could be worth it for the much faster searches afterwards.

```python @Pyodide.exec
import numpy as np
import matplotlib.pyplot as plt

n = np.array(list(range(0,1000000,10000)))
bo = np.log2(n, where=n>0) + n*np.log2(n, where=n>0)  # sorting + binary search
lo = n

fig, ax1 = plt.subplots(1, 1, figsize=(8, 5))

# Full range plot
ax1.plot(n, lo, label='Linear Search')
ax1.plot(n, bo, label='Binary Search')
ax1.set_xlabel('Input Size (n)')
ax1.set_ylabel('Comparisons')
ax1.set_title('Linear vs Binary Search with sorting')
ax1.legend()
ax1.grid(True, linestyle='-.')

plt.tight_layout()
plt.show()
```


### When to Use Binary Search

Binary search is ideal when:

- **The data is already sorted** (or can be sorted once and searched many times)
- **You have a large dataset** - The efficiency gains become significant with larger data
- **You need fast lookups** - When response time is critical
- **You're doing many searches** - The cost of sorting is amortized over multiple searches

### Real-World Applications

Binary search is used everywhere in computing:

- **Database indexing**: Finding records quickly in large databases
- **File systems**: Locating files in directory structures
- **Game development**: Finding collision boundaries, AI decision trees
- **Scientific computing**: Root finding, optimization algorithms
- **Web applications**: Autocomplete features, search suggestions

### Quiz: Binary Search

1. What is the maximum number of comparisons binary search would need for a sorted list of 64 elements?

   [( )] 32
   [( )] 8
   [(X)] 6
   [( )] 64
   ***
   <div class = "answer">

   For 64 elements, binary search needs at most ⌈log₂(64)⌉ = ⌈6⌉ = 6 comparisons. Each comparison cuts the search space in half: 64 → 32 → 16 → 8 → 4 → 2 → 1.

   </div>
   ***

2. What would happen if you used binary search on an unsorted list?

   [( )] It would work but be slower than linear search
   [( )] It would automatically sort the list first
   [(X)] It might return incorrect results
   [( )] It would cause a runtime error
   ***
   <div class = "answer">

   Binary search assumes the data is sorted and uses this property to eliminate half the search space at each step. On unsorted data, this assumption is invalid, so the algorithm might miss the target element even if it exists in the list.

   </div>
   ***


## Practical Applications and Exercises

Now that we understand both linear and binary search, let's apply them to solve some real-world problems. These exercises will help you understand when to choose each algorithm and how to implement them effectively.

### Exercise 1: Linear Search – Find All Occurrences

Modify the existing `linear_search_all` function so that it returns a list of all indices where the target value appears in the list, instead of just the first occurrence.

```python
def linear_search_all(data_list, target):
    """
    Return a list of all indices where target appears in data_list.
    """
    for i in range(len(data_list)):
        if data_list[i] == target:
            return [i]
    return []

# Example usage
numbers = [4, 2, 7, 4, 9, 4, 1]
target = 4

result = linear_search_all(numbers, target)

print(f"All indices of {target}: {result}")
```
@Pyodide.eval

----------------------

**Test your function**

```python
numbers = [4, 2, 7, 4, 9, 4, 1]
target = 4

result = linear_search_all(numbers, target)

if set(result) == {0, 3, 5}:
    print("Test passed!")
else:
    print("Test failed. Missing some occurrences.")
```
@Pyodide.hide


### Exercise 2: Binary Search - Closest match

Try and modify the binary search function to return the index of the closest value to the target if the exact target is not found in the list.

```python
def binary_search_closest(sorted_list, target):
    """
    Return the index of the closest value to target in sorted_list.
    If not found, return None.
    """
    return sorted_list[0] # Placeholder implementation

# Example usage
data = [64, 89,  8,  2, 24,  3, 42, 76]
target = 45

result = binary_search_closest(sorted(data), target)

print(f"Closest value to {target} is {result}")
```
@Pyodide.eval

----------------------

**Test your function**

```python
data = [64, 89,  8,  2, 24,  3, 42, 76]
target = 45
answer = 42

result = binary_search_closest(sorted(data), target)

if result == answer:
    print("Test passed!")
else:
    print(f"Test failed. Looking for {target}, expected closest value to be {answer} but got {result} instead.")
```
@Pyodide.hide



## Algorithm Comparison and Summary

Let's summarize what we've learned about searching algorithms:

### Quick Comparison Table

| Aspect | Linear Search | Binary Search |
|--------|---------------|---------------|
| **Time Complexity** | O(n) | O(log n) |
| **Space Complexity** | O(1) | O(1) |
| **Data Requirement** | Any order | Must be sorted |
| **Best Use Cases** | Small datasets, unsorted data | Large sorted datasets |
| **Implementation** | Simple | Moderate |
| **Best Case** | O(1) - first element | O(1) - middle element |
| **Worst Case** | O(n) - last/not found | O(log n) - not found |


### When to Use Each Algorithm

**Choose Linear Search when:**

- Data size is small (< 100 elements)
- Data is unsorted and sorting is expensive
- You need to find all occurrences
- Simplicity is more important than efficiency
- Data structure doesn't support random access

**Choose Binary Search when:**

- Data is already sorted
- You have a large dataset (> 1000 elements)
- You'll be searching frequently
- Fast lookup time is critical
- You can afford the sorting overhead


### Key Takeaways

1. **Algorithm choice matters**: The difference between O(n) and O(log n) becomes dramatic as data grows
2. **Prerequisites are important**: Binary search's efficiency comes with the requirement of sorted data
3. **Context drives decisions**: The best algorithm depends on your specific use case
4. **Implementation simplicity has value**: Sometimes a simpler algorithm is better overall

### Final Quiz: Putting It All Together

1. You have a database of 100,000 customer records that you search through 1000 times per day. The records are currently unsorted. What's your best strategy?

   [( )] Always use linear search to avoid sorting costs.
   [( )] Sort the data once, then use binary search for all lookups.
   [( )] Use linear search for the first few searches, then switch to binary search.
   [(X)] Sort the data once, then use binary search for all lookups.
   ***
   <div class = "answer">

   With 100,000 records and 1000 searches per day, the cost of sorting once is quickly amortized. Binary search will be dramatically faster (about 17 comparisons vs 50,000 on average), making the total system much more efficient.

   </div>
   ***

2. You're implementing a feature to find all students with a particular grade in a list of 50 student records. Which approach is best?

   [( )] Binary search since it's always faster.
   [(X)] Linear search since you need all occurrences and the data is small.
   [( )] Sort by grade, then use binary search.
   [( )] Use a hash table instead.
   ***
   <div class = "answer">

   Linear search is perfect here because: 
   
   1. You need ALL occurrences, not just one.
   2. The dataset is small (50 elements).
   3. Linear search naturally finds all matches in a single pass.

   </div>
   ***

Congratulations! You now understand the fundamentals of searching algorithms and when to apply them. These concepts form the foundation for more advanced algorithms and data structures you'll encounter in computer science.

## Additional Resources

**Algorithm Visualization Tools:**

* [VisuAlgo - Interactive Algorithm Visualizations](https://visualgo.net/en/bst) - Excellent interactive visualizations for binary search trees and other searching algorithms
* [Algorithm Visualizer](https://algorithm-visualizer.org/) - Visual representations of many different algorithms including searching

**Python Programming Resources:**

* [Python.org Official Documentation](https://docs.python.org/3/) - Comprehensive Python documentation including built-in search functions
* [Python Algorithm Practice](https://leetcode.com/problemset/algorithms/) - Practice implementing searching algorithms with coding challenges
* [Real Python - Search Algorithms](https://realpython.com/binary-search-python/) - Detailed tutorial on implementing search algorithms in Python

**Computer Science Fundamentals:**

* [Khan Academy - Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) - Free course covering algorithm analysis and design
* [MIT OpenCourseWare - Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/) - University-level algorithms course materials

**Advanced Topics:**

* [Binary Search Variations](https://www.geeksforgeeks.org/binary-search/) 
  
  - Different implementations and applications of binary search
* [Hash Tables and Search](https://www.programiz.com/dsa/hash-table) 
  
  - Learn about O(1) average-case searching with hash tables
* [Search in Databases](https://use-the-index-luke.com/) 
  
  - How searching algorithms apply to database systems

**Practice Problems:**

* Try implementing these search variations:
  
  - Find the first occurrence of an element in a sorted array with duplicates.
  - Find the last occurrence of an element in a sorted array.
  - Search in a rotated sorted array.
  - Implement a binary search that works with floating-point numbers.

## Recap

@recap