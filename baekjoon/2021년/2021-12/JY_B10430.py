# baekjoon 10430 : 나머지
# solved by JY
# DATE : 2021.09.23
# 구현

from sys import stdin
input = stdin.readline

A, B, C = map(int, input().split())
print((A+B) % C, ((A % C) + (B % C)) % C, (A*B) % C, ((A % C) * (B % C)) % C, sep="\n")
