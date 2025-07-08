class DoublyNode:
  def __init__(self,value):
    self.value = value
    self.next = None
    self.prev = None


class DoublyLinkedList:
    def __init__(self):
        # Points to the first node in the list
        self.head = None

        # Points to the last node in the list
        self.tail = None

        # Tracks the number of elements
        self.size = 0

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Parameters:
            value: The data to be stored in the new node.

        Behavior:
            - Creates a new node.
            - If list is empty, sets both head and tail to it.
            - Otherwise, links it after the current tail and updates tail.
        """
        new_node = DoublyNode(value)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Link the new node after current tail
            self.tail.next = new_node
            new_node.prev = self.tail

            # Move the tail to the new node
            self.tail = new_node

        self.size += 1

    def __str__(self):
      """
        Returns a human-readable string of the linked list from head to tail.

        Example:
            10 <-> 20 <-> 30 <-> None

        Time Complexity: O(n)
        Space Complexity: O(n)
      """
      values = []
      current = self.head

      while current:
          values.append(str(current.value))
          current = current.next

      return " <-> ".join(values) + " <-> None"
    

    def __repr__(self):
      """
        Returns a developer-friendly representation of the linked list.

        Example:
            DoublyLinkedList([10, 20, 30], size=3)

        Time Complexity: O(n)
        Space Complexity: O(n)
      """
      values = []
      current = self.head

      while current:
          values.append(repr(current.value))  # use repr() for developer-style string
          current = current.next

      return f"DoublyLinkedList([{', '.join(values)}], size={self.size})"
    

    def prepend(self, value):
      """
        Inserts a new node at the beginning of the list.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Parameters:
            value: The data to store in the new head node.

        Behavior:
            - If the list is empty, sets both head and tail to new node.
            - Otherwise:
                - Links new node before current head.
                - Updates head pointer.
      """
      new_node = DoublyNode(value)

      if self.head is None:
          # Empty list: both head and tail point to the new node
          self.head = new_node
          self.tail = new_node
      else:
          # Connect new node to the current head
          new_node.next = self.head
          self.head.prev = new_node

          # Move head to the new node
          self.head = new_node

      self.size += 1

    
    def get(self, index):
      """
        Returns the value at the specified index.

        Time Complexity: O(n) worst-case, but optimized from head/tail

        Parameters:
            index (int): The position (0-based)

        Raises:
            IndexError: If index is out of bounds
      """
      if index < 0 or index >= self.size:
          raise IndexError("Index out of bounds")

      # Optimize: start from closer end (head or tail)
      if index < self.size // 2:
          # Start from head
          current = self.head
          for _ in range(index):
              current = current.next
      else:
          # Start from tail
          current = self.tail
          for _ in range(self.size - 1, index, -1):
              current = current.prev

      return current.value

    def set(self, index: int, value: any) -> None:
      """
        Updates the value at the specified index.

        Time Complexity: O(n) worst-case (optimized via head/tail)
        Space Complexity: O(1)

        Parameters:
            index (int): Position of the node to update
            value (any): New value to set

        Raises:
            IndexError: If index is out of bounds
      """
      if index < 0 or index >= self.size:
          raise IndexError("Index out of bounds")

      # Optimize traversal direction
      if index < self.size // 2:
          current = self.head
          for _ in range(index):
              current = current.next
      else:
          current = self.tail
          for _ in range(self.size - 1, index, -1):
              current = current.prev

      current.value = value

    
    def insert(self, index: int, value: any) -> None:
      """
        Inserts a new node with the given value at the specified index.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Parameters:
            index (int): The position to insert the new node at
            value (any): The data for the new node

        Raises:
            IndexError: If index is out of bounds
      """
      if index < 0 or index > self.size:
          raise IndexError("Index out of bounds")

      if index == 0:
          return self.prepend(value)

      if index == self.size:
          return self.append(value)

      # Create the new node to insert
      new_node = DoublyNode(value)

      # Traverse to the node currently at that index
      if index < self.size // 2:
          current = self.head
          for _ in range(index):
              current = current.next
      else:
          current = self.tail
          for _ in range(self.size - 1, index, -1):
              current = current.prev

      # current now points to the node currently at the index
      # So we insert before `current`

      prev_node = current.prev

      # Link prev_node <-> new_node
      prev_node.next = new_node
      new_node.prev = prev_node

      # Link new_node <-> current
      new_node.next = current
      current.prev = new_node

      # Update size
      self.size += 1


    def delete(self, index: int) -> None:
      """
        Deletes the node at the specified index.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Parameters:
            index (int): The index of the node to remove

        Raises:
            IndexError: If the index is invalid
      """
      if index < 0 or index >= self.size:
          raise IndexError("Index out of bounds")

      # Case 1: Delete head
      if index == 0:
          if self.head == self.tail:
              # Only one node in the list
              self.head = None
              self.tail = None
          else:
              self.head = self.head.next
              self.head.prev = None
          self.size -= 1
          return

      # Case 2: Delete tail
      if index == self.size - 1:
          self.tail = self.tail.prev
          self.tail.next = None
          self.size -= 1
          return

      # Case 3: Delete from middle
      if index < self.size // 2:
          current = self.head
          for _ in range(index):
              current = current.next
      else:
          current = self.tail
          for _ in range(self.size - 1, index, -1):
              current = current.prev

      # Remove `current` node
      prev_node = current.prev
      next_node = current.next

      prev_node.next = next_node
      next_node.prev = prev_node

      self.size -= 1


    def __len__(self):
      """
        Returns the number of elements in the list.

        Time Complexity: O(1)
        Space Complexity: O(1)
      """
      return self.size


    def search(self, value: any) -> int:
      """
        Returns the index of the first occurrence of the given value.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Parameters:
            value: The value to search for

        Returns:
            int: Index of the value, or -1 if not found
      """
      current = self.head
      index = 0

      while current:
          if current.value == value:
              return index
          current = current.next
          index += 1

      return -1


    def reverse(self) -> None:
      """
        Reverses the linked list in place.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Behavior:
            - Swaps each node's next and prev.
            - Swaps the head and tail references.
      """
      current = self.head
      while current:
          # Swap next and prev pointers
          current.prev, current.next = current.next, current.prev
          current = current.prev  # move backward (which is forward now)

      # Swap head and tail
      self.head, self.tail = self.tail, self.head


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for val in ["a", "b", "c", "d"]:
        dll.append(val)

    print("Before reverse:", dll)  # a <-> b <-> c <-> d <-> None
    dll.reverse()
    print("After reverse: ", dll)  # d <-> c <-> b <-> a <-> None

    # Another reverse to get back original
    dll.reverse()
    print("Back to original:", dll)  # a <-> b <-> c <-> d <-> None
