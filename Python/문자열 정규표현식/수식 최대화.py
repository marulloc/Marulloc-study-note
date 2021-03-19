# 프로그래머스 카카오 인턴 수식 최대화 문제
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
p = re.compile("([0-9]*|[\-\+\*])")

def operate(op,arr):
    idx = 1
    while True:
        if idx >= len(arr) - 1 : break
        if arr[idx] == op:
            v = 0
            if op == '-': v = arr[idx-1] - arr[idx + 1]
            if op == '+': v = arr[idx-1] + arr[idx + 1]
            if op == '*': v = arr[idx-1] * arr[idx + 1]
            arr[idx-1:idx+2] = [v]
            idx = 0
        idx+=1
    return arr

def solution(expression):
    match = p.findall(expression)
    arr = []
    for idx in range(len(match)):
        if match[idx] == '' : continue
        if match[idx].isdigit(): arr.append(int(match[idx]))
        else : arr.append(match[idx])
    
    result = []
    cases = ['+-*','+*-','-+*','-*+','*+-','*-+']
    for case in cases:
        tmp = [x for x in arr]
        for op in case:
            tmp = operate(op, tmp)
        if tmp[0] < 0: result.append(-tmp[0])
        else: result.append(tmp[0])
    
    answer = max(result)
    return answer