"""
floyd_warshall.utils
~~~~~~~~~~~~~~~~~~~
This module contains helper functions surrounding the implementation of algorithms.
"""

import time
import sys
from numbers import Number
from tabulate import tabulate
from floyd_warshall.exceptions import InputValidationError


def transform_graph(distance: list[list[Number]]) -> str:
    """
    Function to make graph output more readable for the user by:
        - Replacing MAX_SIZE variables with 'Null'
        - Tabulating nested list into matrix format

    :param distance: graph containing distances between nodes
    :return: String
    """

    transformed = tabulate(
        [[x if x != sys.maxsize else "Null" for x in graph] for graph in distance]
    )
    return transformed


def timeit(func):
    """
    Decorator for augmenting functions with a timer

    :param func: algorithm function
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__} :Time taken: {round(time.time() - start, 10)} seconds")
        return ret

    return wrapper


def validate_input(graph: list[list[Number]]):
    """
    Function for validating user input before passing to algorithms

    If validation fails, an exception is raised to the user

    :param graph: input graph containing distances between nodes
    :return: None
    """

    if not isinstance(graph, list):
        raise InputValidationError(
            "Graph input must be in a list[i][j] for i rows and j columns"
        )

    if not all((isinstance(row, list) for row in graph)):
        raise InputValidationError(
            "Graph input must contain nested lists"
        )

    if not all((isinstance(num, (int, float)) for row in graph for num in row)):
        raise InputValidationError(
            "Your graph contains non-numeric elements, allowable types: int, float"
        )

    if any((len(row) != len(graph) for row in graph)):
        raise InputValidationError(
            "Row and column sizes must be the same, input matrix of n x n"
        )
