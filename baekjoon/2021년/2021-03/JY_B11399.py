# baekjoon 11399 : ATM
# solved twice by JY
# DATE : 2021.03.26
# Greedy 알고리즘, reduce 사용

import sys, functools
input = sys.stdin.readline
N = int(input())
time = sorted(list(map(int, input().split())))
ans = 0
for idx in range(1,N+1):
    ans += functools.reduce(lambda x,y:x+y,time[:idx],0)
print(ans)
