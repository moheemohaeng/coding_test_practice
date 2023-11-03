import time
print('=======================Answer=======================')
start_time = time.time()

#code

def fact_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fact_recursive(n):
    if n<= 1:
        return 1
    return n*fact_recursive(n-1)

print(fact_iterative(5))
print(fact_recursive(5))

#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)