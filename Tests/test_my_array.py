# test_my_array.py
from Linear.arrays import MyArray

if __name__ == "__main__":
    arr = MyArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.append(40)

    arr.delete(1)  # Delete 20
    print(arr)     # [10, 30, 40]

    arr.delete(0)  # Delete 10
    print(arr)     # [30, 40]

    arr.delete(5)  # Should raise IndexError
