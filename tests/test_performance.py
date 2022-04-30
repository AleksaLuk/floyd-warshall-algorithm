"""
Module for performance profiling
"""

import cProfile
import timeit
from floyd_warshall.algorithm import fw_imperative, fw_recursive


def analyse_profiling(graph):
    with cProfile.Profile() as pr:
        fw_imperative(graph)
    print("Imperative profiling")
    pr.print_stats()

    with cProfile.Profile() as pr:
        fw_recursive(graph)
    print("Recursive profiling")
    pr.print_stats()


def analyse_timing(graph, repeats=10000):
    t = timeit.Timer(f"fw_recursive({graph})", globals=globals())
    rec = t.timeit(repeats)
    t = timeit.Timer(f"fw_imperative({graph})", globals=globals())
    imp = t.timeit(repeats)

    print(f"Average recursive time taken: {rec / repeats}")
    print(f"Average imperative time taken: {imp / repeats}")
    print(f"Ratio rec:imp = {rec / imp}")
