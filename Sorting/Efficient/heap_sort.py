def heap_sort(arr):
    """
    Sorts the input list 'arr' in-place using Heap Sort.

    Time Complexity: O(N log N)
    Space Complexity: O(1) (in-place, uses array to simulate heap)
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)
    return arr  # Optional, for chaining

def heapify(arr, n, i):
    """
    Maintains the max heap property for a subtree rooted at index i.
    """
    largest = i      # Initialize largest as root
    left = 2 * i + 1 # left child
    right = 2 * i + 2 # right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def run_heap_sort_tests():
    # Test 1: Unsorted list
    arr1 = [12, 11, 13, 5, 6, 7]
    heap_sort(arr1)
    assert arr1 == [5, 6, 7, 11, 12, 13]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    heap_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [9, 8, 7, 6, 5]
    heap_sort(arr3)
    assert arr3 == [5, 6, 7, 8, 9]

    # Test 4: Duplicates
    arr4 = [4, 2, 2, 8, 3]
    heap_sort(arr4)
    assert arr4 == [2, 2, 3, 4, 8]

    # Test 5: Single element
    arr5 = [99]
    heap_sort(arr5)
    assert arr5 == [99]

    # Test 6: Empty list
    arr6 = []
    heap_sort(arr6)
    assert arr6 == []

    print("All heap sort test cases passed!")

if __name__ == "__main__":
    run_heap_sort_tests()
