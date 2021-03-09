# CPU 스케쥴링

https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Operating%20System/CPU%20%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81.md
https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Operating%20System/CPU%20Scheduling.md

# 멀티프로그래밍의 목적은

- CPU의 속도가 굉장히 빨라서 놀고있기 때문에 context switch를 해서 시간을 시분할해서 프로세스들을 계속 돌림으로써 CPU의 효용을 높이기 위함
- 이를 위해 CPU 스케쥴링이 필요하다.
  ![](https://i.imgur.com/oRMRJnM.png)
- IO를 하면서 대기하는 시간을 IO burst라고 한다.
- 어떨때는 CPU burst(주로 running), 어떨때는 IO burst(waiting, waiting→ready)
- 이렇게 상태가 왔다갔다 하는데 전자가 많으면 CPU bound, 후자의 경우 IO bound라고 한다. 통계를 그려보니까, 상단의 그래프의 형태를 보인다. 즉, CPU만 열심히 쓰는 프로세스는 숫자가 몇개 안되고, IO burst타임이 더많은, IO-bound 의 빈도가 훨씬 더 많다는 것을 알 수 있다.
  > I/O bound의 경우 CPU가 놀고있는 시간이 많으니까, 자원을 효율적으로 쓰기 위해 CPU 스케쥴링이 필요하다.

<br>
<br>

# CPU sheduler

메모리에 로드되어있는 프로세스 중에 어떤 것에 CPU를 할당해주는지 선택한다.

ready상태에 있는 프로세스들 중에서 CPU를 할당해줄 수 있는 프로세스를 선택하는 걸 CPU 스케쥴링 문제라고 한다.

#### 그렇다면 다음 프로세스를 어떻게 선택할까?

#### 대기중인 레디큐를 어떤 형태로 하면 좋을까?

- 링크드 리스트? 이진 트리?
- FIFO Queue : First-in, First-out
- Priority Queue : 이 경우 프로세스의 우선순위를 어떻게 정할 수 있을지가 관건이다

<br>
<br>

### Preemptive vs Non-preemptive (선점형 vs 비선점형)

- 스케쥴러가 쫓아낼 수 있는지 여부. 강제로 쫓아내는 것 vs 자발적으로 나가게 하는 것
- **Non-preemptive 스케쥴링**
  - 어떤 프로세스가 선점을 하고 나면 그 프로세스가 자발적으로 release하기 전까지는 terminate하거나 switching하지 않는다. 쓰도록 내버려둔다.
  - 응답시간의 예측이 편하며, 일괄처리 방식에 적합함. 단점으론 덜 중요한 작업이 자원을 할당 받으면, 중요한 작업이 레디큐에 들어와도 처리 될 수 없다.
- **Preemptive 스케쥴링**
  - 프로세스가 스케쥴러에 의해 쫓겨날 수 있다.
  - 어떤 프로세스가 자원을 사용하고 있을때 우선순위가 더 높은 프로세스가 올경우 자원을 강탈하기 때문에, 우선순위가 높은 프로세스를 빠르게 처리할 수 있다.
  - 빠른 응답 시간을 요구하는 시스템에서 주로 사용된다.
  - 빈번한 context swtich에 대한 오버헤드가 크다

🤔 시스템에서 짧은 빈도마다 발생하는 이벤트?
🤔 스케쥴러는 하드웨어? OS?
**스케줄러란 어떤 프로세스에게 자원을 할당할지를 결정하는 운영체제 커널의 모듈을 지칭한다!!**

<br>
<br>

### Decision Making for CPU-scheduling:

1. running → waiting 해야 하는 경우 : IO를 해야해서
2. running → ready 해야 하는 경우 : 잠깐 쉬어야겠다고 바로 ready로 가는 경우가 있음
3. waiting → ready : IO가 다 끝나서 CPU를 점유하기 위해 ready로 이동
4. 프로세스가 terminate하는 경우

- 1, 4 : no choice - non-preemptive. 자발적으로 가는 경우임. 고민할 필요 없음
- 2, 3 : choices - preemptive해야할까, non-preemptive해야 할까? (현대 시스템에선 대부분 preemptive이긴 함)

<br>
<br>

# Dispatcher

- CPU 스케듈러에 의해 선택된 프로세스에게 CPU코어의 컨트롤을 넘겨주는 모듈.
- 즉 컨텍스트 스위치를 해주는 모듈.
- **dispatcher의 기능\*\***
  - 컨텍스트를 하나의 프로세스에서 다른 프로세스로 넘겨주기
  - 유저모드로 바꿔주기
  - 새로운 프로세스의 적당한 위치로 resume 시키는 것 (jumping to the proper location to resume the user program)

**즉 스케쥴러는 선택해주고, 실제로 switching 해주는 건 dispatcher가 해준다.**

<br>

### dispatcher는 엄청나게 빨라야 한다!

![](https://i.imgur.com/3hfj0a4.png)

p0와 p1이 서로 컨텍스트 스위치 한다고 하면,
pcb0에 상태를 저장하고, pcb1을 restore해와야 한다.
이 시간을 dispatch latency라고 한다.

- dispatch latency
  - the time to stop one process and start another running
  - cpu의 실제 실행시간보다 더 길다면.. no
  - 가급적이면 짧아야 한다.

<br>

### 얼마나 자주 context switch가 발생할까?

![](https://i.imgur.com/Lb1WfSP.png)

vmstat 명령어를 통해 확인할 수 있다.

<br>
<br>

### Scheduling의 목표

1. **CPU utilization** : CPU가 가능한 바쁘게 만들기
2. **Throughput** : throughput 높이기. 어떤 단위 시간 내에 프로세스 "완결수"를 높이자.
3. **Turnaround time**:
   - 어떤 프로세스가 레디 큐에 도착하고 나서부터 실행이 종료되기 까지의 시간.
   - 제출하고 종료되는 시간까지를 단축시키는 것
4. **Waiting time**: (주로 볼 것)
   - 어떤 프로세스가 ready 큐에 대기하고 있는 시간.
   - 레디 큐의 대기시간을 합친것을 최소화 시키자는 것
5. **Response time:**
   - 프로세스가 ready queue에 들어와서 처음으로 실행되기까지의 시간
   - response 시간을 줄이자 (주로 유저 인터페이스. 게임에서 몬스터 공격 시간)

## CPU Scheduling Problem

- 레디 큐에 있는 프로세스들 중에서 어떤 프로세스에게 CPU를 할당해 줄지의 문제.
- solutions

#### 비선점

- FCFS : First-Come, First-Served
  - 문제가 많음. 아주 초창기에 씀. 지금은 아무도 안씀
  - 실행 시간이 짧은 프로세스가 뒤에 오는 경우가 많아지면 평균 대기시간이 길어진다.
- SJF : Shortest Job First (SRTF : Shortest Remaining Time First)
  - 무한 연기가 발생할 수 있다. 따라서 **aging** 기법이나, HRN을 사용한다.
- HRN (Highest Response-ratio Next)
  - SJF에 대기시간까지 고려한 것으로, 대기시간이 긴 프로세스에게 우선순위를 준다고 생각하면된다. 계산된 우선순위로 CPU 할당
  - 우선순위 = (대기시간 + 실행시간) / 실행시간

<br>

#### 선점

- **RR : Round-Robin**
  - time-sharing 방식과 관련된다.
  - CPU 사용시간의 limit(Time slice)을 걸어두는 로직으로 모든 프로세스가 Time slice만큼의 CPU 사용시간을 보장받게 된다.
    - Time Slice를 프로세스의 평균 수행시간보다 짧게 잡으면 빈번한 Context Switch로 오버헤드 증가한다.
    - Time Slice를 너무 크게 잡으면, FCFS와 다름 없어진다.
- Priority-based

  - 대기 큐에 있는 프로세스들에게 우선순위를 부여하고, 우선순위 순으로 CPU를 사용하게 된다.
  - 그러나, 우선순위는 계속 변경된다. 그에 따라 애초에 우선순위가 낮은 프로세스의 기아 Starvation문제가 발생할 수 있다.
    - 그래서 시간이 지날수록 프로세스의 우선순위를 증가시키는 AGING기법 사용

- MLQ : Multi-Level Queue
  - 우선순위마다 레디 큐 형성(각 큐는 라운드 로빈이나 FCFS등 독자적 스케줄링 사용 가능)
  - 우선순위가 낮은 큐에서 작업 실행 중이더라도 상위 단계의 큐에 프로세스가 도착하면 CPU를 빼앗는 선점형 스케줄링
  - 우선순위가 낮은 프로세스가 오랫동안 CPU 할당을 기다리는 기아 현상이 발생할 수도 있음
- MLFQ : Multi-Level Feedback Queue
  - 피드백까지 주는 것. 현대적인 스케쥴러의 모습
    - 우선순위 낮은 레디큐에는 큰 Time Quantum을 줌
    - 맨 아래 큐에서 너무 오래 대기하면 다시 상위 큐로 이동 (에이징 기법을 통한 기아상태 예방)

<br>
<br>

# Round-Robin 스케쥴링

- 위에 배운 스케쥴링들은 time-sharing에는 부적합.
- Round-Robin : 타임 퀀탐만큼만 사용하도록 해주는 Preemptive FCFS.
- time quantum(or time slice)는 아주 작은 시간 단위로 주는데
  - 보통은 10에서 100 밀리 세컨드
- 레디 큐는 어떻게 구현할까?
  - **circular queue**
- 스케쥴러는 circular queue를 돌면서 각 프로세스에 CPU를 할당한다. 타임 퀀텀을 인터벌로 두고.
- allocating the CPU to each process for a time interval of up to 1 time quantum

#### 두 가지 케이스를 살펴보자

1. CPU burst가 one time quantum보다 작은 경우는?

   - 그 프로세스는 스스로 release될 것. 무조건 expires 됐으니까
   - 스케쥴러는 레디큐의 다음 프로세스로 넘어갈 것

2. CPU burst가 one time quantum보다 큰 경우는?

   - 타이머가 동작하여 OS의 인터럽트가 걸어지도록 하여
   - 컨텍스트 스위치가 발생하고,
   - 프로세스는 레디큐의 tail로 놓여질 것

![](https://i.imgur.com/ZjNQUeP.png)

- waiting time
  - p1 = 10-4, p2 = 4, p3 = 7
  - total = 17
  - average = 5.66
    - average waiting time은 좀더 길어질 수 있다. (SJF와 섞어서 쓰면 더 좋은 효율이 날 것. 어쨌든 RR은 무조건 쓰인다)
- RR 스케쥴링은 preemptive하다.
  - 만약에 프로세스의 burst 타임이 time 퀀텀보다 크다면 쫓겨나고 레디큐의 마지막으로 들어가므로.

#### Time quantum

- Time Slice를 프로세스의 평균 수행시간보다 짧게 잡으면 빈번한 Context Switch로 오버헤드 증가한다.
- Time Slice를 너무 크게 잡으면, FCFS와 다름 없어진다.

<br>
<br>

### The performance of the RR scheduling algorithm

- 결국 RR 스케쥴링의 performance는 time quantum의 size에 따라 크게 달라진다.

![](https://i.imgur.com/wLirFVD.png)

타임 퀀텀을 어떻게 주느냐에 따라 os의 성능이 크게 달라진다.

- 타임퀀텀이 무한대인게 FCFS. 타임퀀텀을 너무 작게 주어버리면 계속 쫓겨나기를 반복할 것.
- turnaround 타임도 마찬가지이다. 너무 적게 줘도 문제 너무 많이 줘도 문제.

![](https://i.imgur.com/JmplvUZ.png)

<br>
<br>

# Priority-base Scheduling

우선순위를 줘보기!

- 우선순위를 프로세스에 associate한 뒤에, 가장 높은 우선순위를 가진 프로세스를 할당.
- 우선순위가 모두 같은 경우는 FCFS.
- SJF는 Priority-based scheduling의 특별한 한 형태이다. 이 경우 우선순위는 next-CPU burst의 역인 것.

(책에서는 숫자가 작을수록 높은 priority로 가정 할 것. 자유)

![](https://i.imgur.com/0rNh0Yh.png)

- preemtive / non-preempitve의 문제가 있다.

### Starvation 문제 (indefinite blocking)

- a blocked process : ready to run, but waiting for the CPU
- 낮은 순위를 가진 어떤 프로세스는 어쩌면 영원히 기다려야 할수도 있다.

### starvation 문제를 해결하는 방법은 - aging

- 어떤 프로세스들이 오랜시간 대기하고 있으면 priority를 점점 높여주는 것

**→ 즉 priority 스케쥴링 방식은 항상 starvation 문제를 내포하기 때문에 aging과 같은 방식을 사용해야 한다.**

<br>
<br>

### 일반적으로 RR와 Priority 스케쥴링을 섞어서 사용한다.

- 우선순위가 높은 프로세스를 먼저 사용하되,
- 만약 우선순위가 같다면 RR으로
  ![](https://i.imgur.com/Cw98CEF.png)

<br>
<br>

## Multi-Level Queue(MLQ) 스케쥴링

- 실전 OS 형태
- ![](https://i.imgur.com/HtOtPwt.png)
- 우선순위를 여러개 배정해줘서 각각에 레디큐를 따로 주는 것.

![](https://i.imgur.com/LsTPVg3.png)

- 우선순위가 가장 높은것만 계속 실행하다보면 문제가 생각할 수 있음. 이는 aging과 비슷하게 해결.

![](https://i.imgur.com/SaDK6h3.png)

- 이렇게 점점점 많은 CPU burst time을 할당받기 때문에 CPU를 많이 받는 프로세스는 더 많이 할당받고, 적게 받는 프로세스는 적게 받으므로 더 자주 받을 수 있는 것.

<br>
<br>

## On most modern operating systems

- 현대적 프로세스 스케쥴링 안하고 실제로는 쓰레드 스케쥴링을 하는데 어려우니까 프로세스로 공부했다고 생각하시고

  - 운영체제는 kernal threads 만 스케쥴링함.
  - user threads는 thread library에 의해 관리된다. - User level threads는 응용 프로그램과 Link/Load가 되는 라이브러리로 구현된다. 이 라이브러리 안에 동기화, 스케쥴링 기능이 포함되어 있다. 커널에서는 아무런 지원을 해주지 않으며, 커널이 보기에 user thread는 단지 single process에 불과하다. - 그래서 커널은 유저 스레드에 대해 모른다. - 커널 스레드와 유저 서비스와 매핑만 해주면 됨.
    **→ OS 커널은 cpu scheduling을 kernel thread를 대상으로 한다는 것만 알아두자**

https://genesis8.tistory.com/242

### Real-time OS에서의 스케쥴링은 또 다르다.

- 실시간 ? : 주어진 시간내에 어떤 task를 완료할 수 있을 때
- soft realtime vs hard realtime
  - soft - 크리티컬한 프로세스가 더 빨리 실행되도록 보장하는 경우
  - hard - 어떤 task가 반드시 데드라인 안에 실행되는 경우.
- priority를 가져야 할 것.

<br>
<br>

# 인터럽트

##### < 인터럽트 우선순위 >

- 외부 인터럽트

  - 정전•전원이상 인터럽트 : 정전 또는 전원공급의 이상으로 인한 인터럽트
  - 기계고장 인터럽트 : CPU 및 기타 하드웨어의 오류로 인한 인터럽트
  - 외부 인터럽트 : Timer 나 Operator 로 인한 인터럽트
  - 입출력 인터럽트 : 입출력의 종료나 입출력의 오류로 인한 인터럽트

- 내부 인터럽트 - CPU 코어 외부에서 인터럽트를 거는 경우가 일반적이지만, CPU 내부에서 실행하면서 인터럽트에 걸리는 경우
  프로그램 검사 인터럽트 : Divide by Zero , Overflow/underflow 등

- 소프트웨어 인터럽트
  - 사용자가 프로그램을 실행시키거나 Supervisor(=OS)를 호출하는 동작을 수행하는 경우

> 인터럽트 우선순위
> `정전•전원이상 인터럽트 > 기계고장 인터럽트 > 외부 인터럽트 > 입출력 인터럽트 > 프로그램 검사 인터럽트 > SVC(SuperVisor Call)`
