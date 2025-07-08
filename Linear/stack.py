class Stack:
    def __init__(self):
        """
        Initializes an empty stack using a dynamic array (Python list).

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.data = []

    def push(self, value):
        """
        Pushes a new value onto the top of the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Parameters:
            value (any): The value to be added to the stack.
        """
        self.data.append(value)

    def pop(self):
      """
        Removes and returns the top element from the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The last pushed element (top of the stack)

        Raises:
            IndexError: If the stack is empty
      """
      if not self.data:
          raise IndexError("Pop from empty stack")

      return self.data.pop()
    
    def peek(self):
      """
        Returns the top element of the stack without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The last pushed element (top of the stack)

        Raises:
            IndexError: If the stack is empty
      """
      if not self.data:
          raise IndexError("Peek from empty stack")

      return self.data[-1]
    

    def is_empty(self) -> bool:
      """
        Checks whether the stack is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            bool: True if stack is empty, False otherwise
      """
      return len(self.data) == 0

    def __len__(self) -> int:
      """
        Returns the number of elements in the stack.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: The number of elements in the stack
      """
      return len(self.data)

    def __str__(self) -> str:
      """
        Returns a user-friendly string representation of the stack.

        Example Output:
            Bottom → [1, 2, 3] ← Top

        Time Complexity: O(n)
        Space Complexity: O(n)
      """
      return f"Bottom → {self.data} ← Top"




