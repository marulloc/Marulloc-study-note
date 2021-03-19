# 프로그래머스 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    table = [[0]*4 for _ in range(len(land))]
    table[0] = land[0]
    
    for row in range(1, len(land)):
        for col in range(4):
            if col == 0:
                prev = table[row-1]
                table[row][col] = max(prev[1],prev[2],prev[3])
                table[row][col] += land[row][col]
            elif col == 1:
                table[row][col] = max(prev[0],prev[2],prev[3])
                table[row][col] += land[row][col]
            elif col == 2:
                table[row][col] = max(prev[1],prev[0],prev[3])
                table[row][col] += land[row][col]
            elif col == 3:
                table[row][col] = max(prev[1],prev[2],prev[0])
                table[row][col] += land[row][col]
    answer = max(table[len(land)-1])
    return answer