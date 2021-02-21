# programmers L2 : 카펫
# solved by JY
# DATE : 2021.02.21
# 완전탐색
# brown - 4 = 2(y_r + y_c)
# yellow = y_r * y_c 

def find(yellow):   # yellow 약수(y_r) 구하기
    factor = []
    i = 1
    while i*i <= yellow:
        if yellow % i == 0:
            factor.append(i)
        i += 1

    return factor

def solution(brown, yellow):
    for y_r in find(yellow):
        y_c = int(yellow/y_r)
        if y_c == (brown-4)/2 - y_r:
            return [y_c + 2, y_r + 2]

# run test
print(solution(10, 2))  # [4, 3]
