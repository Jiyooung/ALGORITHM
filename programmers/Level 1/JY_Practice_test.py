# programmers L1 : 모의고사
# solved by JY
# DATE : 2021.02.19
# 완전탐색

import sys

def solution(answers):
    answer = [0] * 3
    check = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for idx in range(len(answers)):
        if answers[idx] == check[0][idx % 5]:
            answer[0] += 1
        if answers[idx] == check[1][idx % 8]:
            answer[1] += 1
        if answers[idx] == check[2][idx % 10]:
            answer[2] += 1

    answer_max = max(answer)
    answer = [idx + 1 for idx in range(3) if answer[idx] == answer_max]

    return answer

# run test
input = sys.stdin.readlines
print(solution([1,2,3,4,5]))    # [1]
print(solution([1,3,2,4,2]))    # [1,2,3]


