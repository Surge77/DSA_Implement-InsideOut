def comb_sort(arr):
    """
    Sorts the input list 'arr' in-place using Comb Sort.

    Time Complexity: O(N^2) worst, O(N log N) average/best (practically faster than bubble sort)
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)
    gap = n
    shrink = 1.3  # Common shrink factor
    swapped = True

    while gap > 1 or swapped:
        # Update the gap for next comb
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        swapped = False
        # Compare and swap elements with 'gap' distance
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return arr  # Optional, for chaining


def run_comb_sort_tests():
    # Test 1: Unsorted list
    arr1 = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
    comb_sort(arr1)
    assert arr1 == sorted(arr1)

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    comb_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    comb_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [2, 2, 2, 1, 1]
    comb_sort(arr4)
    assert arr4 == [1, 1, 2, 2, 2]

    # Test 5: Single element
    arr5 = [42]
    comb_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    comb_sort(arr6)
    assert arr6 == []

    print("All comb sort test cases passed!")

if __name__ == "__main__":
    run_comb_sort_tests()
