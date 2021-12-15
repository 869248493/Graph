import unittest
from Graph import *
from DFS import *
from BFS import *


class TestGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Vertex('s')
        cls.a = Vertex('a')
        cls.b = Vertex('b')
        cls.c = Vertex('c')
        cls.d = Vertex('d')
        cls.e = Vertex('e')

        cls.v_list = [cls.s, cls.a, cls.b, cls.c, cls.d, cls.e]
        cls.g = Graph(cls.v_list)

    def setEdges(self, mode):
        self.g.clear_edges()
        if mode is "bfs":
            self.g.set_directed_edges(self.b, self.c, 1)
            self.g.set_directed_edges(self.b, self.e, 1)
            self.g.set_directed_edges(self.a, self.b, 1)
            self.g.set_directed_edges(self.a, self.c, 1)
            self.g.set_directed_edges(self.s, self.a, 1)
            self.g.set_directed_edges(self.s, self.b, 1)
        elif mode is "dfs_strong_connection":
            self.g.set_directed_edges(self.s, self.a, 1)
            self.g.set_directed_edges(self.s, self.b, 1)
            self.g.set_directed_edges(self.a, self.b, 1)
            self.g.set_directed_edges(self.a, self.e, 1)
            self.g.set_directed_edges(self.a, self.c, 1)
            self.g.set_directed_edges(self.b, self.c, 1)
            self.g.set_directed_edges(self.c, self.d, 1)
            self.g.set_directed_edges(self.d, self.b, 1)
        elif mode is "dfs_isolate_vertex":
            self.g.set_directed_edges(self.s, self.a, 1)
            self.g.set_directed_edges(self.s, self.b, 1)
            self.g.set_directed_edges(self.a, self.b, 1)
            self.g.set_directed_edges(self.a, self.c, 1)
            self.g.set_directed_edges(self.b, self.c, 1)
            self.g.set_directed_edges(self.c, self.d, 1)
            self.g.set_directed_edges(self.d, self.b, 1)
        else:
            raise ValueError('mode does not exist')

    def test_connected(self):
        pass

    def test_bfs(self):
        self.setEdges("bfs")
        bfs = BFS(self.g)
        bfs.bfs_construct(self.s)
        bfs_list = bfs.get_vertex_list()

        expected_list = ['s', 'a', 'b', 'c', 'e']
        self.assertEqual(expected_list, bfs_list)

    def test_dfs_visit(self):
        self.setEdges("dfs_strong_connection")
        dfs = DFS(self.g)
        dfs.dfs_visit(self.s)
        dfs_list = dfs.get_vertex_list()
        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs_list)

    def test_dfs_visit_2(self):
        self.setEdges("dfs_isolate_vertex")
        dfs = DFS(self.g)
        dfs.dfs_visit(self.s)
        dfs_list = dfs.get_vertex_list()
        expected_list = ['s', 'a', 'b', 'c', 'd']
        self.assertEqual(expected_list, dfs_list)

    def test_iterative_dfs_visit(self):
        self.setEdges("dfs_strong_connection")
        dfs = DFS(self.g)
        dfs.dfs_visit_iterative(self.s)
        dfs_list = dfs.get_vertex_list()
        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs_list)

    def test_iterative_dfs_visit_2(self):
        self.setEdges("dfs_isolate_vertex")
        dfs = DFS(self.g)
        dfs.dfs_visit_iterative(self.s)
        dfs_list = dfs.get_vertex_list()
        expected_list = ['s', 'a', 'b', 'c', 'd']
        self.assertEqual(expected_list, dfs_list)

    def test_dfs(self):
        self.setEdges("dfs_isolate_vertex")

        dfs = DFS(self.g)
        dfs.dfs_construct()
        dfs_list = dfs.get_vertex_list()
        expected_list = ['s', 'a', 'b', 'c', 'd','e']
        self.assertEqual(expected_list, dfs_list)


if __name__ == '__main__':
    unittest.main()
