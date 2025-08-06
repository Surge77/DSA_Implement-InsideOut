def odd_even_sort(arr):
    """
    Sorts the input list 'arr' in-place using Odd-Even (Brick) Sort.

    Time Complexity: O(N^2)
    Space Complexity: O(1) (in-place)
    Stable: Yes
    """
    n = len(arr)
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        # Perform Bubble sort on odd indexed elements
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        # Perform Bubble sort on even indexed elements
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr  # Optional, for chaining



def run_odd_even_sort_tests():
    arr1 = [5, 3, 1, 2, 4]
    odd_even_sort(arr1)
    assert arr1 == [1, 2, 3, 4, 5]

    arr2 = [1, 2, 3, 4]
    odd_even_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    arr3 = [4, 3, 2, 1]
    odd_even_sort(arr3)
    assert arr3 == [1, 2, 3, 4]

    arr4 = [2, 2, 1, 1]
    odd_even_sort(arr4)
    assert arr4 == [1, 1, 2, 2]

    arr5 = [42]
    odd_even_sort(arr5)
    assert arr5 == [42]

    arr6 = []
    odd_even_sort(arr6)
    assert arr6 == []

    print("All odd-even sort test cases passed!")

if __name__ == "__main__":
    run_odd_even_sort_tests()
