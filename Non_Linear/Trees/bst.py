class BSTNode:
    """
    Node for a Binary Search Tree.

    :param key: Value to store in the node.
    :param left: Left child (BSTNode or None).
    :param right: Right child (BSTNode or None).
    """
    def __init__(self, key: int):
        self.key = key
        # This just means "left and right can be either a BSTNode, or None."
        self.left: 'BSTNode' | None = None 
        self.right: 'BSTNode' | None = None

    def __repr__(self):
        return f'BSTNode({self.key})'


class BST:
    """
    Binary Search Tree implementation.
    """

    def __init__(self):
        self.root: BSTNode | None = None


    def insert(self, key: int) -> None:
        """
        Insert a key into the BST.

        Args:
            key (int): Value to insert.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(h), due to recursion stack
        """
        def _insert(node: BSTNode | None, key: int) -> BSTNode:
            if node is None:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # If key == node.key, do nothing (no duplicates)
            return node
        
        self.root = _insert(self.root, key)

    
    def search(self, key: int) -> BSTNode | None:
        """
        Search for a key in the BST.

        Args:
            key (int): Value to search for.

        Returns:
            BSTNode | None: Node containing the key, or None if not found.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(h), due to recursion stack
        """
        def _search(node: BSTNode | None, key: int) -> BSTNode | None:
            if node is None:
                return None
            if key == node.key:
                return node
            if key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        
        return _search(self.root, key)
    

    def contains(self, key: int) -> bool:
        """
        Check if a key exists in the BST.

        Args:
            key (int): Value to check for.

        Returns:
            bool: True if key exists, False otherwise.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(h), due to recursion stack
        """
        return self.search(key) is not None


    def min(self) -> BSTNode | None:
        """
        Find the node with the minimum key in the BST.

        Returns:
            BSTNode | None: The node with the smallest key, or None if the tree is empty.

        Time Complexity: O(h), where h = height of tree (worst case, skewed)
        Space Complexity: O(1)
        """
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current

    def max(self) -> BSTNode | None:
        """
        Find the node with the maximum key in the BST.

        Returns:
            BSTNode | None: The node with the largest key, or None if the tree is empty.

        Time Complexity: O(h), where h = height of tree (worst case, skewed)
        Space Complexity: O(1)
        """
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current

    def delete(self, key: int) -> None:
        """
        Delete a key from the BST.

        Args:
            key (int): Value to delete.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(h), due to recursion stack
        """

        def _delete(node: BSTNode | None, key: int) -> BSTNode | None:
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # Node with two children: Get inorder successor (min value in right subtree)
                temp = node.right
                while temp.left:
                    temp = temp.left
                node.key = temp.key  # Copy inorder successor's key
                node.right = _delete(node.right, temp.key)  # Delete inorder successor
            return node

        self.root = _delete(self.root, key)

    # Tree traversals

    def inorder(self) -> list[int]:
        """
        Perform inorder traversal of the BST.

        Returns:
            list[int]: List of keys in sorted order.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h) for recursion stack, where h = height of tree
        """
        result = []
        def _inorder(node: BSTNode | None):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result
    

    def preorder(self) -> list[int]:
        """
        Perform pre order traversal of the BST.

        Returns:
            list[int]: List of keys in pre order (root, left, right) order.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        result = []
        def _preorder(node: BSTNode | None):
            if node:
                result.append(node.key)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result
    


    def postorder(self) -> list[int]:
        """
        Perform postorder traversal of the BST.

        Returns:
            list[int]: List of keys in postorder (left, right, root) order.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        result = []
        def _postorder(node: BSTNode | None):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.key)
        _postorder(self.root)
        return result
    

    def level_order(self) -> list[int]:
        """
        Perform level order (breadth-first) traversal of the BST (no built-in queue).

        Returns:
            list[int]: List of keys in level order.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(n), for the queue in the worst case (last level full)
        """
        result = []
        if not self.root:
            return result
        queue = [self.root]  # Simple list for the queue
        front = 0  # Points to the front of the queue
        while front < len(queue):
            node = queue[front]
            front += 1
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


    def height(self) -> int:
        """
        Compute the height of the BST.

        Returns:
            int: Height (max depth) of the tree; -1 for empty tree.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        def _height(node: BSTNode | None) -> int:
            if node is None:
                return -1  # By convention, empty subtree has height -1
            left_height = _height(node.left)
            right_height = _height(node.right)
            return 1 + max(left_height, right_height)
        return _height(self.root)


    def count_nodes(self) -> int:
        """
        Count the total number of nodes in the BST.

        Returns:
            int: Total number of nodes in the tree.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        def _count(node: BSTNode | None) -> int:
            if node is None:
                return 0
            return 1 + _count(node.left) + _count(node.right)
        return _count(self.root)
    

    def is_empty(self) -> bool:
        """
        Check if the BST is empty.

        Returns:
            bool: True if the BST is empty, False otherwise.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.root is None
    

    def find_parent(self, key: int) -> BSTNode | None:
        """
        Find the parent of the node with the given key.

        Args:
            key (int): The key of the node whose parent to find.

        Returns:
            BSTNode | None: The parent node, or None if key is at root or not found.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(1)
        """
        parent = None
        current = self.root
        while current:
            if key < current.key:
                parent, current = current, current.left
            elif key > current.key:
                parent, current = current, current.right
            else:
                return parent  # Found the key, return its parent
        return None  # Key not found, return None
    

    def leaf_count(self) -> int:
        """
        Count the number of leaf nodes in the BST.

        Returns:
            int: Number of leaf nodes.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        def _leaf_count(node: BSTNode | None) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return _leaf_count(node.left) + _leaf_count(node.right)
        return _leaf_count(self.root)
    

    def sum_nodes(self) -> int:
        """
        Calculate the sum of all node keys in the BST.

        Returns:
            int: Sum of all keys in the tree.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        def _sum(node: BSTNode | None) -> int:
            if node is None:
                return 0
            return node.key + _sum(node.left) + _sum(node.right)
        return _sum(self.root)
    

    def node_depth(self, key: int) -> int:
        """
        Find the depth (distance from root) of the node with the given key.

        Args:
            key (int): The key of the node whose depth to find.

        Returns:
            int: Depth (0 for root, 1 for root's child, etc.), -1 if key not found.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(1)
        """
        current = self.root
        depth = 0
        while current:
            if key == current.key:
                return depth
            elif key < current.key:
                current = current.left
            else:
                current = current.right
            depth += 1
        return -1  # Not found
    

    def path_to_node(self, key: int) -> list[int]:
        """
        Find the path from the root to the node with the given key.

        Args:
            key (int): The key of the node to find the path to.

        Returns:
            list[int]: List of keys forming the path from root to the node. Empty if not found.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(h), for path storage
        """
        path = []
        current = self.root
        while current:
            path.append(current.key)
            if key == current.key:
                return path
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return []  # Not found
    

    def is_balanced(self) -> bool:
        """
        Check if the BST is height-balanced.

        The absolute height difference of left subtree and right subtree must be 0 or 1 to be balanced according to the definition

        For a node to be balanced:

        Calculate the height of its left subtree (h_left)

        Calculate the height of its right subtree (h_right)

        abs(h_left - h_right)

        Returns:
            bool: True if balanced, False otherwise.

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        def _check(node: BSTNode | None) -> tuple[bool, int]:
            if node is None:
                return True, -1  # (is_balanced, height)
            left_balanced, left_height = _check(node.left)
            right_balanced, right_height = _check(node.right)
            balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )
            return balanced, 1 + max(left_height, right_height)
        balanced, _ = _check(self.root)
        return balanced
    

    def lowest_common_ancestor(self, key1: int, key2: int) -> BSTNode | None:
        """
        Find the lowest common ancestor (LCA) of two keys in the BST.

        Args:
            key1 (int): First key.
            key2 (int): Second key.

        Returns:
            BSTNode | None: The LCA node, or None if either key is not found.

        Time Complexity: O(h), where h = height of tree
        Space Complexity: O(1)
        """
        current = self.root
        while current:
            if key1 < current.key and key2 < current.key:
                current = current.left
            elif key1 > current.key and key2 > current.key:
                current = current.right
            else:
                # This is the split point, so current is LCA
                # Optional: Check both keys exist if strict correctness is desired
                if self._exists(current, key1) and self._exists(current, key2):
                    return current
                else:
                    return None
        return None

    def _exists(self, node: BSTNode | None, key: int) -> bool:
        """
        Helper function to check if a key exists in the subtree.
        """
        while node:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False


    def diameter(self) -> int:
        """
        Calculate the diameter (longest path between any two nodes) of the BST.

        Returns:
            int: Diameter of the tree (number of edges in the longest path).

        Time Complexity: O(n), where n = number of nodes
        Space Complexity: O(h), due to recursion stack (h = height of tree)
        """
        def _diameter(node: BSTNode | None) -> tuple[int, int]:
            if node is None:
                return -1, 0  # (height, diameter)
            left_height, left_diameter = _diameter(node.left)
            right_height, right_diameter = _diameter(node.right)
            curr_height = 1 + max(left_height, right_height)
            # Path through current node = left_height + right_height + 2
            curr_diameter = max(left_diameter, right_diameter, left_height + right_height + 2)
            return curr_height, curr_diameter
        _, dia = _diameter(self.root)
        return dia
    

    def serialize(self) -> list[int | None]:
        """
        Serialize the BST to a list using level order traversal with None placeholders.

        This serialize() method converts your entire BST into a flat Python list (array), including None placeholders for missing children, using level order traversal.

        Returns:
            list[int | None]: Serialized representation of the tree.

        Time Complexity: O(n), where n = number of nodes (including Nones)
        Space Complexity: O(n)
        """
        result = []
        queue = [self.root]
        front = 0
        while front < len(queue):
            node = queue[front]
            front += 1
            if node is not None:
                result.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values for compactness
        while result and result[-1] is None:
            result.pop()
        return result
    

    @staticmethod
    def deserialize(data: list[int | None]) -> 'BST':
        """
        Deserialize a level-order array with Nones back to a BST.

        Converts the python list back to a tree

        Args:
            data (list[int | None]): Serialized tree as produced by serialize().

        Returns:
            BST: A new BST with the same structure.

        Time Complexity: O(n), where n = number of elements in data
        Space Complexity: O(n)
        """
        if not data or data[0] is None:
            return BST()

        root = BSTNode(data[0])
        bst = BST()
        bst.root = root
        queue = [root]
        idx = 1  # Index in data list

        while queue and idx < len(data):
            current = queue.pop(0)
            # Left child
            if idx < len(data) and data[idx] is not None:
                current.left = BSTNode(data[idx])
                queue.append(current.left)
            idx += 1
            # Right child
            if idx < len(data) and data[idx] is not None:
                current.right = BSTNode(data[idx])
                queue.append(current.right)
            idx += 1

        return bst

