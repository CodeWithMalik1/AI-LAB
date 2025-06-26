# Input Graph 
graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'C', 'D'], 
    'C': ['A', 'B', 'E'], 
    'D': ['B', 'E'], 
    'E': ['C', 'D'] 
}

# To store visited nodes and queue
visitedNodes = []
queueNodes = []

# BFS function
def bfs(visitedNodes, graph, snode): 
    visitedNodes.append(snode) 
    queueNodes.append(snode) 

    print("\nRESULT:")
    while queueNodes: 
        s = queueNodes.pop(0) 
        print(s, end=" ") 
        for neighbour in graph[s]: 
            if neighbour not in visitedNodes: 
                visitedNodes.append(neighbour) 
                queueNodes.append(neighbour) 

# Main code
snode = input("Enter Starting Node (A, B, C, D, or E): ").upper()
if snode in graph:
    bfs(visitedNodes, graph, snode)
else:
    print("Invalid starting node.")
