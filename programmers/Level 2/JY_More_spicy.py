# programmers L2 : 더 맵게
# solved by JY
# DATE : 2021.03.09
# PriorityQueue() 사용
# 정확도 통과, 효율성 0점

from queue import PriorityQueue

def solution(scoville, K):
    answer = 0
    pq = PriorityQueue()
    for s in scoville:
        pq.put(s)

    while True:
        min1 = pq.get()
        if min1 >= K:
            break
        if pq.empty() == True:
            answer = -1
            break
        min2 = pq.get()
        if min2 == 0:
            answer = -1
            break
        pq.put(min1 + (min2 * 2))
        answer += 1

    return answer

# run test
print(solution([1, 2, 3, 9, 10, 12], 7))    # 2
print(solution([0, 0], 7))    # -1
print(solution([1, 1, 1, 1, 1, 1], 10))    # -1