# baekjoon 10809 : 알파벳 찾기
# solved by JY
# DATE : 2021.11.18
# Implementation

from sys import stdin
input = stdin.readline
s = str(input().rstrip())
for a in "abcdefghijklmnopqrstuvwxyz":
    print(s.find(a), end=' ')