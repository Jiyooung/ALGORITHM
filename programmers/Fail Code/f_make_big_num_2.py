# programmers L2 : 큰 수 만들기
# solved by JY
# DATE : 2021.01.12
# Greedy 알고리즘
# 10번 시간초과
# max()를 사용해서 풀어도 시간초과 발생

def solution(number, k):
    answer = ''
    cur = 0   
    for s in range(len(number) - k - 1, -1, -1):
        max_num = max(number[cur:-s if s > 0 else len(number)])
        cur += number[cur:].index(max_num) + 1
        answer += max_num

    return answer

# run test
print(solution("1119", 2))