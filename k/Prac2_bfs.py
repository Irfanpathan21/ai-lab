#BFS
visited=[]  
queue=[]  
graph={ 
'A':['C','B','D'], 
'B':['A','C'], 
'C':['A','B','E'], 
'D':['A'], 
'E':['C'] 
} 
def bfs(visited,graph,node):  
    visited.append(node)  
    queue.append(node)  
    while queue: 
        s=queue.pop(0)  
        print(s,end=" ") 
        for neighbour in graph[s]: 
            if neighbour not in visited:  
                visited.append(neighbour)  
                queue.append(neighbour) 
bfs(visited,graph,'A')

