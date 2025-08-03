from typing import List, Any

def exponential_search(arr: List[Any], target: Any) -> int:
    """
    Exponential Search for sorted arrays.
    Quickly finds the window containing the target, then uses binary search.

    Args:
        arr (List[Any]): Sorted array (ascending).
        target (Any): Value to search for.

    Returns:
        int: Index of target if found, else -1.

    Time Complexity: O(log position of target)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    # Find range by repeated doubling
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Binary search in the found range: [i//2, min(i, n-1)]
    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = left + (right - left) // 2
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

def test_exponential_search():
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    assert exponential_search(arr, 23) == 5
    assert exponential_search(arr, 2) == 0
    assert exponential_search(arr, 91) == 9
    assert exponential_search(arr, 7) == -1
    assert exponential_search(arr, 100) == -1
    assert exponential_search([], 5) == -1
    assert exponential_search([10], 10) == 0
    assert exponential_search([10], 20) == -1

    print("All tests passed.")

test_exponential_search()
