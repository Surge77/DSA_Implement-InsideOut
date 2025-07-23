class MyArray:
    def __init__(self):
        # Initial capacity — how much space we allocate upfront
        self.capacity = 4

        # Logical size — how many elements are currently stored
        self.count = 0

        # Backing list simulating a fixed-size array
        self.data = [None] * self.capacity  


    def append(self,value):
        """
          Adds a value to the end of the array.
          Amortized Time Complexity: O(1)
          Worst-case (resize): O(n)
        """
        # Check if we need to resize the array
        if self.count == self.capacity:
            self._resize()

        # Add the new value and increment the count
        self.data[self.count] = value
        self.count += 1


    def _resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        # Double the capacity
        self.capacity *= 2
        new_data = [None] * self.capacity

        # Copy over the old data
        for i in range(self.count):
            new_data[i] = self.data[i]

        self.data = new_data


    def get(self, index):
        """
          Retrieves the value at the specified index.
          Time Complexity: O(1)
        """
        if 0 <= index < self.count:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")
        

    def pop(self):
        """
          Removes the last element from the array and returns it.
          Time Complexity: O(1)
        """
        if self.count == 0:
            raise IndexError("Pop from empty array")
        
        value = self.data[self.count - 1]
        self.data[self.count - 1] = None
        self.count -= 1
        return value


    def __len__(self):
        """
          A dunder method
          Returns the number of elements in the array.
          Time Complexity: O(1)
        """
        return self.count
    

    def __getitem__(self, index: int):
      return self.get(index)
    

    def __str__(self):
      """
      Human-readable string representation.
      Example: [10, 20, 30]
      """
      return str(self.data[:self.count])


    def __repr__(self):
      """
        Developer-friendly string representation.
        Example: MyArray([10, 20, 30], size=3, capacity=4)
      """
      return f"MyArray({self.data[:self.count]}, size={self.count}, capacity={self.capacity})"
    

    def set(self, index: int, value: any) -> None:
      """
        Sets the value at the given index. i.e replaces the value at that index.
        Time Complexity: O(1)

        Raises:
            IndexError: If index is invalid
      """
      if index < 0 or index >= self.count:
        raise IndexError("Index out of bounds")

      self.data[index] = value


    def insert(self, index: int, value: any) -> None:
      """
        Inserts a value at the specified index.
        Time Complexity: O(n) in the worst case (if resizing is needed)

        Raises:
            IndexError: If index is invalid
      """
      if index < 0 or index > self.count:
        raise IndexError("Index out of bounds")

      # Resize if necessary
      if self.count == self.capacity:
          self._resize()

      # Shift elements to the right
      for i in range(self.count, index, -1):
          self.data[i] = self.data[i - 1]

      # Insert the new value
      self.data[index] = value
      self.count += 1


    def delete(self, index: int) -> None:
      """
        Deletes the element at the specified index, shifting remaining elements left.
        Time Complexity: O(n) in worst case
      """
      if index < 0 or index >= self.count:
        raise IndexError("Index out of bounds for delete")

      # Shift elements left
      for i in range(index, self.count - 1):
        self.data[i] = self.data[i + 1]

      # Optional: clear the duplicate at the end
      self.data[self.count - 1] = None
      self.count -= 1


    def clear(self):
      """
        Clears the array, resetting it to an empty state.
        Time Complexity: O(n) for clearing the data
      """
      self.data = [None] * self.capacity
      self.count = 0


    def contains(self, value: any) -> bool:
      """
        Checks if the array contains a specific value.
        Time Complexity: O(n) in worst case
      """
      for i in range(self.count):
          if self.data[i] == value:
              return True
      return False
    

    def __index_of__(self, value: any) -> int:
      """
        Returns the index of the first occurrence of a value.
        Time Complexity: O(n) in worst case
      """
      for i in range(self.count):
          if self.data[i] == value:
              return i
      return -1
    



