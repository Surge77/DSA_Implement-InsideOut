def flip(arr, k):
    """
    Reverses the first k elements of arr in place.
    """
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1

def pancake_sort(arr):
    """
    Sorts the input list 'arr' in-place using Pancake Sort.

    Time Complexity: O(N^2)
    Space Complexity: O(1) (in-place)
    Stable: No
    """
    n = len(arr)
    for curr_size in range(n, 1, -1):
        # Find index of the maximum element in arr[0:curr_size]
        max_idx = arr.index(max(arr[0:curr_size]))
        if max_idx != curr_size - 1:
            # Bring max to front, if not already at front
            if max_idx != 0:
                flip(arr, max_idx)
            # Now flip the max to its correct position
            flip(arr, curr_size - 1)
    return arr  # Optional, for chaining



def run_pancake_sort_tests():
    # Test 1: Unsorted list
    arr1 = [3, 6, 1, 10, 2, 5]
    pancake_sort(arr1)
    assert arr1 == [1, 2, 3, 5, 6, 10]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    pancake_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    pancake_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [2, 2, 2, 1, 1]
    pancake_sort(arr4)
    assert arr4 == [1, 1, 2, 2, 2]

    # Test 5: Single element
    arr5 = [42]
    pancake_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    pancake_sort(arr6)
    assert arr6 == []

    print("All pancake sort test cases passed!")

if __name__ == "__main__":
    run_pancake_sort_tests()
