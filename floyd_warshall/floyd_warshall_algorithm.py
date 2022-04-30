import itertools
from tabulate import tabulate
from .utils import transform_graph, timeit


@timeit
def fw_imperative(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    MAX_LENGTH = len(distance[0])

    for intermediate, start_node, end_node in itertools.product(
            range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)
    ):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )
        # Any value that have sys.maxsize has no path
    return distance


class FWRecursiveGraph:
    def __init__(self, distance):
        self.distance = distance
        self.max_length = len(distance[0])
        self.fw_recurive()

    @timeit
    def fw_recurive(self):
        """
        A recursive implementation of Floyd's algorithm
        """
        lookup = {}

        def fw_recur(i, j, k):
            if (i, j, k) in lookup:
                return lookup[(i, j, k)]
            if k == 0:
                return self.distance[i][j]

            distance = min(
                fw_recur(i, j, k-1),
                fw_recur(i, k, k-1) + fw_recur(k, j, k-1)
            )
            lookup[i, j, k] = distance
            return distance

        for i in range(self.max_length):
            for j in range(self.max_length):
                self.distance[i][j] = fw_recur(i, j, self.max_length-1)

        return self.distance

    def __str__(self):
        return tabulate(transform_graph(self.distance))
