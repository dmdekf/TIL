# 20200203-Array 2

## Algorithm(machine way of thinking)

문제를 잘게 쪼개서 분석 - > 코딩으로 치환 하는 습관.

#### 알고리즘이란? 문제를 해결하는 프로그램.

1. Why?
   
   - reduction(구체화) - 기계가 생각하는 방식으로 문제를 접근한다.
     - Algorithm(machine way of thinking)
   
   - complexcity - abstraction(요약)으로 해결
   
     - 시간
   
     - 공간
   
     - 코드 그 자체. - def(함수화)
   
2. 개념
   - machine way of thinking
3. 구조

### Array 2 - 2차원 배열  - 01_List_II.ipynb

선언(만들기)

순회(탐색)

입력

`x`, `y`가 있다는 전제하에 접근하는 것이 좋다.

```python
# 행과 열의 분리가 직관적이다.
# `x`, `y`가 있다는 전제하에 접근하는 것이 좋다.
arr = [

[1, 2, 3],

[4, 5, 6],

[7, 8, 9]

]
```

#### 전치행렬

```python
arr = [
[1, 2, 3, ],
[4, 5, 6, ],
[7, 8, 9, ],
]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

list(zip(*arr))
list(zip([1, 2, 3],[4, 5, 6],[7, 8, 9])) #unpacking

[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
      
       
```

#### (6) 델타를 이용한 2차원 List 순회 값에 인접한 특정한 델타값을 이용함.

https://programmers.co.kr/learn/courses/18/lessons/1878 풀어보기

```python
arr = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]
]

#델타값 어느 특정한 요소에서 시작할 때 행과 열의 값의 이동값을 정한다.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 7 : [1, 1]
# 2: [ 0,1], 6:[1, 0], 8 [1, 2], 12 : [2, 1]
# s=0 이동한 위치의 값들을 s에 저장한다.
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            s+= arr[temp_x][temp_y]
# x = 1, y = 1, => 7
# i = 0 dx[0]=> 0
# x + dx[i] = 1
# y + dy[i] = 0

#첫번째 순회 ->왼쪽
arr[temp_x][temp_y] = [1,0]
#첫번째 순회 ->왼쪽
arr[temp_x][temp_y] = [1,0]

# 두번쨰 오른쪽

# 세번째 위

# 네번째 아래
```



#### 문제풀이

#### 1208 Flatten

```python
import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    d = list(map(int,input().split())) 
    #data
    for c in range(n):
        '''  매 반복 시 sorted가 필요하다. => import hipq(log(n)으로 bigO를 해결.)를 이용하면 간단히 해결.'''
        d.sort()
        d[-1] -= 1
        d[0] += 1

    print('#{} {}'.format(tc, max(d)-min(d)))
    
---------------------------------------------------------------
    
import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    n = int(input())
    d = list(map(int,input().split())) 
    max_idx = 0
    min_idx = 0
    # 첫번째 값은 이미 담겨 있으므로  range(1,100)으로 시작.
    # dumping과정
    for _ in range(n):
        for i in range(1, 100):

            if d[max_idx] < d[i]:
                max_idx = i
            if d[min_idx] > d[i]:
                min_idx = i

        d[max_idx] -=1
        d[min_idx] +=1
    # 비교해보기.
    # print('#{} {}'.format(tc, d[max_idx] - d[min_idx]))

    #dump가 끝난 과정.최대값 최소값 찾기.
    max_value = d[0]
    min_value = d[0]

    for j in range(1,100):
        if max_value < d[j]:
            max_value = j
        if min_value > d[j]:
            min_value =
    print('#{} {}'.format(tc, max_value - min_value))

```

```python
import sys

sys.stdin = open('input.txt') # 상대경로.
```

#### 4831 전기버스.

```python
T = int(input())
for tc in range(1,T+1):
    #K:최대이동 N : 종착지 M : 충전소 설치 개수
    # d : 충전소 설치 위치.
    K , N , M = map(int, input().split())

    d = list(map(int, input().split()))

    # 출발지, 종착지를 넣어주고 해당 인터벌마다 충전소를 확인, 없는 경우 이전 충전소를 확인하는 방식으로 진행.
    d.insert(0, 0) 
    d.append(N)
    # 마지막 충전소 last, 충전횟수 cnt
    last = 0
    cnt = 0
	# M+2 : 처음과 마지막을 추가해 준 값.
    for i in range(1,M+2):
        if d[i] - d[i-1] > K:
            cnt = 0
            break
        if d[i] > last + K:
            last = d[i-1]
            cnt += 1 

    print('#{} {}'.format(tc, cnt))
```

#### 4834

from collections import Counter

counter object



Counter(d).most_common() : 가장 큰 빈도수의 가장 큰 값부터 정렬하여  list[tuple()] return



eliments()

```python
   d = list(input())
    print(Counter(d))
Counter({'8': 6, '6': 6, '4': 6, '3': 5, '7': 5, '0': 5, '1': 5, '5': 4, '9': 4, '2': 4})

print(Counter(d).most_common())
[('9', 18), ('2', 13), ('3', 10), ('5', 10), ('1', 10), ('4', 9), ('8', 9),
('7', 8), ('0', 7), ('6', 6)]

print(list(c.elements()))//

['7', '7', '7', '7', '7', '7', '7', '7', '4', '4', '4', '4', '4', '4', '4',
'4', '4', '6', '6', '6', '6', '6', '6', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0', '8', '8', '8', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1',
'1', '1', '1', '1', '1', '1', '1', '1', '1']
```

### **4835 자주나오는 구간합** !!!

```python
import sys

sys.stdin = open('input.txt')

T = int(input())
# N : 숫자개수, M :구간 d : 숫자리스트
for tc in range(1,T+1):
    N, M = map(int,input().split())
    d = list(map(int, input().split()))

    arr = []

    for i in range(N-M+1):
        arr.append(sum(d[i:i+M]))

    print('#{} {}'.format(tc, max(arr) - min(arr)))
```

```python
from collections import Counter
import sys

sys.stdin = open('input.txt')
# 카드의 특징. 정수, 0-9까지의 한정된 숫자.


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    d = list(input())
    
    c = [0]*10

    for i in d:
        c[int(i)] += 1
    
    max_idx = 0
    max_value = c[0]
    
    for i in range(1,10):
        if max_value <= c[i]:
            max_value = c[i]
            max_idx = i
    print('#{} {} {}'.format(tc, max_idx, max_value))
```

 #### sorting : 단계적 사고력 키우기에 좋다. 면접 질문.









# tip

문제유형 해시

key-value값으로 자료 정렬.

from collections import Counter 이용하기.



https://programmers.co.kr/learn/courses/18/lessons/1878 풀어보기 델타값 기준 행렬 풀어보기.

