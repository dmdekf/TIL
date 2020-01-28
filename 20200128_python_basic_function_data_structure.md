# 20200128

## python

### 문제풀기 03_function_00,01

#### 다중조건

if

if

if

덫을 깔아 놓는 것과 같다. 각각의 그물이 있다. 통과하는 고기가 있다. 모든 고기가 아닌 조건에만 있는 경우 낚는다.

#### 중첩조건

if

elif

elif

거른 것을 다시 거를 때. 조건이 exhaustive 망라적일때. 모든 고기를 낚아서 분류한다. 통과하지 않은 고기는 없다.

#### `all()`

> all은 인자로 받는 iterable(range, list)의 `모든 요소가 참`이거나 `비어있으면` True를 반환합니다.
>
> 이와 같은 함수 `my_all(x)`을 작성하세요.이중배열 중 비어있는 것을 확인할 때 주로 사용.

이중배열 중 비어있는 것을 확인할 때 주로 사용.

```python
def my_all(elem):
    for e in elem:
        if not e:
            return False
    return True
비어있을 경우는 for문을 돌지 않는다.!!!!
```



#### `any()`

> > any는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
> >
> > 이와 같은 함수 `my_any(x)`를 작성하세요.

```python
def my_any(elem):
    for e in elem:
        if e:
            return True
    return False


```



`RDBMS관계형 데이터베이스매니지먼트.`

`File -csv(comma seperate value-엑셀을 더 간단한 버전으로 나타낸 것...)`

### 04_data_structure

#### 문자열 메소드 활용하기(str)

##### `.join(iterable)`

특정한 문자열로 만들어 반환합니다.

**Iterable** 을 해당 문자열을 separator 로 합쳐서 문자열로 반환합니다. split()과 쌍으로 주로 사용된다.

> ```
> iterable
> ```
>
> 각각의 요소를 하나씩 반환할 수 있는 객체를 말한다. List와 Tuple, Dictionary와 Set ,('String')등이 여기에 속한다.

##### `.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

count를 지정하면 해당 갯수만큼만 시행합니다

```python
'woowoowoo'.replace('o','',4)
# 패턴을 사용하여 중간값도 대체할 수 있음.
'woowoowoo'.replace('owoowo','owwo')
```

##### `.strip([chars])`

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip).

지정하지 않으면 공백을 제거합니다. 내부 공백은 되지 않고 양쪽 끝에만 됨. 다른 언어일 경우는 촘핑으로.....? 모든 공백 제거.

#### 탐색 및 검증 .`index(x)`는 없을 경우 error을 뱉는다. catch로 잡아낼 수 있어 안정적.

##### `.find(x)`

x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환합니다.

##### `.index(x)`

x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생합니다.

### 리스트 메소드(list) 파이선의 리스트 linked list, stack, queue를 모두 포함하는 기능이 가능하다.

##### `.extend(iterable)` return값이 없음. 원본 값을 조작함. `+`을 이용하자.

리스트에 iterable(list, range, tuple, string*유의*) 값을 붙일 수가 있습니다.

```python
cafe.append(['cofeenie'])
print(cafe)
print('------')
cafe.extend('빽다방')
print(cafe)
print('-------')
cafe.extend(['coffine gurunaru'])
print(cafe)
print('-------')

['starbucks', 'tomntoms', 'hollys', 'banapresso', 'w cafe', 'coffee bean', 'w cafe', 'coffee bean', ['cofeenie'], '빽', '다', '방', 'coffine gurunaru']
```

##### `.insert(i, x)`[¶](http://localhost:8888/notebooks/04_data_structure.ipynb#.insert(i,-x))

정해진 위치 `i`에 값을 추가합니다.

```python
cafe.insert(0,'맥커피')
cafe.insert(len(cafe),'dd') ==> cafe.append('dd')와 동일.
```

stack : LIFO개념.

 LIFO

.append()로 넣고 .pop()으로 뺀다 라는 느낌.

##### `.pop(i)` return값이 있음.

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환합니다.

