class Graph:
    def __init__(self):
        # Dictionary to store adjacency list
        # {vertex: [(neighbor, weight), ...]}
        self.adj_list = {}

    # Add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")

    # Add a directed, weighted edge
    def add_edge(self, source, destination, weight):
        if source not in self.adj_list:
            self.add_vertex(source)
        if destination not in self.adj_list:
            self.add_vertex(destination)

        self.adj_list[source].append((destination, weight))

    # Remove an edge
    def remove_edge(self, source, destination):
        if source in self.adj_list:
            self.adj_list[source] = [
                (v, w) for (v, w) in self.adj_list[source]
                if v != destination
            ]

    # Display the graph
    def display(self):
        print("Directed Weighted Graph (Adjacency List):")
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")


# Example Usage
if __name__ == "__main__":
    g = Graph()

    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "D", 4)

    g.display()