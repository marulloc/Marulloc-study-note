# split 함수 사용 주의

- 프로그래머스 JadenCase 문제
- https://programmers.co.kr/learn/courses/30/lessons/12951#

### 주의

- `split(" ")`의 경우 공백이 제일 앞에 나오는 문자열에 대해서, `["",토큰1,토큰2]`를 반환하게 된다.
- 즉 split은 기준자의 좌,우 모두 뽑아서 리스트를 반환하게 된다. 인덱스 양 끝에서 기준자가 동작하는 경우 빈 문자열이 오게되므로, index 에러에 주의하자.

```python
def solution(s):
    tokens = s.split(" ")
    answer = []
    for token in tokens:
        if token == '' :
            answer.append("")
            continue

        tmp = token.lower()
        head = tmp[0]
        if head.isalpha(): head = head.upper()

        if len(tmp) > 1: answer.append(head + tmp[1:])
        else :answer.append(head)

    answer = ' '.join(answer)

    return answer
```
