<!--
module_id: tree_traversal
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
comment: Learn fundamental tree searching algorithms including BFS and DFS, with interactive visualizations. Python example code is not provided in this module due to coursework.
long_description: This module introduces tree searching algorithms, fundamental techniques for finding specific elements in data collections. 
estimated_time_in_minutes: 35

@pre_reqs
Learners should be familiar with [Python basics including variables, functions, and methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#1), [lists and basic data structures](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1), and [loops and conditional statements](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_loops_conditionals/python_basics_loops_conditionals.md#1).
@end

@learning_objectives  
- Describe Breadth‑First Search (BFS), its level‑order exploration pattern, and its use for shortest‑path in unweighted graphs.
- Describe Depth‑First Search (DFS), its depth‑first exploration pattern, and its uses (pathfinding, cycle detection, traversals).
- Explain AVL tree properties (balance factor, rotations), how they guarantee O(log n) search/insert/delete.
- Use interactive visualisations to trace algorithm behaviour, debug implementations, and build intuition about performance and traversal order.

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

@end

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_python.md
import: ../module_templates/macros_algo_visualisations.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md
-->

# Tree Traversal Algorithms

@overview

## Attribution

@algo_attribution

## Introduction

Tree and graph traversal algorithms are essential tools in computer science for exploring and processing hierarchical data structures. Trees are widely used to represent relationships, organize data, and enable efficient searching and sorting. In this module, we focus on three key algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and AVL Trees.

You will learn the concepts behind each algorithm, see how they work, and use interactive visualisations to deepen your understanding. A Python code example is provided for DFS only.


## Depth-First Search (DFS)

**Depth-First Search** explores as far as possible along each branch before backtracking. DFS can be implemented using recursion or a stack, and is useful for tasks such as pathfinding, cycle detection, and topological sorting.

Because DFS can be implemented recursively, it is often simpler to code and understand compared to BFS. However, it can be less efficient in terms of memory usage for wide trees or graphs.

DFS will give *a* route to the target node, but not necessarily the shortest route.


### DFS Visualization

Let's see DFS in action:

The visualisation shows multiple possible ways of representing the graph structure.

- Adjacency List.

  - Often implemented a dictionary in Python where each key is a node and the value is a list of connected nodes.
  
- Adjacency Matrix
  
  - Often implemented as a 2D list in Python, the rows and columns represents potential edges, and a value in a given cell indicates whether an edge does exist between the nodes.

<div class="learn-more">

Adjacency matrix approaches can be faster from a performance perspective for dense graphs, but adjacency lists are more memory efficient for sparse graphs.
The issue is that an adjacency matrix grows quadratically $O(n^2)$ with the number of nodes, while an adjacency list grows linearly $O(n + e)$ with the number of edges.

Both approaches can be the correct one depending on the specific use case and graph characteristics.
</div>


This visualisation shows how DFS would search the entire graph.
If you were attempting to find a specific or check the existance of node with a specific value, you would add an additional check when visiting each node to see if it matches the target value, stopping the search if/when that value was found.

@algo_vis(LiaDFS)


### Python Example: DFS Traversal of a tree


BFS works the same way for trees as it does for graphs, since trees are a specific type of graph.

- Directed: edges have a direction (i.e. parent to child).
- Connected: there is a path between any two nodes (i.e. we can get to every node from the root).
- Acyclic: there are no cycles (i.e. we cannot revisit nodes, A -> B -> A -> B etc).

Because trees are acyclic, loops cannot happen and we do not need to keep track of visited nodes as we would for cyclic graphs.

------------------------

Below is a simple Python implementation of DFS for a tree for reference purposes.

This implementation uses class-based nodes and a recursive DFS function to traverse the tree.

- This approach is conceptually simple, but may not be suitable for very deep trees due to recursion limits in Python.
- Managing trees and graphs using class-based nodes can also have performance and memory considerations compared to using adjacency lists or matrices.

<section class="flex-container">
<div class="flex-child" style="min-width: 300px;">
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node):
    if node is None:
        return
    print(node.value)
    # recursively visit each child
    for child in node.children:
        dfs(child)

