# Set

```Javascript
const arr = [1,2,3,3,3,3,3,3]
const onlyone = new Set(arr)
// onlyone => {1,2,3}
```

### Primitive 타입이 아닐 때, 주의해야 함

```Javascript
const arr = [[1,2], [1,3], [1,2], [1,2]]
const onlyone = new Set(arr)
// onlyone => { [1,2], [1,3], [1,2], [1,2] }

const arr2 = [{x:1, y:2}, {x:1, y:3}, {x:1, y:2}]
const onlyone2 = new Set(arr2)
// onlyone2 => { {x:1, y:2}, {x:1, y:3}, {x:1, y:2} }
```

# Stringify 와 parse를 사용하자 - 문자열로 바꿔서, primitive 타입 배열로 바꾸자

```Javascript
const arr = [[1,2], [1,3], [1,2], [1,2]]
const stringiArr = arr.map((v) => JSON.stringify(v))
const onlyoneStr = new Set(stringiArr)               //=> { "[1,2]", "[1,3]" }
const onlyoneArr = onlyone.map((v) => JSON.parse(v)) //=> { [1,2], [1,3] }

const arr2 = [{x:1, y:2}, {x:1, y:3}, {x:1, y:2}]

const stringiArr2 = arr2.map((v) => JSON.stringify(v))
const onlyoneStr2 = new Set(stringiArr2)                 //=> { "{x:1, y:2}", "{x:1, y:2}"}
const onlyoneArr2 = onlyoneStr2.map((v) => JSON.parse(v))//=> { {x:1, y:2}, {x:1, y:2}}
```
