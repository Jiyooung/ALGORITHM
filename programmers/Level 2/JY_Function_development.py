# programmers L2 : 기능개발
# solved by JY
# DATE : 2021.03.04
# deque를 활용한 Queue 구조 사용

import math, collections

def solution(progresses, speeds):
    answer = []
    suc = collections.deque()

    for p, s in zip(progresses, speeds):
        suc.append(math.ceil((100-p)/s))    # 필요한 작업 기간 저장
    first, count = suc.popleft(), 1

    while len(suc) > 0:
        p = suc.popleft()

        if first >= p:
            count += 1
        else:
            answer.append(count)
            first, count = p, 1
    answer.append(count)
    return answer

# run test
print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [2, 1]