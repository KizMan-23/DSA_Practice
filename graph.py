class ad_Graph():
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.matrix = [ [0] * size for _ in range(size)]

    def addNode(self, value):
        if len(self.nodes) < self.size:
            self.nodes.append(value)
        else:
            raise IndexError("Max Node is reached")

    def addEdge(self, src, dst):
        self.matrix[src][dst] = 1

    def checkEdge(self, src, dst):
        return self.matrix[src][dst] == 1 

    def __str__(self):
        for d in self.nodes:
            print(f"  {d}", end="")
        print("")

        for a in range(self.size):
            print(f"{self.nodes[a]}", end="")
        
            for b in self.matrix[a]:
                print(f" {b}", end=" ")   

            print("")
        #__str__ must have a return statement

new_graph = ad_Graph(5)

new_graph.addNode("A")
new_graph.addNode("B")
new_graph.addNode("C")
new_graph.addNode("D")
new_graph.addNode("E")

new_graph.addEdge(0, 1)
new_graph.addEdge(1, 2)
new_graph.addEdge(1, 4)
new_graph.addEdge(2, 3)
new_graph.addEdge(2, 4)
new_graph.addEdge(4, 2)
new_graph.addEdge(4, 0)

# print(new_graph.checkEdge(0,1))
# print(new_graph.checkEdge(3,4))
# print(new_graph)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Adj_Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.adlist = []

    def addNode(self, value):
        if len(self.nodes) < self.size:
            new_node = Node(value)
            self.nodes.append(new_node)
            self.adlist.append(None)  # Initialize an empty adjacency list

    def addEdge(self, src, dst):
        new_adj_node = Node(dst)  # Store dst index in adjacency list
        new_adj_node.next = self.adlist[src]
        self.adlist[src] = new_adj_node

    def checkEdge(self, src, dst):
        current = self.adlist[src]
        while current:
            if current.data == dst:
                return True
            current = current.next
        return False

    def __str__(self):
        result = []
        for i in range(len(self.nodes)):
            adj_str = []
            current = self.adlist[i]
            while current:
                adj_str.append(str(current.data))
                current = current.next
            result.append(f"Vertex {i}: {' -> '.join(adj_str)}")
        return '\n'.join(result)

new_agraph = Adj_Graph(5)

new_agraph.addNode("A")
new_agraph.addNode("B")
new_agraph.addNode("C")
new_agraph.addNode("D")
new_agraph.addNode("E")

new_agraph.addEdge(0, 1)
new_agraph.addEdge(1, 2)
new_agraph.addEdge(1, 4)
new_agraph.addEdge(2, 3)
new_agraph.addEdge(2, 4)
new_agraph.addEdge(4, 2)
new_agraph.addEdge(4, 0)

# print(new_agraph.checkEdge(0,1))
# print(new_agraph.checkEdge(3,4))
print(new_agraph)
