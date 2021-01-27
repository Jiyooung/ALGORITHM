# programmers L2 : 큰 수 만들기
# solved by JY
# DATE : 2021.01.12
# Greedy 알고리즘
# for문으로 다 돌면서 max값 찾음 > 8, 10번 시간초과

def solution(number, k):
    answer = ''
    cur = 0

    # 최소한 필요한 개수를 뒤에 남겨놓고 앞에 수들 중에서 for문으로 max값 구하기
    # 최악의 경우 k * ( len(number) - k - 1 ) 번 비교
    for s in range(len(number) - k - 1, -1, -1):
        max_idx = 0
        max_num = '0'
        for idx, n in enumerate(number[cur: -s if s != 0 else len(number)]):
            if ord(n) > ord(max_num):
                max_idx = idx
                max_num = n
        cur += max_idx + 1
        answer += max_num
    return answer

# run test
print(solution("1119", 2))