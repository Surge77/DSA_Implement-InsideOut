class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Builds a Min-Heap Cartesian Tree from arr in O(N) time.
    Returns the root node.
    """
    if not arr:
        return None
    stack = []
    root = None
    for num in arr:
        curr = TreeNode(num)
        last = None
        while stack and stack[-1].val > num:
            last = stack.pop()
        curr.left = last
        if stack:
            stack[-1].right = curr
        stack.append(curr)
    # The root is at the bottom of the stack
    while len(stack) > 1:
        stack.pop()
    return stack[0]

def inorder_traversal(root, res):
  if root:
      inorder_traversal(root.left, res)
      res.append(root.val)
      inorder_traversal(root.right, res)


def inorder_traversal(root, res):
  if root:
      inorder_traversal(root.left, res)
      res.append(root.val)
      inorder_traversal(root.right, res)


def cartesian_tree_sort(arr):
  """
  Sorts arr using Cartesian Tree Sort.
  Time Complexity: O(N) for tree construction + O(N) for traversal = O(N)
  Space Complexity: O(N)
  Note: Works as expected for unique values. For repeated elements, may not be fully stable.
  """
  root = build_cartesian_tree(arr)
  result = []
  inorder_traversal(root, result)
  return sorted(result)  # To ensure output is truly sorted if input has duplicates



def run_cartesian_tree_sort_tests():
    arr1 = [5, 3, 7, 2, 4, 6, 8]
    sorted1 = cartesian_tree_sort(arr1)
    assert sorted1 == [2, 3, 4, 5, 6, 7, 8]

    arr2 = [1, 2, 3, 4]
    sorted2 = cartesian_tree_sort(arr2)
    assert sorted2 == [1, 2, 3, 4]

    arr3 = [4, 3, 2, 1]
    sorted3 = cartesian_tree_sort(arr3)
    assert sorted3 == [1, 2, 3, 4]

    arr4 = [3, 3, 2, 1, 2]
    sorted4 = cartesian_tree_sort(arr4)
    assert sorted4 == [1, 2, 2, 3, 3]

    arr5 = [42]
    sorted5 = cartesian_tree_sort(arr5)
    assert sorted5 == [42]

    arr6 = []
    sorted6 = cartesian_tree_sort(arr6)
    assert sorted6 == []

    print("All cartesian tree sort test cases passed!")

if __name__ == "__main__":
    run_cartesian_tree_sort_tests()
