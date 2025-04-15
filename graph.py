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
        result  = ""
        for d in self.nodes:
            result += f"  {d}"
        result += "\n"

        for a in range(self.size):
            result += f"{self.nodes[a]}"
        
            for b in self.matrix[a]:
                result += f" {b} "   

            result += "\n"
        #__str__ must have a return statement
        return result
    

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

print(new_agraph.checkEdge(0,1))
print(new_agraph.checkEdge(3,4))
print(new_agraph)


class Graph():
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""

        for node, neighbors in self.adj_list:
            graph_str += f"{node} -> {neighbors}\n"
        return graph_str 

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node Already Exists")

    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node does Not Exist")
        else:
            for neighbor in self.adj_list.values():
                neighbor = neighbor.discard(node)
            
            del self.adj_list[node]
            # self.adj_list[node] = None
            # del node

    def add_edge(self, src_node, dst_node, weighted = None):
        if src_node not in self.adj_list:
            self.adj_list.add_node(src_node)
        
        if dst_node not in self.adj_list:
            self.adj_list.add_node(dst_node)

        if weighted is None:
            self.adj_list[src_node].add(dst_node) #maybe use append??
            if not self.directed:
                self.adj_list[dst_node].add(src_node)
        else:
            self.adj_list[src_node].add((dst_node, weighted))
            if not self.directed:
                self.adj_list[dst_node].add((src_node, weighted))


    def remove_edge(self, src_node, dst_node):
        if src_node in self.adj_list:
            if dst_node in self.adj_list[src_node]:
                self.adj_list[src_node].remove(dst_node)  #remove may not be a list function
            else:
                raise ValueError(f"Node {dst_node} does not exist in Source Node")
            
            if not self.directed:
                if src_node in self.adj_list[dst_node]:
                    self.adj_list[dst_node].remove(src_node)
                else:
                    raise ValueError(f"Source Node may not exist in Node {dst_node}")
        else:
            raise ValueError(f"Node {src_node} does not exist in the Adjacency List")

    def get_neighbors(self, node):
        result = set()
        for neigbors in self.adj_list[node]:
            result.add(neigbors)
        return result

        # return self.adj_list.get(node,set())

    def has_node(self, node):
        return node in self.adj_list

    def has_edge(self, src_node, dst_node):
        pass

    def get_nodes(self):
        pass

    def get_edges(self):
        pass

    def bfs(self, start):
        pass

    def dfs(self, start):
        pass