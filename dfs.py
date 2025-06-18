# Graph represented as an adjacency list (dictionary)
graph = { 
    'A': ['B', 'C'], 
    'B': ['A', 'C', 'D'], 
    'C': ['A', 'B', 'E'], 
    'D': ['B', 'E'], 
    'E': ['C', 'D']
}

# List to keep track of visited nodes
visitedNodes = []

# DFS Function
def dfs(visitedNodes, graph, node):
    if node not in visitedNodes:
        print(node, end=" ")  # Print the current node
        visitedNodes.append(node)  # Mark node as visited