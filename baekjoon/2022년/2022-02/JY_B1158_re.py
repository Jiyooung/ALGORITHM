# baekjoon 1158 : 요세푸스 문제
# solved by JY
# DATE : 2022.02.21
# List 사용

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
people = list(range(1, n+1))
answer = []
i = 0
while people:
    i = (i + k - 1) % len(people)
    answer.append(str(people.pop(i)))

print('<', ', '.join(answer), '>', sep='')