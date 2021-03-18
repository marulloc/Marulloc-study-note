# N진법 함수

### 숫자 배열로 반환

- 즉 10을 'A'로 반환하지 않고 10 그대로 반환한다.
- N진법으로 변환 후 계산이 필요한 경우 이 함수를 사용하자.

```python
# 10진수 정수를 n진법 숫자 배열로 반환
def getBaseX_number(num,x):
    result = []

    now = num
    while now >= x:
        result.append(now % x)
        now = now // x
    result.append(now)
    result.reverse()
    return result
```

<br>
<br>

### 문자 배열로 반환

- 10을 'A'로 반환하는 함수
- 각 digit의 숫자 연산이 필요 없고 그대로 사용하는 경우 이 함수를 쓰자.

```python
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
```

<br>
<br>

# N진수 "숫자"배열을 10진수로 변환

- 만약 11진수 이상이라면, 알파벳 DIGIT을 숫자로 변환해주고 넘겨야 함

```python
# n진법 숫자 배열을 10진수 정수로 변환하여 반환
def getBase10(arr,base):
    result = 0

    for digit in range(len(arr)):
        result += (base**digit) * arr[len(arr)-digit-1]
    return result
```
