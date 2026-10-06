# =====================================================================
# PRACTICAL 7: GREEDY BEST-FIRST SEARCH (GBFS)
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# Evaluation Function: f(n) = h(n)
# Intuition: Hamesha us padosi (node) ko chuno jiska Heuristic h(n)
#            sabse kam ho (jo goal ke sabse kareeb lage).
# =====================================================================

# Q1. STATE / ENVIRONMENT: Graph aur Heuristic values kaise define honge?
# Adjacency list: Graph connections
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

# Heuristic Table: Har node se Goal 'G' tak ka estimated distance h(n)
# Goal 'G' ka heuristic hamesha 0 hota hai!
heuristic = {
    'A': 15,
    'B': 14,
    'C': 13,
    'D': 6,
    'E': 8,
    'F': 5,
    'G': 0,
    'H': 3,
    'K': 20
}

def greedy_bfs(graph, heuristic, start, goal):
    # Q2. MEMORY / TRACKING: Kaunse nodes dekhne baaki hain aur path kaise track karein?
    # 1. 'open_list': Wo nodes jo explore karne ke liye queue me hain.
    # 2. 'visited': Jo nodes hum expand kar chuke hain.
    # 3. 'parent': Goal milne par poora rasta (path) wapas banane ke liye.
    open_list = [start]
    visited = set()
    parent = {start: None}

    while open_list:
        # Q4 (Part 1). GREEDY SELECTION: Sabse kam heuristic h(n) wala node pick karo!
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)
        visited.add(current)

        print(f"Expanding Node: '{current}' with Heuristic h={heuristic[current]}")

        # Q3. GOAL CHECK: Kya hum manzil (goal) par pahunch gaye?
        if current == goal:
            print("\nGoal Reached!")
            # Path reconstruct karna (Goal se Start tak piche aao)
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()  # Start to Goal seedha karo
            return path

        # Q4 (Part 2). EXPLORATION: Current node ke unvisited neighbours ko queue me daalo
        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in open_list:
                open_list.append(neighbour)
                parent[neighbour] = current

    print("Goal tak rasta nahi mila!")
    return None

# Driver Code
start_node = 'A'
goal_node = 'G'
final_path = greedy_bfs(graph, heuristic, start_node, goal_node)
print("Final Shortest/Best Path:", " -> ".join(final_path))
