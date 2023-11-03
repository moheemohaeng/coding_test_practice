import time
print('=======================Answer=======================')
start_time = time.time()

#code

def recursive_func():
    print('재귀함수호출')
    recursive_func()

recursive_func()

#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)