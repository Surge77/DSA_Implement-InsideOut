from typing import List, Any

def bidirectional_linear_search(arr: List[Any], target: Any) -> int:
    """
    Bidirectional Linear Search:
    Searches for the target from both ends of the array simultaneously.

    Args:
        arr (List[Any]): The array to search.
        target (Any): The value to find.

    Returns:
        int: Index of the first occurrence found (could be left or right side).
             Returns -1 if not found.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        if arr[start] == target:
            return start
        if arr[end] == target:
            return end
        start += 1
        end -= 1
    return -1

# -------------------
# Example Test Cases
# -------------------

def test_bidirectional_linear_search():
    assert bidirectional_linear_search([1, 2, 3, 4, 5], 1) == 0       # Target at start
    assert bidirectional_linear_search([1, 2, 3, 4, 5], 5) == 4       # Target at end
    assert bidirectional_linear_search([1, 2, 3, 4, 5], 3) == 2       # Target in middle
    assert bidirectional_linear_search([10, 20, 30, 40], 20) == 1     # Target near start
    assert bidirectional_linear_search([10, 20, 30, 40], 40) == 3     # Target at end
    assert bidirectional_linear_search([7, 8, 9, 8, 7], 7) == 0       # Target at both ends, returns first found
    assert bidirectional_linear_search([7, 8, 9, 8, 7], 8) == 1       # Target in both halves
    assert bidirectional_linear_search([1], 1) == 0                   # Single element
    assert bidirectional_linear_search([], 3) == -1                   # Empty array
    assert bidirectional_linear_search([1, 2, 3, 4, 5], 6) == -1      # Not found

    print("All tests passed.")

test_bidirectional_linear_search()
