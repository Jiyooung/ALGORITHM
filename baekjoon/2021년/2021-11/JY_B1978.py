# baekjoon 1978 : 소수 찾기
# solved by JY
# DATE : 2021.11.21
# 에라토스테네스의 체
# Implementation

from sys import stdin
input = stdin.readline

def find(num):  # num이 소수이면 True 반환
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def solution(nums):
    answer = 0
    for n in nums:
        if n != 1 and find(n) == True:
            answer += 1

    return answer

# run test
N = map(int, input())
nums = list(map(int, input().split()))
print(solution(nums))