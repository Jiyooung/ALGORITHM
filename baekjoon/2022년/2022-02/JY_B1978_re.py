# baekjoon 1978 : 소수 찾기
# solved by JY
# DATE : 2022.02.09
# 에라토스테네스의 체
# 구현

from sys import stdin
input = stdin.readline

n = int(input())
ans = 0

def check(num):
    i = 2
    while i*i <= num:
        if num % i == 0: return False
        i += 1
    return True

for num in list(map(int, input().split())):
    if num != 1 and check(num):
        ans += 1

print(ans)