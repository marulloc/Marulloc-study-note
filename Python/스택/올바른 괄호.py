# 프로그래머스 올바른 괄호 문제
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0: 
            stack.append(c)
            continue
        if c == ')' and stack[len(stack)-1] == '(': stack.pop()
        else: stack.append(c)
    
    if len(stack) == 0: return True
    else: return False
