import threading
import time

def sleep_sort(arr):
    """
    Sorts an array of non-negative integers using Sleep Sort.
    Returns a new sorted list.
    """
    result = []
    threads = []

    def sleeper(n):
        time.sleep(n * 0.01)  # 10ms per unit, not seconds!
        result.append(n)

    for num in arr:
        t = threading.Thread(target=sleeper, args=(num,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # Wait for all threads to finish

    return sorted(result)  # To account for potential thread race

# Usage demo:
if __name__ == "__main__":
    arr = [3, 1, 4, 2, 0]
    sorted_arr = sleep_sort(arr)
    print("Sleep sorted:", sorted_arr)
