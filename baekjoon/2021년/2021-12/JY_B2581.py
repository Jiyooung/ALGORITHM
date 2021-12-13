# baekjoon 2581 : 소수
# solved by JY
# DATE : 2021.12.09
# Implementation

from sys import stdin
input = stdin.readline
m, n = int(input()), int(input())

prime = []

def find(num):  # num이 소수이면 True 반환
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

for i in range(m, n+1):
    if i != 1 and find(i) == True:
        prime.append(i)

if prime:
    print(sum(prime), prime[0], sep='\n')
else:
    print(-1)