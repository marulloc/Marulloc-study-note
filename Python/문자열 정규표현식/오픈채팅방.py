# 프로그래머스 카카오 블라인드 오픈채팅방 문제
# https://programmers.co.kr/learn/courses/30/lessons/42888

import re 
p = re.compile("(Enter|Leave|Change) ([0-9a-zA-Z]+) ?([0-9a-zA-Z]+)?")

def solution(record):
    users = {}
    tmp = []
    for r in record:
        token = p.findall(r)[0]    
        if token[0] == "Enter":
            users[token[1]] = token[2]
            tmp.append(("blank님이 들어왔습니다.",token[1]))
            
        elif token[0] == "Leave":
            tmp.append(("blank님이 나갔습니다.", token[1]))
        else:
            users[token[1]] = token[2]
        
    answer = []
    for t in tmp:
        name = users[t[1]]
        answer.append(t[0].replace("blank",name))
        
    return answer