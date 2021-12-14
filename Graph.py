import random


def dict_keys_to_list(parent_dict):
    res = []
    for key in parent_dict.keys():
        res.append(key.name)
    return res


class Edge:
    def __init__(self, v1, v2, weight=1):
        self.vertices = [v1, v2]
        self.weight = weight


class Vertex:
    def __init__(self, name=None, neighbours=None):
        # neighbours is a list of tuple (vertex, weight)
        if neighbours is None:
            neighbours = []
        self.neighbours = neighbours
        self.name = name
        self.edges = []

        for neighbour in neighbours:
            self.edges.append(Edge(self, neighbour[0], neighbour[1]))

    def __str__(self):
        res = f'{self.name}'
        for neighbour in self.neighbours:
            res += f' -> {neighbour[0].name}, {neighbour[1]}  \n'
        return res


class Graph:
    def __init__(self, vertices=None):
        if vertices is None:
            vertices = []
        self.vertices = vertices

        self.edges = []

        self.dfs_dict = {}

    def add_edges(self, v1, v2, weight):
        pass

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

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex.to_string())

    def itervertices(self):
        pass

    def bfs(self, start=0):
        starting_vertex = self.vertices[start]

        level_dict = {starting_vertex:0}
        current_level = 1
        frontier = [starting_vertex]
        next_tier = []

        while frontier:
            for vertex in frontier:
                for neighbour_weight_pair in vertex.neighbours:
                    neighbour = neighbour_weight_pair[0]
                    if neighbour not in level_dict:
                        level_dict[neighbour] = current_level
                        for next_tier_neighbour in neighbour.neighbours:
                            next_tier.append(next_tier_neighbour[0])
            frontier = next_tier[:]
            next_tier = []
            current_level += 1

        bfs_list = []
        for key in level_dict.keys():
            bfs_list.append(key.name)

        return bfs_list

    def dfs_visit(self, starting_vertex):
        # vertex = self.vertices[vertex_id]
        # parent_dict = {vertex: None}
        if starting_vertex not in self.dfs_dict:
            self.dfs_dict[starting_vertex] = None

        for neighbour_weight_pair in starting_vertex.neighbours:
            neighbour = neighbour_weight_pair[0]
            if neighbour not in self.dfs_dict:
                # Add neighbour to dictionary if not in
                self.dfs_dict[neighbour] = starting_vertex
                self.dfs_visit(neighbour)

    def dfs_visit_iterative(self, starting_vertex):
        # input: starting vertex
        # output: null, adding to class dictionary(dfs_dict{visited_vertex: parent_vertex)

        parent_v = None
        self.dfs_dict[starting_vertex] = None
        # modified stacks
        dfs_tracker = [starting_vertex]
        parent_tracker = [None]

        while dfs_tracker:
            first_vertex = dfs_tracker[0]
            # add first vertex in the tracker to the dictionary
            self.dfs_dict[first_vertex] = parent_tracker[0]

            # remove it from the tracker and set it to parent for the next neighbours
            dfs_tracker.pop(0)
            parent_tracker.pop(0)

            # add neighbours to the front of the tracker
            tmp_neighbours_list = []
            for neighbour_weight_pair in first_vertex.neighbours:
                neighbour = neighbour_weight_pair[0]
                if neighbour not in self.dfs_dict:
                    tmp_neighbours_list.append(neighbour)
                    # add parent for each of the neighbour
                    parent_tracker.append(first_vertex)

            tmp_neighbours_list.extend(dfs_tracker)
            dfs_tracker = tmp_neighbours_list

    def dfs(self):
        for vertex in self.vertices:
            if vertex not in self.dfs_dict:
                self.dfs_dict[vertex] = None
                self.dfs_visit(vertex)

        return dict_keys_to_list(self.dfs_dict)








