class Graph:
    def __init__(self, vertices):
        # Number of vertices
        self.vertices = vertices
        
        # Initialize adjacency matrix with 0s
        self.adj_matrix = [[0 for _ in range(vertices)] 
                           for _ in range(vertices)]

    # Add an edge (undirected graph)
    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1   # Remove this line for directed graph
        else:
            print("Invalid vertex!")

    # Remove an edge
    def remove_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0   # Remove this line for directed graph
        else:
            print("Invalid vertex!")

    # Display the adjacency matrix
    def display(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)


# Example Usage
if __name__ == "__main__":
    g = Graph(4)  # Create a graph with 4 vertices

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)

    g.display()