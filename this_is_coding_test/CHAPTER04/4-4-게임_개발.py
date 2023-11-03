import time
print('=======================Answer=======================')
start_time = time.time()

#code

n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left() :
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


#시작
count = 1
turn_time = 0
while True:

    #일단 회전후 확인
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    #안가본 칸이거나 육지인경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0

    #이동 불가인경우, 한번더 좌회전
    else:
        turn_time += 1
    
    #계속 좌회전 했는데, 다 불가인경우 뒤로 후진
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]

        #후진가능한경우 후진
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        #뒤가 바다여서 후진마저도 불가능한 경우 끝
        else :
            break

        turn_time = 0

print(count)



#code

end_time = time.time()

print('===================================================')
print("time :", end_time - start_time)