# baekjoon 1747 : 소수&팰린드롬
# solved by JY
# DATE : 2022.05.04
# 에라토스테네스의 체
# Implementation

from sys import stdin
input = stdin.readline

num = int(input())

# 소수 판별
def find(num):
    i = 2
    while i*i <= num:
        if num % i == 0: return False    # 소수가 아님
        i += 1
    return True

while 1:
    if num != 1 and find(num): # 소수 발견
        if num == int(''.join(reversed(list(str(num))))):
            print(num)
            break
    num += 1
