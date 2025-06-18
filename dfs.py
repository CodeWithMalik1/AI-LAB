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