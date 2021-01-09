import itertools
# itertools.permutations(n개의 배열or문자열, 자릿수 r)
# itertools.combinations(n개의 배열or문자열, 자릿수 r)

# ''.join(배열 or 튜플)

def solution(numbers):

    # 경우의 수
    targets = set()
    for digit in range(1,len(numbers) + 1):
        for x in itertools.permutations(numbers, digit):
            targets.add(int(''.join(x)))    
    targets = list(targets)

    
    # 에라토스테네스
    maximum = 10**len(numbers)
    isPrime = [True] * maximum
    isPrime[0], isPrime[1] = False,False
    
    for x in range(2,maximum):
        if not isPrime[x]: continue
            
        for mul in range(2, maximum // x):
            isPrime[x * mul] = False

    answer = 0
    for x in targets:
        if isPrime[x]:
            answer += 1
    
    return answer