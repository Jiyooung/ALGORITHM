# programmers L2 : 위장
# solved by JY
# DATE : 2021.02.28
# dictionary 이용

def solution(clothes):
    answer = 0
    dic = {}
    for name, kind in clothes:
        if kind in dic:
            dic[kind].append(name)
        else:
            dic[kind] = [name]

    for d in dic:
        if answer != 0:
            answer += answer * len(dic[d])
        answer += len(dic[d])

    return answer

# run test
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))   # 5
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))   # 3
print(solution([["a", "face"], ["b", "face"], ["c", "face"], ["aa", "f"], ["bb", "f"], ["A", "F"], ["B", "F"]]))   # 35