`i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

##### `.clear()`

리스트의 모든 항목을 삭제합니다. **리턴값이 없다**.



##### `.index(x)`

x 값을 찾아 해당 index 값을 반환합니다. 

앞서 remove 역시도 같은 에러가 발생하였습니다. (ValueError)

 index는 없을 시 오류가 발생합니다

##### `.count(x)`

원하는 값의 개수를 확인할 수 있습니다

##### `.sort()` 변형시키므로 sorted(a)를 쓰기.

정렬을 합니다.

내장함수 `sorted()` 와는 다르게 **원본 list를 변형**시키고, **None**을 리턴합니다

##### `.reverse()` reversed(a)를 사용하기.

반대로 뒤집습니다. **(정렬 아님)**



#### 복사 - 별명붙이기- (mutable에서만 일어남), shallow copy, deepcoapy

##### 별명 붙이기 : id값만을 복사하는 mutable의 특징. dict,list, set

![image-20200128132841195](C:\Users\multicampus\TIL\20200128_python_basic_function.assets\image-20200128132841195.png)

```python
1	original_list = [1, 2, 3]
2	copy_list = original_list
같은 id값
```



![image-20200128133019759](C:\Users\multicampus\TIL\20200128_python_basic_function.assets\image-20200128133019759.png)

```python
1	original_list = [1, 2, 3]
2	copy_list = original_list[:]
다른 id 값
```

슬라이싱을 통하여 값을 지정하는 것은 mutable만 가능.



int, float, complex, bool, string, tuple, frozen set은 immutable

![image-20200128133437249](C:\Users\multicampus\TIL\20200128_python_basic_function.assets\image-20200128133437249.png)

dictionary

![image-20200128133649783](C:\Users\multicampus\TIL\20200128_python_basic_function.assets\image-20200128133649783.png)



#### copy

> 위 코드를 [pythontutor](http://pythontutor.com/) 를 활용하여 자세하게 알아봅시다.

- 파이썬에서 모든 변수는 **객체의 주소**를 가지고 있을 뿐이다.

```
num = [1, 2, 3]
```

- 위와 같이 변수를 생성하면 `[1, 2, 3]` 이라는 객체를 생성하고, 변수에는 객체의 주소가 저장된다.
- 변경가능한(mutable) 자료형과 변경불가능한(immutable) 자료형은 서로 다르게 동작한다



일부 상황에만 서로 `다른 얕은 복사(shallow copy)`이다. example)b = list(a) b = a[:],copy.copy(a)

중첩된 객체들의 경우 복사는 최상단의 값만을 복사하고 나머지는 가리키는 주소가 옴. 

```python
import copy
1	a = [1, 2, [3,4]]
2	b = a[:]
	b = list(a)
    b = copy.copy(a)
3	b[2][0] = 99
4	print(a)
5	
6	b[0] = 24
7	print(a)
8	print(b)
```

![image-20200128134424016](C:\Users\multicampus\TIL\20200128_python_basic_function.assets\image-20200128134424016.png)

- deepcopy 깊은 복사 -cost가 크다. immutable이 deepcopy를 하지 않는 이유. 효율성을 생각한다. 하지만 원본을 훼손하지 않고 싶다면 무조건 `deepcopy`

```python
1	import copy
2	a = [1, 2, [3,4]]
3	b = copy.deepcopy(a)
4	b[2][0] = 99
5	print(a)
6	
7	b[0] = 24
8	print(a)
9	print(b)
```



![image-20200128134633378](C:\Users\multicampus\TIL\20200128_python_basic_function.assets\image-20200128134633378.png)

#### List Comprehension 

List Comprehension은 리스트안에 식, for 문을 지정합니다. 여러 줄의 코드를 한 줄로 줄일 수 있습니다.

#### 곱집합 cartesian product ** 중요함. from itertools import product

```python
from itertools import product
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
pair =product(boys, girls)
print(list(pair))
```



### 딕셔너리 메소드 활용 딕셔너리는순서가 없다고 생각하자.

##### 추가 및 삭제

##### `.pop(key[, default])` pop은 주로 뺀 값을 사용하기때문에 return값이 존재함.

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생합니다.

##### `.update()`

```python
my_dict.update(banana='바나나')
```

##### `.get(x,0)`    .get(key, default값.)

##### Dictionary comprehension

**활용법**

```python
{키: 값 for 키, 값 in 딕셔너리}

dict({키: 값 for 키, 값 in 딕셔너리})

{키: 값 for 키, 값 in 딕셔너리 if 조건식}

{키: 값 if 조건식 else 값 for 키, 값 in 딕셔너리}
```

#### 세트 메소드 활용 set

##### `.remove(elem)`

elem을 세트에서 삭제하고, 없으면 KeyError가 발생

##### `.discard(elem)`

x를 세트에서 삭제하고 없어도 에러가 발생하지 않습니다

##### `.pop()`

**임의의 원소**를 제거해 반환합니다

#pop() takes no arguments (1 given) 원하는 것을 뽑을 수는 없다.

##### `map()`, `zip()`, `filter()`

```python
chars = list(map(str,numbers))
print(''.join(chars))
''.join(map(str,numbers))
```











- 리턴 o, 원본 파괴 x 이걸 많이 쓰자.

> [ : ]  슬라이싱: (shallow copy)
>
> reversed()
>
> sorted()
>
> .pop()



## tip

im d3
이중배열 그리기, 그래프 인접행렬 2차원배열그리기....

1학기 내에 A형 맡기.

comprehension : 포함

inclusion, gunboat, implication, comprehension



front-end : UX적인 요소가 필요함. 비전공 추천.플랫폼에 구애받지 않는 형태로 커리어를 개발할 수 있다. (서버에 비해서 프래임디펜던시가 낮음.)



