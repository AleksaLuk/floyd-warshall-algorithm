import time
from floyd_warshall.exceptions import InputValidationError
from tabulate import tabulate
import sys


def transform_graph(distance):
    transformed = tabulate(
        [[x if x != sys.maxsize else 'Null' for x in graph] for graph in distance]
    )
    return transformed


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__} :Time taken: {round(time.time() - start, 10)} seconds")
        return ret
    return wrapper


def validate_input(graph):
    if isinstance(graph, list):
        raise InputValidationError("Graph input must be in a list[i][j] for i rows and j columns")

    if any((isinstance(num, (int, float)) for row in graph for num in row)):
        raise InputValidationError("Your graph contains non-numeric elements, allowable types: int, float")

    if any((len(row) != len(graph) for row in graph)):
        raise InputValidationError("Row and column sizes must be the same, input matrix of n x n")
