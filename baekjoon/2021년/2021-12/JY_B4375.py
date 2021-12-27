# baekjoon 4375 : 1
# solved by JY
# DATE : 2021.12.27
# Implementation

from sys import stdin

for line in stdin:
    case = int(line)
    if case == 1:
        print(1)
        continue
    
    one, cnt = 1, 1
    while one != 0:
        one = (one*10 + 1)%case
        cnt += 1
            
    print(cnt)