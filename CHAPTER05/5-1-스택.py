import time
print('=======================Answer=======================')
start_time = time.time()

#code

stack = []
stack.append(5)
stack.append(4)
stack.append(6)
print('stack : ', stack)
print('pop : ', stack.pop())
print('stack : ', stack)
#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)