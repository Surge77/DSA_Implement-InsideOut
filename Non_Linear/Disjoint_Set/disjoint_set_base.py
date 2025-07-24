from Linear.arrays import MyArray as Array


class DisjointSet:
    """
    Disjoint Set (Union-Find) Data Structure with optimizations:
    - Path Compression
    - Union by Rank
    """

    def __init__(self, size: int):
        """
        Initialize the disjoint set with `size` elements (0 to size-1).
        Each element is its own parent initially.

        Args:
            size (int): Number of elements in the disjoint set.
        """
        self.n = size
        self.parent = Array()
        self.rank = Array()  # Rank indicates the depth of the tree

        for i in range(size):
            self.parent.append(i)
            self.rank.append(0)

    def _validate(self, x: int):
        """Validate if x is a valid element."""
        if x < 0 or x >= self.n:
            raise ValueError(f"Element {x} is out of bounds (0 to {self.n - 1}).")

    def find(self, x: int) -> int:
        """
        Find the representative (root) of the set containing x.
        Uses Path Compression to flatten the tree.

        Time Complexity: Amortized O(α(n)), nearly constant.
        """
        self._validate(x)
        if self.parent.get(x) != x:
            self.parent.set(x, self.find(self.parent.get(x)))  # Path Compression
        return self.parent.get(x)

    def union(self, x: int, y: int):
        """
        Merge the sets containing x and y.
        Uses Union by Rank to keep the tree shallow.

        Time Complexity: Amortized O(α(n))
        """
        self._validate(x)
        self._validate(y)

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Attach smaller tree under the larger one
            if self.rank.get(root_x) < self.rank.get(root_y):
                self.parent.set(root_x, root_y)
            elif self.rank.get(root_x) > self.rank.get(root_y):
                self.parent.set(root_y, root_x)
            else:
                self.parent.set(root_y, root_x)
                self.rank.set(root_x, self.rank.get(root_x) + 1)

    def connected(self, x: int, y: int) -> bool:
        """
        Check if elements x and y are in the same set.

        Time Complexity: O(α(n))
        """
        return self.find(x) == self.find(y)

    def count_sets(self) -> int:
        """
        Count how many disjoint sets currently exist.
        """
        roots = set()
        for i in range(self.n):
            roots.add(self.find(i))
        return len(roots)

    def __len__(self):
        return self.n

    def __str__(self):
        return "Parents: " + ", ".join(str(self.parent.get(i)) for i in range(self.n))

    def __repr__(self):
        return f"DisjointSet(size={self.n})"


# ------------------- TEST CODE -------------------
if __name__ == "__main__":
    ds = DisjointSet(7)
    print("Initial State:", ds)

    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    print("After unions (0-1-2 and 3-4):", ds)

    print("Find(2):", ds.find(2))
    print("Find(4):", ds.find(4))
    print("Connected(0, 2):", ds.connected(0, 2))
    print("Connected(0, 3):", ds.connected(0, 3))
    print("Total Sets:", ds.count_sets())

    ds.union(2, 3)
    print("After union(2, 3):", ds)
    print("Connected(0, 4):", ds.connected(0, 4))
    print("Total Sets:", ds.count_sets())
