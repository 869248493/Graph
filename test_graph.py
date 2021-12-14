import unittest
from Graph import *


class TestGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s = Vertex('s')
        cls.a = Vertex('a')
        cls.b = Vertex('b')
        cls.c = Vertex('c')
        cls.d = Vertex('d')
        cls.e = Vertex('e')

    def test_connected(self):
        pass

    def test_bfs(self):
        self.e.neighbours = []
        self.d.neighbours = []
        self.c.neighbours = []
        self.b.neighbours = [(self.c, 1), (self.e, 4)]
        self.a.neighbours = [(self.b, 1), (self.c, 1)]
        self.s.neighbours = [(self.a, 1), (self.b, 1)]

        e1 = [self.s, self.a, self.b, self.c]

        g = Graph(e1)
        bfs = g.bfs()

        expected_list = ['s', 'a', 'b', 'c', 'e']
        self.assertEqual(expected_list, bfs)

    def test_dfs_visit(self):
        self.s.neighbours = [(self.a, 1), (self.b, 1)]
        self.a.neighbours = [(self.b, 1), (self.c, 1), (self.e, 6)]
        self.b.neighbours = [(self.c, 1)]
        self.c.neighbours = [(self.d, 1)]
        self.d.neighbours = [(self.b, 1)]
        self.e.neighbours = []

        e1 = [self.s, self.a, self.b, self.c, self.d, self.e]
        g = Graph(e1)
        g.dfs_visit(self.s)
        dfs = dict_keys_to_list(g.dfs_dict)

        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs)

    def test_dfs_visit_2(self):
        self.s.neighbours = [(self.a, 1), (self.b, 1)]
        self.a.neighbours = [(self.b, 1), (self.c, 1)]
        self.b.neighbours = [(self.c, 1)]
        self.c.neighbours = [(self.d, 1)]
        self.d.neighbours = [(self.b, 1)]
        self.e.neighbours = []

        e1 = [self.s, self.a, self.b, self.c, self.d, self.e]
        g = Graph(e1)
        g.dfs_visit(self.s)
        dfs = g.dfs_dict
        dfs = dict_keys_to_list(dfs)

        expected_list = ['s', 'a', 'b', 'c', 'd']
        self.assertEqual(expected_list, dfs)

    def test_dfs(self):
        self.s.neighbours = [(self.a, 1), (self.b, 1)]
        self.a.neighbours = [(self.b, 1), (self.c, 1)]
        self.b.neighbours = [(self.c, 1)]
        self.c.neighbours = [(self.d, 1)]
        self.d.neighbours = [(self.b, 1)]
        self.e.neighbours = []

        e1 = [self.s, self.a, self.b, self.c, self.d, self.e]
        g = Graph(e1)
        dfs = g.dfs()

        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs)

    def test_iterative_dfs_visit(self):
        self.s.neighbours = [(self.a, 1), (self.b, 1)]
        self.a.neighbours = [(self.b, 1), (self.c, 1), (self.e, 6)]
        self.b.neighbours = [(self.c, 1)]
        self.c.neighbours = [(self.d, 1)]
        self.d.neighbours = [(self.b, 1)]
        self.e.neighbours = []

        e1 = [self.s, self.a, self.b, self.c, self.d, self.e]
        g = Graph(e1)
        g.dfs_visit_iterative(self.s)
        dfs = dict_keys_to_list(g.dfs_dict)

        expected_list = ['s', 'a', 'b', 'c', 'd', 'e']
        self.assertEqual(expected_list, dfs)

    def test_iterative_dfs_visit_2(self):
        self.s.neighbours = [(self.a, 1), (self.b, 1)]
        self.a.neighbours = [(self.b, 1), (self.c, 1), (self.e, 6)]
        self.b.neighbours = [(self.c, 1)]
        self.c.neighbours = [(self.d, 1)]
        self.d.neighbours = [(self.b, 1)]
        self.e.neighbours = []

        e1 = [self.s, self.a, self.b, self.c, self.d, self.e]
        g = Graph(e1)
        g.dfs_visit(self.s)
        dfs_recursive = dict_keys_to_list(g.dfs_dict)
        g.dfs_dict = {}
        g.dfs_visit_iterative(self.s)
        dfs_iterative = dict_keys_to_list(g.dfs_dict)
        self.assertEqual(dfs_recursive,dfs_iterative)


if __name__ == '__main__':
    unittest.main()