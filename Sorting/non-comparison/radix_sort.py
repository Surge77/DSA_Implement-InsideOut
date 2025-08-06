def counting_sort_exp(arr, exp):
    """
    A stable counting sort for the digit at exp (1, 10, 100, ...)
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # For decimal digits (0-9)

    # Store count of occurrences in count[]
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable, so iterate in reverse)
    for num in reversed(arr):
        index = (num // exp) % 10
        count[index] -= 1
        output[count[index]] = num

    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Sorts a list of non-negative integers using Radix Sort (LSD variant).

    Time Complexity: O(N * d), where d = max number of digits
    Space Complexity: O(N)
    """
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10
    return arr  # Optional, for chaining


def run_radix_sort_tests():
    # Test 1: Unsorted list
    arr1 = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr1)
    assert arr1 == [2, 24, 45, 66, 75, 90, 170, 802]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    radix_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [9, 8, 7, 6, 5]
    radix_sort(arr3)
    assert arr3 == [5, 6, 7, 8, 9]

    # Test 4: Duplicates
    arr4 = [4, 2, 2, 8, 3]
    radix_sort(arr4)
    assert arr4 == [2, 2, 3, 4, 8]

    # Test 5: Single element
    arr5 = [99]
    radix_sort(arr5)
    assert arr5 == [99]

    # Test 6: Empty list
    arr6 = []
    radix_sort(arr6)
    assert arr6 == []

    # Test 7: Includes zero
    arr7 = [0, 2, 100, 22]
    radix_sort(arr7)
    assert arr7 == [0, 2, 22, 100]

    print("All radix sort test cases passed!")

if __name__ == "__main__":
    run_radix_sort_tests()
