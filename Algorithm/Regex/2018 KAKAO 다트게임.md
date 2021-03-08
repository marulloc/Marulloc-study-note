# 2018 KAKAO BLIND RECRUITMENT [1차] 다트게임

- https://programmers.co.kr/learn/courses/30/lessons/17682
- 정규식으로 그룹화해서 추출하는 방법 연습해야 됨

```js
function solution(dartResult) {
  const score = [0, 0, 0];

  // 어떻게 만들어야 되는거지..
  const regex =
    "([0-9]{1,}[A-Z][*#]?)([0-9]{1,}[A-Z][*#]?)([0-9]{1,}[A-Z][*#]?)";
  const tmp = dartResult.match(regex, "g");
  const regResult = tmp.slice(1, 4);

  regResult.forEach((subStr, idx) => {
    const regex = "([0-9]{1,})([A-Z])([*#])?";
    const regResult = subStr.match(regex);

    const base = Number(regResult[1]);
    const bonus = regResult[2] === "S" ? 1 : regResult[2] === "D" ? 2 : 3;
    const option = regResult[3];

    score[idx] = base ** bonus;
    if (option) {
      if (subStr[2] === "*") {
        score[idx] *= 2;
        if (idx > 0) score[idx - 1] *= 2;
      } else {
        score[idx] *= -1;
      }
    }
  });
  const answer = score.reduce((prev, current) => prev + current, 0);
  return answer;
}
```