# Example usage:
# create nodes
a, b, c = Node('A'), Node('B'), Node('C')
d, e, f = Node('D'), Node('E'), Node('F')

# assign children
a.children = [b, c]
b.children = [d, e, f]

dfs(a)
# Output: A B D E F C
```
@Pyodide.eval

</div>

<div class="flex-child" style="min-width: 100px;max-width: 150px">

```ascii
           .-.
          ( A )
           .-.
          /   \
       .-.     .-. 
      ( B )   ( C )
       .-.     .-. 
      / \ \
     /   . \
    /    |  \ 
 .-.   .-.   .-. 
( D ) ( E ) ( F )
 .-.   .-.   .-. 
```

</div>

</section>

### Quiz: DFS

1. Which statement about Depth-First Search (DFS) is true?

  [( )] It always finds the shortest path.
  [(X)] It explores as far as possible along each branch before backtracking.
  [( )] It requires a queue to operate.
  [( )] It cannot be implemented recursively.
  ***
  <div class = "answer">
  DFS explores as far as possible along each branch before backtracking; it can be implemented recursively or with a stack.
  </div>
  ***

2. Which data structure is typically used to implement DFS?

   [(X)] Stack
   [( )] Queue
   [( )] Heap
   [( )] Linked List
   ***
   <div class = "answer">
   DFS is usually implemented using a stack (either explicitly or via recursion).
   </div>
   ***


## Breadth-First Search (BFS)

**Breadth-First Search** is an algorithm for traversing or searching tree (or graph) data structures. It explores all nodes at the present depth before moving on to nodes at the next depth level. 

BFS is commonly used for finding the shortest path in unweighted graphs and for level-order traversal of trees.

For weighted graphs BFS does not guarantee the shortest path, only the smallest number of edges.

<div class="important">
<b style="color: rgb(var(--color-highlight));">Important Note on Weighted Graphs</b><br>
If edge weight is an factor, then you would use Dijkstra's algorithm or A* search as these take edge weights into account when choosing the next node to explore.
</div>


### BFS Visualization

Let's see BFS in action:

As with DFS we can see the representation of the graph structure in multiple ways.

@algo_vis(LiaBFS)

### Quiz: BFS

1. Which data structure is typically used to implement BFS?
   
   [( )] Stack
   [(X)] Queue
   [( )] Heap
   [( )] Linked List
   ***
   <div class = "answer">
   BFS is usually implemented using a queue to keep track of nodes at the current depth.
   </div>
   ***

2. What is a common application of BFS?
   
   [(X)] Finding the shortest path in an unweighted graph
   [( )] Sorting a list
   [( )] Balancing a tree
   [( )] Hashing data
   ***
   <div class = "answer">
   BFS is commonly used to find the shortest path in unweighted graphs and for level-order traversal of trees.
   </div>
   ***


## AVL Trees

Adelson-Velsky and Landis (**AVL**) trees are self-balancing Binary Search Trees (BST), i.e:

- 0-2 children per node.
- Left child value < Parent value < Right child value.

The distinction from the standard BST is that they maintain a balance condition to ensure that the heights of the two child subtrees of any node differ by at most one. This guarantees $O(\log n)$ time complexity for search, insert, and delete operations.

Balanced trees like AVL trees are crucial for maintaining efficient performance in dynamic datasets where frequent insertions and deletions occur.
AVL trees are widely used in databases and file systems where fast lookups and updates are required.

### Balance

Balance is important for maintaining efficient operations in a binary search tree.

A balanced tree can be searched and modified in logarithmic time $O(\log n)$, while an unbalanced tree can degrade to linear time $O(n)$ in the worst case (e.g, when the tree becomes a degenerate tree resembling a linked list).

-----------------------------------

<section class="flex-container">
<div class="flex-child" style="min-width: 150px;max-width: 300px;">
**A balanced tree**

```ascii
           .--.
          ( 40 )
           .--.
          /    \
      .--.      .--.
     ( 20 )    ( 50 )
      .--.      .--.
     /    \         \ 
 .--.      .--.      .--.
