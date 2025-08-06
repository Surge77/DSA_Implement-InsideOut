def selection_sort(arr):
    """
    Sorts the input list 'arr' in-place using Selection Sort.

    Time Complexity: O(N^2)
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)
    for i in range(n):
        # Assume the minimum is at the current index
        min_idx = i
        # Find the actual minimum in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap if needed
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  # Optional, for chaining


def run_selection_sort_tests():
    # Test 1: Unsorted list
    arr1 = [64, 25, 12, 22, 11]
    selection_sort(arr1)
    assert arr1 == [11, 12, 22, 25, 64]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    selection_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    selection_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [2, 1, 2, 1, 2]
    selection_sort(arr4)
    assert arr4 == [1, 1, 2, 2, 2]

    # Test 5: Single element
    arr5 = [7]
    selection_sort(arr5)
    assert arr5 == [7]

    # Test 6: Empty list
    arr6 = []
    selection_sort(arr6)
    assert arr6 == []

    print("All selection sort test cases passed!")

if __name__ == "__main__":
    run_selection_sort_tests()
