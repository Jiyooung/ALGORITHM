# baekjoon 11000 : 강의실 배정
# solved by JY
# DATE : 2020.01.18
# Greedy 알고리즘
# list로 구현을 시도했으나 PyPy3으로 채점 시 86%에서 시간초과 발생

def solution():
    store = []
    store.append(time[0][1])
    for cur in time[1:]:
        flag = True
        for i in range(len(store)):
            if store[i] <= cur[0]:
                store[i] = cur[1]
                flag = False
                break
        if flag:
            store.append(cur[1])

    return len(store)

# run test
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()
print(solution())