# GCD 최대공약수 - 유클리드 호제법

- A와 B의 최대공약수

1. 변수 `R`을 둔다. `R = A % B`
2. R이 0이 아니면`IF(R != 0)`,
   - B값을 A에 저장 `A = B`
   - R값을 B에 저장 `B = R`
3. R이 0이 될 때까지 Step1, Step2 반복
4. R이 0이 되면, B가 GCD

```js
function getGCD(A, B) {
  let R = A % B;

  while (R !== 0) {
    A = B;
    B = R;
    R = A % B;
  }
  return B;
}
```

<br>
<br>

# LCM 최소공배수

> ### `LCD = (A/GCD) * (B/GCD) * GCD`

- 어떤 수 A에 대해, `A = a * GCD` 성립한다.
- 따라서 `a = A / GCD` 다.
- 또한, `b = B / GCD` 다.
- `LCM = a * b * GCD` 이므로 위와 같은 식이 나온다.
- GCD를 구하고 최소공배수를 구하면 빠름
