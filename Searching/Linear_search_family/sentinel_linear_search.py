from typing import List, Any

def sentinel_search(arr: List[Any], target: Any) -> int:
    """
    Sentinel Linear Search.
    
    Places the target as a sentinel at the end of the list, so the loop 
    only needs to check arr[i] == target, not index bounds at every step.
    
    Args:
        arr (List[Any]): The array to search.
        target (Any): The value to find.
    
    Returns:
        int: Index of first occurrence of target, or -1 if not found.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return -1  # Edge case: empty array
    
    last = arr[-1]           # Save the last element to restore later
    arr[-1] = target         # Set the sentinel
    
    i = 0
    # No need to check i < n here!
    while arr[i] != target:
        i += 1
    
    arr[-1] = last           # Restore original last element
    
    # Determine if the match was within original array (not just at sentinel)
    if i < n - 1 or arr[-1] == target:
        return i
    return -1

# -------------------
# Example Test Cases
# -------------------

def test_sentinel_search():
    assert sentinel_search([1, 2, 3, 4, 5], 3) == 2  # Found in middle
    assert sentinel_search([4, 2, 7, 5], 8) == -1    # Not found
    assert sentinel_search([10, 20, 30], 10) == 0    # First element
    assert sentinel_search([5, 5, 5, 5], 5) == 0     # All elements same
    assert sentinel_search([], 1) == -1              # Empty list
    assert sentinel_search([1, 2, 3, 9], 9) == 3     # Last element

    # Case: last element IS the target, but occurs earlier too
    assert sentinel_search([7, 3, 8, 3], 3) == 1

    print("All tests passed.")

test_sentinel_search()
