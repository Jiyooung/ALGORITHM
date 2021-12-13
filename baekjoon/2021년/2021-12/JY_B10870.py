# baekjoon 10870 : 피보나치 수 5
# solved by JY
# DATE : 2021.12.10
# Recursion

from sys import stdin
input = stdin.readline
n = int(input())

def fib(cnt):
    if cnt == 0: return 0
    if cnt == 1 or cnt == 2: return 1
    return fib(cnt-1) + fib(cnt-2)

print(fib(n))