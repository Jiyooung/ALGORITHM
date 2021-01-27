# programmers L2 : 큰 수 만들기
# solved by JY
# DATE : 2021.01.12
# Greedy 알고리즘
# enumerate() 사용
# 시간초과는 안나지만 효율은 좋진 않음
# 최적화 완료

def solution(number, k):
    stack = []   # stack처럼 쓰이는 list 
     
    for idx, n in enumerate(number):
        # idx - k : 당시에 stack에 있어야 할 최소 숫자 개수, (len(number) - k) - (len(number) - idx)
        # stack에 데이터가 있음 and stack안에 최소의 개수를 만족 and stack의 top과 현재 검사하는 숫자 비교
        while stack and len(stack) > idx - k and n > stack[-1] :
            stack.pop()
        
        if len(stack) < len(number) - k: stack.append(n)    # stack에 자리있으면 추가하기

    return (''.join(stack))

# run test
# print(solution("1119", 2))
# print(solution("99919", 2))
print(solution("144444", 2))