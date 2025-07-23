from Linear.arrays import MyArray as Array
from Linear.singly_linked_list import SinglyLinkedList as LinkedList


class DirectedGraph:
    def __init__(self, num_vertices: int):
        """
        Initialize a directed, unweighted graph with the specified number of vertices.
        Each vertex's adjacency list stores its OUTGOING neighbors.

        Args:
            num_vertices (int): Number of vertices (vertices are 0-based: 0 to num_vertices-1)

        Example:
            g = DirectedGraph(5)  # Creates vertices 0, 1, 2, 3, 4, each with an empty adjacency list
        """
        self.n = num_vertices  # number of vertices
        self.adj = Array()     # Use your custom Array to hold LinkedLists

        for _ in range(num_vertices):
            self.adj.append(LinkedList())  # Each vertex gets its own outgoing neighbor list

    
    def _validate_vertex(self, u: int) -> None:
      if not (0 <= u < self.n):
          raise ValueError(f"Vertex {u} is out of bounds [0, {self.n-1}]")
      

    def add_edge(self, u: int, v: int) -> None:
      """
      Adds a directed edge from vertex u to vertex v.
      Does nothing if the edge already exists.

      Args:
          u (int): Source vertex.
          v (int): Target vertex.

      Raises:
          ValueError: If u or v is out of bounds.

      Time Complexity: O(k), where k is the out-degree of u.
      """
      self._validate_vertex(u)
      self._validate_vertex(v)
      if self.adj[u].search(v) < 0:  # Only add if v is not already a neighbor of u
          self.adj[u].insert(0, v)   # Insert at the head (O(1))


    def remove_edge(self, u: int, v: int) -> None:
      """
      Removes the directed edge from vertex u to vertex v, if it exists.

      Args:
          u (int): Source vertex.
          v (int): Target vertex.

      Raises:
          ValueError: If u or v is out of bounds.

      Time Complexity: O(k), where k is the out-degree of u.
      """
      self._validate_vertex(u)
      self._validate_vertex(v)
      idx = self.adj[u].search(v)
      if idx >= 0:
          self.adj[u].delete(idx)  # Remove v from u's neighbor list


    def has_edge(self, u: int, v: int) -> bool:
        """
        Returns True if there is a directed edge from u to v, otherwise False.

        Args:
            u (int): Source vertex.
            v (int): Target vertex.

        Raises:
            ValueError: If u or v is out of bounds.

        Time Complexity: O(k), where k is the out-degree of u.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self.adj[u].search(v) >= 0



