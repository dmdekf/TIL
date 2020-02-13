# 보충 day04

## 큐빙

디버깅 tips

- 같은 색이면 숫자+문자 조합으로 회전하는 것 관찰하기
- 코드 재사용성 높힐 수 있는 방법 활용하기

![KakaoTalk_20200211_082915073_02](https://user-images.githubusercontent.com/50816217/74199935-e5b0b000-4ca8-11ea-9163-9e8735c25686.jpg)
![KakaoTalk_20200211_082915073_01](https://user-images.githubusercontent.com/50816217/74199939-e9443700-4ca8-11ea-8a1b-7c91c4b14352.jpg)

## 낚시 왕

> https://github.com/pyjune/SSA3_2

시간에 따라 변화하는 상어의 위치를 추적하는 것이므로 하나씩 따로 옮기지 말고 미세먼지, 궁수 문제와 마찬가지로 독립적으로 변화를 기록하고 한번에 결과를 기록한다.

## 연구소

벽을  `3`개 골라서 세운다. 어디서 많이 들어본 문구 아닌가. 그렇다. 가능한 첫번째 접근 방법은 완전탐색이다. 궁수(캐슬디펜스), 사다리 문제처럼 벽을 세울 수 있는 모든 자리 중에서 3개를 고르는 모든 경우의 수를 따져서 답을 도출하는 방식의 접근이 가능하다. 다만 다른 문제와의 차이는 3가지를 선택한 이후에 **탐색(bfs 또는 dfs)**을 도입하는 점이 다르다. 이 문제는 bfs를 사용하는 것이 좋다.

> [https://github.com/pyjune/SSA2/blob/master/0919%EB%B3%B4%EC%B6%A9/%EC%97%B0%EA%B5%AC%EC%86%8C.py](https://github.com/pyjune/SSA2/blob/master/0919보충/연구소.py)

## bfs 너비 우선 탐색

어떤 출발점으로부터 **거리가 같은 점**들을 탐색하는 방식. 2차원에서는 상하좌우에 있는 점을 거리가 1인 점들이라고 할 수 있다. 두 칸 이상 떨어져 있는 점들의 경우 중복을 막기 위해 한번 방문했던 점은 방문하지 않는다. 

##### 매우 중요!!!!!  모든 점을 **최단 거리**로 탐색하게 되어있다. 

![bfs](https://user-images.githubusercontent.com/50816217/74142421-31794000-4c3c-11ea-80ca-5e8cbf0bc577.JPG)

bfs의 특징

- 가까운 거리를 처리하는 동안 멀리 있는 점들을 줄 세운다. bfs 는 출발점이 복수의 갯수
- 인접한 점들을 최단거리를 방문하는 방식이다.
- 가까이 있는 점들을 처리하는 동안 멀리 있는 점들을 큐에 넣어서 처리한다.

```python
def bfs(lab, N, M):
    global maxV
    f = -1
    r = -1
    q = [0] * N*M*2 # 큐 생성
    visited = [[0]*M for _ in range(N)] # visited 생성
    for i in range(N): # 시작점 인큐 및 visited 표시
        for j in range(M):
            if lab[i][j]==2:
                r += 1
                q[r] = i
                r += 1
                q[r] = j
                visited[i][j] = 1
    while(f!=r): # 큐가 비어있지 않으면 반복
        f += 1 # 디큐
        i = q[f]
        f += 1
        j = q[f]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                if lab[ni][nj]==0 and visited[ni][nj]==0: # 인접이면(빈공간이고 바이러스가 퍼지지 않았으면)
                    r += 1
                    q[r] = ni
                    r += 1
                    q[r] = nj
                    visited[ni][nj] = visited[i][j] + 1
    # 모든 칸에 대해 lab[i][j]와 visited[i][j]가 0인 칸 수를 maxV와 비교
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j]==0 and visited[i][j]==0:
                cnt += 1
    if maxV<cnt:
        maxV = cnt
```

   `visited[ni][nj] = visited[i][j] + 1`

==>많은 bfs 문제가 방문했던 점에서 출발점까지의 거리를 요구하기 때문에 탐색을 하는 단계에서 거리를 기록하는 부분이다. 

#####   면접에서 bfs와 dfs 차이를 물어보면 어떤 상황에 사용되는지 대답하는 것이 핵심



