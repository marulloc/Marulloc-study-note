# [카카오 인턴] 동굴 탐험(프로그래머스)

### 문제

오지 탐험가인 프로도는 탐험 도중 n개의 방으로 이루어진 지하 동굴을 탐험하게 되었습니다. 모든 방에는 0부터 n - 1 까지 번호가 붙어있고, 이 동굴에 들어갈 수 있는 유일한 입구는 0번 방과 연결되어 있습니다. 각 방들은 양방향으로 통행이 가능한 통로로 서로 연결되어 있는데, 서로 다른 두 방을 직접 연결하는 통로는 오직 하나입니다. 임의의 서로 다른 두 방 사이의 최단경로는 딱 한 가지만 있으며, 또한 임의의 두 방 사이에 이동이 불가능한 경우는 없습니다.

탐험에 앞서 이 지하 동굴의 지도를 손에 넣은 프로도는 다음과 같이 탐험 계획을 세웠습니다.

1. 모든 방을 적어도 한 번은 방문해야 합니다.
2. 특정 방은 방문하기 전에 반드시 먼저 방문할 방이 정해져 있습니다.
   2-1. 이는 A번 방은 방문하기 전에 반드시 B번 방을 먼저 방문해야 한다는 의미입니다.
   2-2. 어떤 방을 방문하기 위해 반드시 먼저 방문해야 하는 방은 없거나 또는 1개 입니다.
   2-3. 서로 다른 두 개 이상의 방에 대해 먼저 방문해야 하는 방이 같은 경우는 없습니다.
   2-4. 어떤 방이 먼저 방문해야 하는 방이면서 동시에 나중에 방문해야 되는 방인 경우는 없습니다.
   위 계획 중 2-2, 2-3, 2-4는 순서를 지켜 방문해야 하는 두 방의 쌍이 A → B(A를 먼저 방문하고 B를 방문함) 형태로 유일함을 의미합니다. 즉, 프로도는 아래와 같은 형태로 방문순서가 잡히지 않도록 방문 계획을 세웠습니다.

- A → B, A → C (방문순서 배열 order = [...,[A,B],...,[A,C],...]) 형태로 A를 방문 후에 방문해야 할 방이 B와 C로 두 개 또는 그 이상인 경우
- X → A, Z → A (방문순서 배열 order = [...,[X,A],...,[Z,A],...]) 형태로 A를 방문하기 전에 방문해야 할 방이 X와 Z로 두 개 또는 그 이상인 경우
- A → B → C (방문순서 배열 order = [...,[A,B],...,[B,C],...) 형태로 B처럼 A 방문 후이면서 동시에 C 방문 전인 경우
  그리고 먼저 방문해야 할 방과 나중에 방문할 방을 반드시 연속해서 방문해야 할 필요는 없어 A방을 방문한 후 다른 방을 방문한 후 B방을 방문해도 좋습니다.

방 개수 n, 동굴의 각 통로들이 연결하는 두 방의 번호가 담긴 2차원 배열 path, 프로도가 정한 방문 순서가 담긴 2차원 배열 order가 매개변수로 주어질 때, 프로도가 규칙에 맞게 모든 방을 탐험할 수 있을 지 return 하도록 solution 함수를 완성해주세요.

### 입력

- n은 2 이상 200,000 이하입니다.
- path 배열의 세로(행) 길이는 n - 1 입니다.
  - path 배열의 원소는 [방 번호 A, 방 번호 B] 형태입니다.
  - 두 방 A, B사이를 연결하는 통로를 나타냅니다.
  - 통로가 연결하는 두 방 번호가 순서없이 들어있음에 주의하세요.
- order 배열의 세로(행) 길이는 1 이상 (n / 2) 이하입니다.
  - order 배열의 원소는 [방 번호 A, 방 번호 B] 형태입니다.
  - A번 방을 먼저 방문한 후 B번 방을 방문해야 함을 나타냅니다.

### 출력

우선순위에 맞게 방문할 수 있으면 True
아니면 False 반환하라

### 내 풀이

1. 동굴의 통로(간선)이 무작위로 주어지므로, 이것을 처리하는 preProcess함수를 두었다.
   - bfs를 수행하면서, 먼저 방문되었는가 여부로 단방향 간선으로 만든다.
2. 우선순위를 간선으로 처리하여 위상정렬에 이용할 수 있도록 만들었다.
3. 동굴의 시작점도 우선순위에 얽혀있을 수 있으므로, indegree를 조사한다.
4. 입력을 빠르게 하기위해 `sys.stdin.readline()` 사용

```Python
import sys
from collections import deque


def preProcess(graph, indegree):
    queue = deque()
    queue.append(0)

    while queue:
        now = queue.popleft()
        indegree[now] -= len(graph[now])

        for node in graph[now]:
            graph[node].remove(now)
            queue.append(node)


def solution(n, path, order):
    # 초기화
    indegree = [0] * (n)
    graph = [[] for _ in range(n)]
    visited = [False] * n

    for edge in path:
        graph[edge[0]].append(edge[1])
        indegree[edge[1]] += 1
        graph[edge[1]].append(edge[0])
        indegree[edge[0]] += 1

    preProcess(graph,indegree)

    # 우선순위를 단방향 간선으로 처리
    for edge in order:
        graph[edge[0]].append(edge[1])
        indegree[edge[1]] += 1


    # 위상 정렬
    queue = deque()
    if (indegree[0] == 0): queue.append(0)

    while queue:
        now = queue.popleft()
        visited[now] = True

        for near in graph[now]:
            indegree[near] -= 1
            if(indegree[near] == 0) :
                queue.append(near)


    # 출력
    # 방문하지 못한 노드가 있으면, 경로가 없는 것
    answer = True
    for isVisit in visited:
        if not isVisit:
            answer = False

    return answer
```
