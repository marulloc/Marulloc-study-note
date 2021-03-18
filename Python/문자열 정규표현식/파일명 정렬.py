# 프로그래머스 카카오 블라인드 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686#

import re
p = re.compile("([a-zA-Z .\-]+)([0-9]+)([0-9a-zA-Z .\-]*)")

def solution(files):
    # 정규표현식 사용
    tokens = []
    idx = 0
    for file in files:
        match = p.findall(file)[0]
        tokens.append([match[0],match[1],match[2]])
        idx += 1
    
    
    # 정렬
    tokens.sort(key = lambda x : (x[0].lower(), int(x[1])))
    answer = [''.join(token) for token in tokens]
    return answer