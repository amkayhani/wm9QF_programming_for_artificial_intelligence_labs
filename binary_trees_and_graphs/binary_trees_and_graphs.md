<!--
module_id: binary_trees_and_graphs
author: Amir Kayhani
email: amir.kayhani@warwick.ac.uk
version: 1.0.0
current_version_description: Initial version covering binary trees and graphs with Python examples, quizzes, and AI-focused activities.
module_type: standard
docs_version: 1.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Data Structures: Binary Trees and Graphs

comment: Learn how to represent, traverse, and search binary trees and graphs in Python.

long_description: This module introduces binary trees and graphs, two core data structures that underpin search, pathfinding, and hierarchical modelling in AI. You will build these structures in Python, run key traversals, and connect them to real-world AI applications through quizzes and coding activities.

estimated_time_in_minutes: 60

@pre_reqs
Learners should be comfortable with [Python functions and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [lists and dictionaries](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), and [loops and conditionals](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1).
@end

@learning_objectives

- Explain binary tree terminology (root, leaf, depth, height) and graph terminology (nodes, edges, degree, connectivity).
- Traverse binary trees using pre-order, in-order, post-order, and level-order.
- Implement a binary search tree (BST) with insert and search operations.
- Represent graphs using adjacency lists and matrices, then traverse them with BFS and DFS.
- Apply graph algorithms (shortest paths and topological ordering) to AI-related scenarios.

@end

good_first_module: false
collection: programming_for_ai
sequence_name: data_structures
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

# Data Structures: Binary Trees and Graphs

@overview

Binary trees and graphs are the backbone of many AI systems.  
Trees capture hierarchies (decision trees, game trees), while graphs capture relationships (knowledge graphs, routing, social networks).  
In this module, you will learn how to represent, traverse, and search these structures in Python, with activities that mirror how they are used in AI and data science.

---

## Lesson Preparation

@lesson_prep_python_pyodide

---

## 1. Binary Trees

### 1.1 Terminology and Shape

A **binary tree** is a hierarchical structure where each node has at most two children, commonly called `left` and `right`.

- **Root**: topmost node.
- **Leaf**: node with no children.
- **Depth**: edges from the root to a node.
- **Height**: longest path from a node to a leaf.
- **Balanced vs. skewed**: balanced trees keep height small; skewed trees behave like linked lists.

Binary trees appear in AI as **decision trees**, **game trees**, and as the structure behind **binary search trees (BSTs)** that speed up lookups.

### 1.2 Building a Simple Binary Tree

We start with a lightweight `TreeNode` class and create a small tree.

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Build a small tree by hand
root = TreeNode("A",
                left=TreeNode("B",
                              left=TreeNode("D"),
                              right=TreeNode("E")),
                right=TreeNode("C",
                               right=TreeNode("F")))

print("Root:", root.value)
print("Left child of A:", root.left.value)
print("Right child of B:", root.left.right.value)
```
@Pyodide.eval

### 1.3 Depth-First Traversals (DFS on Trees)

Depth-first traversals visit every node without skipping branches. The three classic orders differ in when they process the current node:

- **Pre-order**: node -> left -> right
- **In-order**: left -> node -> right (sorted order for BSTs)
- **Post-order**: left -> right -> node

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

# Build a small tree
root = TreeNode("A",
                left=TreeNode("B",
                              left=TreeNode("D"),
                              right=TreeNode("E")),
                right=TreeNode("C",
                               right=TreeNode("F")))

print("Pre-order:", preorder(root))
print("In-order:", inorder(root))
print("Post-order:", postorder(root))
```
@Pyodide.eval

**Quiz:** Which traversal is guaranteed to return values in sorted order for a valid BST?

[(X)] In-order  
[( )] Pre-order  
[( )] Post-order  
[( )] Reverse level-order  

---

### 1.4 Breadth-First Traversal (Level-Order)

Breadth-first traversal visits nodes level by level. It uses a queue to track which nodes to process next.

```python
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root):
    if root is None:
        return []

    order = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order

# Build a small tree
root = TreeNode("A",
                left=TreeNode("B",
                              left=TreeNode("D"),
                              right=TreeNode("E")),
                right=TreeNode("C",
                               right=TreeNode("F")))

print("Level-order:", level_order(root))
```
@Pyodide.eval

**Your Turn:** Modify `level_order` to return a list of lists (one list per level) so you can see the tree layer by layer.

---

### 1.5 Binary Search Trees (BSTs)

A **BST** keeps the tree ordered: every node's left subtree contains smaller values, and its right subtree contains larger values.  
This invariant allows average-case `O(log n)` search, insert, and delete on balanced trees.

```python
class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BSTNode(key)
        elif key > self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right = BSTNode(key)
        # Duplicates are ignored for simplicity

    def search(self, key):
        if key == self.key:
            return True
        if key < self.key and self.left:
            return self.left.search(key)
        if key > self.key and self.right:
            return self.right.search(key)
        return False

    def inorder(self):
        left = self.left.inorder() if self.left else []
        right = self.right.inorder() if self.right else []
        return left + [self.key] + right

# Demo
bst = BSTNode(50)
for value in [30, 70, 20, 40, 60, 80]:
    bst.insert(value)

print("BST in-order (sorted):", bst.inorder())
print("Search 60:", bst.search(60))
print("Search 25:", bst.search(25))
```
@Pyodide.eval

**Quiz:** Why can searching a balanced BST run in `O(log n)`?

[(X)] Each comparison halves the remaining search space.  
[( )] It scans all nodes once.  
[( )] It always follows the left subtree.  
[( )] It sorts the tree before every search.  

---

### 1.6 Trees and AI Workflows

- **Decision trees**: split feature space to classify or regress.  
- **Random forests** and **gradient boosted trees**: ensembles of decision trees.  
- **Game AI**: minimax search explores a game tree with pruning.  
- **Heuristic search**: A* and BFS often operate over tree-like expansions of states.

**Your Turn:** Extend `BSTNode` with a `find_min` method that returns the smallest key, then use it to implement a simple delete operation for a leaf node.

---

## 2. Graphs

### 2.1 Graph Vocabulary

A **graph** is a set of nodes (vertices) connected by edges.

- **Directed vs. undirected**: edges may have direction.  
- **Weighted vs. unweighted**: edges may carry costs.  
- **Degree**: number of edges incident on a node.  
- **Path and cycle**: sequences of edges that connect nodes; a cycle starts and ends at the same node.  
- **Connected components**: subsets of nodes that are mutually reachable.

Graphs power AI systems such as **knowledge graphs**, **recommender systems**, **routing**, and **influence modelling**.

### 2.2 Representing Graphs in Python

#### Adjacency List (common for sparse graphs)

```python
# Undirected graph as adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

print("Neighbors of A:", graph["A"])
```
@Pyodide.eval

#### Adjacency Matrix (useful for dense graphs)

```python
# Nodes in a fixed order
nodes = ["A", "B", "C", "D"]
index = {node: i for i, node in enumerate(nodes)}

# 0 = no edge, 1 = edge present
adj_matrix = [
    [0, 1, 1, 0],  # A connected to B, C
    [1, 0, 0, 1],  # B connected to A, D
    [1, 0, 0, 1],  # C connected to A, D
    [0, 1, 1, 0],  # D connected to B, C
]

print("Edge A-D?", bool(adj_matrix[index["A"]][index["D"]]))
```
@Pyodide.eval

**Quiz:** For a sparse graph with thousands of nodes but relatively few edges, which representation is typically more memory efficient?

[(X)] Adjacency list  
[( )] Adjacency matrix  
[( )] Both are equal  
[( )] Neither; use a linked list  

---

### 2.3 Breadth-First Search (BFS)

**BFS** explores level by level using a queue. It finds shortest paths in **unweighted** graphs.

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
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
    return order

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

print("BFS from A:", bfs(graph, "A"))
```
@Pyodide.eval

@algo_vis(LiaBFS)

**Your Turn:** Adapt `bfs` to return the shortest number of edges from `start` to every other node (a distance map).

---

### 2.4 Depth-First Search (DFS)

**DFS** explores as far as possible down each branch before backtracking.  
It can be implemented with recursion or an explicit stack.

```python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

print("DFS from A:", dfs(graph, "A"))
```
@Pyodide.eval

@algo_vis(LiaDFS)

**Quiz:** When would DFS be preferred over BFS?

[( )] When you need shortest paths in an unweighted graph.  
[(X)] When exploring deep paths matters (e.g. backtracking search).  
[( )] When memory must stay minimal and graph is dense.  
[( )] When all edges have weights.  

---

### 2.5 Shortest Paths in Weighted Graphs (Dijkstra)

For **weighted** graphs with non-negative edge costs, Dijkstra's algorithm finds shortest paths efficiently using a priority queue.

```python
import heapq

def dijkstra(graph, start):
    # graph: node -> list of (neighbor, weight)
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

weighted_graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("A", 4), ("D", 1)],
    "C": [("A", 1), ("D", 5), ("E", 8)],
    "D": [("B", 1), ("C", 5), ("E", 3)],
    "E": [("C", 8), ("D", 3)]
}

