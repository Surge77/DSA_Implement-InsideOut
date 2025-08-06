def counting_sort(arr):
    """
    Sorts a list of non-negative integers using Counting Sort.
    Returns a new sorted list.

    Time Complexity: O(N + K), where N = len(arr), K = range of input
    Space Complexity: O(N + K)
    """
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_of_elements

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Change count[i] so that it contains actual position of this number in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    output = [0] * len(arr)
    # To make it stable, iterate in reverse order
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output



def run_counting_sort_tests():
    # Test 1: Unsorted list
    arr1 = [4, 2, 2, 8, 3, 3, 1]
    sorted1 = counting_sort(arr1)
    assert sorted1 == [1, 2, 2, 3, 3, 4, 8]

    # Test 2: Already sorted
    arr2 = [1, 2, 3, 4]
    sorted2 = counting_sort(arr2)
    assert sorted2 == [1, 2, 3, 4]

    # Test 3: Reverse sorted
    arr3 = [5, 4, 3, 2, 1]
    sorted3 = counting_sort(arr3)
    assert sorted3 == [1, 2, 3, 4, 5]

    # Test 4: Duplicates and single element
    arr4 = [2, 2, 2, 2]
    sorted4 = counting_sort(arr4)
    assert sorted4 == [2, 2, 2, 2]

    # Test 5: Single element
    arr5 = [99]
    sorted5 = counting_sort(arr5)
    assert sorted5 == [99]

    # Test 6: Empty list
    arr6 = []
    sorted6 = counting_sort(arr6)
    assert sorted6 == []

    # Test 7: Including zero
    arr7 = [0, 2, 1, 0]
    sorted7 = counting_sort(arr7)
    assert sorted7 == [0, 0, 1, 2]

    print("All counting sort test cases passed!")

if __name__ == "__main__":
    run_counting_sort_tests()
