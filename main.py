from Graph import *
from BFS import *
from DFS import *

if __name__ == '__main__':
    s = Vertex('s')
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    v_list = [s, a, b, c, d, e]
    g = Graph(v_list)
    g.set_directed_edges(s, a, 1)
    g.set_directed_edges(s, b, 1)
    g.set_directed_edges(a, e, 1)
    g.set_directed_edges(a, b, 1)
    g.set_directed_edges(a, b, 1)
    g.set_directed_edges(b, c, 1)
    g.set_directed_edges(c, d, 1)
    g.set_directed_edges(d, b, 1)

    print("----------------------------------------Graph----------------------------------------")
    g.print_graph()
    print("----------------------------------------BFS----------------------------------------")
    bfs = BFS(g)
    bfs.bfs_construct(s)
    print(bfs.get_vertex_list())
    print(bfs.get_bfs_string())

    print("----------------------------------------DFS----------------------------------------")
    dfs = DFS(g)
    dfs.dfs_construct()
    print(dfs.get_vertex_list())
    print(dfs.get_dfs_string())
