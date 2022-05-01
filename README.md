# Floyd Warshall - Shortest Paths Algorithm

Simple library for implementing and testing the **Floyd Warshall** algorithm

```python
>>> from floyd_warshall.algorithm import fw_imperative, fw_recursive
>>> from floyd_warshall.utils import transform_graph
>>> from tests.data import graph5 as graph

>>> shortest_paths_imp = fw_imperative(graph)
>>> shortest_paths_rec = fw_recursive(graph)

# Input graph:
>>> print(transform_graph(graph))

----  ----  ----  ----
0     7     Null  8
Null  0     5     Null
Null  Null  0     2
Null  Null  Null  0
----  ----  ----  ----

# Imperative output:
>>> print(transform_graph(shortest_paths_imp))

----  ----  ----  -
0     7     12    8
Null  0     5     7
Null  Null  0     2
Null  Null  Null  0
----  ----  ----  -


# Recursive output:
>>> print(transform_graph(shortest_paths_rec))

----  ----  ----  -
0     7     12    8
Null  0     5     7
Null  Null  0     2
Null  Null  Null  0
----  ----  ----  -


# Custom input
>>> import sys
>>> NO_PATH = sys.maxsize

>>> custom_graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

>>> print(transform_graph(fw_recursive(custom_graph)))

----  ----  ----  -
0     7     12    8
Null  0     5     7
Null  Null  0     2
Null  Null  Null  0
----  ----  ----  -
```


## Cloning the repository

```shell
git clone -c https://gitlab.csc.liv.ac.uk/sgalukow/floyd-warshall-algorithm-assignment.git
```

## Installing dependencies

```shell
pip install -r requirements.txt
```

## Installing the repository
(After installing dependencies)

```shell
python setup.py install
```
