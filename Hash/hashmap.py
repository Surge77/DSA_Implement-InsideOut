class HashMap:
    def __init__(self, capacity: int = 8):
        """
        Initializes the HashMap with fixed capacity.

        Time Complexity: O(1)
        Space Complexity: O(n), where n = capacity

        Parameters:
            capacity (int): The number of buckets (default: 8)
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]  # Separate chaining (list of lists)

    def _hash(self, key: str) -> int:
        """
        Custom hash function using a basic polynomial rolling method.

        Time Complexity: O(len(key))
        Space Complexity: O(1)

        Parameters:
            key (str): The key to be hashed

        Returns:
            int: Index in the buckets array
        """
        hash_code = 0
        for char in key:
            hash_code = (hash_code * 31 + ord(char)) % self.capacity
        return hash_code


    def put(self, key: str, value: any) -> None:
      """
        Inserts or updates the value associated with the key.

        Time Complexity: O(n/k) in worst case (linked list traversal)
        Space Complexity: O(1)

        Parameters:
            key (str): The key to insert/update
            value (any): The value to associate with the key
      """
      index = self._hash(key)
      bucket = self.buckets[index]

      for i, (k, v) in enumerate(bucket):
          if k == key:
              bucket[i] = (key, value)  # Update
              return

      bucket.append((key, value))
      self.size += 1

      # Resize if load factor exceeds 0.7
      if self.size / self.capacity > 0.7:
          self._resize()



    def get(self, key: str) -> any:
      """
        Retrieves the value associated with the given key.

        Time Complexity: O(n/k) in worst case
        Space Complexity: O(1)

        Parameters:
            key (str): The key to look up

        Returns:
            any: The value associated with the key

        Raises:
            KeyError: If the key is not found
      """
      index = self._hash(key)
      bucket = self.buckets[index]

      for k, v in bucket:
          if k == key:
              return v

      raise KeyError(f"Key '{key}' not found in HashMap")
    

    def remove(self, key: str) -> None:
      """
        Removes the key-value pair associated with the given key.

        Time Complexity: O(n/k) in worst case (due to list traversal)
        Space Complexity: O(1)

        Parameters:
            key (str): The key to remove

        Raises:
            KeyError: If the key is not found
      """
      index = self._hash(key)
      bucket = self.buckets[index]

      for i, (k, _) in enumerate(bucket):
          if k == key:
              del bucket[i]
              self.size -= 1
              return

      raise KeyError(f"Key '{key}' not found in HashMap")

      
    def contains(self, key: str) -> bool:
      """
        Checks whether the given key exists in the HashMap.

        Time Complexity: O(n/k)
        Space Complexity: O(1)

        Parameters:
            key (str): The key to check

        Returns:
            bool: True if the key exists, False otherwise
      """
      index = self._hash(key)
      bucket = self.buckets[index]

      for k, _ in bucket:
          if k == key:
              return True

      return False
    

    def __len__(self) -> int:
      """
        Returns the number of key-value pairs in the HashMap.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: Current size of the HashMap
      """
      return self.size


    def __str__(self) -> str:
      """
        Returns a human-readable string of all key-value pairs in the HashMap.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Returns:
            str: A formatted string like:
                HashMap → {'key1': val1, 'key2': val2}
      """
      pairs = []
      for bucket in self.buckets:
          for key, value in bucket:
              pairs.append(f"'{key}': {repr(value)}")
      return "HashMap → {" + ", ".join(pairs) + "}"
    

    def _resize(self) -> None:
      """
        Resizes the HashMap when the load factor exceeds 0.7.
        Rehashes all existing key-value pairs into a larger bucket array.

        Time Complexity: O(n)
        Space Complexity: O(n)
      """
      old_buckets = self.buckets
      self.capacity *= 2
      self.buckets = [[] for _ in range(self.capacity)]
      self.size = 0  # Will be updated in put()

      for bucket in old_buckets:
          for key, value in bucket:
              self.put(key, value)  # re-inserts and rehashes
  

