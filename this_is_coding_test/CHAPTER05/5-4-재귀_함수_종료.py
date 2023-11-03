import time
print('=======================Answer=======================')
start_time = time.time()

#code

def recursive_func(i):
    if i == 100:
        print("끝!")
        return
    print(i, '번째 재귀함수호출')
    recursive_func(i+1)

a = 1
recursive_func(a)

#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)