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
    def __init__(self, value):
        self.value = value
        self.left = None
        self.content = None
        self.right = None
    
    def insert(self, value, content = None):
        if value < self.value: 
            if self.left is None:
                self.left = binary_tree(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = binary_tree(value)
                self.right.content = content
            else:
                self.right.insert(value, content)
        
    def inorder_traverse(self):
        # to go as far left as available at every right
        #returns in increasing order
        if self.left:
            self.left.inorder_traverse()
        print(self.value)
        if self.right:
            self.right.inorder_traverse()

    def preorder_traverse(self):
        print(self.value)
        if self.left:
            self.left.preorder_traverse()
        
        if self.right:
            self.right.preorder_traverse()


    def postorder_traverse(self):
        if self.left:
            self.left.postorder_traverse()
        
        if self.right:
            self.right.postorder_traverse()
        print(self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self

bts = binary_tree(10)

# bts.insert(10)
bts.insert(5, content= {"data": "Hello World"})  #To store and append data in tree node storage
bts.insert(4)
bts.insert(2, {"data": "Hello World"})
bts.insert(1)
bts.insert(3, {"data": "Hello World"})
bts.insert(22)
bts.insert(11, {"data": "Hello World"})
bts.insert(12)


print(bts.left.left.left.right.value)

print(bts.find(5).content['data'])
