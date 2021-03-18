# 카카오 블라인드 압축 문제
# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    idxDict = {}
    for asciicode in range(26): idxDict[chr(asciicode + 65)] = len(idxDict) + 1 
    
    answer = []
    base = 0 
    offset = 1
    while base+offset<=len(msg):
        if msg[base : base + offset] in idxDict: end += 1
        else : 
            answer.append(idxDict[msg[base : base + offset - 1]])
            idxDict[msg[base : base + offset]] = len(idxDict) + 1
            base = base : base + offset - 1
            offset = 1
            
    answer.append(idxDict[msg[start:]])
    return answer