print("Shortest distances from A:", dijkstra(weighted_graph, "A"))
```
@Pyodide.eval

**Quiz:** Which requirement must hold for Dijkstra's algorithm to produce correct results?

[(X)] Edge weights must be non-negative.  
[( )] The graph must be a tree.  
[( )] All edges must have the same weight.  
[( )] The graph must be fully connected.  

---

### 2.6 Directed Acyclic Graphs (DAGs) and Topological Order

Many AI workflows (e.g. data pipelines, neural network layers) can be viewed as DAGs. A **topological order** processes nodes so every edge goes from earlier to later nodes.

```python
from collections import defaultdict, deque

def topological_sort(edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for src, dst in edges:
        graph[src].append(dst)
        indegree[dst] += 1
        indegree.setdefault(src, 0)

    queue = deque([node for node, deg in indegree.items() if deg == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(indegree):
        raise ValueError("Graph has a cycle; topological order impossible.")
    return order

edges = [
    ("ingest", "clean"),
    ("clean", "feature_engineering"),
    ("feature_engineering", "train_model"),
    ("train_model", "evaluate")
]

print("Topological order:", topological_sort(edges))
```
@Pyodide.eval

---

## 3. Trees vs. Graphs: Connecting the Dots

- Every tree is a graph with no cycles; many graph algorithms (BFS/DFS) apply directly.  
- Level-order traversal on a tree is BFS on a graph.  
- A BST is a tree that encodes ordering, while a general graph has no inherent ordering.  
- AI systems often move between both: a decision tree (tree) may become part of a knowledge graph (graph) that links decisions to outcomes or data sources.

**Activity:** Write a function `tree_to_adjacency(root)` that walks a binary tree and returns an adjacency list representing it as an undirected graph.

---

## 4. Practice Activities

1. **BST delete with tests**  
   - Implement `delete(key)` for the three cases: leaf, one child, two children (replace with inorder successor).  
   - Use `find_min` to fetch the smallest node in a subtree.  
   - Fill the blanks below, then run the script to verify sorted in-order after each delete.
```python
class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key, self.left, self.right = key, left, right

    def insert(self, key):
        if key < self.key:
            self.left = self.left.insert(key) if self.left else BSTNode(key)
        elif key > self.key:
            self.right = self.right.insert(key) if self.right else BSTNode(key)
        return self

    def find_min(self):
        return self.left.find_min() if self.left else self

    def delete(self, key):
        if key < self.key:
            # TODO: recurse into left
            ...
        elif key > self.key:
            # TODO: recurse into right
            ...
        else:
            # TODO: handle 0, 1, 2 child cases
            ...
        return self

    def inorder(self):
        left = self.left.inorder() if self.left else []
        right = self.right.inorder() if self.right else []
        return left + [self.key] + right

root = BSTNode(50)
for v in [30, 70, 20, 40, 60, 80]:
    root.insert(v)

for delete_key in [20, 30, 50]:
    root = root.delete(delete_key)
    print(f"After deleting {delete_key}:", root.inorder())
```
@Pyodide.eval

2. **BFS distances and path reconstruction**  
   - Extend BFS to return both `distance` and `parent` maps.  
   - Complete `reconstruct_path` to walk parents backward to the start.
```python
from collections import deque

def bfs_with_parent(graph, start):
    dist = {start: 0}
    parent = {start: None}
    q = deque([start])
    while q:
        node = q.popleft()
        for nbr in graph.get(node, []):
            if nbr not in dist:
                dist[nbr] = dist[node] + 1
                parent[nbr] = node
                q.append(nbr)
    return dist, parent

def reconstruct_path(parent, start, target):
    # TODO: walk backward from target to start using parent map
    ...

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"]
}

dist, parent = bfs_with_parent(graph, "A")
print("Distances from A:", dist)
print("Path A -> E:", reconstruct_path(parent, "A", "E"))
print("Path C -> E:", reconstruct_path(*bfs_with_parent(graph, "C"), start="C", target="E"))
```
@Pyodide.eval


3. **Cycle detection in an undirected graph**  
   - Implement `has_cycle(graph)` using DFS with a `parent` parameter.
```python
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                if dfs(nbr, node):
                    return True
            elif nbr != parent:
                return True  # found a back-edge
        return False

    for node in graph:
        if node not in visited and dfs(node, None):
            return True
    return False

tree_graph = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
cycle_graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
print("Tree has cycle?", has_cycle(tree_graph))   # Expected: False
print("Triangle has cycle?", has_cycle(cycle_graph))  # Expected: True
```
@Pyodide.eval
   - TODO: replace the comments and verify outputs.


4. **Probabilistic paths via negative logs**  
   - Treat edge weights as probabilities `p`; convert to costs `-log(p)` to reuse Dijkstra.  
   - Complete the TODOs to compute the most likely path.
```python
import heapq, math

def most_likely_path(graph, start):
    dist = {start: 0.0}  # stores -log(prob)
    parent = {start: None}
    pq = [(0.0, start)]
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for nbr, p in graph[node]:
            step = -math.log(p)
            new_cost = cost + step
            if new_cost < dist.get(nbr, float("inf")):
                dist[nbr] = new_cost
                parent[nbr] = node
                heapq.heappush(pq, (new_cost, nbr))
    return dist, parent

def path_and_prob(parent, dist, start, target):
    # TODO: rebuild path from parent map, then convert dist[target] back with exp(-cost)
    ...

prob_graph = {
    "A": [("B", 0.9), ("C", 0.5)],
    "B": [("D", 0.6)],
    "C": [("D", 0.95)],
    "D": []
}

dist, parent = most_likely_path(prob_graph, "A")
print(path_and_prob(parent, dist, "A", "D"))  # Expected path A -> C -> D with higher probability
```
@Pyodide.eval

5. **Level-order by levels**  
   - Upgrade `level_order` to return a list of lists (nodes per depth).
```python
from collections import deque

def level_order_levels(root):
    if root is None:
        return []
    levels = []
    q = deque([root])
    while q:
        size = len(q)
        current = []
        for _ in range(size):
            node = q.popleft()
            current.append(node.value)
            if node.left:  # TODO: enqueue left child
                ...
            if node.right:  # TODO: enqueue right child
                ...
        levels.append(current)
    return levels
```
@Pyodide.eval
   - For the sample tree, aim for `[['A'], ['B', 'C'], ['D', 'E', 'F']]`.


---

## Additional Resources

- [Binary Trees (Python docs tutorial section)](https://docs.python.org/3/library/tree.html)  
- [Graphs in NetworkX](https://networkx.org/documentation/stable/tutorial.html)  
- [Decision Trees for ML (scikit-learn)](https://scikit-learn.org/stable/modules/tree.html)  
- [LiaScript Algorithm Visualisations](https://liascript.github.io/course/?https://raw.githubusercontent.com/LiaScript/docs/master/README.md#1)  

---

## Recap

@recap

---
