import time
print('=======================Answer=======================')
start_time = time.time()

#code

h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)

#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)