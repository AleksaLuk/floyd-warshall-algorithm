import sys
NO_PATH = sys.maxsize

graph1 = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

ans1 = [[0, 7, 12, 8],
      [9223372036854775807, 0, 5, 7],
      [9223372036854775807, 9223372036854775807, 0, 2],
      [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]

graph2 = [[0,1,43],
          [1,0,6],
          [-1,-1,0]]

ans2 = [[0,1,7],
        [1,0,6],
        [-1,-1,0]]

graph3 = [[0,   5,  NO_PATH, 10],
        [NO_PATH,  0,  3,  NO_PATH],
        [NO_PATH, NO_PATH, 0,   1],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

ans3 = [[0,5,8,9],
    [NO_PATH,0 ,3,4],
    [NO_PATH,NO_PATH,0,1],
    [NO_PATH,NO_PATH,NO_PATH,0]]

graph4 = [[0,NO_PATH,-2,NO_PATH],
          [4,0,3,NO_PATH],
          [NO_PATH,NO_PATH,0,2],
          [NO_PATH,-1,NO_PATH, 0]]

ans4 = [[0,-1,-2,0],
        [4,0,2,4],
        [5,1,0,2],
        [3,-1,1,0]]

graph5 = [[0,3,6,NO_PATH,NO_PATH,NO_PATH,NO_PATH],
          [3,0,2,1,NO_PATH,NO_PATH,NO_PATH],
          [6,2,0,1,4,2,NO_PATH],
          [NO_PATH,1,1,0,2,NO_PATH,4],
          [NO_PATH,NO_PATH,4,2,0,2,1],
          [NO_PATH,NO_PATH,2,NO_PATH,2,0,1],
          [NO_PATH,NO_PATH,NO_PATH,4,1,1,0]]

ans5 = [[0,3,5,4,6,7,7],
        [3,0,2,1,3,4,4],
        [5,2,0,1,3,2,3],
        [4,1,1,0,2,3,3],
        [6,3,3,2,0,2,1],
        [7,4,2,3,2,0,1],
        [7,4,3,3,1,1,0]]


graphs = [graph1, graph2, graph3, graph4, graph5]
answers = [ans1, ans2, ans3, ans4, ans5]
