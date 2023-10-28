import time
print('=======================Answer=======================')
start_time = time.time()

#code

n = int(input())
x, y = 1,1
plans = input().split()

move_types = ['L','U','R','D']
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    
    x, y = nx, ny
    # print(x, y)

print(x,y)
#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)