class Queue:
    def __init__(self):
        """
        Initializes an empty queue using a list.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.data = []

    def enqueue(self, value):
        """
        Adds a value to the rear of the queue.

        Time Complexity: O(1) amortized
        Space Complexity: O(1)

        Parameters:
            value (any): The value to be added to the queue.
        """
        self.data.append(value)

    
    def dequeue(self):
      """
        Removes and returns the front element from the queue.

        Time Complexity: O(n) due to list shifting
        Space Complexity: O(1)

        Returns:
            The value at the front of the queue

        Raises:
            IndexError: If the queue is empty
      """
      if not self.data:
          raise IndexError("Dequeue from empty queue")

      return self.data.pop(0)
    

    def peek(self):
      """
        Returns the front element of the queue without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            The value at the front of the queue

        Raises:
            IndexError: If the queue is empty
      """
      if not self.data:
          raise IndexError("Peek from empty queue")

      return self.data[0]


    def is_empty(self) -> bool:
      """
        Checks whether the queue is empty.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            bool: True if the queue is empty, False otherwise
      """
      return len(self.data) == 0
    

    def __len__(self) -> int:
      """
        Returns the number of elements currently in the queue.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: The current size of the queue
      """
      return len(self.data)
    

    def __str__(self) -> str:
      """
        Returns a user-friendly string representation of the queue.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Example Output:
            Front → [1, 2, 3] ← Rear
      """
      return f"Front → {self.data} ← Rear"





