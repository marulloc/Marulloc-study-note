### List

1. **배열 끝 추가 `const length = arr.push(x)`**

   - arr이 변경된 후
   - arr의 길이가 반환된다.

<br>

2. **배열 끝 제거 `const popNode = arr.pop()`**
   - arr이 변경되고
   - pop된 데이터가 반환된다.

<br>

3. **배열 앞 추가 `const length = arr.unshift(x)`**

   - arr이 변경되고
   - arr의 길이가 반환된다.

<br>

4. **배열 앞 제거 `const newArr = arr.shift()`**

   - arr이 변경되고
   - unshift된 데이터가 반환된다.

<br>

5. **배열 안, 데이터가 위치한 인덱스 찾기 `const idx = arr.indexOf(x)`**

   - x 값이 위치한 인덱스 반환됨
   - 값이 여러개면, 앞에 위치한 인덱스 반환하고 끝
   - 존재하지 않으면 -1을 반환한다.

<br>

6. **인덱스 위치로 항목 추가, 제거`const removed = arr.splice( 시작 인덱스, 개수 , 값 )`**

   - 첫번째 인자는 인덱스 위치, 두번째 인자는 개수다
   - 세번째 인자가 있으면, 추가하는 것이고 없으면 삭제한다.
   - 배열[시작인덱스: 시작인덱스 + 3] 을 값 하나로 치환하는 함수다. 따라서 세번째 인자가 비어있으면, 그냥 개수만큼 제거하게 된다.
     - n개를 교체할 때, n개의 원소가 모두 값으로 치환되는 것이 아니라, n개 전체를 1개의 값으로 바꾸는 것임
   - 반환값은 교체되는 배열이다.

<br>

7. **배열 복사 `const newArr = arr.slice()`**

   - 깊은 복사다.
   - 그러나 배열 안에 오브젝트가 있으면 오브젝트의 속성까지는 깊은 복사가 되지 않는다. 이런 경우의 배열이라면 `JSON.stringify()`로 만든후 새로운 변수에 할당한 후 `JSON.parse()`로 오브젝트로 만드는 것이 더 빠르다.

   ```javascript
   const newArrayOrObject = JSON.parse(JSON.stringify(arrOrObject));
   ```

   - 위의 정의된 메소드가 쓸 수 없는 상태라면, 아래와 같이 재귀로 가자, 재귀로 돌리면 아무리 깊은 오브젝트라도 깊은 복사를 할 수 있다.

   ```javascript
   // 오브젝트 하나를 깊은 복사해서 새로운 오브젝트를 반환하는 함수
   // 인자가 primitive 라도 동작한다 (else문에 의해)
   const copyDeep = function (obj) {
     let result = {};

     // null 은 js 자체 버그로 인해 typeof null 은 object다.
     // 따라서 && 연산으로 따로 필터링 해줘야 한다.
     if (typeof obj === "object" && target !== null) {
       for (let prop in obj) {
         result[prop] = copyDeep(obj[prop]);
       }
     } else {
       result = obj;
     }

     return result;
   };
   ```

<br>

8. **배열을 문자열로 만들기 join, `const stringArr = arr.join(구분자)`**

   - 각 원소사이에 구분자를 넣은 문자열을 반환해준다.
   - 인자를 안넣으면, 걍 다 붙여서 반환

<br>

9. **문자열을 배열로 만들기 split `const arr = something.split(구분자)`**

   - 문자열을 인자로 들어간 구분자로 분리해서 배열로 반환
   - 인자가 없으면, 문자 하나하나가 배열의 원소가 된다.

<br>

10. **값이나 배열을 합치기 concat `const newArr = arr.concat(1,2,3,[4,5])`**

- 기존 배열에, 인자로 들어온 값이나 배열을 합침
- 원본은 변하지 않음
- 새로운 배열을 반환
- 새로운 배열은 인자가 배열로 들어오더라도 depth가 1이다. `[1,2,3,4,5]`가 됨

<br>
<br>

### 배열 Map Filter 사용

1. **filter(callback)**

- callback은 세개의 인자를 갖는다. callback(element, idx, array)
  - element : 처리할 현재 요소
  - idx : 처리한 현재 요소의 인덱스
  - array: filter를 호출한 배열
- filter는 callback함수가 반환하는 원소만을 담은 배열을 반환한다.
  - 아래 코드 주석처리된 return문을 보면, 오브젝트에 담아서 원소를 반환하든, 문자로 바꿔서 반환하든, 원래 type을 유지한 원소만 추가된다.
  - 가공은 안하고, 진짜 필터링만 담당하는 메소드라고 생각하면 된다.

```Javascript
arr = [1,10,2,20,3,30]

filteredIdx = []
filtered = arr.filter((v,idx) => {
    if (v % 10 === 0){
        filteredIdx.push(idx)
        return v
        //return String(v)  -> 원하는대로 안됨
        //return (v, idx)   -> 원하는대로 안됨
    }
})
```

간단하게 10의 배수만 담은 배열로 바꾸고 싶다면

```Javascript
arr = [1,10,2,20,3,30]
filtered = arr.filter((v) => v % 10 === 0)
```

<br>
<br>

### Map

### Filter + Map

```Javascript
a = [1,2,5,4,5]

b = a.filter((value)=>{
        if(value == 5) return value})
    .map((value)=>value*5)
```
