# baekjoon 1978 : 소수 찾기
# solved by JY
# DATE : 2021.02.21
# 완전탐색

import itertools

def find(num):  # num이 소수이면 True 반환
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def solution(numbers):
    answer = 0
    for n in numbers:
        if n != 0 and n != 1 and find(n) == True:
            answer += 1

    return answer

# run test
import sys
input = sys.stdin.readline
N = map(int, input())
numbers = list(map(int, input().split(" ")))
print(solution(numbers))