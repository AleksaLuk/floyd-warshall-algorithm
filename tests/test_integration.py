import unittest
from ddt import ddt, data, unpack
from tests.data import graphs, answers
from floyd_warshall.floyd_warshall_algorithm import fw_imperative, FWRecursiveGraph, fw_recurive


@ddt
class TestFWAlgorithms(unittest.TestCase):

    @unpack
    @data(*({'graph': graph, 'output': answer} for graph, answer in zip(graphs, answers)))
    def test_fw_imperative(self, graph, output):
        fw_imp_graph = fw_imperative(graph)
        self.assertEqual(fw_imp_graph, output)

    @unpack
    @data(*({'graph': graph, 'output': answer} for graph, answer in zip(graphs, answers)))
    def test_fw_recursive(self, graph, output):
        fw_recur_graph = FWRecursiveGraph(graph).distance
        self.assertEqual(fw_recur_graph, output)

    @unpack
    @data(*({'graph': graph, 'output': answer} for graph, answer in zip(graphs, answers)))
    def test_fw_recursive2(self, graph, output):
        #fw_recur_graph = FWRecursiveGraph(graph).distance
        fw_rec_graph = fw_recurive(graph)
        self.assertEqual(fw_rec_graph, output)


if __name__ == '__main__':
    unittest.main()