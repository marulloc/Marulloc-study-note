# 문자열 관련 메소드

### replace

- 파이썬은 문자열을 변경할 수 있는 replace함수를 제공한다. 자바와 같이 replaceAll함수는 존재하지 않는다.
- 파이썬의 replace함수는 개수를 인자로 넘겨주지 않으면 매치하는 모든 문자를 변경한다.

```python
text = '123,456,789'

replaceAll = text.replace(",","")
#=> 123456789
replace_once = text.replace(",","",1)
#=> 123456,789
replace_twice = text.replace(",","",2)
#=> 123456789

text2 = "hello world"
replaceHello = text2.replace("hello",'hi')
#=> hi world

text3 = "병건,병건,병건"
result = text3.replace("병건","hello")
#=> hello,hello,hello
```

<br>
<br>

### 대소문자 판별

- `string.upper()` 문자열의 모든 문자를 대문자로 변경
- `string.lower()` 문자열의 모든 문자를 소문자로 변경
- `isUpper()` 문자열의 모든 문자가 대문자인 경우 True를 반환, 아니면 False 반환
- `isLower()` 문자열의 모든 문자가 소문자인 경우 True를 반환, 아니면 False 반환

<br>
<br>
