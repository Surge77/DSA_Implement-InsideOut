def gnome_sort(arr):
    """
    Sorts the input list 'arr' in-place using Gnome Sort.

    Time Complexity: O(N^2) worst/average, O(N) best (already sorted)
    Space Complexity: O(1) (in-place)
    Stable: Yes
    """
    n = len(arr)
    index = 0
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr  # Optional, for chaining


def run_gnome_sort_tests():
    # Test 1: Unsorted list
    arr1 = [34, 2, 10, -9]
    gnome_sort(arr1)
    assert arr1 == [-9, 2, 10, 34]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    gnome_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    gnome_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [2, 2, 2, 1, 1]
    gnome_sort(arr4)
    assert arr4 == [1, 1, 2, 2, 2]

    # Test 5: Single element
    arr5 = [42]
    gnome_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    gnome_sort(arr6)
    assert arr6 == []

    print("All gnome sort test cases passed!")

if __name__ == "__main__":
    run_gnome_sort_tests()
