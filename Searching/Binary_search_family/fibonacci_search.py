from typing import List, Any

def fibonacci_search(arr: List[Any], target: Any) -> int:
    """
    Fibonacci Search for sorted arrays (ascending order).

    Args:
        arr (List[Any]): Sorted array (ascending).
        target (Any): Value to search for.

    Returns:
        int: Index of target if found, else -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    n = len(arr)
    # Initialize Fibonacci numbers
    fibM2, fibM1 = 0, 1
    fibM = fibM1 + fibM2

    # Find the smallest Fibonacci number >= n
    while fibM < n:
        fibM2, fibM1 = fibM1, fibM
        fibM = fibM1 + fibM2

    # Marks the eliminated range from the front
    offset = -1

    while fibM > 1:
        # Check if fibM2 is a valid location
        i = min(offset + fibM2, n - 1)
        if arr[i] < target:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i
        elif arr[i] > target:
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        else:
            return i

    # Compare the last element
    if fibM1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1

# -------------------
# Example Test Cases
# -------------------

def test_fibonacci_search():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    assert fibonacci_search(arr, 10) == 0
    assert fibonacci_search(arr, 85) == 8
    assert fibonacci_search(arr, 50) == 5
    assert fibonacci_search(arr, 100) == 10
    assert fibonacci_search(arr, 35) == 2
    assert fibonacci_search(arr, 101) == -1
    assert fibonacci_search(arr, 9) == -1
    assert fibonacci_search([], 5) == -1
    assert fibonacci_search([3], 3) == 0
    assert fibonacci_search([3], 2) == -1
    assert fibonacci_search([5, 10, 10, 10, 20], 10) in {1, 2, 3}  # Finds first match

    print("All tests passed.")

test_fibonacci_search()
