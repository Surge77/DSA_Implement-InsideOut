from typing import List, Any

def rotated_binary_search(arr: List[Any], target: Any) -> int:
    """
    Searches for a target in a rotated sorted array using binary search logic.

    Args:
        arr (List[Any]): Rotated sorted array (ascending, no duplicates).
        target (Any): Value to find.

    Returns:
        int: Index of target if found, else -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        # Check which half is sorted
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# -------------------
# Example Test Cases
# -------------------

def test_rotated_binary_search():
    assert rotated_binary_search([6,7,8,1,2,3,4,5], 3) == 5
    assert rotated_binary_search([4,5,6,7,0,1,2], 0) == 4
    assert rotated_binary_search([4,5,6,7,0,1,2], 3) == -1
    assert rotated_binary_search([1], 1) == 0
    assert rotated_binary_search([1], 5) == -1
    assert rotated_binary_search([1,2,3,4,5,6,7], 4) == 3  # Not rotated
    assert rotated_binary_search([3,1], 1) == 1            # Rotated with 2 elements

    print("All tests passed.")

test_rotated_binary_search()
