def ubiquitous_binary_search(predicate, lo, hi):
    """
    Finds the minimal value in [lo, hi] such that predicate(value) is True.
    Assumes predicate is monotonic: once True, always True for greater values.

    Returns the minimal value (or hi+1 if not found).
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid   # Try lower, keep mid as possible answer
        else:
            lo = mid + 1
    return lo if predicate(lo) else hi + 1  # hi+1 if no solution in range

def min_square_at_least(target):
    def predicate(x):
        return x * x >= target
    # Reasonable upper bound: target (since target*target >= target for target ≥ 1)
    return ubiquitous_binary_search(predicate, 0, target)

def run_ubiquitous_tests():
    # Smallest x such that x*x >= 10: 4 (since 3*3=9 < 10, 4*4=16 ≥ 10)
    assert min_square_at_least(10) == 4
    # x*x >= 1: smallest x is 1
    assert min_square_at_least(1) == 1
    # x*x >= 16: smallest x is 4
    assert min_square_at_least(16) == 4
    # x*x >= 0: smallest x is 0
    assert min_square_at_least(0) == 0

    print("All ubiquitous binary search tests passed!")

if __name__ == "__main__":
    run_ubiquitous_tests()
