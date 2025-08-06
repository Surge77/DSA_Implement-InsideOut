def cocktail_shaker_sort(arr):
    """
    Sorts the input list 'arr' in-place using Cocktail Shaker Sort.

    Time Complexity: O(N^2)
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass (left to right)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swaps, array is sorted
        if not swapped:
            break

        swapped = False
        end -= 1  # Last element is now in place

        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1  # First element is now in place
    return arr  # Optional, for chaining



def run_cocktail_shaker_sort_tests():
    # Test 1: Unsorted list
    arr1 = [5, 1, 4, 2, 8, 0, 2]
    cocktail_shaker_sort(arr1)
    assert arr1 == [0, 1, 2, 2, 4, 5, 8]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    cocktail_shaker_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    cocktail_shaker_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [2, 2, 2, 1, 1]
    cocktail_shaker_sort(arr4)
    assert arr4 == [1, 1, 2, 2, 2]

    # Test 5: Single element
    arr5 = [42]
    cocktail_shaker_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    cocktail_shaker_sort(arr6)
    assert arr6 == []

    print("All cocktail shaker sort test cases passed!")

if __name__ == "__main__":
    run_cocktail_shaker_sort_tests()
