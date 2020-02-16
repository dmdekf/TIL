# 20200214

## Stack

### 괄호문제 '()' -> 변수안에 스택의 길이를 체크하기만 해도 됨.

sys.stdin.readline() : 'string'으로 받을 때 줄바꿈 '\n'이 마지막 에 포함된다. 

-> strip() 을 이용한다.

`D = list(sys.stdin.readline().strip())`

input() : 자체적으로 마지막 줄바꿈을 삭제함.

```python
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    D = list(sys.stdin.readline())
    print(D)

(())())
['(', '(', ')', ')', '(', ')', ')', '\n']

D = list(sys.stdin.readline().strip()) strip() 을 이용한다.
```

```python
'''
1.'('가 나오면 스텍에 '('를 넣어줌.
2. ')'가 나오면 스텍에서 '('를 빼줌
- 스텍이 비어있는지 
-비어있다면  false
-아니면pop()
3. 스텍이 비어있다면 True
아니면 False
'''

import sys

T = int(sys.stdin.readline())


for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = []
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
```



#### 42588 프로그래머스 탑

1. 격자로 그려보기

#### 42858 쇠막대

```py
# arrangement	            return
# ()(((()())(())()))(())	17

def solution(arrangement):
    answer = 0
    stack = 0
    for index, i in enumerate(arrangement):
        
        #레이저를 닫는 괄호일 경우 '('를 제거.
        if i == ')' :
            stack -= 1 
            #레이저가 아닌 경우 쇠막대기로 인식.
            if arrangement[index-1] == ')':
                answer += 1
            else:
                answer += stack
        else:
            stack += 1
    return answer
```



## Graph I

Graph Crash Course

### 핵심내용

- Graph
- Graph 구현
- Graph 탐색 (DFS & BFS)
- Graph 관련 문제

`정점` 과 `간선`

- 선형

  스택, 배열, 큐, 연결리스트, 덱

  1:1 or 자료(데이터)의 관계가 없을 때.

- 비선형: 현실의 복잡도를 반영한 모델링으로 접근..

  graph > Tree

### Graph란?



- `정점(Node)` == `꼭지점(Vertex)`
  - **위치**를 의미한다.
- `간선(Edge)`==`아크(Arc)` == link == branch
  - **위치 간의 관계를 표시한 선**을 의미한다.
- **인접 정점(Adjacent Vertex)**
  - 간선으로 직접 연결된 정점(노드)

#### Graph 구현 & 표현

####  Graph 표현 별 공간(Space) 복잡도 및 시간(Time) 복잡도!!중요.

이차배열

undirected무방향 : 중복표현(대칭형태)

directed방향 :  방향성이 존재하여 각 노드마다 값들이 다름.

딕셔너리(노드 : 연결상태)



#### Graph 탐색 (DFS & BFS)-임의의 방향성을 정해놓고 모두 검색한다는 생각.

목적 : 모든 정점을 한 번씩 조회하기

가능성을 점차 소진시킨다는 생각으로 진행. ->**스택이 공백**이 될 때까지...

**BFS + `큐 `** - 최단경로 찾기 좋음.

옵션 - 넓이우선

**DFS + stack** 헨젤과그래텔의 빵가루.

visited = [], stack = []

갈 수 있는 max, 막히면 한단계 전



## Graph와 Tree의 차이

- 트리는 그래프 중에 속한 특별한 종류라고 볼 수 있음

<div style="text-align:left">
<table>
  <tr>
    <th></th>
    <th style="text-align:center">그래프</th>
    <th style="text-align:center">트리</th>
  </tr>
  <tr>
    <td style="text-align:center">정의</td>
    <td style="text-align:left">노드와 노드를 연결하는 간선으로 표현되는 자료 구조</td>
    <td style="text-align:left">그래프의 한 종류, 방향성이 있는 비순환 그래프</td>
  </tr>
  <tr>
    <td style="text-align:center">방향성</td>
    <td style="text-align:left">방향 그래프, 무방향 그래프 둘다 존재함</td>
    <td style="text-align:left">방향 그래프만 존재함</td>
  </tr>
  <tr>
    <td style="text-align:center">사이클</td>
    <td style="text-align:left">사이클 가능함, 순환 및 비순환 그래프 모두 존재함</td>
    <td style="text-align:left">비순환 그래프로 사이클이 존재하지 않음</td>
  </tr>
  <tr>
    <td style="text-align:center">루트 노드</td>
    <td style="text-align:left">루트 노드 존재하지 않음</td>
    <td style="text-align:left">루트 노드 존재함</td>
  </tr>
  <tr>
    <td style="text-align:center">부모/자식 관계</td>
    <td style="text-align:left">부모 자식 개념이 존재하지 않음</td>
    <td style="text-align:left">부모 자식 관계가 존재함</td>
  </tr>
</table>
</div>

-출처 : fastcampus Chapter17-그래프 이해 강의자료









## tip

mac - homebrew~~~~



programmers - 이확영대표님, 회사 분위기 좋음. 카카오, 네이버 cto. 



facebook - 사람들과의 관계(노드)에서 공통점을 뽑아냄.

> 기존 광고시장의 경우 사람수를 기준으로 잡음.
>
> ​	페북의 경우활성사용자에 초점을 맞췄을 때 실 사용자를 찾기. 일주일안에 7(매직넘버)명의 사람들에게 리퀘를 보내고 수락이 되면 활성사용자의 가능성이 높아짐. - > 페북 가입한 뒤 전화번호를 입력하여 지인들에게 페북 요청 보내기 기능 제안.

​	

