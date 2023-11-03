import time
start_time = time.time()

#code

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)

print(result)
#code

end_time = time.time()
print("time :", end_time - start_time)