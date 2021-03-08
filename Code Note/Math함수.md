# Math Method

<br>
<br>

### 제곱근

- Math.sqrt()

```js
function solution(n) {
  const sqrt = Math.sqrt(n);
  const sqrtFloor = Math.floor(sqrt);

  let answer = 0;
  if (sqrt !== sqrtFloor) answer = -1;
  else answer = (sqrt + 1) ** 2;
  return answer;
}
```
