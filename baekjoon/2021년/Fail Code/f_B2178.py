# baekjoon 2178 : 미로 탐색
# solved by JY
# DATE : 2020.01.19
# DFS는 재귀제한 초과 및 시간 초과 발생으로 구현 불가

def DFS(y, x, count):
    visit[y][x] = count        # 이동할 수 있는 칸이면 + 1

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if yy >= 0 and yy < N and xx >= 0 and xx < M:
            if (visit[y][x] + 1 < visit[yy][xx] or visit[yy][xx] == 0) and miro[yy][x] != 0: # 지금 가는 곳이 내가 가면 더 최단경로임
                DFS(yy, xx, visit[y][x] + 1)

# run test
import sys
sys.setrecursionlimit(10**8)    # 기본 1000재귀를 지원하는 백준의 재귀제한 늘릴 때 사용

N, M = map(int, sys.stdin.readline().split())
miro = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]
for i in range(N):
    miro[i] = list(map(int, sys.stdin.readline().rstrip()))

# print(miro)
dy = [-1, 1, 0, 0]  # 상하좌우
dx = [0, 0, -1, 1]

DFS(0, 0, 1)
# for i in miro:
#     print(i)
# print()
# for i in visit:
#     print(i)

print(visit[N-1][M-1])