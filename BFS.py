class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.level_dict = {}

    def bfs_construct(self, starting_vertex):
        self.level_dict = {starting_vertex: 0}
        current_level = 1
        frontier = [starting_vertex]
        next_tier = []

        while frontier:
            for vertex in frontier:
                neighbours = vertex.get_neighbours()
                for neighbour in neighbours:
                    if neighbour not in self.level_dict:
                        self.level_dict[neighbour] = current_level
                        next_tier_neighbours = neighbour.get_neighbours()
                        for next_tier_neighbour in next_tier_neighbours:
                            next_tier.append(next_tier_neighbour)
            frontier = next_tier[:]
            next_tier = []
            current_level += 1

    def get_vertex_list(self):
        bfs_list = []
        for key in self.level_dict.keys():
            bfs_list.append(key.get_id())

        return bfs_list

    def get_bfs_string(self):
        res = ""
        first_flag = True
        for key in self.level_dict.keys():
            if first_flag:
                res += key.get_id()
                first_flag = False
            else:
                res += f" -> {key.get_id()}"

        return res

    def print_bfs(self):
        print(self.get_bfs_string())
