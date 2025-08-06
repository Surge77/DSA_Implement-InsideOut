def pigeonhole_sort(arr):
    """
    Sorts a list of integers using Pigeonhole Sort.
    Returns a new sorted list.

    Time Complexity: O(N + Range), where Range = max(arr) - min(arr) + 1
    Space Complexity: O(N + Range)
    """
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1

    # Step 1: Create holes (buckets) and initialize counts
    holes = [0] * size

    # Step 2: Populate holes
    for num in arr:
        holes[num - min_val] += 1

    # Step 3: Put elements back into arr
    idx = 0
    for i in range(size):
        while holes[i] > 0:
            arr[idx] = i + min_val
            idx += 1
            holes[i] -= 1
    return arr  # Optional, for chaining


def run_pigeonhole_sort_tests():
    # Test 1: Unsorted list
    arr1 = [8, 3, 2, 7, 4, 6, 8]
    pigeonhole_sort(arr1)
    assert arr1 == [2, 3, 4, 6, 7, 8, 8]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    pigeonhole_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    pigeonhole_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates and negatives
    arr4 = [-3, -1, -2, -1, 0]
    pigeonhole_sort(arr4)
    assert arr4 == [-3, -2, -1, -1, 0]

    # Test 5: Single element
    arr5 = [99]
    pigeonhole_sort(arr5)
    assert arr5 == [99]

    # Test 6: Empty list
    arr6 = []
    pigeonhole_sort(arr6)
    assert arr6 == []

    print("All pigeonhole sort test cases passed!")

if __name__ == "__main__":
    run_pigeonhole_sort_tests()
