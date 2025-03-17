import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 3)]
G.add_edges_from(edges)

def draw_graph(graph, title="Graph Visualization"):
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
    plt.title(title)
    plt.show()

def bfs(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(set(graph.neighbors(node)) - visited)
    
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

def has_cycle(graph):
    try:
        cycle = nx.find_cycle(graph, orientation="original")
        return cycle
    except nx.NetworkXNoCycle:
        return None

def shortest_path(graph, start, end):
    try:
        path = nx.shortest_path(graph, source=start, target=end)
        return path
    except nx.NetworkXNoPath:
        return None

draw_graph(G)

print("BFS Traversal:", bfs(G, 1))
print("DFS Traversal:", dfs(G, 1))
print("Cycle Detected:", has_cycle(G))
print("Shortest Path (1 -> 5):", shortest_path(G, 1, 5))
