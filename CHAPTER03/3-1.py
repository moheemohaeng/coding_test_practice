import time
start_time = time.time()

money = 1260
coin = [500,100,50,10]

how_many_coin = 0
for i in coin :
    how_many_coin += money//i
    money = money - money//i*i

print(how_many_coin)

end_time = time.time()
print("time :", end_time - start_time)