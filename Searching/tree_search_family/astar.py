import heapq
from itertools import count
from typing import Any, Callable, Dict, List, Optional, Tuple

class TreeNode:
    def __init__(self, value: Any, children: List['TreeNode'] = None, cost: float = 1.0):
        self.value = value
        self.children = children or []  # List of child TreeNodes
        self.cost = cost                # Cost from parent to this node (default 1.0)

    def __repr__(self):
        return f"TreeNode({self.value})"

    def __hash__(self):
        # Needed for use in dictionaries (for came_from, g_score)
        return hash(id(self))

def astar_tree_search(
    start: TreeNode,
    goal_fn: Callable[[TreeNode], bool],
    heuristic_fn: Callable[[TreeNode], float],
) -> Optional[List[TreeNode]]:
    """
    A* Search algorithm for trees.
    
    Args:
        start: The starting TreeNode.
        goal_fn: Function that returns True if a node is the goal.
        heuristic_fn: Function estimating cost from a node to the goal.
    
    Returns:
        List[TreeNode]: Path from start to goal (inclusive), or None if not found.
    """
    open_list: List[Tuple[float, float, int, TreeNode]] = []
    tie_breaker = count()  # Unique counter for heap tuple (solves heapq comparison issue)

    # Heap stores: (f_score, g_score, tie_breaker, node)
    heapq.heappush(open_list, (heuristic_fn(start), 0, next(tie_breaker), start))
    came_from: Dict[TreeNode, Optional[TreeNode]] = {start: None}
    g_score: Dict[TreeNode, float] = {start: 0}

    while open_list:
        f, g, _, current = heapq.heappop(open_list)

        if goal_fn(current):
            # Reconstruct the path from start to goal
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse to get path from start to goal

        for child in current.children:
            tentative_g = g_score[current] + child.cost
            if child not in g_score or tentative_g < g_score[child]:
                came_from[child] = current
                g_score[child] = tentative_g
                f_score = tentative_g + heuristic_fn(child)
                # Always add a unique counter so TreeNodes are never directly compared
                heapq.heappush(open_list, (f_score, tentative_g, next(tie_breaker), child))
    return None

# ----------------------
# Example Usage
# ----------------------

# Create a sample tree:
#          A
#       /  |  \
#      B   C   D
#     / \      |
#    E   F     G
#             (goal)

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F', cost=2)  # B -> F edge has cost 2
G = TreeNode('G', cost=1)  # D -> G edge has cost 1

A.children = [B, C, D]
B.children = [E, F]
D.children = [G]

def goal_fn(node): 
    return node.value == 'G'

def heuristic_fn(node):
    if node.value == 'D': return 1    # D is one step from G
    elif node.value == 'G': return 0  # Goal node
    else: return 2                    # Other nodes: simple estimate

# Run the search
path = astar_tree_search(A, goal_fn, heuristic_fn)

if path:
    print("A* Path:", [node.value for node in path])
else:
    print("No path found.")

# Output should be: A* Path: ['A', 'D', 'G']
