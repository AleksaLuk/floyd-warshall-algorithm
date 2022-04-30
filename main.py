from tabulate import tabulate
from floyd_warshall.floyd_warshall_algorithm import fw_imperative, FWRecursiveGraph
from floyd_warshall.utils import transform_graph
from tests.data import graph2 as graph


print("Input graph:")
print(tabulate(transform_graph(graph)))
print("\nImperative output:")
print(tabulate(transform_graph(fw_imperative(graph))))
print("\nRecursion output:")
print(FWRecursiveGraph(graph))
print("Same result: ", )
