def dict_keys_to_list(parent_dict):
    res = []
    for key in parent_dict.keys():
        res.append(key.name)
    return res


def dfs_visit(starting_vertex, dfs_dict):
    # vertex = self.vertices[vertex_id]
    # parent_dict = {vertex: None}
    if starting_vertex not in dfs_dict:
        dfs_dict[starting_vertex] = None

    for neighbour in starting_vertex.neighbours:
        if neighbour not in dfs_dict:
            # Add neighbour to dictionary if not in
            dfs_dict[neighbour] = starting_vertex
            dfs_visit(neighbour, dfs_dict)
    return dfs_dict


def dfs_visit_iterative(starting_vertex):
    # input: starting vertex
    # output: null, adding to class dictionary(dfs_dict{visited_vertex: parent_vertex)
    dfs_dict = {}
    parent_v = None
    dfs_dict[starting_vertex] = None
    # modified stacks
    dfs_tracker = [starting_vertex]
    parent_tracker = [None]

    while dfs_tracker:
        first_vertex = dfs_tracker[0]
        # add first vertex in the tracker to the dictionary
        dfs_dict[first_vertex] = parent_tracker[0]

        # remove it from the tracker and set it to parent for the next neighbours
        dfs_tracker.pop(0)
        parent_tracker.pop(0)

        # add neighbours to the front of the tracker
        tmp_neighbours_list = []
        for neighbour in first_vertex.neighbours:
            if neighbour not in dfs_dict:
                tmp_neighbours_list.append(neighbour)
                # add parent for each of the neighbour
                parent_tracker.append(first_vertex)

        tmp_neighbours_list.extend(dfs_tracker)
        dfs_tracker = tmp_neighbours_list
    return dfs_dict


def dfs(vertices):
    dfs_dict = {}
    for vertex in vertices:
        if vertex not in dfs_dict:
            dfs_dict[vertex] = None
            dfs_visit(vertex, dfs_dict)

    return dict_keys_to_list(dfs_dict)


def dfs_iterative(vertices):
    dfs_dict = {}
    for vertex in vertices:
        if vertex not in dfs_dict:
            dfs_dict[vertex] = None
            dfs_dict = dfs_visit_iterative(vertex)

    return dict_keys_to_list(dfs_dict)