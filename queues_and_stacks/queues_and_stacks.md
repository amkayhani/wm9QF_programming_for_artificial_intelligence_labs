<!--
module_id: queues_and_stacks
author: Amir Kayhani
email: amir.kayhani@warwick.ac.uk
version: 1.0.0
current_version_description: Expanded examples and explanations, including deque.popleft behavior.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Data Structures: Stacks and Queues in Python

comment: Understand and implement stack and queue data structures in Python for algorithmic tasks.

long_description: This module walks through stacks and queues in Python, covering list and deque implementations, key operations, and how these structures power algorithms such as backtracking and breadth-first search.

estimated_time_in_minutes: 45

@pre_reqs
Learners should be comfortable with [basic Python syntax](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1) and [lists plus loops](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1).
@end

@learning_objectives

- Explain the difference between Last-In-First-Out (stack) and First-In-First-Out (queue) access.
- Implement stack operations (`push`, `pop`, `peek`, `is_empty`) using Python lists or `collections.deque`.
- Implement queue operations (`enqueue`, `dequeue`, `peek`, `is_empty`) with `collections.deque` and know when to use `queue.Queue`.
- Apply stacks and queues to simple algorithmic problems like expression checking and breadth-first search.

@end

good_first_module: false
collection: learn_to_code
sequence_name: data_structures_basics
previous_sequential_module: python_basics_lists_dictionaries
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

- data_structures_advanced
- searching_algorithms

@end

@depends_on_knowledge_available_in

- python_basics_variables_functions_methods
- python_basics_lists_dictionaries
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

# Data Structures: Stacks and Queues in Python

@overview

Stacks and queues are foundational linear data structures that control how elements are added and removed. Stacks follow **Last-In-First-Out (LIFO)** rules (think: undo history), while queues use **First-In-First-Out (FIFO)** rules (think: print jobs). By the end of this module you will implement both, compare performance, and practice applying them to common algorithmic tasks.
 

## Lesson Preparation

@lesson_prep_python_pyodide

## Introduction

Stacks and queues show up everywhere: browser back buttons, task schedulers, parsers, graph searches, and buffering data for machine learning pipelines. In this module you'll:

1. Build stacks and queues in Python using the standard library.
2. Compare time complexity of operations on different underlying containers.
3. Apply the structures to quick utilities such as balanced parentheses checks and breadth-first search (BFS).

---

## Stacks (LIFO)

A stack removes the most recently added item first. Common operations:

- `push`: add to the top
- `pop`: remove from the top
- `peek`: inspect the top item
- `is_empty` / `len`: check size or emptiness

### Using a List as a Stack

Python lists support `append` (push) and `pop` from the end in **O(1)** average time, making them a convenient stack.

```python
stack = []
stack.append("input layer")   # push
stack.append("hidden layer")  # push
stack.append("output layer")  # push

top = stack.pop()  # pop
print("Popped:", top)
print("Stack now:", stack)
```
@Pyodide.eval

**Quiz:** What does `stack.pop()` return in the code above?

[( )] `"input layer"`  
[( )] `"hidden layer"`  
[(X)] `"output layer"`  
[( )] It raises an error.  

---

### Implementing a Stack Class

Wrapping stack behavior in a class keeps responsibilities clear and avoids underflow errors.

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Cannot pop from an empty stack.")
        return self._data.pop()

    def peek(self):
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

stack = Stack()
for layer in ("embedding", "encoder", "classifier"):
    stack.push(layer)

print("Top:", stack.peek())
print("Popped:", stack.pop())
print("Remaining:", stack._data)
```
@Pyodide.eval

**Another example:** Undo history for a text buffer. Each action is pushed; undo pops the last action.

```python
actions = []

def type_char(ch):
    actions.append(ch)

def undo():
    if actions:
        return actions.pop()
    return None

for ch in "AI":
    type_char(ch)

print("Buffer after typing:", "".join(actions))
undo()
print("Buffer after undo:", "".join(actions))
```
@Pyodide.eval

---

### Applying Stacks: Balanced Parentheses

Stacks help track opening symbols in expressions. Each opening bracket is pushed; each closing bracket must match the top of the stack.

```python
def balanced(expr):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in expr:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

tests = ["(a+b) * [c-d]", "([)]", "((())", "{[()]()}"]
for t in tests:
    print(t, "->", balanced(t))
```
@Pyodide.eval

**Quiz:** Why is `"([)]"` reported as unbalanced?

[( )] Because it has different types of brackets.  
[(X)] Because the closing order does not match the LIFO ordering of the opening brackets.  
[( )] Because it contains parentheses and brackets in the same string.  
[( )] Because the algorithm always returns False for mixed brackets.  

---

## Queues (FIFO)

A queue removes the earliest added item first. Common operations:

- `enqueue`: add to the back
- `dequeue`: remove from the front
- `peek`: inspect the front item
- `is_empty` / `len`: check size or emptiness

### Using `collections.deque` for Queues

`deque` provides O(1) append and popleft, making it ideal for queues.

```python
from collections import deque

queue = deque()
queue.append("image_01.png")  # enqueue
queue.append("image_02.png")
queue.append("image_03.png")

