# programmers L2 : 소수 찾기
# solved by JY
# DATE : 2021.02.21
# 완전탐색, 순열
# map(''.join, itertools.permutations(a, i)) : a에서 i개 뽑은 모든 순열 반환

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
    number = []
    for i in range(1, len(numbers)+1):
        number += map(int, map(''.join, itertools.permutations(numbers, i)))
    number = set(number)
    for n in number:
        if n != 0 and n != 1 and find(n) == True:
            answer += 1

    return answer

# run test
print(solution("17"))   #3