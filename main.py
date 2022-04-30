"""
Main module for demonstration
"""

from tabulate import tabulate
from floyd_warshall.floyd_warshall_algorithm import fw_imperative, fw_recurive
from floyd_warshall.utils import transform_graph
from tests.data import graph2 as graph

shortest_paths_imp = fw_imperative(graph)
shortest_paths_rec = fw_recurive(graph)

print("Input graph:")
print(tabulate(transform_graph(graph)))
print("\nImperative output:")
print(transform_graph(shortest_paths_imp))
print("\nRecursion output:")
print(transform_graph(shortest_paths_rec))

print("Same result:", shortest_paths_rec == shortest_paths_imp)
