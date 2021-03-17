# 프로그래머스 카카오 블라인드 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683#

# 기준 문자열or배열과 대상 문자열or배열을 입력으로 받고
# True/False 값을 반환, base와 offset을 반환해주면 인덱스 반환이 가능하다.
def isSubString(standard, target):
    base = 0
    offset = 0
    while base + offset < len(standard):
        if standard[base + offset] == target[offset]:
            offset += 1
            if offset >= len(target): return True
            # 이때 base가 일치하는 시작점이며, base+offset-1이 끝나는 지점이다.
        else:
            if offset == 0 : base += 1
            else : base = base + offset
            offset = 0
    return False


def getPlayTime(start,end):
    tmp = start.split(":")
    s = int(tmp[0]) * 60 + int(tmp[1])
    
    tmp = end.split(":")
    e = int(tmp[0]) * 60 + int(tmp[1])
    return e-s

def getPlayed(playtime, base):
    sheet = [x for x in base]
    for idx in range(1,len(sheet)):
        if(sheet[idx] == '#'): sheet[idx-1] += '#'
    sheet = [x for x in sheet if x != '#']
    
    if playtime > len(sheet):
        return sheet * (playtime // len(sheet)) + sheet[:playtime % len(sheet)]
    else : return sheet[:playtime]

def solution(m, musicinfos):
    m = [x for x in m]
    for idx in range(1,len(m)): 
        if(m[idx] == '#'): m[idx-1] += '#'
    m = [x for x in m if x != '#']

    infos = []
    idx = 0
    for music in musicinfos:
        tmp = music.split(",")
        playtime = getPlayTime(tmp[0],tmp[1])
        title = tmp[2]
        sheet = getPlayed(playtime,tmp[3])
        infos.append((playtime, title, sheet,idx))
        idx += 1
    
    # 일치하는 곡 정보 candi에 삽입
    results = []
    for info in infos:
        print(isSubString(info[2], m))
        if isSubString(info[2], m): results.append(info)
    if len(results) <= 0 : return "(None)"
        
    # 일치한 것들을 재생시간 순으로 정렬하고, 
    # 플레이 시간 최댓값을 갖지 못한것들 소거
    maxV = max(results,key=lambda x : x[0])
    results = [x for x in results if x[0] == maxV[0]]
    if len(results) <= 1: return results[0][1]
    
    # 등장한 순서대로
    results.sort(key=lambda x: x[3])
    return results[0][1]