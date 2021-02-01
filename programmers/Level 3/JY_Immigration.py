# programmers L3 : 입국심사
# solved by JY
# DATE : 2021.02.01
# 이분탐색
# mid : 모든 사람이 심사를 받는데 걸리는 시간

def solution(n, times):
    min_t, max_t = 1, max(times)*n

    while min_t < max_t:
        mid = (min_t + max_t) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n:
                break
        if cnt >= n:
            max_t = mid
        else:
            min_t = mid + 1
    return max_t


# run test
# print(solution(6, [7, 10]))  # 28
print(solution(10, [1, 5]))  # 9
