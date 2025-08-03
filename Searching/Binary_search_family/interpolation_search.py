from typing import List, Any

def interpolation_search(arr: List[Any], target: Any) -> int:
    """
    Interpolation Search for uniformly distributed, sorted arrays.

    Args:
        arr (List[Any]): Sorted array (preferably uniformly distributed).
        target (Any): The value to search for.

    Returns:
        int: Index of target if found, else -1.

    Time Complexity:
        Best/Average: O(log log n) for uniform arrays
        Worst: O(n) for non-uniform or clustered data
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        # Handle single-value segment to avoid division by zero
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            else:
                return -1

        # Estimate the probable position of the target
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])

        # Guard against out-of-bounds due to integer division
        if pos < left or pos > right:
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1

# -------------------
# Example Test Cases
# -------------------

def test_interpolation_search():
    # Uniformly distributed, sorted
    assert interpolation_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 70) == 6
    assert interpolation_search([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 15) == -1  # Not present
    assert interpolation_search([10], 10) == 0
    assert interpolation_search([10], 20) == -1
    assert interpolation_search([], 5) == -1
    # Non-uniform
    assert interpolation_search([1, 2, 4, 8, 16, 32, 64], 16) == 4
    assert interpolation_search([1, 2, 4, 8, 16, 32, 64], 5) == -1
    # Duplicates (should find first match)
    assert interpolation_search([10, 10, 10, 10], 10) == 0

    print("All tests passed.")

test_interpolation_search()
