# 2020 KAKAO BLIND RECRUITMENT 문자열 압축

> https://programmers.co.kr/learn/courses/30/lessons/60057#

- BASE 문자열을 잡고
- NEXT 문자열을 WHILE문 돌려서 갯수 파악
- 일치하는 문자열 갯수에 따라서, 그 다음 서브 문자열을 구하는 시작점이 바뀌기 때문에, FOR문 하단에 OFFSET을 구해서 START를 변경해줬다.

```js
function getSubLength(s, length) {
  let subStr = "";

  let start = 0;
  for (start; start < s.length - length; ) {
    let baseStr = s.substring(start, start + length);
    let targetStart = start + length;
    let targetEnd = start + length * 2;
    let nextStr = s.substring(targetStart, targetEnd);

    let cnt = 1;
    while (baseStr === nextStr) {
      cnt++;
      targetStart += length;
      targetEnd += length;
      nextStr = s.substring(targetStart, targetEnd);
    }

    if (cnt >= 2) subStr += String(cnt);
    subStr += baseStr;

    let offset = length * cnt;
    start += offset;
  }
  subStr += s.substring(start);
  return subStr.length;
}

function solution(s) {
  let minLen = 987654321;
  for (let length = 1; length <= s.length; length++) {
    let subLen = getSubLength(s, length);
    minLen = minLen > subLen ? subLen : minLen;
  }
  return minLen;
}
```
