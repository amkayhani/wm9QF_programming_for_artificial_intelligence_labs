<!--
module_id: data_structures_advanced/vis_demo
author:   Amir Kayhani
email:    Amir.kayhani@warwick.ac.uk
version: 0.0.1
current_version_description: Initial version
module_type: standard
docs_version: 2.0.0
language: en
narrator: UK English Female
mode: Textbook
title: data_structures_advanced/vis_demo
comment:  A demo of visualisations for algorithms
estimated_time_in_minutes: 20

link:  ../assets/styles.css
import: ../module_templates/macros.md
import: ../module_templates/macros_algo_visualisations.md
import: ../module_templates/macros_python.md
import: https://dscroft.github.io/Pyodide/README.md
import: https://github.com/LiaScript/CodeRunner/blob/master/README.md

-->

# Attribution

@algo_attribution



# Queues in Python

Queues are a fundamental data structure in computer science, used in various applications such as task scheduling, breadth-first search, and buffering. This section provides a comprehensive guide to understanding, implementing, and applying queues in Python. It includes explanations, Python code examples, diagrams, and exercises to solidify your understanding.

---

## 1. Introduction to Queues

A queue is a linear data structure that follows the First In First Out (FIFO) principle. The element added first is the one to be removed first. Queues are widely used in scenarios where order needs to be preserved.

### Key Operations:
- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove an element from the front of the queue.
- **Peek**: View the front element without removing it.
- **isEmpty**: Check if the queue is empty.

### Real-World Applications:
- Task scheduling in operating systems.
- Breadth-first search in graph algorithms.
- Managing requests in web servers.

---

## 2. Implementing Queues in Python

### Using Lists
Python lists can mimic a queue for small workloads or quick prototypes, but removing from the front is costly because every remaining element must shift left. This makes lists useful for teaching FIFO behaviour, while highlighting why specialised queue types exist for production code.

**How the walkthrough progresses**
1. Begin with an empty list.
2. Append three numbers, so the queue becomes `[1, 2, 3]`.
3. Dequeue with `pop(0)`, which shifts the remaining numbers left; the queue now holds `[2, 3]`.
4. Print statements confirm both the dequeued value and the final state that the diagram illustrates.

@info Complexity snapshot
- Enqueue via `append(...)` is amortised `O(1)`.
- Dequeue via `pop(0)` is `O(n)` because of element shifting.
- Peek with `queue[0]` would be `O(1)`.

```python
# Queue implemented with a Python list (educational example).
queue = []

# Enqueue three items (FIFO order of arrival).
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueuing:", queue)

# Dequeue the oldest item (expensive O(n) operation).
removed = queue.pop(0)
print("Dequeued element:", removed)
print("Queue after dequeuing:", queue)
```
@Pyodide.eval

![Visualization of Queue Operations Using Lists](../assets/media/queues/queue_list.svg)

### Using `collections.deque`
The `deque` class from the `collections` module is optimized for fast appends and pops from both ends.

```python
from collections import deque

# Queue implementation using deque
queue = deque()

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueuing:", queue)

# Dequeue
print("Dequeued element:", queue.popleft())
print("Queue after dequeuing:", queue)
```
@Pyodide.eval

![Visualization of Queue Operations Using deque](../assets/media/queues/queue_deque.svg)

### Using `queue.Queue`
The `queue.Queue` class is thread-safe and suitable for multi-threaded applications.

```python
from queue import Queue

# Queue implementation using queue.Queue
queue = Queue()

# Enqueue
queue.put(1)
queue.put(2)
queue.put(3)
print("Queue size:", queue.qsize())

# Dequeue
print("Dequeued element:", queue.get())
print("Queue size after dequeuing:", queue.qsize())
```
@Pyodide.eval

![Visualization of Queue Operations Using queue.Queue](../assets/media/queues/queue_queue_module.svg)

---

## 3. Types of Queues

### 3.1 Simple Queue
A basic FIFO queue. Suitable for scenarios requiring strict order.

```python
from collections import deque

class SimpleQueue:
    def __init__(self):
        self._q = deque()

    def enqueue(self, item):
        self._q.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._q.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._q[0]

    def is_empty(self):
        return len(self._q) == 0

# Demo
sq = SimpleQueue()
sq.enqueue(10)
sq.enqueue(20)
print("Front element:", sq.peek())
print("Dequeued element:", sq.dequeue())
```
@Pyodide.eval

![Visualization of Simple Queue Operations](../assets/media/queues/simple_queue.svg)

### 3.2 Circular Queue

A circular queue is a linear data structure that connects the last position back to the first position to form a circle. This structure is particularly useful for scenarios where memory needs to be utilized efficiently, such as in buffering and scheduling tasks. Unlike a regular queue, which operates in a strictly linear fashion, the circular queue wraps around, making it a more memory-efficient option in constrained environments.

