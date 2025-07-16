from typing import List, Optional

class MaxHeap:
    """
    A Max-Heap implementation using an array (list) for storage.
    Provides O(log n) insertion and extraction of the maximum element.
    """

    def __init__(self):
        """
        Initialize an empty max-heap.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.data: List[int] = []

    def __len__(self) -> int:
        """
        Return the number of elements in the heap.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.data)
    

    def insert(self, value: int) -> None:
      """
      Insert a value into the heap, maintaining the max-heap property.
      Time Complexity: O(log n)
      Space Complexity: O(1)
      """
      self.data.append(value)
      self._bubble_up(len(self.data) - 1)


    def _bubble_up(self, index: int) -> None:
      """
      Move the element at the given index up to restore the max-heap property.
      Time Complexity: O(log n)
      Space Complexity: O(1)
      """
      parent = (index - 1) // 2
      while index > 0 and self.data[index] > self.data[parent]:
          self.data[index], self.data[parent] = self.data[parent], self.data[index]
          index = parent
          parent = (index - 1) // 2


    def extract_max(self) -> Optional[int]:
      """
      Remove and return the maximum element from the heap.
      Time Complexity: O(log n)
      Space Complexity: O(1)
      """
      if not self.data:
          return None
      max_val = self.data[0]
      last_val = self.data.pop()
      if self.data:
          self.data[0] = last_val
          self._bubble_down(0)
      return max_val


    def _bubble_down(self, index: int) -> None:
      """
      Move the element at index down to restore the max-heap property.
      Time Complexity: O(log n)
      Space Complexity: O(1)
      """
      n = len(self.data)
      while True:
          left = 2 * index + 1
          right = 2 * index + 2
          largest = index

          if left < n and self.data[left] > self.data[largest]:
              largest = left
          if right < n and self.data[right] > self.data[largest]:
              largest = right

          if largest == index:
              break
          self.data[index], self.data[largest] = self.data[largest], self.data[index]
          index = largest

    
    # In most heap implementations, peek() and get_max() (or top()) are actually the same method under different names.
    def get_max(self) -> Optional[int]:
      """
      Return the maximum element from the heap without removing it.
      Time Complexity: O(1)
      Space Complexity: O(1)
      """
      if not self.data:
          return None
      return self.data[0]
    

    def replace(self, value: int) -> Optional[int]:
      """
      Remove and return the maximum element, replacing it with a new value.
      Restores max-heap property by bubbling down from root.
      Time Complexity: O(log n)
      Space Complexity: O(1)
      """
      if not self.data:
          self.data.append(value)
          return None  # No previous max to return
      max_val = self.data[0]
      self.data[0] = value
      self._bubble_down(0)
      return max_val


    def heapify(self, elements: List[int]) -> None:
      """
      Transform a list of elements into a valid max-heap in O(n) time.
      Time Complexity: O(n)
      Space Complexity: O(n) (for the data list)
      """
      self.data = elements[:]
      n = len(self.data)
      # Start from the last parent and heapify-down each node
      for i in reversed(range(n // 2)):
          self._bubble_down(i)

if __name__ == "__main__":
    print("🔹 Testing heapify with [3, 10, 2, 7, 8, 1, 6]")
    elements = [3, 10, 2, 7, 8, 1, 6]
    heap = MaxHeap()
    heap.heapify(elements)
    print("Heap after heapify:", heap.data)
    # Heap property: root is max, and parent >= children everywhere
    def is_max_heap(arr):
        n = len(arr)
        for i in range(n // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                return False
            if right < n and arr[i] < arr[right]:
                return False
        return True

    assert is_max_heap(heap.data), "Heap should satisfy max-heap property after heapify"
    print("✅ heapify test passed.\n")

