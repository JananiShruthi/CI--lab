graph = dict()
node_graph = []
d = 1
cost = []
queue = []
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

def pqueue_enqueue(n, c):
    queue.append((n,c))
    
def pqueue_sort(queue):
    queue.sort(key =lambda x:x[1])
    
def pqueue_dequeue():
    state, cost = queue.pop(0)
    return state, cost
    
def calculate_path(graph, start, goal):
    v = goal
    q = [goal]
    while v != start:
        l = []
        for key, val in graph.items():
            for i in val:
                if i[0] == v:
                    l.append((key , i[1]))
        l.sort(key = lambda x : x[1])
        q.append(l[0][0])
        v = l[0][0]
    q.reverse()
    print(q)
    
def uniform_cost_search(graph, start, goal):
    visited = set()  # Set to store visited states
    pqueue_enqueue(start, 0)  # List to store nodes and their costs

    while queue:
        #queue.sort(key=lambda x: x[1])  # Sort the queue based on cost
        pqueue_sort(queue)
        state, cost = pqueue_dequeue()

        if state == goal:
            calculate_path(graph, start, goal)
            return cost

        visited.add(state)

        for neighbor, edge_cost in graph[state]:
            if neighbor not in visited:
                pqueue_enqueue(neighbor, cost + edge_cost)

    return float('inf')  # If goal state is not reachable

def display():
    for key, val in graph.items():
            print(f"{key}-->{val}")
                           
    
while True:
        print("\n**********CHOICES**********")
        print("1)Grpah initialisation\n2)Add node\n3)Add edge\n4)uniform cost search\n5)Delete node\n6)Delete edge\n7)Exit")
        ch = int(input("Enter the choice: "))
        if ch == 1:
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
        elif ch == 2:
                n = input("Enter the node to add: ")
                if n not in node_graph:
                        node_graph.append(n)
                        graph[n] = []
                else:
                        print("Node already exists")
        elif ch == 3:
                n1, n2 = input("Enter the nodes to add edge between them: ").split()
                c = int(input("Enter the cost for this edge:"))
                addEdge(n1, n2, d, c)
                display()
        elif ch == 4:
                start, goal = input("Enter the start & goal node").split()

                cost = uniform_cost_search(graph, start, goal)

                print(f"Minimum cost from {start} to {goal}: {cost}")
        elif ch == 5:
                n = input("Enter node to delete: ")
                del graph[n]
                for val in graph.values():
                    for i,j in val:
                        if i == n:
                           val.remove((i, j))
                display()
        elif ch == 6:
                n = input("Enter the node to be deleted: ")
                for val in graph.values():
                        for i,j in val:
                            if i == n:
                                val.remove((i,j))
        elif ch == 7:
                display()        
        else:
                print("EXITING!!!")
                break
