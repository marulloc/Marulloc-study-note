# 카카오 블라인드 n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3

# 10진법 수를 정수로 받아
# x진법으로 변경하여 "문자"배열로 반환
def getBaseX_string(num,x):
    result = []

    now = num
    while now >= x:
        tmp = now % x
        if tmp >= 10 : target = chr(65 + tmp - 10)
        else : target = str(tmp)
        result.append(target)
        now = now // x

    if now >= 10 : target = chr(65 + now - 10)
    else : target = str(now)
    result.append(target)
    result.reverse()
    return result


def solution(n, t, m, p):
    # 모든 숫자 
    allNumber = []
    number = 0
    while len(allNumber) <= m*t:
        allNumber += getBaseX_string(number, n)
        number += 1
    
    # 타겟 
    answer = []
    start = 0
    end = m
    while len(answer) <= t-1:
        tmp = allNumber[start:end]
        target = tmp[p-1]
        answer.append(target)
        start += m 
        end += m
        
    answer = ''.join(answer)
    return answer