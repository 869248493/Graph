import unittest
from Graph import *
import BFS, DFS, Edge_Classification


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
        bfs = BFS.bfs(self.g.get_vertex_list())

        expected_list = ['s', 'a', 'b', 'c', 'e']
        self.assertEqual(expected_list, bfs)

    def test_dfs_visit(self):
        self.setEdges("dfs_strong_connection")
        dfs_dict = {}
        dfs = DFS.dict_keys_to_list(DFS.dfs_visit(self.s, dfs_dict))
        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs)

    def test_dfs_visit_2(self):
        self.setEdges("dfs_isolate_vertex")
        dfs_dict = {}
        dfs = DFS.dict_keys_to_list(DFS.dfs_visit(self.s, dfs_dict))
        expected_list = ['s', 'a', 'b', 'c', 'd']
        self.assertEqual(expected_list, dfs)

    def test_iterative_dfs_visit(self):
        self.setEdges("dfs_strong_connection")
        dfs = DFS.dict_keys_to_list(DFS.dfs_visit_iterative(self.s))
        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs)

    def test_iterative_dfs_visit_2(self):
        self.setEdges("dfs_isolate_vertex")
        dfs = DFS.dict_keys_to_list(DFS.dfs_visit_iterative(self.s))
        expected_list = ['s', 'a', 'b', 'c', 'd']
        self.assertEqual(expected_list, dfs)

    def test_dfs(self):
        self.setEdges("dfs_isolate_vertex")

        dfs = DFS.dfs(self.g.get_vertex_list())

        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs)


if __name__ == '__main__':
    unittest.main()
