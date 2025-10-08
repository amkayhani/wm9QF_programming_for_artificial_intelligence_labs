<!--
module_id: sorting_algorithms
author:   David Croft
email:    david.croft@warwick.ac.uk
version: 0.0.1
current_version_description: Initial version
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook
title: Sorting Algorithms
comment:  This module introduces the the concepts of sorting algorithms, and how to implement them in Python.
long_description: This module introduces the the concepts of sorting algorithms in Python, and how to implement them.
estimated_time_in_minutes: 20

@pre_reqs
Learners should be familiar with basic programming concepts and the Python programming language, including importing modules and using functions. Learners do not need to have access to Python or Jupyter notebooks on their own computers.
@end

@learning_objectives  
- Understand the concept of sorting algorithms and their importance in computer science.
- Learn how to implement basic sorting algorithms (Bubble Sort, Selection Sort, Merge Sort) in Python.
- Gain hands-on experience with visualizing sorting algorithms using interactive tools.

@end

good_first_module: false
collection: demystifying
coding_required: false
coding_language: python

@sets_you_up_for
- python_basics_variables_functions
@end

@depends_on_knowledge_available_in
- demystifying_command_line
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

@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_algo_visualisations.md
import: https://dscroft.github.io/Pyodide/README.md
-->



# Sorting Algorithms

@overview

## Attribution

@algo_attribution

## Introduction

**Sorting** is one of the most fundamental operations in computer science. It involves arranging data in a particular order, typically ascending or descending. Sorting is essential because:

- It makes data easier to search through
- It enables efficient data processing algorithms
- It helps in data analysis and visualization
- Many other algorithms rely on sorted data

In this module, we'll explore several classic sorting algorithms, understand how they work, and implement them in Python. We'll also visualize their behavior using interactive tools to help you understand the differences between them.

<div class = "important">
<b style="color: rgb(var(--color-highlight));">Important note</b><br>

While Python has built-in sorting functions like `sorted()` and `.sort()`, understanding how sorting algorithms work under the hood will make you a better programmer and help you choose the right approach for different scenarios.

</div>

## Understanding Algorithm Complexity

Before we dive into specific algorithms, it's important to understand **time complexity** - how the performance of an algorithm changes as the size of the input grows.

We use **Big O notation** to describe time complexity:

- **O(1)**: Constant time - the algorithm takes the same time regardless of input size
- **O(n)**: Linear time - time increases proportionally with input size
- **O(n²)**: Quadratic time - time increases with the square of input size
- **O(n log n)**: Linearithmic time - more efficient than quadratic but slower than linear

For sorting algorithms, we generally want to minimize time complexity, especially for large datasets.

## Bubble Sort

**Bubble Sort** is one of the simplest sorting algorithms to understand. It works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they're in the wrong order. The pass through the list is repeated until the list is sorted.

### How Bubble Sort Works

1. Compare the first two elements
2. If they're in the wrong order, swap them
3. Move to the next pair and repeat
4. Continue until you reach the end of the list
5. Repeat the entire process until no swaps are needed

@algo_vis(LiaBubble)

### Implementing Bubble Sort in Python

Let's implement bubble sort step by step:

```python
def bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        List: Sorted list in ascending order
    """
    # Make a copy to avoid modifying the original list
    arr = arr.copy()
    n = len(arr)
    
    # Traverse through all elements
    for i in range(n):
        # Flag to optimize - if no swaps occur, the list is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, the array is sorted
        if not swapped:
            break
    
    return arr

# Test the function
test_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", test_list)
sorted_list = bubble_sort(test_list)
print("Sorted list:", sorted_list)
```
@Pyodide.eval

**Time Complexity**: O(n²) in the worst case, O(n) in the best case (when the list is already sorted)
**Space Complexity**: O(1) - only uses a constant amount of extra memory

### When to Use Bubble Sort

Bubble sort is rarely used in practice due to its poor performance on large datasets. However, it's useful for:
- Educational purposes (easy to understand)
- Very small datasets
- Situations where simplicity is more important than efficiency

## Selection Sort

**Selection Sort** works by finding the minimum element from the unsorted portion and placing it at the beginning. This process is repeated for the remaining unsorted portion.

### How Selection Sort Works

1. Find the minimum element in the array
2. Swap it with the first element
3. Find the minimum element in the remaining array (excluding the first element)
4. Swap it with the second element
5. Continue until the entire array is sorted

@algo_vis(LiaSelection)

### Implementing Selection Sort in Python

```python
def selection_sort(arr):
    """
    Sort an array using the selection sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        List: Sorted list in ascending order
    """
    arr = arr.copy()
    n = len(arr)
    
    # Traverse through all elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Test the function
test_list = [64, 25, 12, 22, 11, 90]
print("Original list:", test_list)
sorted_list = selection_sort(test_list)
print("Sorted list:", sorted_list)
```
@Pyodide.eval

**Time Complexity**: O(n²) in all cases
**Space Complexity**: O(1)

