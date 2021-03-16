# 1 ~ n까지의 소수 개수를 반환하는 함수
# 에라토스테네스의 체
def eratos(n):
    isPrime = [True for x in range(n+1)]
    
    for number in range(2,n+1):
        if isPrime[number]:
            for mul in range(2,n//number + 1):
                isPrime[number * mul] = False

    count = 0
    for number in range(2,n+1):
        if isPrime[number]: count+=1
    return count