# baekjoon 1037 : 약수
# solved by JY
# DATE : 2021.11.06
# 구현

from sys import stdin
input = stdin.readline
N = int(input())
b = sorted(list(map(int, input().split())))
print(b[0] * b[-1])