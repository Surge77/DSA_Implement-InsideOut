def ternary_search(arr, target):
    """
    Performs ternary search on a sorted array to find the target value.
    Returns the index if found, else -1.

    Time Complexity: O(log₃N)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Divide the current range into three parts
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1  # Search in the first third
        elif target > arr[mid2]:
            left = mid2 + 1   # Search in the third third
        else:
            left = mid1 + 1   # Search in the middle third
            right = mid2 - 1

    return -1  # Not found


def run_tests():
    # Test Case 1: Basic presence
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    assert ternary_search(arr1, 7) == 3
    assert ternary_search(arr1, 1) == 0
    assert ternary_search(arr1, 13) == 6

    # Test Case 2: Not present
    assert ternary_search(arr1, 8) == -1

    # Test Case 3: Edge cases (small array)
    arr2 = [4]
    assert ternary_search(arr2, 4) == 0
    assert ternary_search(arr2, 5) == -1

    arr3 = []
    assert ternary_search(arr3, 1) == -1

    # Test Case 4: Duplicate elements (finds any valid index)
    arr4 = [1, 2, 2, 2, 3]
    assert ternary_search(arr4, 2) in [1, 2, 3]

    # Test Case 5: Negative numbers
    arr5 = [-5, -3, -1, 0, 2]
    assert ternary_search(arr5, -3) == 1
    assert ternary_search(arr5, 0) == 3

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
