# baekjoon 3460 : 이진수
# solved by JY
# DATE : 2021.11.07
# Implementation

from sys import stdin
input = stdin.readline
test = int(input())
num = [int(input()) for _ in range(test)]
for t in range(test):
    b = bin(num[t])[2:]
    l = len(b)
    ans = []
    for check in range(l,0,-1):
        if b[check-1] == "1":
            ans.append(l - check)

    for a in ans:
        print(a, end=" ")
    print()