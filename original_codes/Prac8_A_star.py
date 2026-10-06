# =====================================================================
# PRACTICAL 8: A* (A-STAR) SEARCH ALGORITHM
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# Golden Formula: f(n) = g(n) + h(n)
#   g(n) = Start se current node tak aane ki ASLI cost (Path Cost)
#   h(n) = Current node se Goal tak ka ANDAZA (Heuristic Cost)
#   f(n) = Kul milakar kul lagat (Total Estimated Cost)
# =====================================================================

# Q1. STATE / ENVIRONMENT: Graph aur Heuristics kaise store karein?
# Weighted Graph: Har edge ke saath uska weight/cost diya hai.
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

# Heuristic Table: Goal 'J' tak ka estimated distance h(n)
heuristic = {
    'A': 11, 'B': 6, 'C': 5, 'D': 7, 'E': 3,
    'F': 6,  'G': 5, 'H': 3, 'I': 1, 'J': 0
}

def a_star(graph, heuristic, start, goal):
    # Q2. MEMORY / TRACKING:
    # 1. 'open_set': Jo nodes abhi explore karne baaki hain.
    # 2. 'g_score': Start se har node tak pahunchne ka cheapest cost g(n).
    # 3. 'parent': Best path track karne ke liye.
    open_set = [start]
    g_score = {start: 0}
    parent = {start: None}

    # f(n) = g(n) + h(n) calculate karne ka chota helper
    def get_f_score(node):
        return g_score[node] + heuristic[node]

    while open_set:
        # Q4 (Part 1). BEST CHOICE: Sabse kam f(n) = g(n) + h(n) wala node chuno
        current = min(open_set, key=get_f_score)
        open_set.remove(current)

        print(f"Expanding: {current} | g={g_score[current]}, h={heuristic[current]}, f={get_f_score(current)}")

        # Q3. GOAL CHECK: Kya goal mil gaya?
        if current == goal:
            print("\nOptimal Path Reached!")
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()
            return path, g_score[goal]

        # Q4 (Part 2). EXPLORATION: Current node ke saare padosi (neighbours) check karo
        for neighbour, weight in graph.get(current, []):
            # Nayi g_cost nikaalo: start se current + current se neighbour
            tentative_g = g_score[current] + weight

            # Agar ye naya rasta purane raste se sasta (cheaper) hai:
            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                parent[neighbour] = current
                if neighbour not in open_set:
                    open_set.append(neighbour)

    print("Path nahi mila!")
    return None, 0

# Driver Code
start_node = 'A'
goal_node = 'J'
path, total_cost = a_star(graph, heuristic, start_node, goal_node)
print("Optimal Path :", " -> ".join(path))
print("Total Cost   :", total_cost)
