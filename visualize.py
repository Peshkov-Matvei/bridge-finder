import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, bridges=None, save_to=None):
    """
    Визуализация графа с выделением мостов
    :param graph: список смежности
    :param bridges: список мостов (опционально)
    :param save_to: путь для сохранения изображения (опционально)
    """
    G = nx.Graph()
    
    # Добавляем рёбра
    for v, neighbors in enumerate(graph):
        for u in neighbors:
            if v < u:
                G.add_edge(v, u)
    
    pos = nx.spring_layout(G, seed=42)
    
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5)
    
    if bridges:
        nx.draw_networkx_edges(G, pos, edgelist=bridges, edge_color='red', width=3)
    
    plt.title("Мосты в графе" + ("" if bridges else " (без поиска)"))
    plt.axis('off')
    
    if save_to:
        plt.savefig(save_to, bbox_inches='tight')
        print(f"Граф сохранен в {save_to}")
    else:
        plt.show()
    plt.close()