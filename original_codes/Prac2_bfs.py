# =====================================================================
# PRACTICAL 2: BREADTH FIRST SEARCH (BFS)
# 4-QUESTION FRAMEWORK (Hinglish Guide)
# =====================================================================

# Q1. STATE / ENVIRONMENT: Graph kaisa dikhta hai?
# Answer: Dictionary jisme key = node, aur value = uske connected padosi (neighbours).
graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'E'],
    'D': ['A'],
    'E': ['C']
}

# Q2. MEMORY: Level-by-level explore karne ke liye kya chahiye?
# Answer:
# 1. 'visited': Jo nodes process ho chuke hain unko track karne ke liye.
# 2. 'queue': FIFO (First-In-First-Out) taaki pehle aane wale neighbours pehle explore hon.
visited = []
queue = []

def bfs(visited, graph, start_node):
    # Shuruati node ko queue aur visited dono me daalo
    visited.append(start_node)
    queue.append(start_node)

    # Q3. STOPPING CONDITION: Kab tak chalna hai?
    # Answer: Jab tak queue poori tarah khali (empty) na ho jaye!
    while queue:
        # Queue ke sabse aage (front) wale node ko bahar nikalo (FIFO: pop(0))
        current = queue.pop(0)
        print(current, end=" ")

        # Q4. EXPLORATION / NEXT STEP: Agle neighbours ko kaise explore karein?
        # Current node ke har padosi ko check karo:
        for neighbour in graph[current]:
            # Agar neighbour pehle nahi dekha hai:
            if neighbour not in visited:
                visited.append(neighbour)  # Yaad rakho ki visit kar liya
                queue.append(neighbour)    # Queue me piche add karo agle level ke liye

# Driver Code: Start node 'A' se shuru karo
print("BFS Traversal Result:")
bfs(visited, graph, 'A')
print()
