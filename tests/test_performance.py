"""
Module for performance profiling
"""

import cProfile
from floyd_warshall.floyd_warshall_algorithm import fw_imperative, fw_recurive
from tests.data import graph1 as graph

with cProfile.Profile() as pr:
    fw_imperative(graph)

pr.print_stats()

with cProfile.Profile() as pr:
    fw_recurive(graph)

pr.print_stats()
