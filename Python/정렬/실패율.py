# 프로그래머스 카카오 블라인드 실패율 문제
# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    nowPlay = [0] * (N+2)
    for stage in stages: nowPlay[stage] += 1
    
    arrive = [0] * (N+2)
    arrive[N+1] = nowPlay[N+1]
    for idx in reversed(range(1,N+1)):
        arrive[idx] = arrive[idx+1] + nowPlay[idx]
    
    answerTuple = []
    for idx in range(1,N+1):
        failRatio = 0
        if(arrive[idx] != 0): failRatio = nowPlay[idx] / arrive[idx]
        answerTuple.append((idx,failRatio))
    
    answerTuple.sort(key=lambda x : x[1] ,reverse=True)
    answer = [x[0] for x in answerTuple]
    return answer