def bubble_sort(arr):
    """
    Sorts the input list 'arr' in-place using Bubble Sort.

    Time Complexity: O(N^2)
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)
    for i in range(n):
        # Track if any swap happens in this pass
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps, list is already sorted
        if not swapped:
            break
    return arr  # Optional: for chaining, not required

def run_bubble_sort_tests():
    # Test 1: Basic unsorted list
    arr1 = [5, 1, 4, 2, 8]
    bubble_sort(arr1)
    assert arr1 == [1, 2, 4, 5, 8]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    bubble_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [9, 6, 3, 1]
    bubble_sort(arr3)
    assert arr3 == [1, 3, 6, 9]

    # Test 4: Duplicates
    arr4 = [3, 3, 2, 1, 2]
    bubble_sort(arr4)
    assert arr4 == [1, 2, 2, 3, 3]

    # Test 5: Single element
    arr5 = [7]
    bubble_sort(arr5)
    assert arr5 == [7]

    # Test 6: Empty list
    arr6 = []
    bubble_sort(arr6)
    assert arr6 == []

    print("All bubble sort test cases passed!")

if __name__ == "__main__":
    run_bubble_sort_tests()
