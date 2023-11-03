import time
print('=======================Answer=======================')
start_time = time.time()

#code

# 인접 행렬
INF = 99999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)