from typing import List, Any

def binary_search(arr: List[Any], target: Any) -> int:
    """
    Basic Iterative Binary Search on a sorted (ascending) array.

    Args:
        arr (List[Any]): Sorted array to search.
        target (Any): Value to search for.

    Returns:
        int: Index of target if found, else -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow in other languages
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# -------------------
# Example Test Cases
# -------------------

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2           # Middle
    assert binary_search([1, 2, 3, 4, 5], 1) == 0           # Start
    assert binary_search([1, 2, 3, 4, 5], 5) == 4           # End
    assert binary_search([1, 3, 5, 7, 9], 7) == 3           # Random pos
    assert binary_search([1, 2, 3, 4, 5], 6) == -1          # Not found
    assert binary_search([], 2) == -1                       # Empty
    assert binary_search([1], 1) == 0                       # Single element
    assert binary_search([1], 2) == -1                      # Single element not found

    print("All tests passed.")

test_binary_search()
