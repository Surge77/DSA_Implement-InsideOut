import math

def jump_search(arr, target):
    """
    Performs jump search on a sorted array.
    Returns the index if found, else -1.

    Time Complexity: O(sqrt(N))
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return -1

    # Optimal jump size is sqrt(n)
    step = int(math.sqrt(n))
    prev = 0

    # Jump forward until we find a block where arr[prev] <= target <= arr[min(step, n)-1]
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the found block
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1  # Not found

def run_jump_search_tests():
    # Test Case 1: Target present (middle)
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    assert jump_search(arr1, 7) == 3

    # Test Case 2: Target present (first element)
    assert jump_search(arr1, 1) == 0

    # Test Case 3: Target present (last element)
    assert jump_search(arr1, 13) == 6

    # Test Case 4: Target absent
    assert jump_search(arr1, 6) == -1

    # Test Case 5: Empty array
    arr2 = []
    assert jump_search(arr2, 10) == -1

    # Test Case 6: Single element array (present)
    arr3 = [4]
    assert jump_search(arr3, 4) == 0

    # Test Case 7: Single element array (absent)
    assert jump_search(arr3, 5) == -1

    # Test Case 8: Multiple occurrences (returns any valid index)
    arr4 = [2, 4, 4, 4, 7, 10]
    idx = jump_search(arr4, 4)
    assert idx in [1, 2, 3]

    # Test Case 9: Negative numbers
    arr5 = [-10, -5, 0, 3, 8, 12]
    assert jump_search(arr5, 3) == 3
    assert jump_search(arr5, -10) == 0
    assert jump_search(arr5, 15) == -1

    print("All jump search test cases passed!")

if __name__ == "__main__":
    run_jump_search_tests()
