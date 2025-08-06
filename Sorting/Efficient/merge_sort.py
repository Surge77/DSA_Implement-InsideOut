def merge_sort(arr):
    """
    Sorts the input list 'arr' using Merge Sort (recursive, not in-place).
    Returns a new sorted list.

    Time Complexity: O(N log N)
    Space Complexity: O(N) (additional arrays for merging)
    """
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    mid = len(arr) // 2
    # Recursively sort left and right halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """
    merged = []
    i = j = 0
    # Merge until one side runs out
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def run_merge_sort_tests():
    # Test 1: Unsorted list
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    sorted1 = merge_sort(arr1)
    assert sorted1 == [3, 9, 10, 27, 38, 43, 82]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    sorted2 = merge_sort(arr2)
    assert sorted2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    sorted3 = merge_sort(arr3)
    assert sorted3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates
    arr4 = [2, 3, 1, 2, 1]
    sorted4 = merge_sort(arr4)
    assert sorted4 == [1, 1, 2, 2, 3]

    # Test 5: Single element
    arr5 = [8]
    sorted5 = merge_sort(arr5)
    assert sorted5 == [8]

    # Test 6: Empty list
    arr6 = []
    sorted6 = merge_sort(arr6)
    assert sorted6 == []

    print("All merge sort test cases passed!")

if __name__ == "__main__":
    run_merge_sort_tests()
