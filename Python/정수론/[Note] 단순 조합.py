# 프로그래머스 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3

# 조합을 구하기 위해 combinations
from itertools import combinations 

# 소수 판별 여부 배열을 반환함
# 에라토스테네스의 체 적용
def eratos(n):
    isPrime = [True for _ in range(n+1)]
    
    for number in range(2,n+1):
        if isPrime[number]:
            for mul in range(2,n//number + 1):
                isPrime[number * mul] = False
    return isPrime


# Combinations from itertools
# 조합을 구하고 경우의 수를 모두 더한 것을 원소로 하는 배열 생성
def solution(nums):
    isPrime = eratos(3000)
    sums = list(map(sum,combinations(nums,3)))
    
    answer = 0
    for number in sums:
        if isPrime[number] : answer += 1
    
    return answer