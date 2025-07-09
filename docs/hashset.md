# 🔹 HashSet (Custom Implementation)

Custom implementation of a HashSet using **separate chaining** (list of lists). No built-in `set` or `dict` used.

---

## 🔹 Class: `HashSet`

### 🧱 Core Components:
- Uses a list of buckets to store keys
- Keys are hashed to determine their bucket
- Resizing when load factor > 0.7
- All keys are unique

---

## 🔹 Methods

### `__init__(self, capacity: int = 8)`
Initializes the HashSet with a given capacity.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(n)

---

### `_hash(self, key: str) -> int`
Converts a string key into a valid bucket index.

- **Time Complexity:** O(len(key))  
- **Space Complexity:** O(1)

---

### `add(self, key: str) -> None`
Adds a key to the set if it does not already exist.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)

Triggers `_resize()` if load factor exceeds 0.7.

---

### `contains(self, key: str) -> bool`
Checks if a key is in the set.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)

---

### `remove(self, key: str) -> None`
Removes a key from the set.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)  
- **Raises:** KeyError if the key does not exist

---

### `__len__(self) -> int`
Returns the number of keys in the set.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(1)

---

### `__str__(self) -> str`
Returns a human-readable view of the set.

- **Example Output:** `HashSet → {'apple', 'banana'}`

---

### `_resize(self) -> None`
Doubles the capacity and rehashes all keys when load factor exceeds 0.7.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

## 🔹 Unit Testing

Tests are written in `/Tests/test_hashset.py`.

To run the tests:

```bash
python -m Tests.test_hashset
```

### ✅ Covered Test Cases:
- Adding and duplicate filtering (`add`)
- Checking key presence (`contains`)
- Removing keys (`remove`)
- Error on removing non-existent key
- Output formatting (`__str__`)
- Auto-resizing (`_resize`)

---
