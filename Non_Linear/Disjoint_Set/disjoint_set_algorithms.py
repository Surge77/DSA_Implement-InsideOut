from disjoint_set_base import DisjointSet
from Linear.arrays import MyArray as Array


def detect_cycle_undirected(num_vertices: int, edges: list) -> bool:
    """
    Detect if an undirected graph contains a cycle using Union-Find.

    Args:
        num_vertices (int): Number of vertices.
        edges (list): List of edges (u, v).

    Returns:
        bool: True if a cycle exists, False otherwise.

    Time Complexity: O(E * α(V)) where α is the inverse Ackermann function.
    """
    ds = DisjointSet(num_vertices)

    for u, v in edges:
        root_u = ds.find(u)
        root_v = ds.find(v)
        if root_u == root_v:
            return True  # Cycle found
        ds.union(root_u, root_v)

    return False


def kruskal_mst(num_vertices: int, edges: list):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST).

    Args:
        num_vertices (int): Number of vertices.
        edges (list): List of edges (u, v, weight).

    Returns:
        (Array, float): MST edges and total weight.

    Time Complexity: O(E log E) due to sorting.
    """
    ds = DisjointSet(num_vertices)
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    mst_edges = Array()
    total_weight = 0.0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w
        if len(mst_edges) == num_vertices - 1:
            break

    return mst_edges, total_weight


# ------------------- TEST CODE -------------------
if __name__ == "__main__":
    # Test cycle detection
    num_vertices = 4
    edges = [(0, 1), (1, 2), (2, 3)]
    print("Cycle in graph (expected False):", detect_cycle_undirected(num_vertices, edges))

    edges_with_cycle = [(0, 1), (1, 2), (2, 0)]
    print("Cycle in graph (expected True):", detect_cycle_undirected(3, edges_with_cycle))

    # Test Kruskal's MST
    weighted_edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    mst, total = kruskal_mst(4, weighted_edges)
    print("\nKruskal's MST Edges:")
    for i in range(len(mst)):
        print(mst.get(i))
    print("Total Weight of MST:", total)
