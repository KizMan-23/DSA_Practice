#Q1: check if the path exists between src & dst (directed acyclic graph. i.e--one path). return true or false
#Sample graph
#queue Algorithm = Breath-First-Search(BFS)
#stack Algorithm = Depth-First-Search(DFS)

graph = {
"A": ["B","C"],
"B": ["F","D"],
"C": ["A"],
"D": ["G","I"],
"E": ["H"],
"F": ["E"],
"G": ["H"],
"H": [],
"I": []
}
#algorithm: recursive DFS design

def check_srs_dst(srs, dst, graph):
    if srs == dst:
        return True
    ans = False

    for neighbor in graph[srs]:
        ans = ans or check_srs_dst(neighbor, dst, graph)
    
    return ans

srs, dst = input().split()
print(check_srs_dst(srs,dst,graph))

#Q2: Check if path exists between src and dist (undirected)

un_graph = {
    "A": ["B", "C"],
    "B": ['A',"C","F"],
    "C": ["A"],
    "D": ["G", "B", "I"],
    "E": ["F", "H"],
    "F": ["E", "B"],
    "G": ["D", "H"],
    "H": ["E", "G"],
    "I": ["D"]
    }

def has_undirectedpath(src, dst, graph):
    vis = set()
    if src == dst:
        return True
    vis.add(src)
    ans = False
    for neighbor in graph[src]:
        if neighbor not in vis:
            vis.add(neighbor)
            ans = ans or has_undirectedpath(src, dst, graph)
    
    return ans

# print(has_undirectedpath("A", "D", un_graph))

#Q3: Number of provinces in a graph
vec = 10
edges = [
    (1,3), (1,7), (3,7),
    (4,9), (8,5), (8,6),
    (5,10), (6,10)
]

def unique_province(edges):
    vis = set()
    count = 0
    for nos in range(vec):
        if nos not in vis:
            neighs = unique_province(nos) #perform dfs
            vis.add(neighs)
            
            count += 1
        return

    return count #count should be 4


#TREE ALGO..
class binary_tree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = binary_tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = binary_tree(value)
            else:
                self.right.insert(value)
        
    def inorder_traverse(self):
        pass

    def preorder_traverse(self):
        pass

    def  postorder_traverse(self):
        pass
        

bts = binary_tree(10)

# bts.insert(10)
bts.insert(5)
bts.insert(4)
bts.insert(2)
bts.insert(1)
bts.insert(3)
bts.insert(22)
bts.insert(11)
bts.insert(12)


print(bts.left.left.left.value)
