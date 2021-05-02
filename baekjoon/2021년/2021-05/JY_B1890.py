# baekjoon 1890 : 점프
# solved by JY
# DATE : 2021.05.01
# DFS + DP 알고리즘 사용
# DP[y][x] : (y,x)에서 (N-1, N-1)까지 가는 경로의 개수

from sys import stdin
input = stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [[-1]*N for _ in range(N)]
dy, dx = [1, 0], [0, 1]

def dfs(y, x):
    if y == N-1 and x == N-1:
        return 1

    num = board[y][x]
    if num == 0:
        return 0

    ret = 0
    for i in range(2):
        ny, nx = y + dy[i]*num, x + dx[i]*num

        if ny >= N or nx >= N:
            continue

        if check[ny][nx] != -1:
            ret += check[ny][nx]
        else:
            ret += dfs(ny, nx)
    
    check[y][x] = ret
    return ret

print(dfs(0, 0))
