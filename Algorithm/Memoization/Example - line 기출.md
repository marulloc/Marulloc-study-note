# 2019 상반기 LINE 인턴 채용 코딩테스트

### 문제

https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/

문제
연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.

조건
코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 \* B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
입력 형식
표준 입력의 첫 줄에 코니의 위치 C와 브라운의 위치 B를 공백으로 구분하여 순서대로 읽는다.

출력 형식
브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.

예제
입력: 11 2

출력: 5

코니의 위치: 11 → 12 → 14 → 17 → 21 → 26

브라운의 위치: 2 → 3 → 6 → 12 → 13 → 26

브라운은 코니를 5초 만에 잡을 수 있다.

### 내 풀이 - 오답

- 브라운을 먼저 계산하고
- 코니를 움직이면서 확인하는 로직
- 그러나, 브라운이 어떤 좌표 x에 도달하는 최소 시간를 구하는 것이 아니라, 브라운이 코니를 잡을 수 있는 최소 시간을 구하는 것이기 때문에, x 2 를 통해 움직이는 좌표에선 오답이 발생 할 수 있다.
- 잘못된 로직은 아래와 같다.

```Python
from collections import deque
MAX = 200001
INF = int(1e9)

c_start , b_start = map(int, input().split())

# brown이 x라는 좌표에 도달하는 최단 시간을 배열에 담는다.
brown = [INF] * MAX
brown[b_start] = 0

queue = deque([])
queue.append((b_start, 0))

while queue:
    now = queue.popleft()

    if now[0] - 1 >= 0:
        if brown[now[0] - 1] > now[1] + 1:
            brown[now[0] - 1] = now[1] + 1
            queue.append((now[0] - 1, now[1] + 1))

    if now[0] + 1 < MAX:
        if brown[now[0] + 1] > now[1] + 1:
            brown[now[0] + 1] = now[1] + 1
            queue.append((now[0] + 1, now[1] + 1))

    if now[0] * 2 < MAX:
        if brown[now[0] * 2] > now[1] + 1:
            brown[now[0] * 2] = now[1] + 1
            queue.append((now[0] * 2, now[1] + 1))


# 코니의 위치를 움직이면서, 브라운 배열을 확인
now_c = c_start
w = 0
time = 0
catch_flag = False
while now_c < MAX:
    if brown[now_c] == time:
        catch_flag = True
        break

    now_c += (1 + w)
    time += 1
    w += 1


if catch_flag: print(now_c,time)
else: print(-1)
```

### 따라서

- 코니를 먼저 이동시킨다.
- 좌표 x에 대해 코니의 이동 최단 시간을 구해두고
- 브라운이 움직일 수 있는 모든 좌표를 탐색한다. ( 시간과 함께 enqueue, dequeue)
- dequeue를 하며, 현재 좌표에 도달한 브라운의 시간과, 현재 좌표에 도달한 코니의 시간을 비교(미리 구해둔 배열에서)
  즉, 브라운 -> 코니의 로직을 코니 -> 브라운으로 변경

```Python
from collections import deque
MAX = 200001
INF = int(1e9)

c_start , b_start = map(int, input().split())

# 코니, 위치마다 몇초에 도착하는지
cony = [INF] * MAX
time = 0
w = 0

now_c = c_start
while now_c < MAX:
    cony[now_c] = time

    time += 1
    now_c += (1 + w)
    w += 1


# brown이 움직일 수 모든 경우를 돌면서, 코니의 배열을 확인
# 코니가 어떤 좌표 x에 도달하는데 걸린시간에 cony[x]이므로
# cony[x]의 값과 brown이 x에 도달하는데 걸린시간이 같은 경우를 찾는다.
queue = deque([])
queue.append((b_start, 0))
visited = set()

answer = -1
while queue:
    now = queue.popleft()


    if now[0] >= MAX : continue

    if cony[now[0]] == now[1]:
        answer = now[1]
        break

    next_1 = (now[0] - 1, now[1] + 1)
    next_2 = (now[0] + 1, now[1] + 1)
    next_3 = (now[0] * 2, now[1] + 1)

    if next_1[0] >= 0 and not next_1 in visited :
        visited.add(next_1)
        queue.append(next_1)
    if next_2[0] < MAX and not next_2 in visited:
        visited.add(next_2)
        queue.append(next_2)
    if next_3[0] < MAX and not next_3 in visited:
        visited.add(next_3)
        queue.append(next_3)

print(answer)

```
