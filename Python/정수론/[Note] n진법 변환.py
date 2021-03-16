# 10진법 수를 정수로 받아
# x진법으로 변경하여 배열로 반환
def getBaseX(num,x):
    result = []
    
    now = num
    while now >= x:
        result.append(now % x)
        now = now // x
    result.append(now)
    result.reverse()
    return result


# x진법의 수를 배열로 받아
# 10진법 수로 변환하여 정수 반환
def getBase10(arr,base):
    result = 0

    for digit in range(len(arr)):
        result += (base**digit) * arr[len(arr)-digit-1]
    return result


def solution(n):
    arrBase3 = getBaseX(n,3)
    arrBase3.reverse()
    answer = getBase10(arrBase3,3)
    return answer