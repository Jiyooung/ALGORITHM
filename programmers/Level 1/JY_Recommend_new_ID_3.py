# programmers L1 : 신규 아이디 추천
# solved by JY + best
# DATE : 2021.03.17
# 문자열 구현 문제, 정규 표현식 사용

import re

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    answer = new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer = re.sub('[^a-z0-9\-_.]','',answer)
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer = re.sub('\.+','.',answer)
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. 
    answer = re.sub('^[.]|[.]$', '', answer)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    answer = 'a' if len(answer) == 0 else answer[:15]
    answer = re.sub('^[.]|[.]$', '', answer)
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    answer = answer if len(answer) > 2 else answer + ''.join(answer[-1]*(3-len(answer)))
    return answer

# run test
print(solution("...!@BaT#*..y.abcdefghijklm"), "bat.y.abcdefghi")
print(solution("z-+.^."), "z--")
print(solution("=.="), "aaa")
print(solution("123_.def"), "123_.def")
print(solution("abcdefghijklmn.p"), "abcdefghijklmn")