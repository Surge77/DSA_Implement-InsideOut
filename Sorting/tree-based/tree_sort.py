class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    """Insert a value into BST (allows duplicates on right)."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder_traversal(root, res):
    """Append the in-order traversal of BST to res."""
    if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)

def tree_sort(arr):
    """
    Sorts a list using Tree Sort (BST).
    Time Complexity: O(N log N) average, O(N^2) worst (unbalanced)
    Space Complexity: O(N) for tree
    Stable: No (BST does not preserve order of duplicates)
    """
    root = None
    for num in arr:
        root = insert(root, num)
    result = []
    inorder_traversal(root, result)
    return result


def run_tree_sort_tests():
        arr1 = [5, 3, 7, 2, 4, 6, 8]
        sorted1 = tree_sort(arr1)
        assert sorted1 == [2, 3, 4, 5, 6, 7, 8]

        arr2 = [1, 2, 3, 4]
        sorted2 = tree_sort(arr2)
        assert sorted2 == [1, 2, 3, 4]

        arr3 = [4, 3, 2, 1]
        sorted3 = tree_sort(arr3)
        assert sorted3 == [1, 2, 3, 4]

        arr4 = [3, 3, 2, 1, 2]
        sorted4 = tree_sort(arr4)
        assert sorted4 == [1, 2, 2, 3, 3]

        arr5 = [42]
        sorted5 = tree_sort(arr5)
        assert sorted5 == [42]

        arr6 = []
        sorted6 = tree_sort(arr6)
        assert sorted6 == []

        print("All tree sort test cases passed!")

if __name__ == "__main__":
    run_tree_sort_tests()
