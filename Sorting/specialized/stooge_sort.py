def stooge_sort(arr, l=0, h=None):
    """
    Sorts arr[l..h] using Stooge Sort (in-place).
    Time Complexity: O(N^(log 3 / log 1.5)) ≈ O(N^2.71)
    Space Complexity: O(log N) (recursion stack)
    """
    if h is None:
        h = len(arr) - 1
    if l >= h:
        return arr

    # If first is greater than last, swap
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    # If there are at least 3 elements
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h)
        stooge_sort(arr, l, h - t)
    return arr  # Optional, for chaining


def run_stooge_sort_tests():
    arr1 = [2, 4, 5, 3, 1]
    stooge_sort(arr1)
    assert arr1 == [1, 2, 3, 4, 5]

    arr2 = [1, 2, 3]
    stooge_sort(arr2)
    assert arr2 == [1, 2, 3]

    arr3 = [3, 2, 1]
    stooge_sort(arr3)
    assert arr3 == [1, 2, 3]

    arr4 = [7, 7, 7]
    stooge_sort(arr4)
    assert arr4 == [7, 7, 7]

    arr5 = [42]
    stooge_sort(arr5)
    assert arr5 == [42]

    arr6 = []
    stooge_sort(arr6)
    assert arr6 == []

    print("All stooge sort test cases passed!")

if __name__ == "__main__":
    run_stooge_sort_tests()
