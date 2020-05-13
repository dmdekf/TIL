# Javascript
diff w/ python

## I. 스코프 & 변수
### (1) 스코프
중2병 히키코모리 막내동생 법칙
- **JS의 경우 중괄호가 있을 경우, 스코프를 만든다.**
    - (1) function일 경우
    - (2) 제어문(if/switch/while/for 등)일 경우 
- `var` function에서만 스코프로 묶임(fuction scope)
- `let`은 중괄호가 있을 경우(block scope) 동일하게 작동

### (2) var, let, const
- ~~`var`: 할당 및 선언은 자유, 함수 스코프(절대 쓰지 않는다)~~
- `let`: 할당 자유, 선언은 한번, 블록 스코프
- `const`: 할당 & 선언 한번, 블록 스코프

### (3) Identifier(식별자) Convention 
- 변수, 함수, 객체: 캐멀 케이스(camelCase)
- 클래스, 생성자: 파스칼 케이스(PascalCase)
- 상수: 대문자 스네이크 케이스(SNAKE_CASE)

### (4) Hoisting(호이스팅)
> 1. var를 쓰지 않는다. 
> 2. function 선언형으로 쓰지 않는다. 

- why? 생각했던대로 코드가 움직이지 않음
-> 실행 전에 한 번 훑어서, 선언 이전에 참조가 가능하게 함

- (참고) 함수 선언형과 표현식
```js
// 선언형
function hello() {}

// 표현식
const hello = function() {}

```

## II. 자료형
### (1) 숫자
```js
const num1 = 123
const num2 = -2.88
const a = NaN // Not a Number
const b = Infinity
const c = -Infinity 
```

### (2) 글자
- 합체(concatenation): `+`
- 수술(interpolation): `template literal ${}`

```js
const firstName = 'John'
const lastName = "Kang"
const middleName = `Dongju`

const fullName = firstName + lastName
const greeting = `Hello ${middleName}`
```

### (3) 불리언
- 뭐가 참에 가깝고, 뭐가 거짓에 가깝냐
- `true`, `false` (소문자)

#### 1. Truthy
Falsy가 아닌 모든 값들

#### 2. Falsy
없거나, 정의되지 않거나 `null`, `undefined` 등

## III. 자료구조
어떻게 저장하고, 조작하는지(CRUD) => 메서드를 보자

### (1) Array (python `list`)
#### 1. Array helper method
TBC..

### (2) Object (python `dict`)
TBC..

## VII. 함수
- 선언식(statement)
- 표현식(expression)
- Arrow Fuction
1. 클래스 정의에서 사용 X
 -> (클래스) 메소드(OOP) 함수가 아닌 곳에서만
2. 생성자로 사용 X
3. 이벤트 리스너 콜백 함수 사용 X

## VIII. OOP
- 매우 유연한 객체를 통한 OOP
- class를 잠시 잊어두세요(Prototypal Inheritance)
- ES6+부터 `class` 도입
```js
class Person {
    constructor(name, birth) {
        this.name = name
        this.birth = birth
    }
    greeting() {
        return `안녕하십니까. ${this.name}`
    }
}
```
