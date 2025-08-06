def shell_sort(arr):
    """
    Sorts the input list 'arr' in-place using Shell Sort.

    Time Complexity: Best: O(N log N), Worst: depends on gap sequence (typically O(N^2))
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)
    gap = n // 2  # Initial gap size

    # Reduce gap and perform gapped insertion sort
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reduce the gap for next pass
    return arr  # Optional, for chaining


def run_shell_sort_tests():
    # Test 1: Unsorted list
    arr1 = [12, 34, 54, 2, 3]
    shell_sort(arr1)
    assert arr1 == [2, 3, 12, 34, 54]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    shell_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    shell_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [4, 2, 2, 8, 3]
    shell_sort(arr4)
    assert arr4 == [2, 2, 3, 4, 8]

    # Test 5: Single element
    arr5 = [99]
    shell_sort(arr5)
    assert arr5 == [99]

    # Test 6: Empty list
    arr6 = []
    shell_sort(arr6)
    assert arr6 == []

    print("All shell sort test cases passed!")

if __name__ == "__main__":
    run_shell_sort_tests()
