class CircularQueue:
    def __init__(self, capacity: int):
        """
        Initializes a circular queue with fixed capacity.

        Time Complexity: O(1)
        Space Complexity: O(n), where n = capacity

        Parameters:
            capacity (int): The maximum number of elements the queue can hold
        """
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0


    def enqueue(self, value):
      """
        Adds a value to the rear of the queue.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Raises:
            OverflowError: If the queue is full
      """
      if self.size == self.capacity:
          raise OverflowError("Circular queue is full")

      self.data[self.rear] = value
      self.rear = (self.rear + 1) % self.capacity
      self.size += 1


    def dequeue(self):
      """
        Removes and returns the front element of the queue.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Raises:
            IndexError: If the queue is empty
      """
      if self.size == 0:
          raise IndexError("Dequeue from empty queue")

      value = self.data[self.front]
      self.data[self.front] = None  # Optional: clear slot
      self.front = (self.front + 1) % self.capacity
      self.size -= 1
      return value


    def __len__(self) -> int:
      """
        Returns the number of elements currently in the queue.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: current size of the queue
      """
      return self.size
    

    def peek(self):
      """
        Returns the front element of the queue without removing it.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Raises:
            IndexError: If the queue is empty
      """
      if self.size == 0:
          raise IndexError("Peek from empty queue")

      return self.data[self.front]


    def is_empty(self) -> bool:
      """
        Returns True if the queue is empty, else False.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            bool: True if empty, False otherwise
      """
      return self.size == 0


    def is_full(self) -> bool:
      """
        Returns True if the queue is full, else False.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            bool: True if full, False otherwise
      """
      return self.size == self.capacity


    def __str__(self) -> str:
      """
        Returns a user-friendly string showing queue contents from front to rear.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Returns:
            str: Formatted queue string like: Front → [10, 20, 30] ← Rear
      """
      if self.size == 0:
          return "Front → [] ← Rear"

      result = []
      index = self.front
      for _ in range(self.size):
          result.append(self.data[index])
          index = (index + 1) % self.capacity

      return f"Front → {result} ← Rear"


