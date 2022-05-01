"""
main
~~~~~~~~~~~~~~~~~~~
Main module used for demonstration.
"""

import sys
from floyd_warshall.algorithm import fw_imperative, fw_recursive
from floyd_warshall.utils import transform_graph
from tests.data import graph1 as graph
from tests.test_performance import analyse_timing, analyse_profiling

print("Input graph:")
print(transform_graph(graph))

shortest_paths_imp = fw_imperative(graph)
shortest_paths_rec = fw_recursive(graph)

print("\nImperative output:")
print(transform_graph(shortest_paths_imp))
print("\nRecursion output:")
print(transform_graph(shortest_paths_rec))

print("Same result:", shortest_paths_rec == shortest_paths_imp)
print()

analyse_timing(graph, repeats=100)
print()
analyse_profiling(graph)

# Custom input
NO_PATH = sys.maxsize

custom_graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0],
]
print(transform_graph(fw_recursive(custom_graph)))
