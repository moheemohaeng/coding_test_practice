import time
print('=======================Answer=======================')
start_time = time.time()

#code

# 인접 리스트 방식
graph = [[] for i in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)

#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)