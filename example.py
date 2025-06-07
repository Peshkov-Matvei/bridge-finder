from bridge import find_bridges
from visualize import draw_graph


graph = [
    [1, 2],
    [0, 2, 3],
    [0, 1],
    [1, 4],
    [3, 5],
    [4],
]


bridges = find_bridges(graph)
print("Найденные мосты:")
for bridge in bridges:
    print(f"{bridge[0]} -- {bridge[1]}")

draw_graph(graph, bridges, save_to="graph_with_bridges.png")

cycle = [[1, 4], [0, 2], [1, 3], [2, 4], [3, 0]]
draw_graph(cycle, save_to="cycle_without_bridges.png")