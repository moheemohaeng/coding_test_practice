import time
start_time = time.time()

#code

n, m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max_num = data[n-1]
min_num = data[n-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += max_num
        m -= 1
    if m == 0:
        break
    result += min_num
    m -= 1

print(result)

#code

end_time = time.time()
print("time :", end_time - start_time)