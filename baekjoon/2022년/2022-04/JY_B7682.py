# baekjoon 7682 : 틱택토
# solved by JY
# DATE : 2022.04.22
# Implementation

from sys import stdin
input = stdin.readline

while(1):
    tic = list(input().rstrip())
    if ''.join(tic) == 'end': break
    cnt_x, cnt_o = tic.count('X'), tic.count('O')
    
    # 1. X개수 = O개수 or O개수 + 1
    if cnt_x not in [cnt_o, cnt_o + 1]:
        print('invalid')
        continue

    # 2. 승자가 있는 판인지 확인 (상하좌우대각선 3개 되는지)
    win_x, win_o = 0, 0
    a = [[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for i in range(8):
        chk = 0
        for j in a[i]:
            if tic[j] == 'X': chk -= 1
            elif tic[j] == 'O': chk += 1
        if chk == -3: win_x += 1
        if chk == 3: win_o += 1
    
    # 2-1. 승자가 있다면 개수 확인 -> 아래가 성립하면 valid, 성립하지 않으면 invalid
    if win_x > 0 and win_o > 0:
        print('invalid')
        continue

    if (win_x > 0 and win_o == 0) or (win_x == 0 and win_o > 0):
        # X가 승일 경우, X개수 = O개수 + 1
        # O가 승일 경우, X개수 = O개수
        if (win_x and cnt_x == cnt_o + 1) or (win_o and cnt_x == cnt_o):
            print('valid')
            continue
        else:
            print('invalid')
            continue
    
    # 3. 승자가 없다
    # 3-1. 게임이 안끝났다면(말을 더 놓을 수 있다) cnt_x + cnt_o < 9 invalid
    if cnt_x + cnt_o < 9:
        print('invalid')
        continue
    # 3-2. 게임이 끝났다 valid
    else:
        print('valid')
        continue


# test input
# XXXOO.XXX
# XOXOXOXOX
# OXOXOXOXO
# XXOOOXXOX
# XO.OX...X
# .XXX.XOOO
# X.OO..X..
# OOXXXOOXO
# .........
# XXOOOXXXO
# XO.X.OXO.
# XXXXOOXOO
# XOXOXOXO.
# XOXOXOX..
# .OXXOX.OX
# XXOOXOXXO
# end

# test answer
# invalid
# valid
# invalid
# valid
# valid
# invalid
# invalid
# invalid
# invalid
# valid
# invalid
# valid
# invalid
# valid
# invalid
# invalid
