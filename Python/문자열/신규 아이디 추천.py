# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# 프로그래머스 신규아이디 추천

def solution(new_id):
    answer = ""
    
    # step 1
    result = new_id.lower()
    
    # step 2
    for char in result :
        if char.isalnum() or char in ["-","_","."]:
            answer += char
    
    # step 3
    while '..' in answer: 
        answer = answer.replace('..','.')
    
    # step 4
    if answer.startswith("."): answer = answer[1:]
    if answer.endswith("."): answer = answer[:len(answer)-1]
    
    # step 5
    if len(answer) < 1 : answer = "a"
        
    # step 6
    if len(answer) >= 16 : answer = answer[:15]
    if answer.endswith("."): answer = answer[:len(answer)-1]
    
    # step 7
    if len(answer) <= 2: 
        answer += answer[len(answer)-1] * (3 - len(answer))
    
    return answer