from typing import List, Any

def recursive_linear_search(arr: List[Any], target: Any, idx: int = 0) -> int:
    """
    Recursive Linear Search.
    
    Args:
        arr (List[Any]): The array to search.
        target (Any): The value to find.
        idx (int): Current index (default 0).
    
    Returns:
        int: Index of target if found, else -1.
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack.
    """
    if idx >= len(arr):    # Base case: reached end
        return -1
    if arr[idx] == target: # Base case: found
        return idx
    return recursive_linear_search(arr, target, idx + 1)  # Recursive call

# -------------------
# Example Test Cases
# -------------------

def test_recursive_linear_search():
    assert recursive_linear_search([2, 4, 6, 8], 6) == 2
    assert recursive_linear_search([1, 3, 5], 2) == -1
    assert recursive_linear_search([], 9) == -1
    assert recursive_linear_search([9, 8, 7], 9) == 0
    assert recursive_linear_search([5, 7, 5, 9], 5) == 0
    assert recursive_linear_search([1], 1) == 0
    assert recursive_linear_search([1], 2) == -1

    print("All tests passed.")

test_recursive_linear_search()
