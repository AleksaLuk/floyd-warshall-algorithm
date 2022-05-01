"""
floyd_warshall.algorithm
~~~~~~~~~~~~~~~~~~~
File containing imperative and recursive versions of the Floyd Warshall algorithm.
"""


import itertools
from numbers import Number
from floyd_warshall.utils import validate_input


def fw_imperative(distance: list[list[Number]]) -> list[list[Number]]:
    """
    An imperative implementation of Floyd's algorithm

    :param distance: input graph containing n x n columns and rows
    :return: output graph with updated distances between nodes
    """

    validate_input(distance)
    distance = distance.copy()
    max_length = len(distance[0])

    for intermediate, start_node, end_node in itertools.product(
        range(max_length), range(max_length), range(max_length)
    ):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node],
        )
        # Any value that have sys.maxsize has no path
    return distance


def fw_recursive(distance: list[list[Number]]) -> list[list[Number]]:
    """
    A recursive implementation of Floyd's algorithm

    :param distance: input graph containing n x n columns and rows
    :return: output graph with updated distances between nodes
    """

    validate_input(distance)
    distance = distance.copy()
    lookup = {}
    max_length = len(distance[0])

    def fw_recur(i, j, k, distance):
        if (i, j, k) in lookup:
            return lookup[(i, j, k)]
        if k == 0:
            return distance[i][j]

        length = min(
            fw_recur(i, j, k - 1, distance),
            fw_recur(i, k, k - 1, distance) + fw_recur(k, j, k - 1, distance),
        )
        lookup[i, j, k] = length
        return length

    for i in range(max_length):
        for j in range(max_length):
            distance[i][j] = fw_recur(i, j, max_length - 1, distance)

    return distance


# class FWRecursiveGraph:
#     """Class implementation of the recursive FW algorithm"""
#
#     def __init__(self, distance):
#         self.distance = distance
#         self.max_length = len(distance[0])
#         self.fw_recurive()
#
#     def fw_recurive(self):
#         """
#         A recursive implementation of Floyd's algorithm
#         """
#
#         lookup = {}
#
#         def fw_recur(i, j, k):
#             if (i, j, k) in lookup:
#                 return lookup[(i, j, k)]
#             if k == 0:
#                 return self.distance[i][j]
#
#             distance = min(
#                 fw_recur(i, j, k-1),
#                 fw_recur(i, k, k-1) + fw_recur(k, j, k-1)
#             )
#             lookup[i, j, k] = distance
#             return distance
#
#         for i in range(self.max_length):
#             for j in range(self.max_length):
#                 self.distance[i][j] = fw_recur(i, j, self.max_length-1)
#
#         return self.distance
#
#     def __str__(self):
#         return transform_graph(self.distance)
