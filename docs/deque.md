# 🔁 Deque (Double-Ended Queue)

A **Deque** (Double-Ended Queue) is a linear data structure that allows **insertion and deletion from both ends** — front and rear. It’s extremely flexible and commonly used in problems involving sliding windows, palindromes, and backtracking.

---

## 📦 Implementation Details

This custom Deque is implemented from scratch using a **doubly linked list** for O(1) operations at both ends.

---

## ✅ Supported Operations

| Method            | Description                           | Time Complexity |
|-------------------|----------------------------------------|-----------------|
| `append_left()`   | Add element to front                   | O(1)            |
| `append_right()`  | Add element to rear                    | O(1)            |
| `pop_left()`      | Remove and return element from front   | O(1)            |
| `pop_right()`     | Remove and return element from rear    | O(1)            |
| `peek_left()`     | Get front element without removing     | O(1)            |
| `peek_right()`    | Get rear element without removing      | O(1)            |
| `__len__()`       | Return current size of deque           | O(1)            |
| `is_empty()`      | Check if deque is empty                | O(1)            |
| `__str__()`       | Visualize deque from front to rear     | O(n)            |

---

## 🧪 Example Usage

```python
from Linear.deque import Deque

dq = Deque()
dq.append_left(10)
dq.append_right(20)
dq.append_left(5)

print(dq)            # Front → [5, 10, 20] ← Rear
print(dq.pop_right())  # 20
print(dq.peek_left())  # 5
print(len(dq))         # 2
