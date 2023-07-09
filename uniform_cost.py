graph = dict()
node_graph = []
d = 1
cost = []
#Graph initialization
def addEdge(node1, node2, d, c):
    if node1 not in graph:
        graph[node1] = [] #When a node comes initially it will not be having any neighbours
        
    if node2 not in graph:
        graph[node2] = []
        
    if(d == 1):
        t = (node2, c)
        graph[node1].append(t)
        
    else:
        t1 = (node2, c)
        graph[node1].append(t1)
        t2 = (node1, c)
        
        
def uniform_cost_search(graph, start, goal):
    visited = set()  # Set to store visited states
    queue = [(start, 0)]  # List to store nodes and their costs

    while queue:
        queue.sort(key=lambda x: x[1])  # Sort the queue based on cost
        state, cost = queue.pop(0)

        if state == goal:
            return cost

        visited.add(state)

        for neighbor, edge_cost in graph[state]:
            if neighbor not in visited:
                queue.append((neighbor, cost + edge_cost))

    return float('inf')  # If goal state is not reachable
    
def display():
    for key, val in graph.items():
            print(f"{key}-->{val}")

d = int(input("Directed graph(1) or undirected graph(0)"))
nodes, edges = input("Enter number of nodes and no. of edges").split()
print("Enter the node who has edges between them: ")
for i in range(int(edges)):
    node1, node2 = input().split()
    c = int(input(("Now enter the cost for this edge: ")))
    addEdge(node1, node2, d, c)
    if node1 not in node_graph:
        node_graph.append(node1)
    if node2 not in node_graph: 
        node_graph.append(node2)

print("The node list is: ", node_graph)
display()

start, goal = input("Enter the start & goal node").split()

cost = uniform_cost_search(graph, start, goal)

print(f"Minimum cost from {start} to {goal}: {cost}")
