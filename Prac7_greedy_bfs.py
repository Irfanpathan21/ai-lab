# =====================================================================
# PRACTICAL 7: GREEDY BEST-FIRST SEARCH (GBFS)
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Informed Search using Heuristics Only
# GOLDEN FORMULA:
#   f(n) = h(n)  [Greedy choice: pick node with smallest heuristic]
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Compare with A* (Prac 8):
#       Greedy chooses min by `heuristic[n]`.
#       A* chooses min by `g_score[n] + heuristic[n]`.
#   - To adapt to any other graph: Just change 'graph' and 'heuristic' dictionaries!
# =====================================================================

# 1. State / Graph Representation and Heuristics to Goal 'G'
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'K', 'D'],
    'C': ['E', 'F', 'A'],
    'D': ['G', 'B'],
    'E': ['G', 'C'],
    'F': ['H', 'C'],
    'G': ['D', 'E', 'H', 'K'],
    'H': ['F', 'G'],
    'K': ['G', 'B']
}

heuristic = {
    'A': 15, 'B': 14, 'C': 13, 'D': 6,
    'E': 8,  'F': 5,  'G': 0,  'H': 3, 'K': 20
}

# 2. Universal Greedy BFS Template Function
def greedy_bfs(start, goal):
    open_list = [start]
    visited = set()
    parent = {start: None}

    while open_list:
        # Core Greedy Rule: Pick node with smallest heuristic h(n)
        curr = min(open_list, key=lambda n: heuristic[n])
        open_list.remove(curr)
        visited.add(curr)

        # Goal Check: Reconstruct path if reached
        if curr == goal:
            path = []
            while curr:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]

        # Explore unvisited neighbours
        for nbr in graph[curr]:
            if nbr not in visited and nbr not in open_list:
                parent[nbr] = curr
                open_list.append(nbr)

    return None

# 3. Driver Code
start_node, goal_node = 'A', 'G'
path = greedy_bfs(start_node, goal_node)
print(f"Greedy BFS Path from {start_node} to {goal_node}:")
print(" -> ".join(path))
