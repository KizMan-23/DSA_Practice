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
        for a in range(self.size):
            for b in self.matrix[a]:

                print(f" {b}", end="")
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


print(new_graph)