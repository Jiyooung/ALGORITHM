# baekjoon 2805 : 나무 자르기
# solved by JY
# DATE : 2021.01.28
# 이분탐색
# mid_h : 나무 자르는 높이
import sys

def solution():
    answer, min_h, max_h = 0, 0, max(tree)
    while min_h <= max_h:
        mid_h = (min_h + max_h)//2 
        # ret = mid_h 높이로 잘랐을 때 획득한 나무의 길이
        ret = sum(t-mid_h if t-mid_h > 0 else 0 for t in tree)

        if ret >= M:
            min_h, answer = mid_h + 1, mid_h
        else:
            max_h = mid_h - 1
            
    return answer

# run test
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
print(solution())
