# =====================================================================
# PRACTICAL 1: DEPTH FIRST SEARCH (DFS)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Tree / Graph Traversal using Recursion (LIFO)
# CORE CONCEPT:
#   1. Visit current node, mark as visited.
#   2. Recurse deeply on each unvisited neighbour.
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Change Graph: Simply modify the 'graph' dictionary connections.
#   - Goal Search:  Add `if node == goal: return True` inside dfs().
#   - Path Finding: Pass `path + [node]` in recursive call.
# =====================================================================

# 1. State / Graph Representation (Adjacency List)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'E'],
    'D': ['A'],
    'E': ['C']
}

visited = []

# 2. Universal DFS Template Function
def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")
        for neighbour in graph[node]:
            dfs(neighbour)

# 3. Driver Code
print("DFS Traversal:")
dfs('A')
print()
