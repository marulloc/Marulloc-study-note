# ascii 코드 이용

- 문자 'a'의 아스키코드는 `"a".charCodeAt()`
- 아스키코드 100인 문자는 `String.fromCharCode(100)`

```js
function solution(s, n) {
  const charArr = s.split("");

  const asciiArr = charArr.map((char) => {
    const ascii = char.charCodeAt();

    if (ascii === " ".charCodeAt()) {
      return ascii;
    } else if (ascii >= "a".charCodeAt() && ascii <= "z".charCodeAt()) {
      const start = ascii - "a".charCodeAt();
      const distance = (start + n) % ("z".charCodeAt() - "a".charCodeAt() + 1);
      return "a".charCodeAt() + distance;
    } else if (ascii >= "A".charCodeAt() && ascii <= "Z".charCodeAt()) {
      const start = ascii - "A".charCodeAt();
      const distance = (start + n) % ("Z".charCodeAt() - "A".charCodeAt() + 1);
      return "A".charCodeAt() + distance;
    }
  });

  const answer = asciiArr.map((asc) => String.fromCharCode(asc)).join("");
  return answer;
}
```
