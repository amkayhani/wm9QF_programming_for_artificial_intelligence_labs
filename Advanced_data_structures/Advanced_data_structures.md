<!--
module_id: data_structures
author:   Amir Kayhani
email:    amir.kayhani@warwick.ac.uk
version: 1.0.0
current_version_description: Initial version introducing queues, stacks, graphs, and trees in Python with code examples and visualisations.
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Data Structures in Python: Queues, Stacks, Graphs, and Trees

comment: Learn how to implement and use queues, stacks, graphs, and trees in Python for AI and data science applications.

long_description: This module introduces four fundamental data structures in computer science—queues, stacks, graphs, and trees—and shows how to implement and use them in Python. You will explore real-world applications in AI and data science, including search algorithms and hierarchical data modelling, and practice using these structures through interactive coding activities.

estimated_time_in_minutes: 60

@pre_reqs
Learners should be familiar with [Python basics including variables, functions, and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [lists and basic data structures](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), and [loops and conditional statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1).
@end

@learning_objectives

- Describe the core ideas behind queues, stacks, graphs, and trees.
- Implement queues and stacks in Python using built‑in data structures.
- Represent graphs using adjacency lists and traverse them using breadth‑first search (BFS) and depth‑first search (DFS).
- Implement simple tree structures in Python and perform basic traversals.
- Relate these data structures to AI and data science workflows, such as search and hierarchical modelling.

@end

good_first_module: false
collection: programming_for_ai
sequence_name: algorithms
coding_required: true
coding_level: intermediate
coding_language: python

@sets_you_up_for

- searching_algorithms
- sorting_algorithms
- data_structures_advanced
- algorithm_analysis

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
import: ../module_templates/macros_algo_visualisations.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Data Structures in Python: Queues, Stacks, Graphs, and Trees

@overview

In this module, you will learn four of the most important data structures in computer science and AI: **queues**, **stacks**, **graphs**, and **trees**.  
These structures appear everywhere—from scheduling tasks in operating systems, to exploring networks, to representing decision processes in AI models.

By the end of the module, you will be able to implement each structure in Python, understand how they work conceptually, and apply them to typical AI and data‑science problems such as search and hierarchical modelling.

---

## Lesson Preparation

@lesson_prep_python_pyodide

---

## 1. Queues in Python

### 1.1 What is a Queue?

A **queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle:

- The **first** element added is the **first** one removed.
- New elements are added at the **rear**, and elements are removed from the **front**.

Typical applications of queues:

- **Task scheduling** (e.g. jobs waiting to run on a CPU or GPU)
- **Breadth‑first search (BFS)** in graphs and trees
- **Buffers** in streaming systems or message queues

### 1.2 Implementing a Queue with `collections.deque`

Python’s `collections.deque` provides efficient appends and pops from both ends—perfect for implementing a queue.

```python
from collections import deque

# Create an empty queue
queue = deque()

# Enqueue (add to rear)
queue.append("task_1")
queue.append("task_2")
queue.append("task_3")
print("Queue after enqueuing:", queue)

# Dequeue (remove from front)
first_task = queue.popleft()
print("Dequeued:", first_task)
print("Queue now:", queue)
```
@Pyodide.eval

@info
Complexity snapshot:

- `append` – O(1)
- `popleft` – O(1)
@end

### 1.3 Queue Visualisation (Optional)

Use the visualisation below to see how a queue behaves.

@algo_vis(QueueArray)

### 1.4 Activity: Implementing a Simple Queue Class

Let’s wrap queue behaviour in a small class.

```python
from collections import deque

class SimpleQueue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data.popleft()

    def peek(self):
        if not self._data:
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

# Demo
q = SimpleQueue()
q.enqueue("A")
q.enqueue("B")
print("Front element:", q.peek())
print("Dequeued:", q.dequeue())
print("Is empty?", q.is_empty())
```
@Pyodide.eval

**Your Turn:**  
Extend `SimpleQueue` with a `size` method that returns the current number of elements.

---

## 2. Stacks in Python

### 2.1 What is a Stack?

A **stack** is another linear data structure, but it follows **Last In, First Out (LIFO)**:

- The **last** element added is the **first** one removed.
- Think of a stack of plates: you add and remove plates from the **top**.

Typical applications of stacks:

- **Function call stacks** in programming languages
- **Undo/redo** systems in editors
- **Depth‑first search (DFS)** in graphs and trees

### 2.2 Implementing a Stack with Lists

Python lists already support efficient operations at the end, so they work well as stacks.

```python
# Stack implemented with a list
stack = []

# Push elements
stack.append("home")
stack.append("search")
stack.append("results")
print("Stack after pushes:", stack)

# Pop the top element
last_page = stack.pop()
print("Popped:", last_page)
print("Stack now:", stack)
```
@Pyodide.eval

@info
Complexity snapshot:

- `append` – O(1) amortised
- `pop` (from end) – O(1)
@end

### 2.3 Activity: Stack Class and Balanced Brackets

Implement a small stack class and use it to solve a classic problem: checking whether brackets in an expression are balanced.

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0


def is_brackets_balanced(expression):
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


print(is_brackets_balanced("(2 + 3) * [4 - {5 / 2}]"))  # True
print(is_brackets_balanced("(2 + 3]"))                  # False
```
@Pyodide.eval

**Your Turn:**  
Modify `is_brackets_balanced` so it also ignores non‑bracket characters safely (e.g. letters, digits).

---

## 3. Graphs in Python

### 3.1 What is a Graph?

A **graph** is a collection of **nodes** (also called vertices) connected by **edges**.

- Nodes might represent people, web pages, or cities.
- Edges represent relationships: friendships, links, or roads.

Graphs are central in AI:

- **Knowledge graphs** represent relationships between entities.
- **Search problems** (e.g. shortest path) are modelled using graphs.
- **Social networks**, recommender systems, and more can be represented as graphs.

We will represent graphs using an **adjacency list**: a dictionary mapping each node to a list of neighbours.

```python
# Undirected graph represented as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

print(graph["A"])  # Neighbours of A
```
@Pyodide.eval

### 3.2 Graph Visualisations

Use these visualisations to get an intuition for how graph algorithms behave.

#### Breadth‑First Search (BFS)

@algo_vis(LiaBFS)

#### Depth‑First Search (DFS)

@algo_vis(LiaDFS)

### 3.3 BFS in Python

**Breadth‑First Search (BFS)** explores a graph level by level using a queue.  
It is often used to find the shortest path in an unweighted graph.

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
    return order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

print("BFS from A:", bfs(graph, "A"))
```
@Pyodide.eval

### 3.4 DFS in Python

**Depth‑First Search (DFS)** explores as far as possible down one path before backtracking.  
DFS can be implemented using recursion or an explicit stack.

```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)
    return order


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

print("DFS from A:", dfs(graph, "A"))
```
@Pyodide.eval

**Your Turn:**  
Adapt the BFS code to compute the shortest number of steps from `start` to every other node in the graph.

---

## 4. Trees in Python

### 4.1 What is a Tree?

A **tree** is a special kind of graph with no cycles:

- One node is designated as the **root**.
- Every other node has exactly one **parent**.
- Trees naturally represent **hierarchies**: file systems, organisation charts, game decision trees, etc.

A **binary tree** is a tree where each node has at most two children: `left` and `right`.

### 4.2 Tree Visualisation

Use the binary search tree visualisation to see insertions and traversals.

@algo_vis(LiaBST)

### 4.3 Implementing a Simple Binary Tree

We will define a small `TreeNode` class and then build a simple tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Build a small tree
root = TreeNode("A",
                left=TreeNode("B",
                              left=TreeNode("D"),
                              right=TreeNode("E")),
                right=TreeNode("C",
                               right=TreeNode("F")))
```
@Pyodide.eval

### 4.4 Tree Traversals

We will implement three standard **depth‑first** traversals:

- **Pre‑order**: visit node → left → right
- **In‑order**: visit left → node → right
- **Post‑order**: visit left → right → node

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


root = TreeNode("A",
                left=TreeNode("B",
                              left=TreeNode("D"),
                              right=TreeNode("E")),
                right=TreeNode("C",
                               right=TreeNode("F")))

print("Pre‑order: ", preorder(root))
print("In‑order:  ", inorder(root))
print("Post‑order:", postorder(root))
```
@Pyodide.eval

### 4.5 Trees, Search, and AI

Trees are used extensively in AI:

- **Game trees** for planning moves (e.g. chess engines).
- **Decision trees** for classification and regression.
- **Search trees** (like those used in heuristic search algorithms).

Often, AI algorithms explore or build trees dynamically, using **BFS** or **DFS** over the tree structure.

**Your Turn:**  
Modify the `TreeNode` class to include a `__repr__` method that returns a helpful string representation of a node (e.g. `"TreeNode(value='A')"`) to make debugging easier.

---

## 5. Summary and Next Steps

In this module, you have:

- Implemented **queues** and **stacks** in Python and seen how they support FIFO and LIFO behaviour.
- Represented **graphs** via adjacency lists and traversed them using **BFS** and **DFS**.
- Built and traversed simple **binary trees**, connecting them to AI concepts such as search and decision structures.

These data structures underpin many advanced AI techniques. As a next step, explore:

- `searching_algorithms` for more detail on search strategies.
- `sorting_algorithms` to understand how ordered data interacts with these structures.
- `data_structures_advanced` for richer visualisations and more complex variations.

---

## Recap

@recap

---
