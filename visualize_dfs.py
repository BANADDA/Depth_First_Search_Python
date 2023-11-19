import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def depth_first_search(self, start_vertex):
        visited = set()
        traversal_order = []
        self._dfs_util(start_vertex, visited, traversal_order)
        return traversal_order

    def _dfs_util(self, vertex, visited, traversal_order):
        visited.add(vertex)
        traversal_order.append(vertex)
        for neighbour in self.adjacency_list[vertex]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited, traversal_order)


def create_graph():
    g = Graph()
    num_edges = None
    while num_edges is None:
        try:
            num_edges = int(input("Enter the number of edges: "))
            if num_edges <= 0:
                print("Please enter a positive number of edges.")
                num_edges = None
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for _ in range(num_edges):
        edge_input = input("Enter edge (u v): ")
        try:
            u, v = map(int, edge_input.split())
            g.add_edge(u, v)
        except ValueError:
            print("Invalid input format. Enter two integers separated by space.")
            continue

    return g


def visualize_dfs(graph, traversal_order):
    G = nx.DiGraph()
    for u, v_list in graph.adjacency_list.items():
        for v in v_list:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))

    nx.draw(G, pos, with_labels=True, node_size=800, node_color="skyblue", font_weight="bold", font_size=10, arrows=True)

    for i in range(len(traversal_order) - 1):
        u, v = traversal_order[i], traversal_order[i + 1]
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='red', arrows=True)

    plt.title('Depth First Search Visualization')
    plt.show()


if __name__ == "__main__":
    graph = create_graph()

    start_vertex = None
    while start_vertex is None or start_vertex not in graph.adjacency_list:
        try:
            start_vertex = int(input("Enter the starting vertex for DFS: "))
            if start_vertex not in graph.adjacency_list:
                print(f"Vertex {start_vertex} does not exist in the graph. Please enter a valid vertex.")
        except ValueError:
            print("Invalid input. Please enter a valid vertex.")

    print("Performing Depth First Search...")
    traversal_order = graph.depth_first_search(start_vertex)
    print("Depth First Traversal Order:", traversal_order)

    visualize_dfs(graph, traversal_order)
