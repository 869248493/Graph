import random


class DirectedEdge:
    def __init__(self, v_from, v_to, weight=1):
        self.v_from = v_from
        self.v_to = v_to
        self.weight = weight

    def get_weight(self):
        return self.weight


class Vertex:
    def __init__(self, name=None):
        self.neighbours = []
        self.name = name
        self.edges = []

    def __str__(self):
        res = ""
        for edge in self.edges:
            res += f"\n   {edge.get_weight()}\n{self.get_name()} ->- {edge.v_to.get_name()}"
        return res

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_neighbour(self, vertex):
        self.neighbours.append(vertex)


class Graph:
    def __init__(self, vertices=None):
        if vertices is None:
            vertices = []
        self.vertices = vertices

        self.edges = []

    def set_directed_edges(self, v_from, v_to, weight):
        edge = DirectedEdge(v_from, v_to, weight)
        self.edges.append(edge)
        v_from.add_edge(edge)
        v_from.add_neighbour(v_to)

    def clear_edges(self):
        self.edges = []
        for vertex in self.vertices:
            vertex.edges = []
            vertex.neighbours = []

    def get_vertex_list(self):
        return self.vertices

    def print_graph(self):
        print("------------------------")
        for vertex in self.vertices:
            print(f"Vertex {vertex.get_name()}:\n{vertex}")
            print("------------------------")

    def generate_random_DAG(self, no_vertices, max_weight=10, max_neighbours=3):
        # Generate some vertices
        for i in range(no_vertices):
            vertex = Vertex()
            vertex.name = f'V{i}'
            self.vertices.append(vertex)

        # Link vertices
        for i in range(no_vertices):
            number_of_neighbours = random.randrange(1, max_neighbours+1)

            # number_of_neighbours -= len(self.vertices[i].neighbours)
            for j in range(number_of_neighbours):
                # create neighbour instance
                if i != no_vertices-1:
                    neighbour_index = random.randrange(i+1, no_vertices)
                    neighbour_weight = random.randrange(1, max_weight+1)
                    neighbour = (self.vertices[neighbour_index],neighbour_weight)
                    self.vertices[i].neighbours.append(neighbour)
