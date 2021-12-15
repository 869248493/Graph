from Graph import *
import BFS, DFS

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
    # g.print_graph()
    print(BFS.bfs(v_list))