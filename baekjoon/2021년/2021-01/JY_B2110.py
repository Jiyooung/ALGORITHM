# baekjoon 2110 : 공유기 설치
# solved by JY
# DATE : 2021.01.31
# 이분탐색
# mid : 인접한 두 공유기 사이의 거리

def check(mid) :
    cnt, s = 1, house[0]
    for idx in range(1,N):
        if house[idx] - s >= mid:
            cnt += 1
            s = house[idx]
    return False if cnt < C else True

def solution(min_d, max_d):
    while min_d <= max_d :
        mid = (min_d + max_d) // 2

        if check(mid):
            min_d = mid + 1
        else:
            max_d = mid - 1
    return max_d

# run test
import sys
input = sys.stdin.readline
N, C = map(int, input().split(" "))
house = [int(input()) for _ in range(N)]
house.sort()
print(solution(1, house[-1] - house[0]))