# baekjoon 2501 : 약수 구하기
# solved by JY
# DATE : 2021.12.09
# Implementation

from sys import stdin
input = stdin.readline
n, k = map(int, input().split())

for i in range(1, n+1):
    if n % i == 0:
        k = k - 1
        if k == 0:
            print(i)
            break

if k != 0:
    print(0)