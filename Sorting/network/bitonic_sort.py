def bitonic_merge(arr, low, cnt, direction):
    """
    Merges a bitonic sequence in 'arr' starting at index 'low' of length 'cnt'
    into ascending order if direction=1, descending if direction=0.
    """
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if (direction == 1 and arr[i] > arr[i + k]) or (direction == 0 and arr[i] < arr[i + k]):
                arr[i], arr[i + k] = arr[i + k], arr[i]
        bitonic_merge(arr, low, k, direction)
        bitonic_merge(arr, low + k, k, direction)

def bitonic_sort(arr, low=0, cnt=None, direction=1):
    """
    Bitonic sort for arr[low:low+cnt] in 'direction':
        direction = 1 for ascending, 0 for descending
    """
    if cnt is None:
        cnt = len(arr)
    if cnt > 1:
        k = cnt // 2
        # First half in ascending order, second in descending
        bitonic_sort(arr, low, k, 1)
        bitonic_sort(arr, low + k, k, 0)
        # Merge the bitonic sequence
        bitonic_merge(arr, low, cnt, direction)
    return arr  # Optional, for chaining



def run_bitonic_sort_tests():
    # Test 1: Power of 2 size, random order
    arr1 = [3, 7, 4, 8, 6, 2, 1, 5]
    bitonic_sort(arr1)
    assert arr1 == [1, 2, 3, 4, 5, 6, 7, 8]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
    bitonic_sort(arr2)
    assert arr2 == [1, 2, 3, 4, 5, 6, 7, 8]

    # Test 3: Reverse sorted
    arr3 = [8, 7, 6, 5, 4, 3, 2, 1]
    bitonic_sort(arr3)
    assert arr3 == [1, 2, 3, 4, 5, 6, 7, 8]

    # Test 4: Duplicates
    arr4 = [3, 1, 3, 2, 2, 4, 1, 4]
    bitonic_sort(arr4)
    assert arr4 == [1, 1, 2, 2, 3, 3, 4, 4]

    # Test 5: Single element
    arr5 = [42]
    bitonic_sort(arr5)
    assert arr5 == [42]

    # Test 6: Empty list
    arr6 = []
    bitonic_sort(arr6)
    assert arr6 == []

    print("All bitonic sort test cases passed!")

if __name__ == "__main__":
    run_bitonic_sort_tests()
