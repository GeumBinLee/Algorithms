graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
}

visited = []
queue = []

def bfs(visited, graph, node) :
    visited.append(node)
    queue.append(node)
    
    while queue :
        s = queue.pop(0)
        print (s)
        
        for neighborhood in graph[s] :
            if neighborhood not in visited :
                visited.append(neighborhood)
                queue.append(neighborhood)

bfs(visited, graph ,'A')