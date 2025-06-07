def find_bridges(graph):
    """
    Находит все мосты в неориентированном графе
    :param graph: список смежности (list of lists)
    :return: список мостов (list of tuples)
    """
    n = len(graph)
    tin = [-1] * n
    low = [-1] * n
    bridges = []
    timer = 0
    
    def dfs(v, parent=-1):
        nonlocal timer
        tin[v] = low[v] = timer
        timer += 1
        for u in graph[v]:
            if u == parent:
                continue
            if tin[u] == -1:
                dfs(u, v)
                low[v] = min(low[v], low[u])
                if low[u] > tin[v]:
                    bridges.append((min(v, u), max(v, u)))
            else:
                low[v] = min(low[v], tin[u])
    
    for i in range(n):
        if tin[i] == -1:
            dfs(i)
            
    return bridges

def read_graph_from_file(filename):
    """Чтение графа из файла"""
    graph = []
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            neighbors = list(map(int, f.readline().split()))
            graph.append(neighbors)
    return graph