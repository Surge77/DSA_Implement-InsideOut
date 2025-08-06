def insertion_sort_run(arr, left, right):
    """
    Helper function to sort a subarray arr[left:right+1] using insertion sort.
    """
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def merge(arr, l, m, r):
    """
    Helper function to merge two sorted subarrays arr[l:m+1] and arr[m+1:r+1].
    """
    len1, len2 = m - l + 1, r - m
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr):
    """
    Simplified Timsort implementation.
    """
    n = len(arr)
    RUN = 32

    # Step 1: Sort small runs using insertion sort
    for start in range(0, n, RUN):
        end = min(start + RUN - 1, n - 1)
        insertion_sort_run(arr, start, end)

    # Step 2: Merge runs
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2
    return arr  # Optional, for chaining



def run_tim_sort_tests():
    # Test 1: Unsorted list
    arr1 = [5, 21, 7, 23, 19]
    tim_sort(arr1)
    assert arr1 == [5, 7, 19, 21, 23]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    tim_sort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [9, 7, 5, 3, 1]
    tim_sort(arr3)
    assert arr3 == [1, 3, 5, 7, 9]

    # Test 4: Duplicates
    arr4 = [4, 2, 2, 8, 3]
    tim_sort(arr4)
    assert arr4 == [2, 2, 3, 4, 8]

    # Test 5: Single element
    arr5 = [99]
    tim_sort(arr5)
    assert arr5 == [99]

    # Test 6: Empty list
    arr6 = []
    tim_sort(arr6)
    assert arr6 == []

    print("All tim sort test cases passed!")

if __name__ == "__main__":
    run_tim_sort_tests()
