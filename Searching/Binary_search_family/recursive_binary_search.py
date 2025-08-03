from typing import List, Any

def recursive_binary_search(arr: List[Any], target: Any, left: int = 0, right: int = None) -> int:
    """
    Recursive Binary Search on a sorted (ascending) array.

    Args:
        arr (List[Any]): Sorted array to search.
        target (Any): Value to search for.
        left (int): Left index of current search window.
        right (int): Right index of current search window.

    Returns:
        int: Index of target if found, else -1.

    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack.
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

# -------------------
# Example Test Cases
# -------------------

def test_recursive_binary_search():
    assert recursive_binary_search([1, 2, 3, 4, 5], 3) == 2          # Middle
    assert recursive_binary_search([1, 2, 3, 4, 5], 1) == 0          # Start
    assert recursive_binary_search([1, 2, 3, 4, 5], 5) == 4          # End
    assert recursive_binary_search([1, 3, 5, 7, 9], 7) == 3          # Random pos
    assert recursive_binary_search([1, 2, 3, 4, 5], 6) == -1         # Not found
    assert recursive_binary_search([], 2) == -1                      # Empty
    assert recursive_binary_search([1], 1) == 0                      # Single element
    assert recursive_binary_search([1], 2) == -1                     # Single element not found

    print("All tests passed.")

test_recursive_binary_search()
