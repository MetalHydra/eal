import random 
import time

rands = [random.randint(0,10000) for _ in range(10000)]

#native implementation
s_time = time.time()
nums = [4000,8000,16000,32000,64000,128000,256000]
min_num = 1000000
for _num in nums:
    x1, x2 = 0,0
    for i in range(len(rands)):
        for j in range(1, len(rands)):
            if abs(rands[i] - rands[j]) < min_num:
                min_num = abs(rands[i] - rands[j])
                x1 = rands[i]
                x2 = rands[j]
    e_time = time.time()
    print(f'ellapsed time native: {e_time-s_time}')
    print(f'min pair x1, x2: {x1}, {x2} with value: {min_num}')

    s_time = time.time()
    sorted_rands = sorted(rands)
    min_num = 1000000
    x1, x2 = 0,0
    for i in range(1,len(sorted_rands)):
        if abs(sorted_rands[i] - sorted_rands[i-1]) < min_num:
            min_num = abs(sorted_rands[i] - sorted_rands[i-1])
            x1 = sorted_rands[i-1]
            x2 = sorted_rands[i]
    e_time = time.time()
    print(f'ellapsed time: {e_time-s_time}')
    print(f'min pair x1, x2: {x1}, {x2} with value: {min_num}')

