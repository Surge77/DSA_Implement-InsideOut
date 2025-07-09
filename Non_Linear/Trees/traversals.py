from Non_Linear.Trees.binary_tree import Node, BinaryTree

class TreeTraversals:
    @staticmethod
    def iterative_inorder(root: 'Node') -> list[int]:
      """
      Performs an iterative inorder traversal (Left -> Root -> Right).

      Args:
          root (Node): The root of the binary tree.

      Returns:
          list[int]: A list of node values in inorder sequence.

      Time Complexity: O(n)
      Space Complexity: O(h) — h = height of the tree (stack depth)
      """
      stack, result = [], []
      current = root

      while current or stack:
          # Reach the leftmost Node of the current Node
          while current:
              stack.append(current)
              current = current.left

          # Current is None here, so we backtrack
          current = stack.pop()
          result.append(current.value)

          # Visit the right subtree
          current = current.right

      return result

    @staticmethod
    def iterative_preorder(root: 'Node') -> list[int]:
        """
        Performs an iterative preorder traversal (Root -> Left -> Right).

        Args:
            root (Node): The root of the binary tree.

        Returns:
            list[int]: A list of node values in preorder sequence.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return []

        stack, result = [root], []

        while stack:
            current = stack.pop()
            result.append(current.value)

            # Push right first so that left is processed first
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result

    @staticmethod
    def iterative_postorder(root: 'Node') -> list[int]:
        """
        Performs an iterative postorder traversal (Left -> Right -> Root)
        using a modified reverse preorder trick.

        Args:
            root (Node): The root of the binary tree.

        Returns:
            list[int]: A list of node values in postorder sequence.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return []

        stack, result = [root], []

        while stack:
            current = stack.pop()
            result.append(current.value)

            # Push left first so right is processed before left
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        # Reverse the process to get left → right → root
        return result[::-1]
