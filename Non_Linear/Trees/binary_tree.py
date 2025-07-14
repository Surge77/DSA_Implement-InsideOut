class Node:
    """
    Represents a single node in a binary tree.

    Attributes:
        value (int): The data held by the node.
        left (Node): Pointer to the left child node.
        right (Node): Pointer to the right child node.
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    A class to represent a binary tree with insertion and traversal methods.

    Attributes:
        root (Node): The root node of the tree.
    """
    def __init__(self):
        self.root = None


    def insert(self, value: int) -> None:
        """
        Inserts a new node into the binary tree in level-order fashion.

        Time Complexity: O(n)
        Space Complexity: O(n) for queue

        Args:
            value (int): The value to insert into the tree.
        """
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)


    def inorder(self) -> list[int]:
        """
        Performs inorder traversal: Left -> Root -> Right

        Returns:
            list[int]: Inorder sequence of node values.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def _inorder(node: Node) -> list[int]:
            if not node:
                return []
            return _inorder(node.left) + [node.value] + _inorder(node.right)

        return _inorder(self.root)


    def preorder(self) -> list[int]:
        """
        Performs preorder traversal: Root -> Left -> Right

        Returns:
            list[int]: Preorder sequence of node values.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def _preorder(node: Node) -> list[int]:
            if not node:
                return []
            return [node.value] + _preorder(node.left) + _preorder(node.right)

        return _preorder(self.root)


    def postorder(self) -> list[int]:
        """
        Performs postorder traversal: Left -> Right -> Root

        Returns:
            list[int]: Postorder sequence of node values.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def _postorder(node: Node) -> list[int]:
            if not node:
                return []
            return _postorder(node.left) + _postorder(node.right) + [node.value]

        return _postorder(self.root)


    def level_order_traversal(self) -> list[int]:
        """
        Performs a level-order traversal (BFS) and returns list of values.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Returns:
            list[int]: Values in level-order.
        """
        if self.root is None:
            return []

        result = []
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result



    def search(self, target: int) -> bool:
        """
        Searches for a value in the binary tree using level-order traversal.

        Args:
            target (int): The value to search for.

        Returns:
            bool: True if found, False otherwise.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not self.root:
            return False

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.value == target:
                return True

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return False
    


    def height(self) -> int:
        """
        Calculates the height of the binary tree.

        Returns:
            int: Height of the tree (0 if empty).

        Time Complexity: O(n)
        Space Complexity: O(h) — due to recursion stack (h = height of tree)
        """
        def _height(node: Node) -> int:
            if not node:
                return 0
            left_height = _height(node.left)
            right_height = _height(node.right)
            return 1 + max(left_height, right_height)

        return _height(self.root)
        

    # No recursion in this method just iteration + level order traversal (BFS)
    def delete(self, target: int) -> bool:
        """
        Deletes a node by value using level-order logic.
        Replaces the node with the deepest rightmost node.

        Args:
            target (int): Value to delete.

        Returns:
            bool: True if deletion successful, False otherwise.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not self.root:
            return False

        if self.root.left is None and self.root.right is None:
            if self.root.value == target:
                self.root = None
                return True
            return False

        queue = [self.root]
        target_node = None
        last_node = None
        parent_of_last = None

        # Level-order traversal to find target and deepest node
        while queue:
            current = queue.pop(0)

            if current.value == target:
                target_node = current

            # In a typical binary tree each node has only reference to its children- not to its parent so you must remember parent as you traverse
            # We append both left and right children to the queue to make sure every node is visited (level by level), so you can find both the target and the deepest rightmost node—essential for correct deletion in a general binary tree!
            if current.left:
                parent_of_last = current
                queue.append(current.left)
            if current.right:
                parent_of_last = current
                queue.append(current.right)

            last_node = current  # Always update to keep deepest

        if target_node is None:
            return False  # Not found

        # Replace value
        target_node.value = last_node.value

        # Remove deepest node
        if parent_of_last.right == last_node:
            parent_of_last.right = None
        elif parent_of_last.left == last_node:
            parent_of_last.left = None

        return True


    def count_leaf_nodes(self) -> int:
        """
        Counts the number of leaf nodes in the binary tree.

        A leaf node is defined as a node with no left or right children.

        Returns:
            int: Total number of leaf nodes.

        Time Complexity: O(n)
        Space Complexity: O(h) — due to recursion stack (h = height of tree)
        """
        def _count_leaves(node: Node) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return _count_leaves(node.left) + _count_leaves(node.right)

        return _count_leaves(self.root)


    
    def diameter(self) -> int:
        """
        Calculates the diameter of the binary tree.

        Diameter is defined as the number of nodes on the longest path
        between any two nodes in the tree.

        Returns:
            int: Diameter of the tree.

        Time Complexity: O(n)
        Space Complexity: O(h) — h = height of tree (recursion stack)
        """
        self.max_diameter = 0

        def _dfs(node: Node) -> int:
            if not node:
                return 0

            left_height = _dfs(node.left)
            right_height = _dfs(node.right)

            # Local diameter = left + right + 1 (this node included)
            local_diameter = left_height + right_height + 1
            self.max_diameter = max(self.max_diameter, local_diameter)

            # Return height of this node
            return 1 + max(left_height, right_height)

        _dfs(self.root)
        return self.max_diameter



    # Mirroring a binary tree means swapping left and right children of all nodes
    def mirror(self) -> None:
        """
        Mirrors the binary tree in-place by swapping left and right subtrees.

        Time Complexity: O(n)
        Space Complexity: O(h) — h = height of tree (recursion stack)
        """
        def _mirror(node: Node) -> None:
            if not node:
                return

            # Swap left and right
            node.left, node.right = node.right, node.left

            # Recursion on subtrees
            _mirror(node.left)
            _mirror(node.right)

        _mirror(self.root)



    # A tree is symmetric if its left and right subtrees are mirror images of each other.
    # The left subtree is a mirror reflection of the right subtree, both in shape and values.
    def is_symmetric(self) -> bool:
        """
        Checks whether the tree is symmetric around its center.

        Returns:
            bool: True if symmetric, False otherwise.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _is_mirror(n1: Node, n2: Node) -> bool:
            if not n1 and not n2: # if both children of root are none it becomes symmetric and returns True
                return True
            if not n1 or not n2: # If one of the children is present it becomes Asymmetric
                return False
            if n1.value != n2.value: # Both children exist, but values differ — not a mirror
                return False

            return _is_mirror(n1.left, n2.right) and _is_mirror(n1.right, n2.left)

        return _is_mirror(self.root.left, self.root.right) if self.root else True # Uf the tree is empty it automatically becomes symmetric



    def lowest_common_ancestor(self, p_val: int, q_val: int) -> int:
        """
        Finds the lowest common ancestor of two nodes in the binary tree.

        Args:
            p_val (int): Value of the first node.
            q_val (int): Value of the second node.

        Returns:
            int: Value of the lowest common ancestor node.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _lca(node: Node) -> Node:
            if not node:
                return None # Base case: empty tree

            if node.value == p_val or node.value == q_val:
                return node

            left = _lca(node.left)
            right = _lca(node.right)

            if left and right:
                return node  # This node is the LCA

            return left if left else right

        lca_node = _lca(self.root)
        return lca_node.value if lca_node else None



    def path_to_node(self, target: int) -> list[int]:
        """
        Finds the path from root to the node with the given value.

        Args:
            target (int): The target node's value.

        Returns:
            list[int]: List of node values from root to target. Empty if not found.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _dfs_path(node: Node, path: list[int]) -> bool:
            if not node:
                return False

            path.append(node.value)

            if node.value == target:
                return True

            if _dfs_path(node.left, path) or _dfs_path(node.right, path):
                return True

            path.pop()  # backtrack
            return False

        path = []
        _dfs_path(self.root, path)
        return path



    def max_path_sum(self) -> int:
        """
        Calculates the maximum path sum in the binary tree.

        A path can start and end at any node.

        Returns:
            int: The maximum path sum.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        self.max_sum = float('-inf')

        def _dfs(node: Node) -> int:
            if not node:
                return 0

            # Get max gain from left and right (ignore negatives)
            left_gain = max(_dfs(node.left), 0)
            right_gain = max(_dfs(node.right), 0)

            # Local path sum passing through this node
            local_sum = node.value + left_gain + right_gain

            # Update global max
            self.max_sum = max(self.max_sum, local_sum)

            # Return one side to parent
            return node.value + max(left_gain, right_gain)

        _dfs(self.root)
        return self.max_sum



    def max_root_to_leaf_sum(self) -> int:
        """
        Finds the maximum path sum from root to any leaf.

        Returns:
            int: Maximum sum from root to leaf.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _dfs(node: Node) -> int:
            if not node:
                return float('-inf')  # Don't take null paths

            if not node.left and not node.right:
                return node.value  # Leaf node

            return node.value + max(_dfs(node.left), _dfs(node.right))

        return _dfs(self.root)



    def min_root_to_leaf_sum(self) -> int:
        """
        Finds the minimum path sum from root to any leaf.

        Returns:
            int: Minimum sum from root to leaf.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def _dfs(node: Node) -> int:
            if not node:
                return float('inf')  # Invalid path

            if not node.left and not node.right:
                return node.value  # Leaf node

            left_sum = _dfs(node.left)
            right_sum = _dfs(node.right)

            return node.value + min(left_sum, right_sum)

        return _dfs(self.root) if self.root else 0
    
    
    def min_root_to_leaf_path(self) -> list[int]:
        """
        Finds the actual path from root to leaf with the minimum sum.

        Returns:
            list[int]: List of node values representing the minimum path.

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not self.root:
            return []

        self.min_sum = float('inf')
        self.min_path = []

        def _dfs(node: Node, path: list[int], current_sum: int):
            if not node:
                return

            path.append(node.value)
            current_sum += node.value

            # If leaf node, check and update min
            if not node.left and not node.right:
                if current_sum < self.min_sum:
                    self.min_sum = current_sum
                    self.min_path = path.copy()

            _dfs(node.left, path, current_sum)
            _dfs(node.right, path, current_sum)

            path.pop()  # backtrack

        _dfs(self.root, [], 0)
        return self.min_path
