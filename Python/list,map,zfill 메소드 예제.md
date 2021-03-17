# 프로그래머스 카카오 블라인드

- https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

### map

- map의 람다함수가 매개변수를 두개 이상 필요로 할 때
  - 컬렉션을 두개 넘겨주면 된다. 대신 정수 하나만 넘기고 싶다면..
  - 리스트 컴프리헨션으로 iterable 객체로 만들어서 보내면 된다.. (이래도 되나 싶긴 하네)

<br>

### zfill

- 이진수의 자릿수를 통일시키기 위해 zfill 메소드 사용

<br>

### 2,8,16진수

- `bin()`: 2진수 문자열로 변환
- `oct()`: 8진수 문자열로 변환
- `hex()`: 16진수 문자열로 변환

<br>
<br>

```python
def setting(value,n):
    result = bin(value)[2:]
    result = result.zfill(n)
    return result

def solution(n, arr1, arr2):
    answer = []

    firstMap = list(map(setting,arr1,[n for _ in range(n)]))
    secondMap = list(map(setting,arr2,[n for _ in range(n)]))

    for row in range(n):
        tmp = ""
        for col in range(n):
            if firstMap[row][col] == "1" or secondMap[row][col] =='1': tmp += '#'
            else: tmp += " "
        answer.append(tmp)


    return answer
```
