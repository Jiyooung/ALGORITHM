# baekjoon 1495 : 기타리스트
# solved by JY
# DATE : 2021.05.06
# DP 알고리즘 사용(완탐 느낌)
# check[n][v] = n번 째 곡이 v 볼륨이 가능하면 1

from sys import stdin
input = stdin.readline
N, S, M = map(int, input().split())
V = list(map(int, input().split()))
check = [[0]*(M+1) for _ in range(N+1)]
check[0][S] = 1

for idx, v in enumerate(V):
    for start in range(M+1):
        if check[idx][start] == 1:
            if start + v <= M:
                check[idx+1][start + v] = 1
            if 0 <= start - v:
                check[idx+1][start - v] = 1

for idx in range(M, -1, -1):
    if check[N][idx] == 1:
        print(idx)
        exit(0)

print(-1)