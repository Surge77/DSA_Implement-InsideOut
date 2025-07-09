# 🔹 HashMap (Custom Implementation)

Custom implementation of a HashMap using **separate chaining** (list of lists). No built-in `dict` or `set` used.

---

## 🔹 Class: `HashMap`

### 🧱 Core Components:
- Fixed-size array (`buckets`) of lists to handle collisions.
- Polynomial rolling hash function.
- Auto-resizing when load factor exceeds 0.7.

---

## 🔹 Methods

### `__init__(self, capacity: int = 8)`
Initializes the HashMap with given capacity.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(n), where n = capacity

---

### `_hash(self, key: str) -> int`
Custom hash function to map string key to an array index.

- **Time Complexity:** O(len(key))  
- **Space Complexity:** O(1)

---

### `put(self, key: str, value: any) -> None`
Inserts or updates the key-value pair.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)

Triggers `_resize()` if load factor > 0.7.

---

### `get(self, key: str) -> any`
Retrieves value associated with the key.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)

Raises `KeyError` if key is not found.

---

### `remove(self, key: str) -> None`
Deletes the key-value pair.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)

Raises `KeyError` if key is not found.

---

### `contains(self, key: str) -> bool`
Checks whether key exists in HashMap.

- **Time Complexity:** O(n/k)  
- **Space Complexity:** O(1)
---

### `__len__(self) -> int`
Returns the number of key-value pairs.

- **Time Complexity:** O(1)  
- **Space Complexity:** O(1)

---

### `__str__(self) -> str`
Returns a human-readable representation.

- **Example Output:** `HashMap → {'name': 'Alice', 'age': 25}`

---

### `_resize(self) -> None`
Doubles capacity and rehashes all keys when load factor > 0.7.

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

## 🔹 Unit Testing

Tests are written using `unittest` in `/Tests/test_hashmap.py`.

To run:

```bash
python -m Tests.test_hashmap
```

### ✅ Covered Test Cases:
- Insert and update (`put`)
- Retrieval and key errors (`get`)
- Removal and non-existing key (`remove`)
- Presence checks (`contains`)
- Length validation (`__len__`)
- Output formatting (`__str__`)
- Auto-resizing (`_resize`)

---
