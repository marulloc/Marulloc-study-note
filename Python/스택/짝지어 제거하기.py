def solution(s):
    stack = []

    for character in s:
        if len(stack) == 0: stack.append(character)
        else :
            if stack[len(stack)-1] == character: stack.pop()
            else: stack.append(character)
    
    if len(stack) != 0: return 0
    else: return 1