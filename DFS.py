class DFS:
    def __init__(self, graph):
        self.dfs_dict = {}
        self.graph = graph

    def dfs_construct(self):
        for vertex in self.graph.get_vertex_list():
            if vertex not in self.dfs_dict:
                self.dfs_dict[vertex] = None
                self.dfs_visit(vertex)

    def get_vertex_list(self):
        res = []
        for key in self.dfs_dict.keys():
            res.append(key.id)
        return res

    def get_dfs_string(self):
        res = ""
        first_flag = True
        for key in self.dfs_dict.keys():
            if first_flag:
                res += key.get_id()
                first_flag = False
            else:
                res += f" -> {key.get_id()}"

        return res

    def print_dfs(self):
        print(self.get_dfs_string())

    def reset_dfs_dict(self):
        self.dfs_dict = {}

    def dfs_visit(self, starting_vertex):
        # vertex = self.vertices[vertex_id]
        # parent_dict = {vertex: None}
        if starting_vertex not in self.dfs_dict:
            self.dfs_dict[starting_vertex] = None

        for neighbour in starting_vertex.neighbours:
            if neighbour not in self.dfs_dict:
                # Add neighbour to dictionary if not in
                self.dfs_dict[neighbour] = starting_vertex
                self.dfs_visit(neighbour)
        return self.dfs_dict

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
            for neighbour in first_vertex.neighbours:
                if neighbour not in self.dfs_dict:
                    tmp_neighbours_list.append(neighbour)
                    # add parent for each of the neighbour
                    parent_tracker.append(first_vertex)

            tmp_neighbours_list.extend(dfs_tracker)
            dfs_tracker = tmp_neighbours_list
        return self.dfs_dict
