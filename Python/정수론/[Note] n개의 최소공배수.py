from math import gcd
# math 라이브러리에서 최대공약수 함수 import
# 최소공배수 구하는 함수
def lcm(x,y): return x * y // gcd(x,y)

def solution(arr):
    value = lcm(arr[0],arr[1])
    for idx in range(2,len(arr)):
        value = lcm(value, arr[idx])
    
    answer = value
    return answer