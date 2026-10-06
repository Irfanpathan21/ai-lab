#DFS
visited=[]
graph={
'A':['C','B','D'],
'B':['A','C'],
'C':['A','B','E'],
'D':['A'],
'E':['C'],
}

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
            
dfs(visited,graph,'A')

