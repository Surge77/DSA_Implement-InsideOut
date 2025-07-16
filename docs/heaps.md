# Heap

A heap is a complete binary tree where each node is ordered with respect to its children, according to the min or max heap property.

Complete: No gaps except possibly at the end of the last level.

Binary: Each node has up to two children.

Heap property: In min-heap, parent ≤ children. In max-heap, parent ≥ children.

--- 

In standard min/max binary heaps, all efficient access and modification is done using just array indexing formulas. There is no more efficient way in this setting.

Arrays + index math are not just a convenient trick—they’re the most efficient way to access and modify elements in standard binary heaps, precisely because the “completeness” guarantees the mapping works for all nodes, and every operation needs only a handful of index calculations.

This is why every major language uses arrays/lists for heaps.

#### Heap is a Tree “In Concept,” but…

A heap is defined as a complete binary tree with the heap property (min or max at root).

This definition is about relationships: “every parent is smaller/larger than its children.”

### Why Not Use Nodes/Pointers Like BSTs?
In a binary search tree (BST), nodes can be anywhere—left and right children can be far apart in memory, and you often have to deal with empty (null) child pointers. Traversal is pointer-heavy.

Heaps are always complete: all levels are filled, except possibly the last, which is filled left to right.
This means the “shape” is always predictable.


### When do we use `_bubble_down` 

When do we use it?

After removing the min element (the root), we move the last element to the root.

This new root might break the min-heap property: it could be larger than its children.

Goal: Move it down to its correct spot so every parent is less than or equal to its children.


### What does `Heapify` method do?

Heapify takes any list of numbers and rearranges them so that they follow the rules of a max-heap—meaning every parent is bigger than its children.

After heapify, the biggest number will be at the top (root), and every subtree will also be a heap. It turns a random list into a heap in one efficient process, not by inserting one at a time.