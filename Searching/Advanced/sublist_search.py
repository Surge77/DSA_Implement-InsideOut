def sublist_search(main_list, pattern):
    """
    Returns True if 'pattern' appears as a contiguous sublist in 'main_list'.
    Returns False otherwise.

    Time Complexity: O((N-M+1) * M), where N = len(main_list), M = len(pattern)
    Space Complexity: O(1) extra (excluding input lists)
    """
    n, m = len(main_list), len(pattern)
    if m == 0:
        return True  # Convention: Empty pattern matches anywhere
    if m > n:
        return False  # Can't be a sublist if longer

    for i in range(n - m + 1):
        # Compare slices directly
        if main_list[i:i + m] == pattern:
            return True
    return False

def run_sublist_search_tests():
    # Test 1: Basic match
    assert sublist_search([1, 2, 3, 4, 5], [3, 4]) == True

    # Test 2: Pattern at start
    assert sublist_search([1, 2, 3], [1, 2]) == True

    # Test 3: Pattern at end
    assert sublist_search([5, 7, 9, 11], [9, 11]) == True

    # Test 4: No match
    assert sublist_search([1, 2, 3, 4], [2, 4]) == False

    # Test 5: Full list match
    assert sublist_search([1, 2, 3], [1, 2, 3]) == True

    # Test 6: Pattern longer than list
    assert sublist_search([1, 2], [1, 2, 3]) == False

    # Test 7: Empty pattern (matches everywhere)
    assert sublist_search([1, 2, 3], []) == True

    # Test 8: Empty main list
    assert sublist_search([], [1]) == False

    # Test 9: Both empty
    assert sublist_search([], []) == True

    # Test 10: Pattern with repeated elements
    assert sublist_search([1, 2, 2, 2, 3], [2, 2, 3]) == True

    print("All sublist search test cases passed!")

if __name__ == "__main__":
    run_sublist_search_tests()
