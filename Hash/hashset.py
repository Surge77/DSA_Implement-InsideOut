class HashSet:
    def __init__(self, capacity: int = 8):
        """
        Initializes an empty HashSet with fixed capacity.

        Time Complexity: O(1)
        Space Complexity: O(n), where n = capacity
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key: str) -> int:
        """
        Hash function to convert key into a bucket index.

        Time Complexity: O(len(key))
        Space Complexity: O(1)

        Parameters:
            key (str): The key to hash

        Returns:
            int: The index where the key should be stored
        """
        hash_code = 0
        for char in key:
            hash_code = (hash_code * 31 + ord(char)) % self.capacity
        return hash_code
    
    def __len__(self) -> int:
      """
        Returns the number of unique keys in the HashSet.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Returns:
            int: Total number of keys in the set
      """
      return self.size
    
    
    def add(self, key: str) -> None:
        """
          Adds a key to the HashSet if not already present.

          Time Complexity: O(n/k) in worst case
          Space Complexity: O(1)

          Parameters:
              key (str): The value to insert into the set
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for existing_key in bucket:
            if existing_key == key:
                return  # Already exists, do nothing

        bucket.append(key)
        self.size += 1

        if self.size / self.capacity > 0.7:
            self._resize()


    def contains(self, key: str) -> bool:
      """
        Checks whether the key exists in the HashSet.

        Time Complexity: O(n/k)
        Space Complexity: O(1)

        Parameters:
            key (str): The key to search for

        Returns:
            bool: True if the key exists, False otherwise
      """
      index = self._hash(key)
      bucket = self.buckets[index]

      for existing_key in bucket:
          if existing_key == key:
              return True

      return False
    
    def remove(self, key: str) -> None:
      """
        Removes the given key from the HashSet.

        Time Complexity: O(n/k)
        Space Complexity: O(1)

        Parameters:
            key (str): The key to remove

        Raises:
            KeyError: If the key does not exist in the set
      """
      index = self._hash(key)
      bucket = self.buckets[index]

      for i, existing_key in enumerate(bucket):
          if existing_key == key:
              del bucket[i]
              self.size -= 1
              return

      raise KeyError(f"Key '{key}' not found in HashSet")

    def __str__(self) -> str:
      """
        Returns a human-readable string representation of the HashSet.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Returns:
            str: Formatted like: HashSet → {'apple', 'banana'}
      """
      elements = []
      for bucket in self.buckets:
          for key in bucket:
              elements.append(f"'{key}'")
      return "HashSet → {" + ", ".join(elements) + "}"
    
  
    def _resize(self) -> None:
      """
        Doubles the capacity of the HashSet and rehashes all keys.

        Time Complexity: O(n)
        Space Complexity: O(n)
      """
      old_buckets = self.buckets
      self.capacity *= 2
      self.buckets = [[] for _ in range(self.capacity)]
      self.size = 0  # Will be updated during re-insertion

      for bucket in old_buckets:
          for key in bucket:
              self.add(key)  # Rehash & reinsert


    