## Graphs

### Basic setup method in the graph

### `add_edge` method:

#### What problem is this solving?
We need to connect two vertices (u and v) in an undirected graph by updating their adjacency lists.

#### Why do we check .search(v) < 0?
In a simple graph, we don’t want duplicate entries (e.g., 0 → 1 listed twice).

.search(v) scans adj[u] for v. If not found, we insert v.

#### Why insert at position 0?
For a singly linked list, inserting at the head is O(1).

Appending at the end would require traversing the list (O(n)).

#### How does it maintain undirectedness?
We add v to u’s adjacency list and u to v’s adjacency list.

This creates a "two-way road" between u and v.


### `remove_vertex_reindex` method

```python

def remove_vertex_reindex(self, u: int):
    """
    Remove vertex u and all edges to/from u.
    After removal, all vertex indices greater than u shift down by 1.
    All adjacency list values greater than u are decremented by 1.

    Tradeoff:
        - Keeps the graph compact (no 'holes').
        - **Vertex IDs change** for all nodes after u. Any outside code or labels that depended on the original indices will need to be updated.

    Time Complexity: O(V + E), where V = number of vertices, E = number of edges.

    Example:
        Before: 0: 1 -> 2, 1: 0, 2: 0
        remove_vertex_reindex(1)
        After:  0: 1, 1: 0
    """
    # ... implementation ...

```


### `remove_vertex_static` method

```python

def remove_vertex_static(self, u: int):
    """
    Remove vertex u but keep vertex IDs unchanged.
    - Deletes all edges to/from u (empties its adjacency list and removes u from all others).
    - Leaves a 'hole': u is now an unused ID.
    - This is helpful if you want external references or labels to remain valid.
    - Traversal and algorithms must skip such 'removed' vertices.

    Tradeoff:
        - Vertex indices are stable (good for mapping with external data).
        - The graph may have 'inactive' or empty nodes, which must be accounted for in all operations.

    Time Complexity: O(V + E), where V = number of vertices, E = number of edges.

    Example:
        Before: 0: 1 -> 2, 1: 0, 2: 0
        remove_vertex_static(1)
        After:  0: 2, 1: (empty), 2: 0

    Note:
        If you run traversals, always check that a vertex's list is non-empty and/or implement a 'removed' flag or set for extra safety.
    """
    # ... implementation ...

    

```


### `dfs` method:

In DFS, the core steps for a node u are:

Visit the node u (mark it as visited).

Print (or process) u immediately when you first visit it.

Go deeper by calling DFS on all unvisited neighbors of u.

Backtrack when there are no more unvisited neighbors.


### Why Do We Print When We Visit?
DFS is about exploring as soon as you see a node.

Once you visit u, you “discover” it and record it (print/process it).

Then, you dive into its neighbors without waiting.


### DFS vs BFS Printing
DFS: Print when you visit (immediate discovery).

BFS: Print when you dequeue (when it's that node's "turn" at its level).


## Islands or connected components

### What does this mean in graph terms?

An island = a connected component.

Connected component: A set of vertices where:

Every vertex can be reached from every other vertex (within that set).

There is no path to vertices outside that set.

--- 
A graph is a set of nodes (vertices) connected by edges.

Some nodes can be reached from others (via paths).

Some nodes cannot be reached at all because they’re in different disconnected regions.

An island is simply one of those disconnected regions — a set of nodes that are internally connected but have no edges connecting them to nodes outside the set.

---

### Why is this important?
Identifies “clusters” or “groups” in a graph (e.g., friend circles, sub networks).

Useful for network analysis, clustering, and error detection.

### How to compute them?
Loop over all vertices.

For each unvisited vertex, run BFS or DFS to mark all nodes in its component.

Start a new component for each such run.