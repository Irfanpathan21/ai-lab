# =====================================================================
# PRACTICAL 1: DEPTH FIRST SEARCH (DFS)
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

# Q2. MEMORY / LOOP PROTECTION: Repeat na ho aur infinite loop se kaise bache?
# Answer: 'visited' list banayenge jo track karegi kaunsa node pehle se dekh chuke hain.
visited = []

# DFS Function (Uses Call Stack / Recursion to go deep)
def dfs(visited, graph, node):
    # Q3. STOPPING CONDITION / CHECK: Kya ye node pehle visit kiya hai?
    # Agar abhi tak visit nahi kiya, tabhi aage badho.
    if node not in visited:
        print(node, end=' ')
        visited.append(node)   # Mark kar do ki ab dekh liya

        # Q4. EXPLORATION / NEXT STEP: Agle kadam par kaha jayein?
        # Is node ke har ek padosi (neighbour) ke andar deeply ghuso (recursion).
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code: Start node 'A' se DFS shuru karo
print("DFS Traversal Result:")
dfs(visited, graph, 'A')
print()