( 10 )    ( 30 )    ( 60 )
 .--.      .--.      .--.
```
</div>

<div class="flex-child" style="min-width: 150px;max-width: 300px;">
**An unbalanced tree**

```ascii
           .--.
          ( 30 )
           .--.
          /    \
      .--.      .--.
     ( 20 )    ( 40 )
      .--.      .--.
     /              \
 .--.                .--. 
( 10 )              ( 60 )
 .--.                .--. 
                    /    
                .--. 
               ( 50 )
                .--. 
```
</div>
<div class="flex-child" style="min-width: 150px;max-width: 300px;">
**A degenerate tree**

```ascii
 .--.
( 10 )
 .--.
     \
      .--.
     ( 20 )
      .--.
          \
           .--. 
          ( 30 )
           .--. 
               \
                .--. 
               ( 40 )
                .--. 
                    \
                     .--. 
                    ( 50 )
                     .--. 
                         \
                          .--. 
                         ( 60 )
                          .--.
```
</div>
</section>


<div class="important">
<b style="color: rgb(var(--color-highlight));">Perfectly</b>

A tree does not need to have all layers fully filled to be considered balanced. 
The key requirement is that the heights of the two child subtrees of any node differ by at most one.

In the balanced example above, it would be possible to add an additional node under the '50' node without increasing the number of layers in the tree.

If a tree is filled completely on all layers, then it is referred to as a "perfectly balanced" tree.
</div>

---------------------

Tree balance can be determined using the balance factor of the tree and subtrees.

- Balance Factor: 
  
  - Left Subtree Height - Right Subtree Height
  - For an AVL tree, the balance factor must be -1, 0, or +1 for every node.
  - If the balance factor goes outside this range after an insertion or deletion, rotations are performed to restore balance.

- Subtree height: 
  
  - The number of nodes on the longest path from a given node to any leaf node in its subtree.

- Tree height: 
 
  - The number of nodes on the longest path from the root to any leaf node, i.e. the number of layers.

----------------------

<section class="flex-container">
<div class="flex-child" style="min-width: 150px;max-width: 300px;">
**A balanced tree**

*Balance factor is shown next to each node.*

```ascii
            .--.
          0( 40 )
            .--.
           /    \
       .--.      .--.
     0( 20 )  -1( 50 )
       .--.      .--.
      /    \         \ 
  .--.      .--.      .--.
0( 10 )   0( 30 )   0( 60 )
  .--.      .--.      .--.
```
</div>

<div class="flex-child" style="min-width: 150px;max-width: 300px;">
**An unbalanced tree**

*Note that node 40 has a balance factor of -2.*

```ascii
            .--.
         -1( 30 )
            .--.
           /    \
       .--.      .--.
     1( 20 )  -2( 40 )
       .--.      .--.
      /              \
  .--.                .--. 
0( 10 )             1( 60 )
  .--.                .--. 
                     /    
                 .--. 
               0( 50 )
                 .--. 
```
</div>
</section>



### Rotations

With AVL trees, when an insertion or deletion causes the tree to become unbalanced, as indicated by the balance factor, AVL trees perform rotations to restore balance. 

There are for possible imbalances depending on the balance factor of the node ($\text{bf}$) and it's left and right child balance factors ($\text{bfl}$ and $\text{bfr}$):

| Case | Condition | Rotation |
|------|-----------|-----------|
| Left-Left (LL)   | $\text{bf} \geq +2$ and $\text{bfl} \geq 0$ | Right |
| Right-Right (RR) | $\text{bf} \leq -2$ and $\text{bfr} \leq 0$ | Left |
| Left-Right (LR)  | $\text{bf} \geq +2$ and $\text{bfl} < 0$    | Left then Right |
| Right-Left (RL)  | $\text{bf} \leq -2$ and $\text{bfr} > 0$    | Right then Left |

----------------------------------

For LL and RR cases, a single rotation is sufficient to restore balance.

<section class="flex-container">
<div class="flex-child" style="min-width: 150px;">

**Left-Left (LL) example**

```ascii
            .--.      
          2( 30 )
            .--.
           /
       .--.
     1( 20 )
       .--.
      /
  .--. 
