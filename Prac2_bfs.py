# =====================================================================
# PRACTICAL 2: BREADTH FIRST SEARCH (BFS)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Level-by-Level Graph Traversal using Queue (FIFO)
# CORE CONCEPT:
#   1. Add start node to queue and visited list.
#   2. While queue is not empty: pop front node (`pop(0)`).
#   3. Add all unvisited neighbours to both visited list and queue.
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Difference with DFS: DFS uses recursion/stack; BFS uses queue.pop(0).
#   - Shortest Path: Store (node, path) in queue (like Practical 3: Water Jug)!
#   - Level Order in Tree: Same exact code, tree nodes are graph keys.
# =====================================================================

# 1. State / Graph Representation (Adjacency List)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'E'],
    'D': ['A'],
    'E': ['C']
}

# 2. Universal BFS Template Function
def bfs(start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# 3. Driver Code
print("BFS Traversal:")
bfs('A')
print()