Selection sort performs fewer swaps than bubble sort, which can be advantageous when the cost of swapping is high.

## Merge Sort

**Merge Sort** is a divide-and-conquer algorithm that divides the array into two halves, sorts them separately, and then merges them back together. This is much more efficient than bubble sort and selection sort for large datasets.

### How Merge Sort Works

1. **Divide**: Split the array into two halves
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the two sorted halves back together

@algo_vis(LiaMerge)

### Implementing Merge Sort in Python

```python
def merge_sort(arr):
    """
    Sort an array using the merge sort algorithm.
    
    Args:
        arr: List of comparable elements
    
    Returns:
        List: Sorted list in ascending order
    """
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: Sorted list
        right: Sorted list
    
    Returns:
        List: Merged sorted list
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right array
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# Test the function
test_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", test_list)
sorted_list = merge_sort(test_list)
print("Sorted list:", sorted_list)
```
@Pyodide.eval

**Time Complexity**: O(n log n) in all cases
**Space Complexity**: O(n) - requires additional memory for the temporary arrays

Merge sort is much more efficient than bubble sort and selection sort for large datasets and has consistent performance regardless of the initial order of the data.

## Comparing Sorting Algorithms

Let's compare the performance of our three sorting algorithms:

```python
import time
import random

def time_sorting_algorithm(sort_func, arr):
    """Time how long it takes to sort an array."""
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return end_time - start_time, sorted_arr

# Create test data of different sizes
small_data = [random.randint(1, 100) for _ in range(50)]
medium_data = [random.randint(1, 1000) for _ in range(200)]

print("Performance Comparison:")
print("=" * 50)

for name, data in [("Small (50 elements)", small_data), ("Medium (200 elements)", medium_data)]:
    print(f"\n{name}:")
    
    # Test Bubble Sort
    time_taken, _ = time_sorting_algorithm(bubble_sort, data)
    print(f"Bubble Sort: {time_taken:.6f} seconds")
    
    # Test Selection Sort
    time_taken, _ = time_sorting_algorithm(selection_sort, data)
    print(f"Selection Sort: {time_taken:.6f} seconds")
    
    # Test Merge Sort
    time_taken, _ = time_sorting_algorithm(merge_sort, data)
    print(f"Merge Sort: {time_taken:.6f} seconds")
```
@Pyodide.eval

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

The timing results may vary between runs due to system load and other factors. The important thing to notice is the relative performance differences between the algorithms, especially as the data size increases.

</div>

## Quiz: Sorting Algorithms

1. Which sorting algorithm has the best worst-case time complexity?

   [( )] Bubble Sort
   [( )] Selection Sort
   [(X)] Merge Sort
   [( )] All have the same complexity
   ***
   <div class = "answer">

   Merge Sort has O(n log n) time complexity in all cases, while Bubble Sort and Selection Sort both have O(n²) worst-case time complexity. This makes Merge Sort much more efficient for large datasets.

   </div>
   ***

2. Which sorting algorithm uses the least additional memory?

   [(X)] Both Bubble Sort and Selection Sort
   [( )] Merge Sort
   [( )] None of them use additional memory
   [( )] They all use the same amount of memory
   ***
   <div class = "answer">

   Both Bubble Sort and Selection Sort have O(1) space complexity, meaning they sort the array in-place using only a constant amount of extra memory. Merge Sort requires O(n) additional space for the temporary arrays used during merging.

   </div>
   ***

3. In what scenario might you choose Bubble Sort over Merge Sort?

   [( )] When you have a very large dataset
   [( )] When performance is critical
   [(X)] When you need a simple algorithm for educational purposes or very small datasets
   [( )] When you want the fastest possible sorting
   ***
   <div class = "answer">

   While Merge Sort is generally superior in terms of performance, Bubble Sort might be chosen when simplicity and ease of understanding are more important than efficiency, such as in educational contexts or when dealing with very small datasets where the performance difference is negligible.

   </div>
   ***

## Python's Built-in Sorting

Python provides highly optimized built-in sorting functions that you should use in real applications:

```python
# Using the sorted() function (returns a new sorted list)
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sorted(numbers)
print("Original:", numbers)
print("Sorted (new list):", sorted_numbers)

# Using the .sort() method (sorts the list in-place)
numbers_copy = numbers.copy()
numbers_copy.sort()
print("Sorted in-place:", numbers_copy)

# Sorting in descending order
descending = sorted(numbers, reverse=True)
print("Descending order:", descending)

# Sorting strings
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)
print("Sorted words:", sorted_words)

# Sorting by custom criteria (length of strings)
sorted_by_length = sorted(words, key=len)
print("Sorted by length:", sorted_by_length)
```
@Pyodide.eval

Python's built-in sorting uses **Timsort**, a hybrid algorithm that combines merge sort and insertion sort, achieving O(n log n) performance with excellent real-world performance characteristics.

## Practical Exercises

### Exercise 1: Modify Bubble Sort

Modify the bubble sort implementation to sort in descending order instead of ascending order:

