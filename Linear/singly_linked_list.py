class Node:
    def __init__(self, value):
        # Stores the actual data
        self.value = value

        # Points to the next node (initially None)
        self.next = None


class SinglyLinkedList:
  def __init__(self):
    self.head = None      # Start of the list
    self.tail = None      # End of the list (for fast appends)
    self.size = 0         # Number of nodes in the list


  def append(self, value):
    """
    Appends a new node with the given value to the end of the linked list.

    Time Complexity:
        ✅ O(1) — Constant time, because we maintain a tail pointer.

    Space Complexity:
        ✅ O(1)

    Parameters:
        value: The data to be stored in the new node.

    Behavior:
        - Creates a new Node with the given value.
        - If the list is empty, sets both head and tail to the new node.
        - Otherwise, links the current tail to the new node, then updates tail.
    """
    new_node = Node(value)

    if self.head is None:
        # List is empty — new node becomes head and tail
        self.head = new_node
        self.tail = new_node
    else:
        # Attach to current tail and update tail pointer
        self.tail.next = new_node
        self.tail = new_node

    self.size += 1



  def insert_at_start(self, data):
    """
    Inserts a new node at the beginning of the linked list.

    Time Complexity: O(1)
    Space Complexity: O(1)

    Parameters:
        data: The value to store in the new node.

    Behavior:
        - Creates a new node with the provided data.
        - Sets its `next` to the current head.
        - Updates the head pointer to this new node.
    """
    # Create the new node with the given data
    new_node = Node(data)

    # Point this new node's next to the current head
    new_node.next = self.head

    # Move the head pointer to the new node
    self.head = new_node


  def __str__(self):
    """
    Returns a human-readable string representation of the linked list.

    Example:
        "10 -> 20 -> 30 -> None"

    Time Complexity:
        ✅ O(n) — Must visit each node once.

    Space Complexity:
        ✅ O(n) — To build the string.

    Behavior:
        - Traverses the list from head to tail.
        - Collects each node’s value into a list of strings.
        - Joins them using '->' for a clean visual.
    """
    values = []
    current = self.head

    while current:
        values.append(str(current.value))
        current = current.next

    return " -> ".join(values) + " -> None"

  def __repr__(self):
    """
    Returns a developer-friendly string representation of the linked list.

    Useful for debugging — shows head, tail, and size.

    Example:
        "SinglyLinkedList(size=3, head=10, tail=30)"
    """
    head_val = self.head.value if self.head else None
    tail_val = self.tail.value if self.tail else None
    return f"SinglyLinkedList(size={self.size}, head={head_val}, tail={tail_val})"
  

  def prepend(self, value):
    """
    Inserts a new node with the given value at the beginning of the list.

    Time Complexity:
        ✅ O(1)

    Space Complexity:
        ✅ O(1)

    Behavior:
        - Creates a new node.
        - Points it to the current head.
        - Updates the head to the new node.
        - If the list was empty, sets tail as well.
    """
    new_node = Node(value)

    if self.head is None:
        # List is empty, so both head and tail point to the new node
        self.head = new_node
        self.tail = new_node
    else:
        # Point the new node to current head, then move head
        new_node.next = self.head
        self.head = new_node

    self.size += 1


  def __len__(self):
    """
    Returns the number of elements in the linked list.

    Time Complexity: O(1)
    Space Complexity: O(1)

    Behavior:
        - Simply returns the current size of the list.
        - Supports built-in len() calls like len(my_list).
    """
    return self.size
  

  def get(self, index):
    """
    Returns the value at the given index in the linked list.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Parameters:
        index (int): Position to retrieve value from (0-based).

    Raises:
        IndexError: If index is out of bounds.

    Behavior:
        - Traverses the list node by node until reaching the target index.
        - Returns the node’s value.
    """
    if index < 0 or index >= self.size:
        raise IndexError("Index out of bounds")

    current = self.head
    for _ in range(index):
        current = current.next

    return current.value


  def set(self, index, value):
      """
      Updates the value of the node at the specified index.i.e doesn't shift the element just replaces it with new element

      Time Complexity: O(n)
      Space Complexity: O(1)

      Parameters:
          index (int): Position of the node to update.
          value (any): New value to store.

      Raises:
          IndexError: If index is out of bounds.

      Behavior:
          - Traverses to the node at the given index.
          - Updates the node’s value with the new value.
      """
      if index < 0 or index >= self.size:
          raise IndexError("Index out of bounds")

      current = self.head
      for _ in range(index):
          current = current.next

      current.value = value

    
  def delete(self, index):
    """
    Deletes the node at the specified index from the linked list.

    Time Complexity: O(n) — must traverse to the index
    Space Complexity: O(1)

    Parameters:
        index (int): The position of the node to delete.

    Raises:
        IndexError: If index is out of bounds.

    Behavior:
        - If index is 0: Removes the head.
        - Otherwise: Traverse to the node before the target, relink its next.
        - If deleting the tail, update the tail pointer.
    """
    if index < 0 or index >= self.size:
        raise IndexError("Index out of bounds")

    if index == 0:
        # Remove head
        self.head = self.head.next
        if self.size == 1:
            self.tail = None
    else:
        # Traverse to node before the one we want to delete
        current = self.head
        for _ in range(index - 1):
            current = current.next

        node_to_delete = current.next
        current.next = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = current

    self.size -= 1


  def insert(self, index, value):
    """
    Inserts a new node with the given value at the specified index.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Parameters:
        index (int): Position to insert at (0-based).
        value (any): Value to insert.

    Raises:
        IndexError: If index is invalid (not in range [0, size]).

    Behavior:
        - If index == 0 → calls prepend()
        - If index == size → calls append()
        - Otherwise → inserts in the middle and shifts links
    """
    if index < 0 or index > self.size:
        raise IndexError("Index out of bounds")

    if index == 0:
        self.prepend(value)
    elif index == self.size:
        self.append(value)
    else:
        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1


  def search(self, value):
    """
    Searches for the first occurrence of a value in the list.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Parameters:
        value (any): The value to search for.

    Returns:
        int: The index of the first match, or -1 if not found.

    Behavior:
        - Traverses from head to tail.
        - Compares each node’s value.
        - Returns the index when found.
    """
    current = self.head
    index = 0

    while current:
        if current.value == value:
            return index
        current = current.next
        index += 1

    return -1  # Not found
  
  def reverse(self):
    """
    Reverses the linked list in place.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Behavior:
        - Flips all next pointers to point backward.
        - Updates head and tail accordingly.
    """
    prev = None
    current = self.head

    self.tail = self.head  # The current head will become the tail

    while current:
        next_node = current.next  # Store reference to the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    self.head = prev  # After loop, prev will be the new head




