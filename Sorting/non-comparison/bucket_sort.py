def bucket_sort(arr):
    """
    Sorts a list of real numbers in [0, 1) using Bucket Sort.

    Time Complexity: O(N + N^2/k + k), where k = number of buckets
    Space Complexity: O(N + k)
    """
    n = len(arr)
    if n == 0:
        return arr

    # 1. Create n empty buckets
    buckets = [[] for _ in range(n)]

    # 2. Put array elements into buckets
    for num in arr:
        index = int(num * n)  # Index in [0, n-1]
        buckets[index].append(num)

    # 3. Sort individual buckets
    for bucket in buckets:
        bucket.sort()  # You can use insertion sort for educational purposes

    # 4. Concatenate all buckets into arr
    idx = 0
    for bucket in buckets:
        for num in bucket:
            arr[idx] = num
            idx += 1
    return arr  # Optional, for chaining


def run_bucket_sort_tests():
    # Test 1: Random floats
    arr1 = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    bucket_sort(arr1)
    assert arr1 == sorted(arr1)

    # Test 2: Already sorted
    arr2 = [0.1, 0.2, 0.3, 0.4]
    bucket_sort(arr2)
    assert arr2 == [0.1, 0.2, 0.3, 0.4]

    # Test 3: Reverse sorted
    arr3 = [0.9, 0.7, 0.5, 0.3]
    bucket_sort(arr3)
    assert arr3 == [0.3, 0.5, 0.7, 0.9]

    # Test 4: Duplicates
    arr4 = [0.25, 0.25, 0.75, 0.75, 0.5]
    bucket_sort(arr4)
    assert arr4 == [0.25, 0.25, 0.5, 0.75, 0.75]

    # Test 5: Single element
    arr5 = [0.99]
    bucket_sort(arr5)
    assert arr5 == [0.99]

    # Test 6: Empty list
    arr6 = []
    bucket_sort(arr6)
    assert arr6 == []

    print("All bucket sort test cases passed!")

if __name__ == "__main__":
    run_bucket_sort_tests()