front = queue.popleft()  # dequeue
print("Dequeued:", front)
print("Queue now:", list(queue))
```
@Pyodide.eval

#### How `popleft` Works

`popleft` removes the element at the **front (left side)** of the deque in O(1) time by moving an internal pointer—no elements are shifted like they would be in a list with `pop(0)`. That is why `deque` beats lists for queues.

```python
from collections import deque

q = deque(["first", "second", "third"])
print("Before:", list(q))
served = q.popleft()  # removes "first"
print("Served:", served)
print("After:", list(q))
```
@Pyodide.eval

**Quick tip:** use `appendleft` to push urgent items to the front, and still remove with `popleft`.

```python
from collections import deque

alerts = deque()
alerts.append("low")         # normal arrival
alerts.appendleft("urgent")  # push to front

print(alerts.popleft())  # "urgent"
print(alerts.popleft())  # "low"
```
@Pyodide.eval

**Bonus:** `deque` can act as a fixed-length rolling buffer. When `maxlen` is reached, new appends automatically drop items from the left (oldest)—effectively calling `popleft` for you.

```python
from collections import deque

recent_scores = deque(maxlen=3)
for score in [0.7, 0.8, 0.6, 0.9]:
    recent_scores.append(score)
    print(list(recent_scores))
# Output shows the oldest score disappearing as new scores arrive
```
@Pyodide.eval

**Quiz:** Which method removes the front element from a `deque` used as a queue?

[(X)] `popleft()`  
[( )] `pop()`  
[( )] `appendleft()`  
[( )] `clear()`  

---

### Thread-Safe Queues

When multiple threads are producing or consuming tasks, use `queue.Queue`, which handles locking for you.

```python
from queue import Queue

task_queue = Queue(maxsize=2)
task_queue.put("batch_1")
task_queue.put("batch_2")
print("Full?", task_queue.full())
print("Dequeued:", task_queue.get())
print("Remaining size:", task_queue.qsize())
```
@Pyodide.eval

---

### Applying Queues: Simple BFS

Breadth-first search visits neighbors layer by layer using a queue. Here we traverse an unweighted graph stored as an adjacency list.

```python
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs(start, graph):
    visited = set()
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        queue.extend(graph[node])
    return order

print("BFS from A:", bfs("A", graph))
```
@Pyodide.eval

---

## Performance Considerations

Choosing the right underlying container matters for speed and clarity.

| Operation / Structure      | List as Stack (`append`/`pop`) | List as Queue (`pop(0)`) | `collections.deque` | `queue.Queue` |
|----------------------------|-------------------------------|--------------------------|---------------------|---------------|
| Push/Enqueue (append)      | O(1) average                   | O(1) average             | O(1)                | O(1)          |
| Pop/Dequeue from front     | O(n) (shift all items)         | O(n)                     | O(1) `popleft()`    | O(1)          |
| Thread-safe                | No                             | No                       | No                  | Yes           |
| Typical uses               | Undo stacks, parsing           | Not recommended          | Task queues, BFS    | Producer/consumer, workers |

**Rule of thumb:** use lists for stacks, `deque` for queues, and `queue.Queue` when threads are involved.

---

## Activities

### Activity 1: Evaluate Postfix Expressions (Stack)

Complete the `evaluate_postfix` function so it can handle basic arithmetic operators using a stack.

```python
def evaluate_postfix(tokens):
    stack = []
    ops = {"+": lambda a, b: a + b,
           "-": lambda a, b: a - b,
           "*": lambda a, b: a * b,
           "/": lambda a, b: a / b}

    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(float(token))
    return stack.pop()

expr = "3 4 2 * 1 5 - 2 3 ^ ^ / +".split()
print("Result:", evaluate_postfix(expr[:5]))  # try with shorter slices first
```
@Pyodide.eval

**Your Turn:** Add error handling for empty stacks and unknown operators, then test with different expressions.

---

### Activity 2: Print Queue Simulation

Use a `deque` to simulate a printer queue that supports enqueueing jobs, serving them in order, and reporting the current queue.

```python
from collections import deque

def process_jobs(jobs):
    queue = deque(jobs)
    while queue:
        current = queue.popleft()
        print("Printing:", current)
    print("All jobs done.")

process_jobs(["report.pdf", "chart.png", "summary.docx"])
```
@Pyodide.eval

**Your Turn:** Extend the simulation with priorities by placing urgent jobs at the front using `appendleft`.

---

### Activity 3: Level-Order Traversal of a Binary Tree

Implement `level_order` to traverse a binary tree using a queue. Use `None` to represent missing children.

```python
from collections import deque

def level_order(tree):
    result = []
    queue = deque([0])  # start with index 0 (root)
    while queue:
        idx = queue.popleft()
        if idx >= len(tree) or tree[idx] is None:
            continue
        result.append(tree[idx])
        queue.append(2 * idx + 1)  # left child index
        queue.append(2 * idx + 2)  # right child index
    return result

tree = ["A", "B", "C", "D", None, "E", "F"]
print("Level order:", level_order(tree))
```
@Pyodide.eval

**Your Turn:** Modify the function to return nodes grouped by level (list of lists).

---

## Additional Resources

- [Python `collections.deque` Documentation](https://docs.python.org/3/library/collections.html#collections.deque)
- [Python `queue` Module Documentation](https://docs.python.org/3/library/queue.html)
- [Real Python Guide to Queues and Stacks](https://realpython.com/queue-in-python/)
- [Breadth-First Search Explanation](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

---

## Recap

@recap
