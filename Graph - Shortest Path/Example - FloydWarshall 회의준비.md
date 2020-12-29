# 회의준비(백준)

### 문제

https://www.acmicpc.net/problem/2610
KOI 준비를 위해 회의를 개최하려 한다. 주최측에서는 회의에 참석하는 사람의 수와 참석자들 사이의 관계를 따져 하나 이상의 위원회를 구성하려고 한다. 위원회를 구성하는 방식은 다음과 같다.

1. 서로 알고 있는 사람은 반드시 같은 위원회에 속해야 한다.
2. 효율적인 회의 진행을 위해 위원회의 수는 최대가 되어야 한다.

이런 방식으로 위원회를 구성한 후에 각 위원회의 대표를 한 명씩 뽑아야 한다. 각 위원회의 대표만이 회의 시간 중 발언권을 가지며, 따라서 회의 참석자들이 자신의 의견을 말하기 위해서는 자신이 속한 위원회의 대표에게 자신의 의견을 전달해야 한다. 그런데 각 참석자는 자신이 알고 있는 사람에게만 의견을 전달할 수 있어 대표에게 의견을 전달하기 위해서는 때로 여러 사람을 거쳐야 한다. 대표에게 의견을 전달하는 경로가 여러 개 있을 경우에는 가장 적은 사람을 거치는 경로로 의견을 전달하며 이때 거치는 사람의 수를 참석자의 의사전달시간이라고 한다.

위원회에서 모든 참석자들의 의사전달시간 중 최댓값이 최소가 되도록 대표를 정하는 프로그램을 작성하시오.

예를 들어 1번, 2번, 3번 세 사람으로 구성되어 있는 위원회에서 1번과 2번, 2번과 3번이 서로 알고 있다고 하자. 1번이 대표가 되면 3번이 대표인 1번에게 의견을 전달하기 위해서 2번을 거쳐야만 한다. 반대로 3번이 대표가 되어도 1번이 대표인 3번에게 의견을 전달하려면 2번을 거쳐야만 한다. 하지만 2번이 대표가 되면 1번과 3번 둘 다 아무도 거치지 않고 대표에게 직접 의견을 전달 할 수 있다. 따라서 이와 같은 경우 2번이 대표가 되어야 한다.

### 입력

첫째 중에 회의에 참석하는 사람의 수 N이 주어진다. 참석자들은 1부터 N까지의 자연수로 표현되며 회의에 참석하는 인원은 100 이하이다. 둘째 줄에는 서로 알고 있는 관계의 수 M이 주어진다. 이어 M개의 각 줄에는 서로 아는 사이인 참석자를 나타내는 두개의 자연수가 주어진다.

### 출력

첫째 줄에는 구성되는 위원회의 수 K를 출력한다. 다음 K줄에는 각 위원회의 대표 번호를 작은 수부터 차례로 한 줄에 하나씩 출력한다. 한 위원회의 대표가 될 수 있는 사람이 둘 이상일 경우 그중 한 명만 출력하면 된다.

### 내 풀이

`tmp = [ a for a in graph[x] if a != INF]`
`max_dist = max(tmp)`
INF 값을 뺀 나머지 원소들만 있는 배열을 구하고 최댓값 구함

```Python
from collections import deque

def dfs(x):
    group[x] = group_num

    for neighbour in range(1, n+1):
        if graph[x][neighbour] == INF: continue
        if group[neighbour] == 0: dfs(neighbour)

# 초기화
INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 위원회 구성
group = [0] * (n+1)
group_num = 1

for x in range(1,n+1):
    if group[x] == 0:
        dfs(x)
        group_num += 1


# 플로이드 워셜
for stopOver in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            cost = min(graph[start][end], graph[start][stopOver] + graph[stopOver][end])
            graph[start][end] = cost


# 출력
group_max = [(-1, INF)] * group_num
for x in range(1, n+1):
    tmp = [ a for a in graph[x] if a != INF]
    max_dist = max(tmp)

    gn = group[x]
    if group_max[gn][1] > max_dist:
        group_max[gn] = (x, max_dist)

print(group_num -1 )
group_max.sort()
for i in range(1, group_num):
    print(group_max[i][0])
```
