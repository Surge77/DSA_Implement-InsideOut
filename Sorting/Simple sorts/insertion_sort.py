def insertion_sort(arr):
    """
    Sorts the input list 'arr' in-place using Insertion Sort.

    Time Complexity: O(N^2) worst/average, O(N) best (already sorted)
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert key after shifting
        arr[j + 1] = key
    return arr  # Optional, for chaining


def run_insertion_sort_tests():
    # Test 1: Unsorted list
    arr1 = [12, 11, 13, 5, 6]
    insertion_sort(arr1)
    assert arr1 == [5, 6, 11, 12, 13]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    insertion_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [9, 7, 5, 3, 1]
    insertion_sort(arr3)
    assert arr3 == [1, 3, 5, 7, 9]

    # Test 4: Duplicates
    arr4 = [3, 1, 2, 3, 1]
    insertion_sort(arr4)
    assert arr4 == [1, 1, 2, 3, 3]

    # Test 5: Single element
    arr5 = [42]
    insertion_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    insertion_sort(arr6)
    assert arr6 == []

    print("All insertion sort test cases passed!")

if __name__ == "__main__":
    run_insertion_sort_tests()
