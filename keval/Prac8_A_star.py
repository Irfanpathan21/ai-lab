

def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}      # store distance from starting node
    f = {}      # store total cost
    parents = {}
    # distance of starting node from itself is zero
    g[start_node] = 0
    # start node is root node
    parents[start_node] = start_node
    n = None
    while len(open_set) > 0:
        n = None
        total_f = 100
        # find node with lowest f(n)
        for v in open_set:
            if n == stop_node:
                break
            if n not in open_set:
                print("Node =", v, "Cost =", g[v] + heuristic(v))
                if g[v] + heuristic(v) < total_f:
                    n = v
            elif g[n] + heuristic(n) > g[v] + heuristic(v):
                n = v
        if n is None:
            print("Path does not exist!")
            return None
        print("Node for expansion --->", n)
        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    print(
                        m,
                        "Child of",
                        n,
                        "Parent Node total cost g[n]=",
                        g[n],
                        "w=",
                        weight,
                        "h(m)=",
                        heuristic(m),
                    )
                    g[m] = g[n] + weight
                    f[m] = g[m] + heuristic(m)
                    print("g[m] =", g[m], "f[m] =", f[m])
                    open_set.add(m)
                    parents[m] = n
                else:
                    if g[m] > g[n] + weight:
                        print("updated weight for", m)
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found : {}".format(path))
            return path
        print("remove", n)
        open_set.remove(n)
        closed_set.add(n)
    print("Path does not exist!")
    return None

# Define function to return neighbor and its distance
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }

    return H_dist[n]

Graph_nodes = {
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

print("Name : Keval Doshi")
print("SAP ID : 53013240009")
print("-" * 40)

aStarAlgo('A', 'J')
