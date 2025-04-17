
#TREE ALGO..
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.content = None
        self.right = None
    
    def insert(self, value, content = None):
        if value < self.value: 
            if self.left is None:
                self.left = BinaryTree(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def deleteNode(self, value):
        if self is None:
            return None
        
        if value < self.value:
            if self.left:
                self.left = self.left.deleteNode(value)
            
        elif value > self.value:
            if self.right:
                self.right = self.right.deleteNode(value)
            
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            
            
            #find the min from subtree
            cur = self.right
            while cur.left:
                cur = cur.left
            self.value = cur.value
            self.content = cur.content

            self.right = self.right.deleteNode(cur.value)
            return self

        return self

        
    def inorder_traverse(self):
        # to go as far left as available at every right
        #returns in increasing order
        in_order = []
        if self.left:
            in_order.extend(self.left.inorder_traverse())
        in_order.append(self.value)
        if self.right:
            in_order.extend(self.right.inorder_traverse())

        return in_order

    def preorder_traverse(self):
        pre_order = []
        pre_order.append(self.value)
        if self.left:
            pre_order.extend(self.left.preorder_traverse())
        
        if self.right:
            pre_order.extend(self.right.preorder_traverse())
        
        return pre_order


    def postorder_traverse(self):
        post_order = []
        if self.left:
            post_order.extend(self.left.postorder_traverse())
        
        if self.right:
            post_order.extend(self.right.postorder_traverse())
        post_order.append(self.value)
        return post_order

    def find(self, value):
        if self is None:
            return None
        
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
    visited = set()
    ans = False
    if srs not in graph:
        return ans
    
    if srs == dst:
        return True
    visited.add(srs)

    for neighbor in graph[srs]:
        if neighbor not in visited:
            visited.add(neighbor)
            ans = ans or check_srs_dst(neighbor, dst, graph)
    
    return ans



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

# def has_undirected_path(src, dst, graph):
#     vis = set()
#     if src not in graph or dst not in graph:
#         return False
    
#     if src == dst:
#         return True
    
#     vis.add(src)
#     for neighbor in graph[src]:
#         if neighbor not in vis:
#             # vis.add(neighbor)
#             if has_undirected_path(neighbor, dst, graph):
#                 return True    
    
#     return False

def has_undirected_path_iterative(src, dst, graph):
    if src not in graph or dst not in graph:
        return False
    if src == dst:
        return True
    
    visited = set()
    stack = [src]
    
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return False
#Q3: Number of provinces in a graph
vec = 10
edges = [
    (1,3), (1,7), (3,7),
    (4,9), (8,5), (8,6),
    (5,10), (6,10)
]

def unique_province(vec, edges):
    #convert the edges to adjacency list first
    graph = {i: [] for i in range(1, vec + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    vis = set()
    count = 0
    stack = []

    for nos in graph:
        stack.append(nos)
        node = stack.pop()
        if node not in vis:
            vis.add(node)
            count += 1
            for neighbors in graph[node]:
                if neighbors not in vis:
                    vis.add(neighbors)
                # stack.append(sorted(neighbors, reverse=True))

    return count

if __name__ == '__main__':
    bts = BinaryTree(10)

    bts.insert(5, content= {"data": "Hello World"})  #To store and append data in tree node storage
    bts.insert(4)
    bts.insert(2)
    bts.insert(1)
    bts.insert(3)
    bts.insert(22)
    bts.insert(11)
    bts.insert(12)


    print(bts.left.left.left.right.value)

    print(bts.find(5).content['data'])
    print(bts.inorder_traverse())
    print(bts.deleteNode(5))
    print(bts.postorder_traverse())

    srs = "A"
    dst = "H"
    print(check_srs_dst(srs,dst,graph))

    print(has_undirected_path_iterative("A", "D", un_graph))

    print("Count of Provinces in the Edge", unique_province(vec, edges=edges))