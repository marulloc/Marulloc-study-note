## 10진수를 n진수로 변환하는 함수

```js
function makeBaseX(num, x) {
  // n진법 변환 => 각 digit 배열로 반환
  const arrBaseX = [];

  let now = num;
  while (now >= x) {
    arrBaseX.unshift(now % x);
    now = Math.floor(now / x);
  }
  arrBaseX.unshift(now);
  return arrBaseX;
}
```

<br>
<br>
<br>

## n진수를 10진수로 변환하는 함수

```js
function makeBase10(arr, base) {
  // n진수의 digit을 배열로 받고, 10진수로 반환하는 함수
  let power = 0;
  let numBase10 = 0;

  for (let power = 0; power < arr.length; power++) {
    numBase10 += base ** power * arr[arr.length - power - 1];
  }

  return numBase10;
}
```

> #### 예제
>
> https://programmers.co.kr/learn/courses/30/lessons/68935#