0( 10 )
  .--. 
```
</div>

<div class="flex-child" style="min-width: 150px;">

**Right Rotation**

```ascii
            .--.      
          2( 30 )
            .--.
           /
       .--.
     1( 20 ) <- Rotate 
       .--.     around
      /         this
  .--.          node
0( 10 )
  .--. 
```
</div>

<div class="flex-child" style="min-width: 150px;">

**After Right Rotation**

```ascii
       .--.           
     1( 20 )
       .--.
      /    \
  .--.      .--.
0( 10 )   0( 30 )
  .--.      .--.
```
</div>
</section>

For the Right-Right (RR) case, a Left Rotation is performed in a similar manner but in the opposite direction.

--------------------------

The Left-Right (LR) and Right-Left (RL) cases require a double rotation to restore balance.

Effectively we convert the LR or RL case into an LL or RR case, and then solve the new case as before.

<section class="flex-container">
<div class="flex-child" style="min-width: 150px;max-width: 300px;">

**Left-Right (LR) example**

<br>

```ascii
        .--.           
      2( 60 )
        .--.
       /
   .--.
-1( 40 )
   .--.
       \
        .--. 
      0( 50 )
        .--. 
```
</div>

<div class="flex-child" style="min-width: 150px;max-width: 300px;">

**Step 1: Left Rotation on left child**

*Tree is now a Left-Left (LL) case*

```ascii
            .--.      
          2( 60 )
            .--.
           /
       .--.
     1( 50 )
       .--. 
      /     
  .--.      
0( 40 )
  .--. 
```
</div>

<div class="flex-child" style="min-width: 150px;max-width: 300px;">

**Step 2: Right Rotation**

<br>

```ascii
       .--.           
     1( 50 )
       .--.
      /    \
  .--.      .--.
0( 40 )   0( 60 )
  .--.      .--.
```
</div>
</section>

-----------------------------------

<div class="cool-fact">
<b style="color: rgb(var(--color-highlight));">Alternatives</b><br>

AVL trees are one of several types of self-balancing binary search trees. Others include Red-Black Trees, Splay Trees, and B-Trees. Each has its own balancing strategies and performance characteristics.

AVL trees are one of the more strictly balanced options, which ensures that the tree is always optimally balanced but can be more computationally intensive during insertions and deletions compared to some alternatives like Red-Black Trees which allow for a bit more imbalance to reduce the number of rotations needed.
</div>


### AVL Tree Visualization

Let's see AVL trees in action:

@algo_vis(LiaAVLtree)


### Quiz: AVL Trees

1. What is the primary purpose of an AVL tree?

   [( )] To store data in a linear fashion
   [(X)] To maintain balance in a binary search tree for efficient operations
   [( )] To sort data in ascending order
   [( )] To implement a stack data structure
   ***
   <div class = "answer">
   The primary purpose of an AVL tree is to maintain balance in a binary search tree, ensuring efficient search, insert, and delete operations.
   </div>
   ***

2. What is the maximum allowed balance factor for any node in an AVL tree?

   [( )] 0
   [(X)] 1
   [( )] 2
   [( )] 3
   ***
   <div class = "answer">
   The maximum allowed balance factor for any node in an AVL tree is 1, meaning the heights of the two child subtrees can differ by at most one.
   </div>       
   ***

## Recap

@recap