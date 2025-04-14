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

print(new_graph.checkEdge(0,1))
print(new_graph.checkEdge(3,4))
print(new_graph)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Adj_Graph():
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.adlist = []

    def addNode(self, value):
        new_list = Node(value)

        if len(self.nodes) < self.size:
            self.nodes.append(new_list)
    
    def addEdge(self, src, dst):
        current_list = self.nodes[src]
        current_list = Node(current_list)
        next_node = self.nodes[dst][0]

        current_list.next = next_node

    def checkEdge(self, src, dst):
        current_list = self.nodes[src]
        
        for a in current_list:
            if a == self.nodes[dst]:
                return True
            else:
                return False
    
    def __str__(self):
        pass
    



new_graph = Adj_Graph(5)

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

print(new_graph.checkEdge(0,1))
print(new_graph.checkEdge(3,4))
print(new_graph)
