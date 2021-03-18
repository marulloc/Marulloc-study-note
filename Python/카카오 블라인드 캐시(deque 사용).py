# 프로그래머스 카카오 블라인드 캐시 문제
# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    deq = deque([])
    for city in cities:
        city = city.lower()
        if city not in deq : 
            answer += 5
            if cacheSize == 0: continue
            if len(deq) >= cacheSize : deq.popleft()
            deq.append(city)
        else : 
            deq.remove(city)
            deq.append(city)
            answer += 1       
    return answer