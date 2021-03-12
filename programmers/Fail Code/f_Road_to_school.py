# programmers L3 : 등굣길
# solved by JY
# DATE : 2021.03.11
# BFS 사용
# 시간초과 > 실패

dx = [1, 0]
dy = [0, 1]
num = 1000000007
def solution(m, n, puddles):
    answer = 0
    min_length = 200
    que = [[1,1]]
    count = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    while len(que) > 0:
        x, y = que.pop(0)
        cnt = count[y][x]
        
        for i in range(2):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if xx <= m and yy <= n:
                if [xx, yy] in puddles:
                    continue
                if [xx, yy] == [m, n]:
                    if min_length > cnt + 1:
                        min_length = cnt + 1
                        answer = 1
                    else:
                        answer += 1
                    continue
                
                if count[yy][xx] != 0:
                    if cnt + 1 <= count[yy][xx]:
                        que.append([xx, yy])
                        count[yy][xx] = cnt + 1
                else:
                    que.append([xx, yy])
                    count[yy][xx] = cnt + 1
                
    return answer%num

# run test
print(solution(4, 3, [[2,2]]), 4)