```python
def bubble_sort_descending(arr):
    """
    Sort an array in descending order using bubble sort.
    Complete this function.
    """
    # Your code here
    return arr

# Test your function
test_data = [3, 1, 4, 1, 5, 9, 2, 6]
result = bubble_sort_descending(test_data)
print("Descending order:", result)  # Should print [9, 6, 5, 4, 3, 2, 1, 1]
```
@Pyodide.eval

------------------

**Test your function**

```python
import random

test_data = [random.randint(1, 99) for _ in range(10)]
rev_data = sorted(test_data, reverse=True)
result = bubble_sort_descending(test_data)

if result == rev_data:
    print( "Passed!" )
else:
    print( "Failed!" )
    print(f"            Input: {test_data}")
    print(f"   Expected order: {rev_data}")  # Should print the list sorted in descending order
    print(f"Function returned: {result}")
```
@Pyodide.hide


### Exercise 2: Bogo Sort

Bogo sort is a highly ineffective sorting algorithm based on the generate and test paradigm. 
The algorithm randomly shuffles the input values until they find a permutations of the array until it finds one that is sorted.

Such an algorithm is not useful in any real application.

```python
def bogo_sort(arr):
    """
    Sort an array using bogo sort and count the number of iterations.
    Return both the sorted array and the number of iterations.
    """
    counter = 0
    # Your code here
    return arr, counter

# Test your function
test_data = [5, 2, 8, 1, 9]
sorted_arr, counter = bogo_sort(test_data)

print(f"Sorted: {sorted_arr}")
print(f"Iterations taken: {counter}")
```
@Pyodide.eval

------------------

**Test your function**

```python
test_data = [5, 2, 8, 1, 9]
sorted_arr, counter = bogo_sort(test_data)
if sorted_arr == sorted(test_data):
    print( "Passed!" )
    print(f"Iterations taken: {counter}")
else:
    print( "Failed!" )
    print(f"            Input: {test_data}")
    print(f"   Expected order: {sorted(test_data)}")  # Should print the list sorted in ascending order
    print(f"Function returned: {sorted_arr}")
```
@Pyodide.hide


There is no reliable way to automatically test this function beyond verifying that the output is sorted. The number of iterations will vary randomly each time it runs—even for small input arrays, it can take anywhere from 1 to potentially an infinite number of iterations.

You can experiment by increasing the size of the input array to observe how it affects the number of iterations required. However, be aware that this algorithm is extremely inefficient, so sorting larger inputs may take a very long time!

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Don't worry if these exercises seem challenging at first! Start by understanding the existing code, then make small modifications. You can always refer back to the implementations above for guidance.

</div>


### Exercise 3: Stalin sort

Stalin sort is another joke sorting algorithm.

It 'sorts' the given array but getting rid of any values that are not already sorted.

```python
def stalin_sort(arr):
    """
    Sort an array using Stalin sort.
    """
    return arr

test_data = [24, 48, 5, 50, 90, 30, 54, 53]
sorted_data = stalin_sort(test_data)

print(f"'Sorted': {sorted_data}")
```
@Pyodide.eval

------------------

**Test your function**

```python
test_data = [24, 48, 5, 50, 90, 30, 54, 53]
expected  = [24, 48, 50, 90]
result = stalin_sort(test_data)

if result == expected:
    print( "Passed!" )
else:
    print( "Failed!" )
    print(f"            Input: {test_data}")
    print(f"   Expected order: {expected}")
    print(f"Function returned: {result}")
```
@Pyodide.hide

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

Don't worry if these exercises seem challenging at first! Start by understanding the existing code, then make small modifications. You can always refer back to the implementations above for guidance.

</div>


## Real-World Applications

Sorting algorithms are used everywhere in computing:

- **Database systems**: Sorting query results, indexing
- **Search engines**: Ranking search results
- **Graphics**: Sorting polygons for rendering
- **Data analysis**: Preparing data for statistical analysis
- **Operating systems**: Managing processes and memory
- **Compression algorithms**: Many rely on sorted data

Understanding these algorithms helps you make informed decisions about when to use built-in functions versus implementing custom solutions.


## Additional Resources

* **Algorithm Visualizations**: The interactive visualizations in this module are provided by [David Galles' Algorithm Visualizations](https://www.cs.usfca.edu/~galles/visualization/). Explore these tools to deepen your understanding of how different algorithms work.

* **Python Documentation**: Learn more about Python's built-in sorting functions in the [official Python documentation](https://docs.python.org/3/howto/sorting.html).

* **Big O Notation**: For a deeper dive into algorithm complexity analysis, check out [this comprehensive guide to Big O notation](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/).

* **Advanced Sorting Algorithms**: Once you're comfortable with these basics, explore more advanced algorithms like Quick Sort, Heap Sort, and Radix Sort.

* **Practice Problems**: Try implementing sorting algorithms on coding practice websites like [LeetCode](https://leetcode.com/) or [HackerRank](https://www.hackerrank.com/) to reinforce your understanding.

