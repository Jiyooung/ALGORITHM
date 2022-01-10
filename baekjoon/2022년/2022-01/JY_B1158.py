# baekjoon 1158 : 요세푸스 문제
# solved by JY
# DATE : 2022.01.06
# List 사용

from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
que = list(range(1,n+1))
ans = []
idx = 0
while que:
    idx = (idx + k - 1) % len(que)
    ans.append(str(que.pop(idx)))

print('<', ', '.join(ans), '>', sep='')