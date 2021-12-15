def bfs(vertices, start=0):
    starting_vertex = vertices[start]

    level_dict = {starting_vertex: 0}
    current_level = 1
    frontier = [starting_vertex]
    next_tier = []

    while frontier:
        for vertex in frontier:
            for neighbour in vertex.neighbours:
                if neighbour not in level_dict:
                    level_dict[neighbour] = current_level
                    for next_tier_neighbour in neighbour.neighbours:
                        next_tier.append(next_tier_neighbour)
        frontier = next_tier[:]
        next_tier = []
        current_level += 1

    bfs_list = []
    for key in level_dict.keys():
        bfs_list.append(key.name)

    return bfs_list
