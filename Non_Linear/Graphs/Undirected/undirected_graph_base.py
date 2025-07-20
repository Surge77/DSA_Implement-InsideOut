from Linear.arrays import MyArray as Array
from Linear.singly_linked_list import SinglyLinkedList as LinkedList

class Graph:
    def __init__(self, num_vertices: int):
        self.n = num_vertices  # number of vertices (0 to n-1)
        self.adj = []          # create an empty Python list
        for _ in range(num_vertices):
            self.adj.append(LinkedList())  # put an empty LinkedList for each vertex


    def add_edge(self, u: int, v: int):
        """

        Remember this: u chya list madhe v ahe ka? => not specific to this method but common analogy for other methods
        Whether in the u's list v is present or not

        Adds a two-way (undirected) connection between nodes u and v.

        Checks if the edge already exists using .search(v) (returns -1 if not found).

        If not present, inserts v into u's list and u into v's list (since the graph is undirected).
        
        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        if self.adj[u].search(v) < 0: # search() is method implemented in my LinkedList class which returns a int value or -1 
            self.adj[u].insert(0, v) # We insert at the head of the linkedList because For a singly linked list, inserting at the head is O(1).
        if self.adj[v].search(u) < 0:
            self.adj[v].insert(0, u)


    def remove_edge(self, u: int, v: int):
        """

        Searches for v in u's adjacency list and removes it, and vice versa.

        Removes both directions, maintaining the undirected property.           

        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        u_index = self.adj[u].search(v)
        if u_index >= 0:
            self.adj[u].delete(u_index)
            
        v_index = self.adj[v].search(u)
        if v_index >= 0:
            self.adj[v].delete(v_index)


    def has_edge(self, u: int, v: int) -> bool:
        """
        Returns True if v is found in u's neighbor list.
        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self.adj[u].search(v) >= 0


    def neighbors(self, u: int):
        """
        Returns the entire neighbor list for node u.
        """
        self._validate_vertex(u)
        return self.adj[u]


    def _validate_vertex(self, u: int):
        """
        Raise ValueError if vertex u is out of valid range [0, n-1].
        """
        if not (0 <= u < self.n):
            raise ValueError(f"Vertex {u} is out of bounds [0, {self.n-1}]")
        

    def add_vertex(self):
        """
        Add a new vertex to the graph.
        Time: O(1)
        Side effect: The new vertex's index will be (self.n).
        """
        self.adj.append(LinkedList())
        self.n += 1
        
    

    def remove_vertex_reindex(self, u: int):
        """

        This remove method is a bit tough to visualize
        Remove vertex u and re-index all remaining vertices (0 to n-2).
        - All vertices with index > u are shifted down by 1.
        - All adjacency values > u are decremented by 1.

        Time Complexity: O(V + E).
        Use this if compact indexing is desired.
        """
        self._validate_vertex(u)

        # Step 1: Remove all references to u in adjacency lists
        for v in range(self.n):
            if v == u:
                continue
            idx = self.adj[v].search(u)
            if idx >= 0:
                self.adj[v].delete(idx)
            # Adjust neighbor values > u
            for i in range(len(self.adj[v])):
                neighbor = self.adj[v].get(i)
                if neighbor > u:
                    self.adj[v].set(i, neighbor - 1)

        # Step 2: Remove adjacency list of u
        self.adj.pop(u)
        self.n -= 1


    def remove_vertex_static(self, u: int):
        """
        This remove method is easy to understand as there are no index shifting 
        Remove vertex u but keep all other vertex IDs unchanged.
        - Simply deletes u's adjacency list.
        - Removes u from all neighbor lists.

        Time Complexity: O(V + E).
        Use this for debugging or when vertex IDs should not shift.
        """
        self._validate_vertex(u)

        # Remove u from every other adjacency list
        for v in range(self.n):
            if v == u:
                continue
            idx = self.adj[v].search(u)
            if idx >= 0:
                self.adj[v].delete(idx)

        # Clear adjacency list of u (mark as removed)
        self.adj[u] = LinkedList()

    
    def edge_count(self):
        """
        Returns the current number of edges in the undirected graph.
        Time: O(V + E)
        """
        total = 0
        for u in range(self.n):
            total += len(self.adj[u])
        return total // 2  # Each edge counted twice
    

    # def bfs(self, start):
    #     """
    #     Breadth-First Search traversal from the starting vertex.
    #     Prints nodes in the order visited.
    #     Uses a manual queue built from your MyArray.

    #     Time: O(V + E)
    #     """
    #     self._validate_vertex(start)
    #     visited = [False] * self.n  # Could use MyArray for extra challenge
    #     queue = Array()
    #     queue.append(start)
    #     visited[start] = True

    #     while len(queue) > 0:
    #         u = queue.get(0)  # Always dequeue from the head
    #         queue.delete(0)
    #         print(u, end=" ")

    #         for i in range(len(self.adj[u])):
    #             v = self.adj[u].get(i)
    #             if not visited[v]:
    #                 queue.append(v)
    #                 visited[v] = True

    def bfs(self, start):
        """
        In BFS we always immediately print the node when we pop it off from the front of the queue and print it in the output and after that we check the neighbors of that node if they are visited or unvisited

        Breadth-First Search traversal from the starting vertex.
        Prints:
        1. Normal BFS order (single line).
        2. Level-wise traversal.
        Uses a manual queue built from your MyArray.

        Time: O(V + E)
        """
        self._validate_vertex(start)
        visited = [False] * self.n
        queue = Array()
        queue.append(start)
        visited[start] = True

        normal_order = []  # To store normal BFS order
        level = 0

        print("Graph BFS from", start, ":")

        while len(queue) > 0:
            level_size = len(queue)
            print(f"Level {level}:", end=" ")

            for _ in range(level_size):
                u = queue.get(0)
                queue.delete(0)
                print(u, end=" ")  # Print node for current level
                normal_order.append(u)

                for i in range(len(self.adj[u])):
                    v = self.adj[u].get(i)
                    if not visited[v]:
                        queue.append(v)
                        visited[v] = True

            print()  # newline after each level
            level += 1

        # Print BFS normal order at the end
        print("\nBFS Traversal (Normal Order):")
        print(" ".join(map(str, normal_order)))


    def dfs(self, start):
        """
        Perform Depth-First Search (DFS) starting from 'start'.
        Prints the nodes in DFS order.

        Uses:
            - Recursion
            - List for visited flags

        Time Complexity: O(V + E)
        """
        self._validate_vertex(start)
        visited = [False] * self.n

        def _dfs(u):
            visited[u] = True
            print(u, end=" ")
            for i in range(len(self.adj[u])):
                v = self.adj[u].get(i)
                if not visited[v]:
                    _dfs(v)

        _dfs(start)

    def connected_components(self):
        """
        Finds and returns all connected components in the undirected graph.
        Each component is a list of node indices.

        Returns:
            List[List[int]]: A list where each entry is a list of vertices in one component.

        Time Complexity: O(V + E)
        """
        visited = [False] * self.n
        components = []

        def dfs(u, current):
            visited[u] = True
            current.append(u)
            for i in range(len(self.adj[u])):
                v = self.adj[u].get(i)
                if not visited[v]:
                    dfs(v, current)

        for u in range(self.n):
            if not visited[u] and len(self.adj[u]) > 0:
                component = []
                dfs(u, component)
                components.append(component)
            elif not visited[u]:
                # Isolated node (no neighbors), count as its own component
                components.append([u])
                visited[u] = True

        return components



    def vertex_count(self):
        """
        Returns the current number of vertices in the graph.
        Time: O(1)
        """
        return self.n


    def __len__(self):
        """
        Returns the number of vertices in the graph (so len(graph) works).
        Time: O(1)
        """
        return self.n


    def __str__(self):
        """
        Return a readable string representation of the graph for users.
        Each vertex and its adjacency list (as a linked list with arrows) is displayed line by line.
        Example:
            Graph with 3 vertices:
            0: 1 -> 2
            1: 0
            2: 0
        """
        result = [f"Graph with {self.n} vertices:"]
        for u in range(self.n):
            # Build the arrow-separated string using your LinkedList's get method
            if len(self.adj[u]) == 0:
                arrow_str = "(empty)"
            else:
                arrow_str = " -> ".join(str(self.adj[u].get(i)) for i in range(len(self.adj[u])))
            result.append(f"  {u}: {arrow_str}")
        return "\n".join(result)
    

    def __repr__(self):
        """
        Return an unambiguous, dev-friendly string with construction info.
        Shows the number of vertices and list of edges.
        Example:
            Graph(num_vertices=3, edges=[(0, 1), (0, 2)])
        """
        edges = []
        for u in range(self.n):
            for i in range(len(self.adj[u])):
                v = self.adj[u].get(i)
                if u < v:
                    edges.append(f"({u}, {v})")
        return f"Graph(num_vertices={self.n}, edges=[{', '.join(edges)}])"
    
