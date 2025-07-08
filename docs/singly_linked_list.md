# 🔗 Singly Linked List — Python Implementation Guide

A **Singly Linked List** is a linear data structure where each element (node) points to the next. Unlike arrays, it does **not require contiguous memory** and allows **dynamic resizing**.

This document covers the implementation, operations, time complexities, and usage patterns for a custom `SinglyLinkedList` class built from scratch in Python.

---

## 🧱 Node Structure

Each node contains:
- `value`: The actual data
- `next`: Pointer to the next node (or `None`)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```