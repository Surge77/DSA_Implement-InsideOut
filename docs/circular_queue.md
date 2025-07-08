# 🔁 Circular Queue — Python (From Scratch)

A **Circular Queue** is a linear data structure that uses a fixed-size list in a circular fashion.  
It solves the performance issue of `O(n)` dequeues in normal queues by wrapping `front` and `rear` pointers.

---

## 🧠 Key Concepts

- **Fixed size**: All operations happen within a constant-size list
- **Efficient**: All operations are O(1) using pointer arithmetic
- **Real-world use**: CPU scheduling, buffers, caches, etc.

---

## 🧩 Supported Operations

| Method         | Description                        | Time Complexity |
|----------------|------------------------------------|-----------------|
| `enqueue()`    | Add value at the rear              | O(1)            |
| `dequeue()`    | Remove value from the front        | O(1)            |
| `peek()`       | Return front element (no removal)  | O(1)            |
| `__str__()`    | Print queue from front → rear      | O(n)            |
| `__len__()`    | Number of elements in queue        | O(1)            |
| `is_empty()`   | Check if queue is empty            | O(1)            |
| `is_full()`    | Check if queue is full             | O(1)            |

---

## 🧪 Example Usage

```python
from Linear.circular_queue import CircularQueue

q = CircularQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)         # Front → [10, 20, 30] ← Rear
print(q.peek())  # 10

q.dequeue()
q.enqueue(40)
print(q)         # Front → [20, 30, 40] ← Rear
