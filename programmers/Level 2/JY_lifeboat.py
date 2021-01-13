# programmers L2 : 구명보트
# solved by JY
# DATE : 2020.01.12
# Greedy 알고리즘
# 몸무게가 많이 나가는 친구부터 내보내기
# 합이 딱 맞는 친구와 나가기, 없으면 limit에 가장 가깝게 도달하는 친구랑 같이 가기
# 정확성 통과, 효율성 0점
# remove > O(N)

def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    while len(people) > 0:
        p = people[0]
        if limit - p in people[1:]:    # limit 꽉 채울 사람이 있다
            people.remove(limit - p)
        elif limit - p >= people[-1]:  # 같이 갈 사람이 있다
            for p2 in people[1:]:
                if p + p2 <= limit:
                    people.remove(p2)
                    break

        people.remove(p)
        answer += 1

    return answer


# run test
# people = [70,50,80,50]
people = [70, 80, 50]
limit = 100
print(solution(people, limit))