![Circular Queue Illustration](https://angelvyas.com/posts/data_structures/images/cirq.jpg)

*Image Source: [Angel Vyas - Circular Queue](https://angelvyas.com/posts/data_structures/circularq/)*

#### Key Features:
- **Efficient Memory Usage**: Unlike a simple queue, a circular queue reuses empty spaces created by dequeuing elements. This ensures that no memory is wasted, especially in scenarios where the queue is frequently updated.
- **Fixed Size**: Circular queues are often implemented with a fixed size, making them suitable for hardware-level applications where memory constraints are critical. For example, embedded systems often use circular queues to manage tasks efficiently.

**Question:**
Which of the following scenarios best demonstrates the advantage of a circular queue's efficient memory usage?

@Pyodide.eval

[( )] A queue where elements are added and removed in a strictly sequential order.
[(X)] A queue where elements are frequently dequeued and enqueued, creating empty spaces.
[( )] A queue that dynamically resizes itself when full.
[( )] A queue used in a stack-based memory allocation system.
***
<div class="answer">
Circular queues reuse empty spaces created by dequeuing elements, making them ideal for scenarios with frequent enqueue and dequeue operations.
</div>
***

#### Operations:
- **Enqueue**: Add an element to the rear of the queue. If the queue is full, the operation cannot proceed, and an overflow condition is raised.
- **Dequeue**: Remove an element from the front of the queue. If the queue is empty, the operation cannot proceed, and an underflow condition is raised.
- **isFull**: Check if the queue is full. This operation is crucial for ensuring that no additional elements are added beyond the queue's capacity.
- **isEmpty**: Check if the queue is empty. This operation helps in determining whether there are any elements to process.

**Question:**
What is the time complexity of the `enqueue` operation in a circular queue implemented using an array?

@Pyodide.eval

[( )] O(n)
[( )] O(log n)
[(X)] O(1)
[( )] O(n^2)
***
<div class="answer">
The `enqueue` operation in a circular queue has a time complexity of O(1) because it involves a simple arithmetic operation to update the rear pointer and insert the element.
</div>
***

#### Python Implementation:
```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            raise OverflowError("Queue is full")
        elif self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:  # Single element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear >= self.front:
            print("Queue:", self.queue[self.front:self.rear + 1])
        else:
            print("Queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

# Demo
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
print("Dequeued:", cq.dequeue())
cq.display()
```
@Pyodide.eval

**Question:**
In the given Python implementation of a circular queue, what will happen if the `dequeue` method is called on an empty queue?

@Pyodide.eval

[( )] It will return `None`.
[( )] It will remove the last element in the queue.
[(X)] It will raise an `IndexError`.
[( )] It will reset the `front` and `rear` pointers to -1.
***
<div class="answer">
Calling `dequeue` on an empty queue raises an `IndexError` because the `front` pointer is set to -1, indicating that the queue is empty.
</div>
***

#### Applications of Circular Queues:
- **Task Scheduling**: Circular queues are used in round-robin scheduling algorithms. These algorithms allocate a fixed time slice to each task, ensuring fairness and efficient CPU utilization.
- **Buffering**: Used in scenarios like streaming data where a fixed-size buffer is required. For instance, audio and video streaming applications use circular queues to manage data packets efficiently.
- **Traffic Management**: Circular queues help in managing traffic signals efficiently. By cycling through signals in a fixed order, circular queues ensure smooth traffic flow and reduce congestion.
- **Data Mining and AI**: Circular queues are used in sliding window algorithms, which are essential for processing streaming data. For example, in real-time anomaly detection or predictive modeling, a circular queue can maintain a fixed-size window of the most recent data points for analysis. Another example is in natural language processing (NLP), where circular queues can be used to manage a rolling context window for tasks like sentiment analysis or text summarization.

**Question:**
A video streaming service uses a circular queue to buffer data packets. If the buffer size is 10 packets and the service receives 15 packets, what happens to the first 5 packets?

@Pyodide.eval

[( )] They are processed immediately.
[( )] They are stored in a secondary buffer.
[(X)] They are overwritten by the new packets.
[( )] They are sent back to the sender.
***
<div class="answer">
In a circular queue, when the buffer is full, new data overwrites the oldest data. Thus, the first 5 packets are overwritten by the new packets.
</div>
***

**Question:**
In a traffic management system, a circular queue is used to manage traffic signals. If there are 4 signals (A, B, C, D) and the queue starts at A, what will be the order of signals after 3 cycles?

@Pyodide.eval

[( )] A, B, C, D, A, B, C, D, A, B, C, D
[(X)] A, B, C, D, A, B, C, D, A, B, C, D
[( )] D, C, B, A, D, C, B, A, D, C, B, A
[( )] A, D, C, B, A, D, C, B, A, D, C, B
***
<div class="answer">
In a circular queue, the order of elements remains consistent as the queue cycles through. After 3 cycles, the order of signals will still be A, B, C, D repeated three times.
</div>
***

**Question:**
A machine learning model uses a sliding window algorithm with a circular queue to process streaming data. If the window size is 5 and the queue currently holds [10, 20, 30, 40, 50], what happens when a new data point (60) is added?

@Pyodide.eval

[( )] The queue expands to hold 6 elements.
[( )] The queue discards all elements and starts fresh with [60].
[(X)] The oldest element (10) is removed, and the queue becomes [20, 30, 40, 50, 60].
[( )] The queue raises an overflow error.
***
<div class="answer">
In a sliding window algorithm using a circular queue, adding a new element when the queue is full removes the oldest element to maintain the fixed window size. The queue becomes [20, 30, 40, 50, 60].


