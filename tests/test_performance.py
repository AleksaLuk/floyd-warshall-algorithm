"""
tests.test_performance
~~~~~~~~~~~~~~~~~~~
This module contains performance functions for testing the algorithm run times and profiling.
"""

from numbers import Number
import cProfile
import timeit
from floyd_warshall.algorithm import fw_imperative, fw_recursive


def analyse_profiling(graph: list[list[Number]]):
    """
    Function which prints a profiling table for each algorithm implementation
    for a particular input graph. This is useful for analysing the difference
    in function calls between recursive and imperative versions

    :param graph: input graph containing n x n columns and rows
    :return: None
    """

    with cProfile.Profile() as profiler:
        fw_imperative(graph)
    print("Imperative profiling")
    profiler.print_stats()

    with cProfile.Profile() as profiler:
        fw_recursive(graph)
    print("Recursive profiling")
    profiler.print_stats()


def analyse_timing(graph: list[list[Number]], repeats=10000):
    """
    Function which runs both implementations of the algorithm for an input graph
    and prints an average run time per implementation over n repeats

    :param graph: input graph containing n x n columns and rows
    :param repeats: Number of times the algorithm run should be repeated
    :return: None
    """

    timer = timeit.Timer(f"fw_recursive({graph})", globals=globals())
    rec = timer.timeit(repeats)
    timer = timeit.Timer(f"fw_imperative({graph})", globals=globals())
    imp = timer.timeit(repeats)

    print(f"Average recursive time taken: {rec / repeats} seconds")
    print(f"Average imperative time taken: {imp / repeats} seconds")
    print(f"Ratio recursive / imperative = {rec / imp}")
