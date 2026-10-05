# =====================================================================
# PRACTICAL 8: A* (A-STAR) SEARCH ALGORITHM
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Optimal Informed Search using Path Cost + Heuristic
# GOLDEN FORMULA:
#   f(n) = g(n) + h(n)
#     g(n) = Actual cost from start node to current node
#     h(n) = Estimated heuristic cost from current node to goal
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - Compare with Greedy BFS (Prac 7):
#       In Greedy BFS: pick min by `heuristic[n]`
#       In A*:         pick min by `g_score[n] + heuristic[n]`
#   - Dijkstra's Algorithm: If h(n) = 0 for all nodes, A* becomes Dijkstra!
# =====================================================================

# 1. State / Weighted Graph Representation and Heuristics to Goal 'J'
graph = {
    'A': [('B', 6), ('F', 10)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 10), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': []
}

heuristic = {
    'A': 11, 'B': 6, 'C': 5, 'D': 7, 'E': 3,
    'F': 6,  'G': 5, 'H': 3, 'I': 1, 'J': 0
}

# 2. Universal A* Template Function
def a_star(start, goal):
    open_list = [start]
    g_score = {start: 0}
    parent = {start: None}

    while open_list:
        # Core A* Rule: Pick node with smallest f(n) = g(n) + h(n)
        curr = min(open_list, key=lambda n: g_score[n] + heuristic[n])
        open_list.remove(curr)

        # Step-by-Step Node Expansion Progression
        g, h = g_score[curr], heuristic[curr]
        print(f"Expanding: {curr} | g={g}, h={h}, f={g + h}")

        # Goal Check: Reconstruct optimal path if reached
        if curr == goal:
            path = []
            while curr:
                path.append(curr)
                curr = parent[curr]
            return path[::-1], g_score[goal]

        # Explore weighted neighbours
        for nbr, cost in graph[curr]:
            new_g = g_score[curr] + cost
            if nbr not in g_score or new_g < g_score[nbr]:
                g_score[nbr] = new_g
                parent[nbr] = curr
                if nbr not in open_list:
                    open_list.append(nbr)

    return None, 0

# 3. Driver Code
start_node, goal_node = 'A', 'J'
path, total_cost = a_star(start_node, goal_node)
print(f"A* Optimal Path from {start_node} to {goal_node}:")
print(" -> ".join(path))
print(f"Total Path Cost: {total_cost}")
