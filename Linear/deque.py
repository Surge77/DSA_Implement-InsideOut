class Node:
    def __init__(self, value):
        """
        A node for the doubly linked list used by Deque.

        Parameters:
            value (any): Data stored in this node.
        """
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        """
        Initializes an empty deque using a doubly linked list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.head = None  # Front of the deque
        self.tail = None  # Rear of the deque
        self.size = 0     # Number of elements


    def append_right(self, value):
      """
        Adds a new element to the rear (tail) of the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Parameters:
            value (any): The value to insert at the end.
      """
      new_node = Node(value)

      if self.tail is None:
          # First element being inserted
          self.head = self.tail = new_node
      else:
          # Link the new node at the end
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node

      self.size += 1


    def __str__(self):
      """
        Returns a human-readable string representation of the deque from front to rear.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Example:
            Front → [10, 20, 30] ← Rear
      """
      values = []
      current = self.head
      while current:
          values.append(current.value)
          current = current.next
      return f"Front → {values} ← Rear"


    def append_left(self, value):
      """
        Adds a new element to the front (head) of the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Parameters:
            value (any): The value to insert at the front.
      """
      new_node = Node(value)

      if self.head is None:
          # First element being inserted
          self.head = self.tail = new_node
      else:
          # Link new node at the front
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node

      self.size += 1


    def pop_right(self):
      """
        Removes and returns the element from the rear (tail) of the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The value at the rear of the deque.

        Raises:
            IndexError: If the deque is empty.
      """
      if self.tail is None:
          raise IndexError("Pop from empty deque")

      value = self.tail.value

      if self.head == self.tail:
          # Only one element
          self.head = self.tail = None
      else:
          self.tail = self.tail.prev
          self.tail.next = None

      self.size -= 1
      return value


    def pop_left(self):
      """
        Removes and returns the element from the front (head) of the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The value at the front of the deque.

        Raises:
            IndexError: If the deque is empty.
      """
      if self.head is None:
          raise IndexError("Pop from empty deque")

      value = self.head.value

      if self.head == self.tail:
          # Only one element
          self.head = self.tail = None
      else:
          self.head = self.head.next
          self.head.prev = None

      self.size -= 1
      return value


    def peek_left(self):
      """
        Returns the front element without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The value at the front of the deque.

        Raises:
            IndexError: If the deque is empty.
      """
      if self.head is None:
          raise IndexError("Peek from empty deque")
      return self.head.value


    def peek_right(self):
      """
        Returns the rear element without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The value at the rear of the deque.

        Raises:
            IndexError: If the deque is empty.
      """
      if self.tail is None:
          raise IndexError("Peek from empty deque")
      return self.tail.value


    def __len__(self):
      """
        Returns the number of elements in the deque.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: number of elements in the deque
      """
      return self.size


    def is_empty(self):
      """
        Returns True if the deque is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            bool: True if empty, False otherwise
      """
      return self.size == 0


if __name__ == "__main__":
    dq = Deque()
    dq.append_left("a")
    dq.append_right("b")
    dq.append_right("c")

    print(dq.peek_left())   # a
    print(dq.peek_right())  # c
    print(len(dq))          # 3
    print(dq.is_empty())    # False

    dq.pop_left()
    dq.pop_left()
    dq.pop_left()
    print(dq.is_empty())    # True
