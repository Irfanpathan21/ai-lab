
graph = {
    'A': ['B','C'],
    'B': ['A','K','D'],
    'C': ['E','F','A'],
    'D': ['G','B'],
    'E': ['G','C'],
    'F': ['H','C'],
    'G': ['D','E','H','K'],
    'H': ['F','G'],
    'K': ['G','B']
}

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

print("Name:- Keval Doshi")
print("Sap Id:- 53013240009")
print("-" * 40)
start = 'A'
goal = 'G'

visited = []
not_visited = [start]

while not_visited:

    h = []
    for i in not_visited:
        h.append(heuristic[i])

    print("Not Visited :", not_visited)
    print("H Values    :", h)

    minimum = min(h)
    index = h.index(minimum)
    current = not_visited.pop(index)
    print("Selected Node:", current)
    visited.append(current)

    for i in graph[current]:
        if i not in visited and i not in not_visited:
            not_visited.append(i)
    print("Visited     :", visited)
    print("Not Visited :", not_visited)
    print("-" * 30)

    if current == goal:
        print("Goal Reached!")
        break

print("Path:", " -> ".join(visited))
