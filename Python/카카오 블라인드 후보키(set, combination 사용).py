# 프로그래머스 카카오 블라인드 후보키 문제
# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations 

def solution(relation):
    column = len(relation[0])
    row = len(relation)
    
    # 조합 
    combins = []
    for n in range(1,column + 1): combins += combinations([x for x in range(column)], n)

    # 유일성 판단
    case = {}
    for combin_col in combins:
        case[combin_col] = set()
        for tup in range(row):
            tmp = ""
            for col in combin_col: tmp += relation[tup][col]
            case[combin_col].add(tmp)
        case[combin_col] = len(case[combin_col])    
        if case[combin_col] < row : del case[combin_col]
    
    # 최소성 판단
    answer = len(case)
    for key in case:
        for anotherKey in case:
            if case[anotherKey] == False : continue
            if key != anotherKey and len(set(key) & set(anotherKey)) >= len(key):
                case[anotherKey] = False
                answer -= 1
    return answer

# 딕셔너리의 key를 set으로 바꿔서 교집합 개수로 속했는지 여부를 판단했음