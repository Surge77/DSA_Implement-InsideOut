from typing import List, Any, Optional

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Perform a basic linear search for the target in arr.

    Args:
        arr (List[Any]): The list to search.
        target (Any): The value to find.

    Returns:
        int: Index of target if found; else -1.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index at first occurrence
    return -1  # Not found

# Alternate: Return all indices where target appears
def linear_search_all(arr: List[Any], target: Any) -> List[int]:
    """
    Return a list of all indices where target appears in arr.

    Time Complexity: O(n)
    Space Complexity: O(k), k = count of target in arr
    """
    return [i for i, v in enumerate(arr) if v == target]


