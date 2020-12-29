# Strongly Connected Component

### 문제

https://www.acmicpc.net/problem/2150
방향 그래프가 주어졌을 때, 그 그래프를 SCC들로 나누는 프로그램을 작성하시오.

방향 그래프의 SCC는 우선 정점의 최대 부분집합이며, 그 부분집합에 들어있는 서로 다른 임의의 두 정점 u, v에 대해서 u에서 v로 가는 경로와 v에서 u로 가는 경로가 모두 존재하는 경우를 말한다.

### 입력

첫째 줄에 두 정수 V(1 ≤ V ≤ 10,000), E(1 ≤ E ≤ 100,000)가 주어진다. 이는 그래프가 V개의 정점과 E개의 간선으로 이루어져 있다는 의미이다. 다음 E개의 줄에는 간선에 대한 정보를 나타내는 두 정수 A, B가 주어진다. 이는 A번 정점과 B번 정점이 연결되어 있다는 의미이다. 이때 방향은 A → B가 된다.

정점은 1부터 V까지 번호가 매겨져 있다.

### 출력

첫째 줄에 SCC의 개수 K를 출력한다. 다음 K개의 줄에는 각 줄에 하나의 SCC에 속한 정점의 번호를 출력한다. 각 줄의 끝에는 -1을 출력하여 그 줄의 끝을 나타낸다. 각각의 SCC를 출력할 때 그 안에 속한 정점들은 오름차순으로 출력한다. 또한 여러 개의 SCC에 대해서는 그 안에 속해있는 가장 작은 정점의 정점 번호 순으로 출력한다.

### 내 풀이

- 파이썬은 디폴트로 재귀 호출 1000번까지만 허용한다.
  - 임의적으로 늘려주기 위해 `sys.setrecursionlimit` 호출

```Python
import sys
sys.setrecursionlimit(12000)
from collections import deque

# 초기화 & 입력
V, E =  map(int, input().split())
graph = [[] for _ in range(V + 1)]
rgraph = [[] for _ in range(V +1 )]
stack = []
scc = []

for i in range(E):
    s,e = map(int, input().split())
    graph[s].append(e)
    rgraph[e].append(s)

visited = [False] * (V+1)
rvisited = [False] * (V+1)



# 위상정렬을 위한 dfs
def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)

    stack.append(x)
    #print(stack)

for i in range(1,V+1):
    if not visited[i]:
        dfs(i)

# SCC 탐색을 위한 dfs
def reverse_dfs(x, component):
    rvisited[x] = True

    for node in rgraph[x]:
        if not rvisited[node]:
            component = reverse_dfs(node, component)

    component.append(x)
    return component


while len(stack) > 0:
    now = stack.pop()
    if not rvisited[now]:
        component = reverse_dfs(now,[])
        scc.append(component)


# 출력부
# 정렬
for c in scc: c.sort()
scc.sort()

print( len(scc))
for c in scc:
    for x in c:
        print(x, end=' ')
    print(-1)
```
