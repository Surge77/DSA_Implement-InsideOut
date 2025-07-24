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



    def neighbors(self, u: int):
        """
        Returns a list of all outgoing neighbors of vertex u.

        Args:
            u (int): The vertex whose neighbors we want.

        Raises:
            ValueError: If u is out of bounds.

        Returns:
            List[int]: A list of all vertices v such that u -> v.
        """
        self._validate_vertex(u)
        result = []
        adjacency_list = self.adj.get(u)  # Get the LinkedList for vertex u
        for i in range(len(adjacency_list)):
            result.append(adjacency_list.get(i))
        return result
    

    def out_degree(self, u: int) -> int:
        """
        Returns the number of outgoing edges from vertex u.

        Args:
            u (int): The vertex whose out-degree we want.

        Raises:
            ValueError: If u is out of bounds.

        Returns:
            int: Out-degree of vertex u.
        """
        self._validate_vertex(u)
        return len(self.adj.get(u))
    

    # dunder methods

    def __len__(self) -> int:
        """Returns the number of vertices in the graph."""
        return self.n


    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the graph.
        Example:
            Graph with 4 vertices:
            0: 2 -> 1
            1: 2
            2: 3
            3: (empty)
        """
        lines = [f"Graph with {self.n} vertices:"]
        for u in range(self.n):
            neighbors = [str(self.adj.get(u).get(i)) for i in range(len(self.adj.get(u)))]
            if neighbors:
                lines.append(f"  {u}: " + " -> ".join(neighbors))
            else:
                lines.append(f"  {u}: (empty)")
        return "\n".join(lines)


    def __repr__(self) -> str:
        """
        Returns a developer-friendly string with vertices and edges.
        Example:
            DirectedGraph(num_vertices=4, edges=[(0, 1), (0, 2), (1, 2), (2, 3)])
        """
        edges = []
        for u in range(self.n):
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                edges.append(f"({u}, {v})")
        return f"DirectedGraph(num_vertices={self.n}, edges=[{', '.join(edges)}])"


    def __contains__(self, vertex: int) -> bool:
        """Checks if a vertex exists in the graph (0 <= vertex < n)."""
        return 0 <= vertex < self.n


    def __iter__(self):
        """Iterates over all vertices."""
        return iter(range(self.n))


    def in_degree(self, v: int) -> int:
        """
        Returns the number of incoming edges to vertex v.

        Args:
            v (int): The vertex whose in-degree we want.

        Raises:
            ValueError: If v is out of bounds.

        Returns:
            int: In-degree of vertex v.
        """
        self._validate_vertex(v)
        count = 0
        for u in range(self.n):
            if self.adj.get(u).search(v) >= 0:
                count += 1
        return count


    def vertex_count(self) -> int:
        """
        Returns the number of vertices in the graph.

        Returns:
            int: Number of vertices (n).
        """
        return self.n


    def edge_count(self) -> int:
        """
        Returns the total number of directed edges in the graph.

        Returns:
            int: Total number of directed edges.
        """
        total = 0
        for u in range(self.n):
            total += len(self.adj.get(u))  # Outgoing edges from u
        return total
    


    def bfs(self, start: int):
        """
        Performs Breadth-First Search (BFS) starting from 'start'.
        Prints vertices in the order they are visited.

        Args:
            start (int): The starting vertex.

        Raises:
            ValueError: If start is out of bounds.

        Time Complexity: O(V + E)
        """
        self._validate_vertex(start)
        visited = [False] * self.n
        queue = Array()

        queue.append(start)
        visited[start] = True

        print(f"BFS starting from vertex {start}: ", end="")
        while len(queue) > 0:
            u = queue.get(0)  # Dequeue from front
            queue.delete(0)
            print(u, end=" ")

            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        print()  # newline at the end


    def dfs(self, start: int):
        """
        Performs Depth-First Search (DFS) starting from 'start'.
        Prints vertices in the order they are visited.

        Args:
            start (int): The starting vertex.

        Raises:
            ValueError: If start is out of bounds.

        Time Complexity: O(V + E)
        """
        self._validate_vertex(start)
        visited = [False] * self.n

        def _dfs(u):
            visited[u] = True
            print(u, end=" ")
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                if not visited[v]:
                    _dfs(v)

        print(f"DFS starting from vertex {start}: ", end="")
        _dfs(start)
        print()  # newline at the end


    def has_path(self, u: int, v: int) -> bool:
        """
        Checks if there is a path from vertex u to vertex v in the directed graph.

        Args:
            u (int): Start vertex.
            v (int): Target vertex.

        Raises:
            ValueError: If u or v is out of bounds.

        Returns:
            bool: True if there is a path from u to v, else False.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)

        if u == v:
            return True

        visited = [False] * self.n
        queue = Array()
        queue.append(u)
        visited[u] = True

        while len(queue) > 0:
            current = queue.get(0)
            queue.delete(0)

            if current == v:
                return True

            for i in range(len(self.adj.get(current))):
                neighbor = self.adj.get(current).get(i)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False


    def connected_components(self):
        """
        Finds all Strongly Connected Components (SCCs) in the directed graph
        using Kosaraju's algorithm.

        Returns:
            List[List[int]]: A list of SCCs, each SCC is a list of vertices.

        Time Complexity: O(V + E)
        """
        visited = [False] * self.n
        stack = []

        # Step 1: Fill vertices in stack according to their finishing times
        def dfs_fill(u):
            visited[u] = True
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                if not visited[v]:
                    dfs_fill(v)
            stack.append(u)

        for u in range(self.n):
            if not visited[u]:
                dfs_fill(u)

        # Step 2: Reverse the graph
        reversed_graph = DirectedGraph(self.n)
        for u in range(self.n):
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                reversed_graph.add_edge(v, u)

        # Step 3: Perform DFS on reversed graph using the stack order
        visited = [False] * self.n
        scc_list = []

        def dfs_collect(u, component):
            visited[u] = True
            component.append(u)
            for i in range(len(reversed_graph.adj.get(u))):
                v = reversed_graph.adj.get(u).get(i)
                if not visited[v]:
                    dfs_collect(v, component)

        while stack:
            u = stack.pop()
            if not visited[u]:
                component = []
                dfs_collect(u, component)
                scc_list.append(component)

        return scc_list


    def topological_sort(self):
        """
        Returns a topological order of vertices in the directed graph.
        Works only if the graph is a DAG (Directed Acyclic Graph).

        Raises:
            ValueError: If the graph has a cycle.

        Returns:
            List[int]: Vertices in topological order.
        """
        visited = [0] * self.n  # 0 = unvisited, 1 = visiting, 2 = visited
        stack = []
        has_cycle = [False]  # To detect cycles (use list as mutable flag)

        def dfs(u):
            if visited[u] == 1:  # back edge detected
                has_cycle[0] = True
                return
            if visited[u] == 2:
                return
            visited[u] = 1  # mark as visiting
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                dfs(v)
            visited[u] = 2  # mark as visited
            stack.append(u)

        for u in range(self.n):
            if visited[u] == 0:
                dfs(u)

        if has_cycle[0]:
            raise ValueError("Graph contains a cycle. Topological sort not possible.")

        stack.reverse()
        return stack


    def has_cycle(self) -> bool:
        """
        Detects if the directed graph contains a cycle.

        Returns:
            bool: True if a cycle exists, otherwise False.

        Time Complexity: O(V + E)
        """
        visited = [False] * self.n
        rec_stack = [False] * self.n

        def dfs(u: int) -> bool:
            visited[u] = True
            rec_stack[u] = True

            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                if not visited[v]:
                    if dfs(v):
                        return True
                elif rec_stack[v]:  # Back-edge found
                    return True

            rec_stack[u] = False  # Remove from recursion stack
            return False

        for u in range(self.n):
            if not visited[u]:
                if dfs(u):
                    return True
        return False


    def clone(self):
        """
        Creates and returns a deep copy of the directed graph.

        Returns:
            DirectedGraph: A new graph that is a deep copy of the current one.

        Time Complexity: O(V + E)
        """
        new_graph = DirectedGraph(self.n)
        for u in range(self.n):
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                new_graph.add_edge(u, v)
        return new_graph
    

    def clear(self):
        """
        Removes all edges from the graph but keeps all vertices.

        Time Complexity: O(V)
        """
        for u in range(self.n):
            self.adj.set(u, LinkedList())  # Replace each adjacency list with a new empty LinkedList


    def transpose(self):
        """
        Creates and returns the transpose of the current graph.
        (Reverses the direction of all edges.)

        Returns:
            DirectedGraph: A new graph with all edges reversed.

        Time Complexity: O(V + E)
        """
        transposed = DirectedGraph(self.n)
        for u in range(self.n):
            for i in range(len(self.adj.get(u))):
                v = self.adj.get(u).get(i)
                transposed.add_edge(v, u)
        return transposed


