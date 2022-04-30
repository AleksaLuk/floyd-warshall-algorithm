import time


def transform_graph(distance):
    return [[x if x < 100000000000000 else 'Null' for x in graph] for graph in distance]


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print(f"Time taken: {round(time.time() - start, 10)} seconds")
        return ret
    return wrapper
