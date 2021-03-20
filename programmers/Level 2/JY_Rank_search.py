# programmers L2 : 순위 검색
# solved by JY
# DATE : 2021.03.18
# dictionary 사용
# 정확도 100%, O(50000*100000)이라 효율성 0%

import collections

def solution(info, query):
    answer = []
    store = collections.defaultdict(set)
    scores = collections.defaultdict(set)

    for idx, st in enumerate(info):
        l, e, n, f, s = st.split(' ')
        store[l].add(idx)
        store[e].add(idx)
        store[n].add(idx)
        store[f].add(idx)
        scores[s].add(idx)

    for q in query:
        l, _, e, _, n, _, f, s = q.split(' ')
        tmp = set(i for i in range(len(info)))
        if l != '-':
            tmp &= store[l]
        if e != '-':
            tmp &= store[e]
        if n != '-':
            tmp &= store[n]
        if f != '-':
            tmp &= store[f]
        if s != '-':
            t = set()
            for score in scores:
                if int(score) >= int(s):
                    t.update(scores[score])
            tmp &= t
        answer.append(len(tmp))

    return answer

# run test
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]), [1,1,1,1,2,4])
# print(solution())