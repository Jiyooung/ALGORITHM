# baekjoon 1654 : 랜선 자르기
# solved by JY
# DATE : 2021.12.13
# BinarySearch

from sys import stdin
input = stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

def find():     # 이분탐색으로 랜선의 길이를 찾는 함수
    answer, left, right = 0, 0, max(lan)

    while left <= right:
        mid = (left + right + 1) // 2

        if check(mid) and mid >= answer:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

def check(ans):     # mid가 가능한지 확인 = 만들어지는 랜선의 갯수가 n보다 크거나 같다.
    cnt = 0
    for i in range(k):
        cnt += lan[i]//ans
    return True if cnt >= n else False

print(find())