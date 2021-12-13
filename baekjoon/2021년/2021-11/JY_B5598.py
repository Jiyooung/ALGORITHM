# baekjoon 5598 : 카이사르 암호
# solved by JY
# DATE : 2021.11.18
# Implementation

from sys import stdin
input = stdin.readline
s = list(input().rstrip())

for i in range(len(s)):
    if s[i] in ['A','B','C']:
        print(chr(ord(s[i]) + 23), end='')
    else:
        print(chr(ord(s[i]) - 3), end='')