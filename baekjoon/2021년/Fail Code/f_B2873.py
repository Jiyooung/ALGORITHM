# baekjoon 2873 : 롤러코스터
# solved by JY
# DATE : 2021.03.26
# dfs, dp로 풀어보려다가 RecursionError 나서 stop

import sys
input = sys.stdin.readline
R, C = map(int, input().split())
happiness = []
for r in range(R):
    happiness.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]  # 상우하좌
dy = [-1, 0, 1, 0]
direction = ['U','R','D','L',]
dp = [[0]*C for _ in range(R)]
dp[0][0] = happiness[0][0]
ans = ''
def dfs(y, x, visit, ret):
    global ans
    if [y,x] == [R-1, C-1]:
        ans = ret
        # print(dp[y][x], ret)
        return
    # 마지막 행 > 하, 좌만 가능
    if y == R-1:
        start, end = 0, 2
    # 마지막 열 > 상, 우만 가능
    elif x == C-1:
        start, end = 2, 4
    else:   # 상하좌우 모두
        start,end = 0, 4
    for idx in range(start,end):
        yy = y + dy[idx]
        xx = x + dx[idx]

        if yy >= 0 and yy < R and xx >= 0 and xx < C and visit[yy][xx] == 0:
            if dp[yy][xx] == 0 or dp[y][x]+happiness[yy][xx] > dp[yy][xx]:
                visit[yy][xx] = 1
                dp[yy][xx] = dp[y][x]+happiness[yy][xx]
                dfs(yy,xx,visit,ret+direction[idx])
                visit[yy][xx] = 0

def rule(n1, n2, s1, s2, s3):
    global ans
    ans += s1*(n2 - 1)
    n = n1 - 1
    while n > 0:
        ans += s3
        n -= 1
        if ans[-2] == s1:
            ans += s2*(n2 - 1)
        elif ans[-2] == s2:
            ans += s1*(n2 - 1)

if R%2 == 1:
    rule(R,C,'R','L','D')
elif C%2 == 1:
    rule(C,R,'D','U','R')
else:
    visit = [[0] * C for _ in range(R)]
    visit[0][0] = 1
    dfs(0, 0, visit, '')


print(ans)


