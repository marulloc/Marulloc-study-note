# [카카오 인턴] 동굴 탐험(프로그래머스)

### 문제

### 입력

### 출력

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
