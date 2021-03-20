# programmers L1 : 신규 아이디 추천
# solved by JY
# DATE : 2021.03.17
# 문자열 구현 문제, ascii 사용

def solution(new_id):
    new = list(new_id)
    spectial = ['-', '_', '.']
    point = -1
    for idx, n in enumerate(new[:]):
        # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
        if ord(n) >= 65 and ord(n) <= 90:
            new[idx] = chr(ord(n) + 32)
        # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        elif not((ord(n) >= 97 and ord(n) <= 122) or (ord(n)>=48 and ord(n) <= 57) or n in spectial):
            new[idx] = ''
        # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
        if new[idx] == '.':
            if point != idx-1:
                point = idx
            else:
                new[idx] = ''
                point += 1
        if new[idx] == '' and point == idx-1:
            point += 1

    new = list(''.join(new))    # '' 제거
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new) > 0:
        for idx in range(-1,1):
            if new[idx] == '.':
                new[idx] = ''

    new = ''.join(new)
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new) == 0:
        new += 'a'

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(new) >= 16:
        if new[14] == '.':
            new = new[:14]
        else:
            new = new[:15]
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new) <= 2:
        last = new[-1]
        while len(new) < 3:
            new += last

    return new

# run test
print(solution("...!@BaT#*..y.abcdefghijklm"), "bat.y.abcdefghi")
print(solution("z-+.^."), "z--")
print(solution("=.="), "aaa")
print(solution("123_.def"), "123_.def")
print(solution("abcdefghijklmn.p"), "abcdefghijklmn")