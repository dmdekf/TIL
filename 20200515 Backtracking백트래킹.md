# 20200515 Backtracking백트래킹

> - 모든 후보를 검사하지 않는다.
>
> 상태공간트리를 깊이우선탐색(dfs)하는 방법 +  정답으로 갈 것 같지 않으면 더이상 깊이우선탐색을 중단(prunning:가지치기)

> 불피요한 경로를 조기에 차단하여 회수를 줄인다.

- 백트래킹 절차

1. 상태 공간 트리의 깊이우선 검색을 실시
2. 각 노드가 유망한지 점검(가지치기)
3. 그 노드가 유망하지 않으면 그노드의 부모 노드로 돌아가서 검색을 계속한다.

![image-20200515095415254](assets/image-20200515095415254.png)

- state space tree 상태 공간 트리 에서 목표탐색

  ![image-20200515094531052](C:\Users\peach\AppData\Roaming\Typora\typora-user-images\image-20200515094531052.png)

- leaf node : 목표탐색의 마지막 구간.

  ![image-20200515095131110](C:\Users\peach\AppData\Roaming\Typora\typora-user-images\image-20200515095131110.png)

- 백트래킹을 이용한 퀸 문제 탐색

  ![image-20200515100221255](assets/image-20200515100221255.png)

![image-20200515100512388](assets/image-20200515100512388.png)

![image-20200515100647961](assets/image-20200515100647961.png)

![image-20200515104635159](assets/image-20200515104635159.png)

![image-20200515105132344](assets/image-20200515105132344.png)