import random

def is_sorted(arr):
    """
    Checks if arr is sorted in non-decreasing order.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr, max_attempts=100000):
    """
    Sorts 'arr' using bogosort (randomly shuffles until sorted).
    max_attempts prevents infinite loops on non-trivial arrays.

    Time Complexity: O((N!) * N) expected
    Space Complexity: O(1) in-place
    """
    attempts = 0
    while not is_sorted(arr) and attempts < max_attempts:
        random.shuffle(arr)
        attempts += 1
    return arr  # Optional, for chaining


def run_bogosort_tests():
    # WARNING: Bogosort is extremely slow for N > 5!
    arr1 = [3, 2, 1]
    bogosort(arr1)
    assert arr1 == [1, 2, 3]

    arr2 = [1]
    bogosort(arr2)
    assert arr2 == [1]

    arr3 = []
    bogosort(arr3)
    assert arr3 == []

    print("All bogosort test cases (small inputs!) passed.")

if __name__ == "__main__":
    run_bogosort_tests()
