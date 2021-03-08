# reduce 함수

- 배열 전체 덧셈하는 예제

### reduce의 콜백함수의 인자

1. initialValue
   - 초기화값이자 값이 축적되는 변수
2. currentValue
   - 순회하는 배열의 각 원소
3. currentIndex
   - reduce의 두 번째 인자를 사용했으면, 0부터 인덱스가 시작된다.
   - 두 번째 인자를 사용하지 않았으면, 1부터 인덱스가 시작된다.
4. array
   - reduce를 호출한 배열

```js
function solution(n) {
  const arr = [];
  for (let num = 1; num <= n; num++) {
    if (n % num === 0) arr.push(num);
  }

  const initValue = 0;
  const answer = arr.reduce((initValue, current, currentIdx, array) => {
    return current + initValue;
  }, initValue);

  return answer;
}
```
