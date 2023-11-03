import time
print('=======================Answer=======================')
start_time = time.time()

#code
from collections import deque
queue = deque()
queue.append(5)
queue.append(4)
queue.append(6)
print('queue : ', queue)
print('pop : ', queue.popleft())
print('queue : ', queue)


#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)