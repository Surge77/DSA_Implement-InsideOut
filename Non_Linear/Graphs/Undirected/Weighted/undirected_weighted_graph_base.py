from Linear.arrays import MyArray as Array
from Linear.singly_linked_list import SinglyLinkedList as LinkedList


class UndirectedWeightedGraph:
    """
    Implementation of an undirected weighted graph using adjacency lists.
    Each vertex maintains a LinkedList of (neighbor, weight) pairs.
    """

    def __init__(self, num_vertices: int):
        """
        Initialize the graph with a given number of vertices.

        Args:
            num_vertices (int): Number of vertices (0-based indexing).
        """
        self.n = num_vertices  # Total number of vertices
        self.adj = Array()  # Array of adjacency lists

        # Create an empty adjacency list for each vertex
        for _ in range(num_vertices):
            self.adj.append(LinkedList())

    def _validate_vertex(self, u: int) -> None:
        """Raise ValueError if the vertex u is out of bounds."""
        if u < 0 or u >= self.n:
            raise ValueError(f"Vertex {u} is out of bounds. Must be between 0 and {self.n - 1}.")

    def add_edge(self, u: int, v: int, weight: float) -> None:
        """
        Add an undirected edge (u, v) with a given weight.

        Time Complexity: O(deg(u) + deg(v)) due to search in adjacency lists.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        # Check if edge already exists
        if self.adj[u].search((v, weight)) != -1 or self.adj[v].search((u, weight)) != -1:
            return  # Avoid duplicate edges

        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def remove_edge(self, u: int, v: int) -> None:
        """
        Remove the undirected edge (u, v).

        Time Complexity: O(deg(u) + deg(v))
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        # Remove from u's adjacency list
        for i in range(len(self.adj[u])):
            if self.adj[u].get(i)[0] == v:
                self.adj[u].delete(i)
                break

        # Remove from v's adjacency list
        for i in range(len(self.adj[v])):
            if self.adj[v].get(i)[0] == u:
                self.adj[v].delete(i)
                break

    def has_edge(self, u: int, v: int) -> bool:
        """
        Check if there is an edge between u and v.

        Time Complexity: O(deg(u))
        """
        self._validate_vertex(u)
        for i in range(len(self.adj[u])):
            if self.adj[u].get(i)[0] == v:
                return True
        return False

    def neighbors(self, u: int):
        """
        Return all neighbors of vertex u along with weights as a list of (neighbor, weight).

        Time Complexity: O(deg(u))
        """
        self._validate_vertex(u)
        result = []
        for i in range(len(self.adj[u])):
            result.append(self.adj[u].get(i))
        return result

    def degree(self, u: int) -> int:
        """
        Return the degree (number of edges) of vertex u.

        Time Complexity: O(1) (LinkedList length tracking)
        """
        self._validate_vertex(u)
        return len(self.adj[u])

    def vertex_count(self) -> int:
        """Return the total number of vertices in the graph."""
        return self.n

    def edge_count(self) -> int:
        """
        Return the total number of edges in the graph.
        Since this is an undirected graph, each edge is stored twice.
        """
        count = 0
        for i in range(self.n):
            count += len(self.adj[i])
        return count // 2

    def edges(self):
        """
        Return a list of all edges in the graph as (u, v, weight).

        Time Complexity: O(V + E)
        """
        result = []
        for u in range(self.n):
            for i in range(len(self.adj[u])):
                v, w = self.adj[u].get(i)
                if u < v:  # To avoid duplicate edges
                    result.append((u, v, w))
        return result

    def __len__(self) -> int:
        """Return the number of vertices."""
        return self.n

    def __str__(self) -> str:
        """Return a readable string representation of the graph."""
        output = []
        for u in range(self.n):
            neighbors = ", ".join(f"{v}(w={w})" for v, w in self.neighbors(u))
            output.append(f"{u}: {neighbors}")
        return "\n".join(output)

    def __repr__(self) -> str:
        return f"UndirectedWeightedGraph(num_vertices={self.n})"


# ------------------- TEST CODE -------------------
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = UndirectedWeightedGraph(5)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(3, 4, 5)

    print("Graph Representation:")
    print(g)

    print("\nNeighbors of vertex 1:", g.neighbors(1))
    print("Has edge (0, 1):", g.has_edge(0, 1))
    print("Has edge (2, 4):", g.has_edge(2, 4))
    print("Degree of vertex 1:", g.degree(1))
    print("Total vertices:", g.vertex_count())
    print("Total edges:", g.edge_count())
    print("All edges:", g.edges())

    print("\nRemoving edge (0, 1)...")
    g.remove_edge(0, 1)
    print(g)
