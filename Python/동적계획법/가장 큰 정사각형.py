# 프로그래머스 가장 큰 정사각형
# https://programmers.co.kr/learn/courses/30/lessons/12905
# board[i][j]의 의미는 
# i행j열의 사각형이 추가되었을 때,
# 0행0열 부터 i행 j열까지 만들수 있는 정사각형의 최대 길이를 의미한다.


def solution(board):
    for y in range(1,len(board)):
        for x in range(1,len(board[0])):
            prev = min(board[y-1][x-1], board[y-1][x], board[y][x-1])
            if board[y][x] == 0 or prev == 0: continue
            board[y][x] = max(prev + 1, board[y][x])
    
    maxV = -1
    for y in range(0,len(board)):
        for x in range(0, len(board[0])):
            maxV = max(maxV, board[y][x])

    return maxV * maxV