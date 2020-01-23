# 20200123

## python

### 핵심은 "Abscraction"요약 - divide & conquer 

complexity를 얼마나 잘 요약해서 쓸 수 있는가.

저장 : 메모리 데이터에 이름을 붙이는 binding 

조건

반복

에서 함수 -> 객체로 발전.

> **문제 해결**을 위해서 저장과 계산을 잘하는 컴퓨터에게 명령을 시킨다.
>
> complexity가 컴퓨터와 문제 전달 과정의 큰 관건.
>
> input을 잘 전달하면 무조건 output이 나온다. 
>
> ploblem - > solution

#### 함수 - module화(부분화)를 통해 compose(조립화)가 가능.

##### 왜 쓸까? 사람이 이해하기 편하도록. procedure(절차)을 추상화.(조건&반복)

> 코드 자체가 복잡해졌음. 
>
> 복잡함을 숨기자. 
>
> 다른 사람들은 신경쓰지 않고 ouptpu만을 생각하고 쓸 수 있게 만든다.

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181746-2a1d9400-a665-11e9-804e-e92940d4fc82.png", alt="func.png">
</center>

#####  **parameter(매개변수) & argument(인자, 전달인자)**

만드는 시점 정의

: parameter(매개변수) 이름표?dust

활용되는 시점 (호출)

: argument(인자, 전달인자) 메모리 값을 가지는...?

```python
def rectangle(width, height):
    area = height * width
    perimeter = 2 * (width + height)
    return area, perimeter   # 출력값은 튜플 하나이다. 여러개가 담긴 튜플형태.immutable
    
rectangle(30,20)

area , perimeter = rectangle(30,20)
print(area)
print(perimeter)
600
100
```

```python
#알고리즘 실수
numbers = [5, 4, 3, 2, 1]

sorted(numbers)					#sortied()는 return값이 있다.
sorted_numbers = numbers.sort()  # .sort()는 return값이 없다. 원본을 훼손하며 리턴값이 없는 함수는 쓰지 않는 게 좋다.
print(sorted_numbers)
None
```

텍스트에서 단어 골라보기split()은 리스트 반환.

```python
from urllib.request import urlopen
from collections import Counter
shakespeare = urlopen('https://gist.githubusercontent.com/hphk-john/9b30d71a66e7de312a75fbd31c81c8ad/raw/9ebbe8e083997458d288d057330f4e2cc8089380/shakespear.txt')
words = shakespeare.read().decode().split()

Counter(words).most_common(10)
[('the', 23242),
 ('I', 19540),
 ('and', 18297),
 ('to', 15623),
 ('of', 15544),
 ('a', 12532),
 ('my', 10824),
 ('in', 9576),
 ('you', 9081),
 ('is', 7851)]
```

리스트의 값의 합 sum()

```python
def my_list_max(a, b):
#     a = [10, 3]
#     b = [5, 9 ]
    sum(a)
    sum(b)
    if sum(a) > sum(b):
        return a
    else:
        return b
```

#### 1. 위치 인자 (Positional Arguments)

인자는 위치로 판단한다.

#### 2. 기본 인자 값 (Default Argument Values

뒤에서 부터 채워 나간다.

```python
def func(p1=v1):
    return p
```

#### 3. 키워드 인자 (Keyword Arguments) - 함수를 유추해볼 수 있다.

변수의 이름으로  **위치에 상관 없이**  특정 인자를 전달할 수 있습니다. 

#### 4. 가변 인자 리스트 (Arbitrary Argument Lists) 

 `print()`처럼 **개수가 정해지지 않은 임의의 인자**를 받기 위해서는 가변인자를 활용합니다. 

가변인자는 **`tuple`** 형태로 처리가 되며, **매개변수에 `*`로 표현**합니다. 

 형식 인자 목록의 **마지막 ** `*args`로 주로 명명한다.

정의되지 않은 키워드 인자를 처리

```python
def func(a, b, *args):
```

##### 5.def func(**kwargs): 키벨류 페어의 쌍 a = b

```python
def func(**kwargs):
```

> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미
>
> 딕셔너리 생성 함수 예시(키워드 인자)

#### unpacking arguments list

```python
args = [1, 46, -1]
range(*args)
print(range)
```



parameter에 `*` `**` 가 있을 경우 패킹 

argument에 `*` `**` 가 있을 경우 언패킹.????????????????????????????

url get 함수 만들어보기.

```python
def my_url(itemPerPage=10, **kwargs):
    # 검증 key 또는 targetDt 가 없으면, 필수 요청변수가 누락되었습니다. 를 출력
    if 'key' not in kwargs or 'targetDt' not in kwargs:
        return '필수 요청 변수가 누락되었습니다.'
# itemPerPage 의 범위가 1~10 을 넘어가면, 1~10 까지의 값을 넣어주세요. 를 출력
    if int(itemPerPage) not in range(1,11):
        return '1~10 까지의 값을 넣어주세요'
    base_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage={itemPerPage}&'
    
    for key, value in kwargs.items():
        base_url += f'{key}={value}&'
    return base_url[:-1]

api = {
    
    'targetDt': 'yyyymmdd'
}

my_url(1,**api)
```

#### return값이 없는 함수는 뭘까???? 쓰지 않는 것을 추천.

##### 찾아보기.



#### 이름공간(namespace)  : 중2병걸린 히키코모리 막내동생. 나만 가능해.넌안돼.

- `L`ocal scope: 정의된 함수

- `E`nclosed scope: 상위 함수

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

Built-in scope 은 모든 scope에 없을 때 궁극적으로 도달하는 범위.



#### 객체 - 왜 쓸까?사람이 이해하기 편하도록.저장을 추상화















## Tip

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181750-2ab62a80-a665-11e9-84f3-c2445c098a18.png", alt="programming principle">
</center>
do not repeat your self

DRY