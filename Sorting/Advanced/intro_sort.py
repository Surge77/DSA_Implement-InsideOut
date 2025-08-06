import math

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def heapify(arr, n, i, left):
    largest = i
    l = 2 * (i - left) + 1 + left
    r = 2 * (i - left) + 2 + left
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, left)

def heap_sort(arr, left, right):
    n = right + 1
    for i in range((left + n) // 2 - 1, left - 1, -1):
        heapify(arr, n, i, left)
    for i in range(right, left, -1):
        arr[left], arr[i] = arr[i], arr[left]
        heapify(arr, i, left, left)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def introsort_util(arr, left, right, maxdepth):
    size_threshold = 16  # For small arrays, use insertion sort
    if right - left <= size_threshold:
        insertion_sort(arr, left, right)
    elif maxdepth == 0:
        heap_sort(arr, left, right)
    else:
        pivot = partition(arr, left, right)
        introsort_util(arr, left, pivot - 1, maxdepth - 1)
        introsort_util(arr, pivot + 1, right, maxdepth - 1)

def introsort(arr):
    """
    Sorts 'arr' in-place using IntroSort (Quick Sort + Heap Sort + Insertion Sort).
    """
    n = len(arr)
    maxdepth = int(2 * math.log2(n)) if n > 0 else 0
    introsort_util(arr, 0, n - 1, maxdepth)
    return arr  # Optional, for chaining



def run_introsort_tests():
    # Test 1: Unsorted list
    arr1 = [10, 3, 5, 7, 2, 9, 1]
    introsort(arr1)
    assert arr1 == [1, 2, 3, 5, 7, 9, 10]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    introsort(arr2)
    assert arr2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [9, 7, 5, 3, 1]
    introsort(arr3)
    assert arr3 == [1, 3, 5, 7, 9]

    # Test 4: Duplicates
    arr4 = [4, 2, 2, 8, 3]
    introsort(arr4)
    assert arr4 == [2, 2, 3, 4, 8]

    # Test 5: Single element
    arr5 = [99]
    introsort(arr5)
    assert arr5 == [99]

    # Test 6: Empty list
    arr6 = []
    introsort(arr6)
    assert arr6 == []

    print("All introsort test cases passed!")

if __name__ == "__main__":
    run_introsort_tests()
