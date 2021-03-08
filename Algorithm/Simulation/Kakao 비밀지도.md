# 2018 KAKAO BLIND RECRUITMENT

- https://programmers.co.kr/learn/courses/30/lessons/17681

```js
function makeBaseX(num, x) {
  const arrBaseX = [];

  let now = num;
  while (now >= x) {
    arrBaseX.unshift(now % x);
    now = Math.floor(now / x);
  }
  arrBaseX.unshift(now);
  return arrBaseX;
}

function solution(n, arr1, arr2) {
  const answer = [];

  for (let col = 0; col < n; col++) {
    let tmp = "";
    const row1 = makeBaseX(arr1[col], 2);
    const row2 = makeBaseX(arr2[col], 2);

    while (row1.length < n) {
      row1.unshift(0);
    }
    while (row2.length < n) {
      row2.unshift(0);
    }

    row1.forEach((elem, idx) => {
      if (elem === 0) tmp = tmp + (row2[idx] === 0 ? " " : "#");
      else tmp = tmp + "#";
    });
    answer.push(tmp);
  }
  return answer;
}
```
