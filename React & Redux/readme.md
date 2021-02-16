# **_React_**

> #### 목차
>
> 1. _About React_
> 2. _Virtual DOM_
> 3. _Hooks_
> 4. _React optimization_

<br>

## **_1. About React_**

### [***About React***] UI 라이브러리 리액트

리액트는 UI "라이브러리"다.
따라서 하나의 Web APP을 완성하려면 다른 라이브러리들을 필요로 한다.

<br>

### [***About React***] SPA

<br>

### [***About React***] UI 데이터 관리

- 리액트는 **UI 데이터가 변경되면 화면을 리-렌더 한다.**<br>
  리액트에서 UI 데이터는 "속성값"과 "상태값"이다. 따라서, 속성값과 상태값이 아닌 일반 변수가 변경되면 리액트는 변경을 인지하지 못하고 화면을 리-렌더하지 않는다.

- 부모가 리-렌더 되면 자식 또한 리-렌더 된다.<br>
  부모가 리-렌더 되면 자식 컴포넌트의 속성값과 상태값이 바뀌지 않아도 자동으로 리-렌더 되는데, 이때 **React.memo**로 리-렌더를 방지하여 최적화 할 수 있다.

- 상태값이 **객체**인 경우<br>
  리액트는 **얕은 비교**를 통해 상태 변경 여부를 판단한다.
  따라서 상태가 **객체인 경우 참조값을 비교**하기 때문에, 객체(상태의 집합)의 속성(하나의 상태)이 변경되어도 똑같다고 판단하여 리-렌더를 진행하지 않는다.
  따라서, 우리는 항상 상태를 **불변 객체**로 다뤄야 한다. 불변객체로 다루면 리액트의 **얕은 비교로도 객체, 일반 변수의 상태 변경을 파악할 수 있다.**

- 속성값을 **객체 리터럴, 함수 리터럴**로 넘겨주는 경우<br>
  자식 컴포넌트의 속성값에 객체나 함수를 리터럴 형태로 넘겨주는 경우, 부모가 리-렌더 될 때, 객체나 함수가 재생성 되면서 자식들이 리-렌더 된다.
  이때 메모이제이션을 해주는 훅(**useCallback**, **useMemo**)을 사용하거나 상수로 쓰이는 객체는 컴포넌트 외부로 빼놓아 렌더링 최적화를 해야한다.

<br>

### [***About React***] 상태 변경은 "비동기 + 일괄" 처리

```jsx
const [count, setCount] = useState(0);
const onClick = () => {
  setCount(count + 1);
  setCount(count + 1);
  console.log(count); //변경되지 않은 이전의 값을 출력함
};
```

- **비동기 처리**<br>
  만약 상태 변경에 대해 "동기 처리"를 하게 되면, 상태 변경 함수가 호출될 때마다 화면을 다시 그리는 동안 브라우저가 멈추므로 성능 이슈가 발생한다.
- **일괄 처리**<br>
  리액트는 상태 업데이트를 16ms마다 일괄로 처리하여 리-렌더를 진행한다. `setCount`를 두 번 해도, 두 번째 `setCount`는 아직 증가되지 않은 count 값을 들고 대기 queue에 들어가기 때문에 `+1`은 단 한번만 이뤄진다. queue가 존재하여 비동기와 일괄처리 되더라도 "**호출순서 === 처리순서**"가 보장된다. 만약, 상태 변경을 바로바로 한다면 상태 변경 함수가 호출될 때 마다 화면을 다시 그리므로 성능 이슈가 발생한다.

### [***About React***] 리액트의 렌더링 과정

<br>
<br>

## **_2. Virtual DOM_**

### [***Virtual DOM***]

### [***Virtual DOM***]

### [***Virtual DOM***]

<br>
<br>

## **_3. Hooks_**

### [***Hooks***] useState

### [***Hooks***] useEffect

### [***Hooks***] useRef

### [***Hooks***] useReducer

### [***Hooks***] useContext (Context API)

### [***Hooks***] useLayoutEffect

### [***Hooks***] useImperativeHandle

### [***Hooks***] useDebugValue

<br>
<br>

## **_4.React optimization_**

### [***React optimization***] React.memo

### [***React optimization***] useMemo

### [***React optimization***] useCallback

### [***React optimization***] Virtual DOM optimization

<br>
<br>

# **_Redux_**
