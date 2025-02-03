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
            ans = ans or has_undirectedpath(src, dst, graph)
    
    return ans

print(has_undirectedpath("A", "D", un_graph))

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
