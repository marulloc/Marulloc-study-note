# EX 1

- 프로그래머스 다트게임의 일부
- https://programmers.co.kr/learn/courses/30/lessons/17682

### 문제

- "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
  - 예) `1S2D*3T`
- 점수는 0에서 10 사이의 정수이다.
- 보너스는 S, D, T 중 하나이다.
- 옵션은 `*`이나 `#` 중 하나이며, 없을 수도 있다.
- 0~10의 정수와 문자 S, D, T, `*`, `#`로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

> 여기선 분리만 한다.

### 입력 예시

```
1S2D*3T, 1D2S#10S, 1D2S0T, 1S*2T*3S,
1D#2S*3S, 1T2D3D#, 1D2S3T*
```

### 정규표현식 사용

```python
import re

def solution(dartResult):
    p = re.compile("([0-9]+[SDT][*#]?)")

    '''여러개 찾아야 하므로 findall 사용'''
    matchList = p.findall(dartResult)
    print(matchList)
```
