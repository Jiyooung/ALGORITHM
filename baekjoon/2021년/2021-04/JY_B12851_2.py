# baekjoon 12851 : 숨바꼭질 2
# solved by JY + best
# DATE : 2021.04.20
# BFS 알고리즘 사용

from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().split())

if N >= K:
    print(N-K, 1, sep='\n')
    exit(0)

que = deque([N])
INF = float('inf')
visit, way = [INF]*100001, [0]*100001
visit[N], way[N] = 0, 1
while que:
    x = que.popleft()

    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < 100001:
            if visit[nx] == INF:
                visit[nx] = visit[x] + 1
                way[nx] = way[x]
                que.append(nx)
            elif visit[nx] == visit[x]+1:
                way[nx] += way[x]

print(visit[K], way[K], sep='\n')