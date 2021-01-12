# programmers L2 : 큰 수 만들기
# solved by JY
# DATE : 2020.01.12
# Greedy 알고리즘
# count = 제거한 숫자 개수
# 최적화 완료
# best code에 비해 for문 안에 if가 있어서 시간 더걸림

def solution(number, k):
    stack = []
    count = 0
     
    for n in number:
        while stack and count < k and n > stack[-1] :
            stack.pop()
            count += 1
        if len(stack) < len(number) - k: stack.append(n)

    return ''.join(stack)

# run test
# print(solution("4177252841", 4))
print(solution("99991", 2))