from Linear.arrays import MyArray as Array
from Linear.singly_linked_list import SinglyLinkedList as LinkedList

from Linear.arrays import MyArray as Array
from Linear.singly_linked_list import SinglyLinkedList as LinkedList


class DirectedWeightedGraph:
    """
    Directed Weighted Graph implementation using adjacency lists.
    Each vertex maintains a linked list of (neighbor, weight) pairs.
    """

    def __init__(self, num_vertices: int):
        """
        Initialize a directed weighted graph with the specified number of vertices.

        Args:
            num_vertices (int): Number of vertices (0-based: 0 to num_vertices-1).
        """
        self.n = num_vertices
        self.adj = Array()

        # Each vertex gets its own adjacency list
        for _ in range(num_vertices):
            self.adj.append(LinkedList())

    def _validate_vertex(self, u: int):
        """Raise ValueError if the vertex is out of bounds."""
        if u < 0 or u >= self.n:
            raise ValueError(f"Vertex {u} is out of bounds. Valid range: 0 to {self.n - 1}")

    def add_edge(self, u: int, v: int, weight: float):
        """
        Add a directed edge u -> v with the given weight.

        Time Complexity: O(deg(u))
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        # Check if edge already exists
        for i in range(len(self.adj[u])):
            neighbor, _ = self.adj[u].get(i)
            if neighbor == v:
                return  # Edge already exists

        self.adj[u].append((v, weight))

    def remove_edge(self, u: int, v: int):
        """
        Remove the directed edge u -> v if it exists.

        Time Complexity: O(deg(u))
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        for i in range(len(self.adj[u])):
            neighbor, _ = self.adj[u].get(i)
            if neighbor == v:
                self.adj[u].delete(i)
                return

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if there is a directed edge u -> v.

        Time Complexity: O(deg(u))
        """
        self._validate_vertex(u)
        for i in range(len(self.adj[u])):
            neighbor, _ = self.adj[u].get(i)
            if neighbor == v:
                return True
        return False

    def neighbors(self, u: int):
        """
        Return a list of (neighbor, weight) pairs for vertex u.

        Time Complexity: O(deg(u))
        """
        self._validate_vertex(u)
        result = []
        for i in range(len(self.adj[u])):
            result.append(self.adj[u].get(i))
        return result

    def edges(self):
        """
        Return a list of all directed edges (u, v, weight).

        Time Complexity: O(V + E)
        """
        result = []
        for u in range(self.n):
            for i in range(len(self.adj[u])):
                v, w = self.adj[u].get(i)
                result.append((u, v, w))
        return result

    def vertex_count(self) -> int:
        """Return the total number of vertices."""
        return self.n

    def edge_count(self) -> int:
        """Return the total number of directed edges."""
        count = 0
        for u in range(self.n):
            count += len(self.adj[u])
        return count

    def __len__(self):
        return self.n

    def __str__(self):
        """
        String representation of the graph.
        Each vertex lists its outgoing edges with weights.
        """
        lines = []
        for u in range(self.n):
            neighbors = ", ".join(f"{v}(w={w})" for v, w in self.neighbors(u))
            lines.append(f"{u}: {neighbors}")
        return "\n".join(lines)

    def __repr__(self):
        return f"DirectedWeightedGraph(num_vertices={self.n})"


# ------------------- TEST CODE -------------------
if __name__ == "__main__":
    g = DirectedWeightedGraph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 1)

    print("Graph Representation:")
    print(g)

    print("\nEdges:", g.edges())
    print("Has edge (0 -> 1):", g.has_edge(0, 1))
    print("Has edge (1 -> 0):", g.has_edge(1, 0))
    print("Neighbors of 0:", g.neighbors(0))
    print("Total Vertices:", g.vertex_count())
    print("Total Edges:", g.edge_count())

    print("\nRemoving edge (0 -> 2)...")
    g.remove_edge(0, 2)
    print(g)
