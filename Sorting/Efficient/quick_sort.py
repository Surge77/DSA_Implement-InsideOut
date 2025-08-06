def quick_sort(arr, low=0, high=None):
    """
    Sorts the input list 'arr' in-place using Quick Sort (Lomuto partition scheme).

    Time Complexity: O(N log N) average, O(N^2) worst-case
    Space Complexity: O(log N) average (due to recursion stack)
    """
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Partition the array
        p = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr  # Optional, for chaining

def partition(arr, low, high):
    """
    Lomuto partitioning:
    Picks the last element as pivot, places it at correct sorted position,
    and places all smaller elements to left of pivot and all greater to right.
    """
    pivot = arr[high]
    i = low - 1  # Place for smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    # Place pivot in the right position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def run_quick_sort_tests():
    # Test 1: Unsorted list
    arr1 = [10, 7, 8, 9, 1, 5]
    quick_sort(arr1)
    assert arr1 == [1, 5, 7, 8, 9, 10]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    quick_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    quick_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [4, 2, 2, 8, 3]
    quick_sort(arr4)
    assert arr4 == [2, 2, 3, 4, 8]

    # Test 5: Single element
    arr5 = [42]
    quick_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    quick_sort(arr6)
    assert arr6 == []

    print("All quick sort test cases passed!")

if __name__ == "__main__":
    run_quick_sort_tests()
