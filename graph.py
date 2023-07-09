graph = dict()
visited = []
node_graph = []
d = 1
#Graph initialization
def addEdge(node1, node2, d):
    if node1 not in graph:
        graph[node1] = [] #When a node comes initially it will not be having any neighbours
        
    if node2 not in graph:
        graph[node2] = []
        
    if(d == 1):
        graph[node1].append(node2)
        
    else:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
def get_Adj_list(node1):
    values = []
    for k,v in graph.items():
        if(k == node1):
            values = [x for x in v]
    return values

#Basically to find the BFS the graph must be directed
def bfs(start, end):
    queue = []
    v = 1 #indicating queue is not empty as we add the start node into the queue
    queue.append(start)
    for key, val in graph.items():
        if start in val:
            for i in val:
                if(i not in queue):
                    queue.append(i)
        while queue:
            v = queue[0]
            queue.remove(queue[0])
            print(v, end = " ")
            if(v == end):
                v = 0
                break
            l = get_Adj_list(v)
            for i in l:
                queue.append(i)
            if not queue:
                v = 0 #indicating queue is empty
        if v == 0:
            break
    '''queue.append(start)
    while queue:
        v = queue[0]
        queue.remove(queue[0])
        print(v, end = " ")
        if(v == end):
            break
        l = get_Adj_list(v)
        for i in l:
            if i not in queue:
                queue.append(i)'''
        

def dfs(start, end):
    stack = []
    visited = []
    stack.append(start)
    while stack:
        u = stack[-1]
        stack.remove(stack[-1])
        print(u, end = " ")
        if u == end:
            break
        l = get_Adj_list(u)
        for i in l:
            if i not in stack:
                stack.append(i)
                    

def display():
    for key, val in graph.items():
            print(f"{key}-->{val}")


while True:
    print("\n")
    print("Your choices: ")
    print("1) Graph initialization")
    print("2) Add node")
    print("3) Add edge")
    print("4) Get adjacency list for a particular node")
    print("5) BFS")
    print("6) Delete Node")
    print("7) Delete edge")
    print("8) Display graph")
    print("9) DFS")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        d = int(input("Directed graph(1) or undirected graph(0)"))
        nodes, edges = input("Enter number of nodes and no. of edges").split()
        print("Enter the node who has edges between them: ")
        for i in range(int(edges)):
            node1, node2 = input().split()
            addEdge(node1, node2, d)
            if node1 not in node_graph:
                node_graph.append(node1)
            if node2 not in node_graph: 
                node_graph.append(node2)
        
        print("The node list is: ", node_graph)
        display()

    elif ch == 2:
        n = input("Enter the node: ")
        if(n not in node_graph and n not in graph):
            graph[n] = []
            node_graph.append(n)
            print("Node added sucessfully")
        else:
            print("Node already exist")

    elif ch == 3:
        node1, node2 = input("Enter the 2 nodes between whom you want to create an edge").split()
        addEdge(node1, node2, d)
        display()

    elif ch == 4:
        #Finding all the adjacent nodes for a given node
        nd = input("Enter a node to find their adjacent elements: ")
        v= get_Adj_list(nd)
        print("The adjacent node(s) to ", nd, " are ", v)
        
    elif ch == 5:
        #Basically to find the BFS the graph must be directed
        start , end = input("Enter the start and the end node: ").split()
        bfs(start, end)

    elif ch == 6:
        n = input("Enter the node to delete")
        if n in node_graph:
            node_graph.remove(n)
            del graph[n]
            for key, val in graph.items():
                if n in val:
                    val.remove(n)
            print("Node deleted sucessfully")
            display()
        else:
            print("Node not available")
            display()
    
    elif ch == 7:
        #Deleting only the edge not the node
        node1, node2 = input("Enter the 2 nodes between whom you want to remove an edge: ").split()
        for key,val in graph.items():
            if key == node1:
                if(node2 in val):
                    val.remove(node2)
            if key == node2:
                if(node1 in val):
                    val.remove(node1)
        display()                    
        
    elif ch == 8:
        #Display graph      
        display() 
    
    elif ch == 9:
        start ,end = input("Enter the start and the end node: ").split()
        dfs(start, end)
        
    else:
        print("Exiting!!!!")
        break

