### list

1. 배열 끝 추가 `const length = arr.push(x)`

   - arr이 변경된 후
   - arr의 길이가 반환된다.

2. 배열 끝 제거 `const popNode = arr.pop()`

   - arr이 변경되고
   - pop된 데이터가 반환된다.

3. 배열 앞 추가 `const length = arr.unshift(x)`

   - arr이 변경되고
   - arr의 길이가 반환된다.

4. 배열 앞 제거 `const newArr = arr.shift()`

   - arr이 변경되고
   - unshift된 데이터가 반환된다.

5. 배열 안, 데이터가 위치한 인덱스 찾기 `const idx = arr.indexOf(x)`

   - x 값이 위치한 인덱스 반환됨
   - 값이 여러개면, 앞에 위치한 인덱스 반환하고 끝
   - 존재하지 않으면 -1을 반환한다.

6. 인덱스 위치로 항목 추가, 제거`const removed = arr.splice( 시작 인덱스, 개수 , 값 )`

   - 첫번째 인자는 인덱스 위치, 두번째 인자는 개수다
   - 세번째 인자가 있으면, 추가하는 것이고 없으면 삭제한다.
   - 배열[시작인덱스: 시작인덱스 + 3] 을 값 하나로 치환하는 함수다. 따라서 세번째 인자가 비어있으면, 그냥 개수만큼 제거하게 된다.
     - n개를 교체할 때, n개의 원소가 모두 값으로 치환되는 것이 아니라, n개 전체를 1개의 값으로 바꾸는 것임
   - 반환값은 교체되는 배열이다.

7. 배열 복사 `const newArr = arr.slice()`

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

8. join, toString

9. concat

### Object { k:v }

### Set { }

### Sort
