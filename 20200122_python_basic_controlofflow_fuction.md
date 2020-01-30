# 20200122

## Python

#### 제어문

##### **index와 함께 `for` 문 활용!!! 중요 -enumerate()**

> iterable > squence

> iterable = sequence + dict + 순회가능한 객체(generator를 이용하여....)

`enumerate`(*iterable*, *start=0*) tuple return

```
Init signature: enumerate(iterable, start=0)
Docstring:     
Return an enumerate object.
```

나열된 것을 돌려주는 함수.

열거 객체(???????????)를 돌려줍니다. *iterable* 은 시퀀스, [이터레이터](https://docs.python.org/ko/3.6/glossary.html#term-iterator) 또는 이터레이션을 지원하는 다른 객체여야 합니다. [`enumerate()`](https://docs.python.org/ko/3.6/library/functions.html#enumerate) 에 의해 반환된 이터레이터의 [`__next__()`](https://docs.python.org/ko/3.6/library/stdtypes.html#iterator.__next__) 메서드는 카운트 (기본값 0을 갖는 *start* 부터)와 *iterable* 을 이터레이션 해서 얻어지는 값을 포함하는 튜플을 돌려줍니다.

<center><img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png", alt="container"/></center>

```
for menu in enumerate(lunch):
    print(menu)
    
(0, '짜장면')
(1, '초밥')
(2, '치킨')
(3, '아이스크림')
(4, '샤브샤브')
(5, '호두과자')
for idx, menu in enumerate(lunch):
    if menu == '샤브샤브':
        print(idx, menu)
4 샤브샤브
lunch.index('샤브샤브')
4
```

##### *빈도수 측정* dictionary 구축하기 (`for`, `if`) - 자주 사용함.!!!!

> 다음과 같은 리스트가 있을 때 각각의 요소의 개수를 value 값으로 갖는 딕셔너리를 만드세요.
>
> ```python
> book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
> 
> 예시 출력)
> {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
> ```

```
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
title_counter = {}
# (1) for 문 활용
for title in book_title:
    if title in title_counter:
        title_counter[title] += 1
    else:
        title_counter[title] = 1
 
{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

# (2) .count() 쓰기
title_counter = {}
for title in book_title:
    title_counter[title] = book_title.count(title)
print(title_counter)

title_counter = {}
for title in set(book_title): # 순회요소의 중복값을 제거한 set이용.순회횟수최소화
    title_counter[title] = book_title.count(title)
print(title_counter)

# (3) .get() method #초기값 initializing 가능. 
title_counter = {}

for title in book_title:
    title_counter[title] = title_counter.get(title,0) +1
print(title_counter)

# (4) collentions.Counter(스퀀스형자료) 사용 from collections import Counter 
from collections import Counter
print(collections.Counter(book_title))
print(dict(Counter(book_title)))

print(max(dict(Counter(book_title)).values()))
2
```

최빈도 :` max()`

`split(어떻게 나눌 지 값을 적는다.)`

```
numbers.split(sep=None, maxsplit=-1)
Docstring:
Return a list of the words in the string, using sep as the delimiter string.

sep
  The delimiter according which to split the string.
  None (the default value) means split according to any whitespace,
  and discard empty strings from the result.
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.
Type:      builtin_function_or_method
```

`map(적용할 함수 이름, 적용할 iterable)`

### 보충문제 풀이 pset01,pset02

- 1.양수/음수/0의 비율을 각각 순서대로 출력하시오.

  ```
  예시 입력)
  0 -1 3 5 
  
  예시 출력)
  0.5 0.25 0.25
  ```

```
(1)
numbers.split()
numberlist = []
for number in numbers.split()
    number_list.append(int(number))
(2)map()    
list(map(int, numbers.split()))
(3)list comprehension
[int(n) for n in numbers.split()]

numbers = input()
# 아래에 코드를 작성하세요.
percent_dic = {
    'plus' : 0,
    'minus' : 0,
    'zero' : 0,
    
}
num_list = []
for num in numbers.split(' '):
    num_list.append(num)
print(num_list)

for num in num_list:
    if int(num) > 0:
        percent_dic['plus'] += 1/len(num_list)
    elif int(num) < 0:
        percent_dic['minus'] += 1/len(num_list)
    else:
        percent_dic['zero'] +=1/len(num_list)

print(percent_dic.values())

(1)
numbers.split()
number_list = []
for number in numbers.split():
    number_list.append(int(number))
(2)    
print(list(map(int, numbers.split())))
(3)
print([int(n) for n in numbers.split()])
```

list comprehension 풀이.

```
tc = input()
numbers = [int(tc) for n in tc.split()]

total = len(numbers)

positive = len([number for number in numbers if number > 0])
negative = len([number for number in numbers if number < 0])
zero = len([number for number in numbers if number == 0])
print(positive / total, negative / total, zero / total)
```

#### List comprehension 성능상 다중항보다 좋음. 

list를 순회하여 특정 조건의 값들로 구성된 list를 만들 때 사용.

- 3.두 단어 중에 중복된 알파벳이 있는지 여부를 판단하여 True 혹은 False를 반환하시오

```
def is_contain_same_alphabet(a, b):
    # 아래에 코드를 작성하시오.
    for char in a:
        if char in b:
            return True
return False                          #return 을 만나면 함수는 종료된다.

print(is_contain_same_alphabet('my', 'sweet home'))
print(is_contain_same_alphabet('oreo', 'kikat'))
```

#### continue

```
for age in ages:
    if age < 20:
        continue
    print(f'{age}살은 성인입니다.')
23살은 성인입니다.
30살은 성인입니다.
25살은 성인입니다.
31살은 성인입니다.
```



#### computer science

divide & conquer

#### `range()` 함수

list 나 tuple 에 비해 범위의 크기에 무관하게 항상 같은 (작은) 양의 메모리를 사용한다. (start, stop, step 값만을 저장).

range() 가 돌려준 객체(iterable)는 리스트인 것 같지만, 리스트가 아니다.

```
for _ in range(10):
    print('안녕')
안녕
안녕
안녕
안녕
안녕
안녕
안녕
안녕
안녕
안녕
```

#### break

`break` 문은 반복문을 종료하는 표현입니다.

`for` 나 `while` 문으로부터 빠져나가게 만듭니다.

```
for i in range(10):
    if i > 1:
        print('0이랑 1만 필요해!!')
        break
    print(i)
```

조건문과 반복문, break를 활용하여 다음 headlines 리스트의 요소들을 130자 크기의 하나의 문자열로 이어 붙이는 코드를 작성하세요.

``` 

```

```
headlines = [
    "Local Bear Eaten by Man",
    "Legislature Announces New Laws",
    "Peasant Discovers Violence Inherent in System",
    "Cat Rescues Fireman Stuck in Tree",
    "Brave Knight Runs Away",
    "Papperbok Review: Totally Triffic"
]
news_join = ''

for headline in headlines:
    news_join += headline + ' '
    if len(news_join) > 130:
        news_join = news_join[:130]
        print(news_join)
        break
print(' '.join(headlines)[:130])
```

#### 문제풀이 /problems/02_control_of_flow_00

##### 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

------

```
예시 입력)
'Life is too short, you need python'

예시 출력)
Lf s t shrt, y nd pythn

vowels = 'aeiou'

result = ''
for char in my_str:
    if char not in vowels:
        result += char
print(result)
```

#### 문제풀이 02_control_of_flow_01

##### 달력 출력하기

```
calendar = { 
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

for month, day_count in calendar.items():
    count = 0
    print(f'{month:10}','월')
    for day in weeks:
        print(f'{day}',end = ' ')
    print()
    
    for i in range(1,day_count+1):
        print(f'{i:2}', end=' ')
        count += 1
        if count == 7:
            print()
            count = 0
    print()
```











## Tip

알고리즘 d3까지 풀어보기. im통과.

소프트 제타위키 정답.

[https://zetawiki.com/wiki/SW_Expert_%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8](https://zetawiki.com/wiki/SW_Expert_아카데미)



sk, lg, samsung A형이 ssafy A형보다 쉬움....



- 알고리즘강의

coursera

스탠포드- 언어 제한 없음 강력추천  tim roughgarden.prof., 프린스턴- 자바기반 알고리즘 algorithms, part 1,2

- 알고리즘은

design -> analyze -> implement -> experiment

Input -> Output을 조작하는 것. 잘 정리하는 것이 중요하다.

- 재귀

  sicp 재귀.

  berkeley 61 A recursion www.cs61a.org

- fintech

world quant 취직시 30억을 돌릴 수 있게 해줌.... 

- 소수찾기

에라토스테네스의 체