# programmers L3 : 순위
# solved by JY
# DATE : 2021.03.17
# 

def solution(n, results):
    answer = 0
    weight = [[0]*n for _ in range(n)]
    cnt = {}
    for win, lose in results:
        weight[win-1][lose-1] = -1
        weight[lose-1][win-1] = 1
        cnt[win-1] = cnt[win-1] + 1 if cnt.get(win-1) != None else 1
        cnt[lose-1] = cnt[lose-1] + 1 if cnt.get(lose-1) != None else 1

    cnt = sorted(cnt.items(), key = lambda x:x[1], reverse=True)

    for player, _ in cnt:
        win, lose = [], []
        for other, result in enumerate(weight[player]):
            if result == 1:     # player를 이긴 사람들의 모임
                win.append(other)
            elif result == -1:  # player한테 진 사람들의 모임
                lose.append(other)
        for w in win:
            for l in lose:
                weight[w][l] = -1
                weight[l][w] = 1

    for player in weight:
        if player.count(0) == 1:
            answer += 1

    return answer

# run test
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(3, [[1,2],[1,3]]), 1)
print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
print(solution(3,[[3,2],[3,1]]), 1)
print(solution(4, [[1,2],[1,3],[3,4]]), 1)