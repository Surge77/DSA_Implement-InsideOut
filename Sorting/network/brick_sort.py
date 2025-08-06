def brick_sort(arr):
    """
    Sorts the input list 'arr' in-place using Brick Sort (Odd-Even Sort).

    Time Complexity: O(N^2)
    Space Complexity: O(1) (in-place)
    Stable: Yes
    """
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        # Odd indexed pass
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        # Even indexed pass
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

    return arr  # Optional, for chaining


def run_brick_sort_tests():
    arr1 = [5, 3, 1, 2, 4]
    brick_sort(arr1)
    assert arr1 == [1, 2, 3, 4, 5]

    arr2 = [1, 2, 3, 4]
    brick_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    arr3 = [4, 3, 2, 1]
    brick_sort(arr3)
    assert arr3 == [1, 2, 3, 4]

    arr4 = [2, 2, 1, 1]
    brick_sort(arr4)
    assert arr4 == [1, 1, 2, 2]

    arr5 = [42]
    brick_sort(arr5)
    assert arr5 == [42]

    arr6 = []
    brick_sort(arr6)
    assert arr6 == []

    print("All brick sort test cases passed!")

if __name__ == "__main__":
    run_brick_sort_tests()
