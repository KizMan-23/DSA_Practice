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

        for node, neighbors in self.adj_list.items():
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
                neighbor = neighbor.discard(node)  #discard..
            
            del self.adj_list[node]
            
            

    def add_edge(self, src_node, dst_node, weighted = None):
        if src_node not in self.adj_list:
            self.add_node(src_node)
        
        if dst_node not in self.adj_list:
            self.add_node(dst_node)

        if weighted is None:
            self.adj_list[src_node].add(dst_node)
            if not self.directed:
                self.adj_list[dst_node].add(src_node)
        else:
            self.adj_list[src_node].add((dst_node, weighted))
            if not self.directed:
                self.adj_list[dst_node].add((src_node, weighted))


    def remove_edge(self, src_node, dst_node):
        if src_node in self.adj_list.keys():
            for edge in self.adj_list[src_node]:
                    if edge[0] == dst_node:
                        self.adj_list[src_node].remove(dst_node)

                    self.adj_list[src_node].remove(dst_node)
                # if isinstance(dst_node, tuple):
                #     dst_node = dst_node[0]
            
            if not self.directed:
                for edge in self.adj_list[dst_node]:
                    if edge[0] == src_node:
                        self.adj_list[dst_node].remove(src_node)
                        
                    self.adj_list[dst_node].remove(src_node)
                    # if isinstance(src_node, tuple):
                    #     src_node = src_node[0]      
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
        if src_node in self.adj_list:
            if dst_node in self.adj_list[src_node]:
                return True
            else:
                return False
        else:
            raise ValueError("Source Node Not In Adjacency List")
                    

    def get_nodes(self):
        nodes = []
        for n in self.adj_list:
            nodes.append(n)
        return nodes

    def get_edges(self):
        edges = []
        for src_node, neighbors in self.adj_list.items():
            for dst in neighbors:
                edges.append((src_node, dst))
        
        return edges

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node=node)
                for neighbor in sorted(neighbors,reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
                    
        return order

    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node=node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
                    
        return order
    
    def check_print(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

    def dijkstra(self, start):
        import heapq
        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            neighbors = self.adj_list.get(current_distance, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = current_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(heap, (distance, to))
        
        return distances

    def shortest_path(self, start, end):
        import heapq
        distances = {node: float('inf') for node in self.adj_list}
        previous = {node: None for node in self.adj_list}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance == end:
                break
            if current_distance > distances[current_node]:
                continue
            neighbors = self.adj_list.get(current_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to, weight  = neighbor
                else:
                    to, weight = neighbor, 1
                distance = current_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    previous[to] = current_node
                    heapq.heappush(heap, (distance, to))
        
        path = []
        node =  end
        while node is not None:
            path.append(node)
            node = previous.get(node)
        path.reverse()
        if path[0] == start:
            return path
        return []

    def to_adj_matrix(self):
        nodes = self.get_nodes()
        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)

        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                if isinstance(to_node, tuple):
                    to, weight = to_node
                    matrix[index[from_node]][index[to]] = weight
                else:
                    matrix[index[from_node]][index[to_node]] = 1
        
        return matrix

                    
if __name__ == "__main__":
    g = Graph(directed=True)

    g.add_edge("A","B", 1)
    g.add_edge("A", "C", 10)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 1)
    g.add_edge("D", "C", 1)
    g.add_edge("A", "E", 2)
    g.add_edge("E", 'F', 1)
    g.add_edge('G', 'F', 1)
    g.add_edge('F', 'H', 1)
    g.add_edge('H', 'I', 1)
    g.add_edge('I', 'G', 100)

    # print(g)
    print(g.check_print())
    print(g.get_nodes())
    print(g.remove_edge('A', 'C'))
    print(g.get_neighbors('A'))

    print("BFS FROM A: ", g.bfs('A'))
    print("DFS FROM C: ",  g.dfs('A'))