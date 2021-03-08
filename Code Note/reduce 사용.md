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

<br>
<br>

### reduce 2

- 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요. 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

```js
function solution(n) {
  const numArr = String(n).split("");

  const answer = numArr.reduce((sum, current) => {
    return sum + Number(current);
  }, 0);

  return answer;
}
```

<br>
<br>
<br>

### reduce 최소값 찾기

```js
function solution(arr) {
  const min = arr.reduce((prev, current) => {
    return prev > current ? current : prev;
  });

  const minIdx = arr.indexOf(min);
  const answer = arr.filter((value, idx) => {
    return minIdx !== idx;
  });

  if (answer.length === 0) answer.push(-1);
  return answer;
}
```

<br>
<br>
<br>

# map

- 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
  - 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
  - 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

```js
function solution(s) {
  const subStrings = s.split(" ");

  const answer = [];
  for (let str of subStrings) {
    const tmp = str
      .split("")
      .map((char, idx) => {
        if (idx % 2 === 0) return char.toUpperCase();
        else return char.toLowerCase();
      })
      .join("");
    answer.push(tmp);
  }

  return answer.join(" ");
}
```
