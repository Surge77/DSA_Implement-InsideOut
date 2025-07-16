from typing import List, Optional

class MinHeap:
    """
    A Min-Heap implementation using an array (list) for storage.
    Provides O(log n) insertion and extraction of the minimum element.
    """

    def __init__(self):
        """Initialize an empty min-heap."""
        self.data: List[int] = []


    def insert(self, value: int) -> None:
        """
        Insert a value into the heap, maintaining the min-heap property.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        self.data.append(value) # appends the new value at the end of the list to maintain the heap as complete binary tree
        self._bubble_up(len(self.data) - 1) # Bubble up from new values position 
        #  The new value might be smaller than its parent, which would break the min-heap property, so we move it up until order is restored.


    def extract_min(self) -> Optional[int]:
        """
        Remove and return the minimum element from the heap.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Handle empty heap
        if not self.data:
            return None
        min_val = self.data[0] # Stores the first element from the list which is minimum 
        last_val = self.data.pop() # Removes the last element and stores it
        if self.data:
            self.data[0] = last_val
            self._bubble_down(0) # The last element (now at the root) might be greater than its children, breaking the min-heap rule.
            # Fix this by "bubbling down" from the root using _bubble_down(0).
        return min_val # after restoring the heap order return the value you removed


    def get_min(self) -> Optional[int]:
        """
        Get the minimum element without removing it.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.data:
            return None
        return self.data[0]


    def _bubble_up(self, index: int) -> None:
        """
        Restore the heap property going up from index.

        After append, only one thing can break: the new element might be smaller than its parent. This method moves the element up until the parent is smaller or it reaches the root.
        
        """
        parent = (index - 1) // 2 # calculates parent index for the current node
        # As long as we’re not at the root (index > 0) and the current value is less than its parent, keep moving up.
        while index > 0 and self.data[index] < self.data[parent]: 
            self.data[index], self.data[parent] = self.data[parent], self.data[index] # Swap the current node and its parent.
            # Move up one level and repeat the check.
            index = parent
            parent = (index - 1) // 2


    def _bubble_down(self, index: int) -> None:
        """
        Restore the heap property going down from index.
        
        After removing the min element (the root), we move the last element to the root

        This new root might break the min-heap property: it could be larger than its children.

        Goal: Move it down to its correct spot so every parent is less than or equal to its children.
        
        """
        n = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest


    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self.data)


    def __str__(self) -> str:
        """String representation for debugging."""
        return str(self.data)

