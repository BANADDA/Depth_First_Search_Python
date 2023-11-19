from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store graph
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        # Function to add an edge to the graph
        self.adjacency_list[u].append(v)

    def depth_first_search(self, start_vertex):
        # Function to perform DFS traversal
        
        # Create a set to store visited vertices
        visited = set()
        
        # Call the recursive helper function
        self._dfs_util(start_vertex, visited)

    def _dfs_util(self, vertex, visited):
        # Recursive utility function for DFS traversal
        
        # Mark the current node as visited and print it
        visited.add(vertex)
        print(vertex, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.adjacency_list[vertex]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)


def create_graph():
    # Function to create a graph based on user input
    
    g = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        g.add_edge(u, v)

    return g


# Driver's code
if __name__ == "__main__":
    # Create the graph based on user input
    graph = create_graph()

    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print("Depth First Traversal:")
    graph.depth_first_search(start_vertex)
