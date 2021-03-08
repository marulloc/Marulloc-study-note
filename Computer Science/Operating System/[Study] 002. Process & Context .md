# 프로세스 상태 변이

![](https://camo.githubusercontent.com/0a17a2b39898ede5cbc8c2c7e09a971e81b9e08ca952d891351a1542819f6b1d/68747470733a2f2f7777772e63732e7569632e6564752f7e6a62656c6c2f436f757273654e6f7465732f4f7065726174696e6753797374656d732f696d616765732f43686170746572332f335f30325f50726f6365737353746174652e6a7067)

![](https://camo.githubusercontent.com/ea08a2f6e21144b9bc6a72c25000642c6c1406eccb40978425fb0c7a98bbbdb3/68747470733a2f2f696d67312e6461756d63646e2e6e65742f7468756d622f5237323078302e7138302f3f73636f64653d6d746973746f72793226666e616d653d687474702533412532462532466366696c6532382e75662e746973746f72792e636f6d253246696d61676525324631323630393935303530453138433843323443303334)

- 처음에는 NEW 상태.(하드디스크 -> 메모리에 적재되기 직전까지의 단계)
- 초기화가 끝나고 CPU에 점유되기 위해 READY 상태가 됨. (레디 큐에 PCB가 들어감)
- 운영체제가 CPU를 이 프로세스에게 주면 RUNNING상태가 됨.

  - RUNNING -> READY
    - Interrupt가 발생하면, (time burst 또는 정전 등의 이벤트) 커널프로세스에게 cpu를 주기위해, 기존에 cpu를 점유하고 있던 프로세스는 레디 큐로 빠짐 (CPU가 요청해서 READY상태가 된 것이 아니기 때문에, 비자발적인 CONTEXT SWITCH라고도 한다.)
  - RUNNING -> WAITING(BLOCKED)

    - I/O를 포함한 이벤트를 요청하고 완료되기를 기다리는 상태(웨이팅 큐에 PCB가 들어감)(자발적인 CONTEXT SWITCH)

  - WAITING(BLOCKED) -> READY

    - I/O가 끝나면 다시 READY 큐로 되돌아감.

  - READY -> RUNNING
    - os가 CPU를 주면 (**scheduler dispatch**) running하게 됨.
  - RUNNING -> TERMINATED
    - running하다가 exit()나 return과 같이 명시적으로 끝나는 명령어를 받으면 terminated.
  - READY / WAITING(BLOCKED) -> SUSPENDED
    - 메모리 부족으로 인한 swap out과 같은 외부적인 이유로 프로세스의 수행 정지된 상태
      > ready상태나 waiting 상태의 페이지? 프로세스? 들도 swap out될 수 있다.
      > 🤔 아마..  
      > 공간적 지역성: 프로세스가 프로그램/데이터의 특정 영역을 집중적으로 참조하는 현상. 참조한 영역과 인접한 영역을 참조.
      > 시간적 지역성(Temporal locality) :한번 참조한 영역을 곧 다시 참조하는 특성
      > 요론 페이지들이 swap out되는 것이 아닐까..

🤔 interrupt 우선순위
🤔 자발적/비자발적 컨텍스트 스위칭

<br>
<br>
<br>

# PCB (Process Control Block)

![](https://i.imgur.com/yXcvxcP.png)

- Sleep Queue, Scheduling Queue에 프로세스 그 자체가 들어가는 것은 아니다. PCB라는 것이 Queue의 노드가 된다.
- PCB는 커널이 프로세스 관리를 위해, 프로세스에 대한 중요정보를 저장해 둔 것이다. (프로세스의 메타데이터)
- 따라서, 프로세스는 각각의 PCB를 갖게된다. 즉, 메모리에 로드되면, 커널은 프로세스의 PCB를 만들어 따로 저장하고 사용한다.
- PCB가 프로세스의 중요한 정보를 포함하고 있기 때문에, 일반 사용자가 접근하지 못하도록 보호된 메모리 영역 안에 남는다. 일부 운영 체제에서 PCB는 커널 스택의 처음에 위치한다.
  - Process state : 프로세스의 상태 ex.new/running/waiting
  - Program counter : 메모리에 있는 명령어를 fetching하는데 어디에있는 메모리를 가져와야 하는가? PC에 있는 메모리를 fetch해오는 것.
    - ex PC에 0xFFFE라는 주소가 있으면 메모리에서 해당 주소에 있는 명령어를 fetch.
  - CPU registers : IR, DR 등을 포함. PC도 일종의 CPU register. 일종의 문맥(context)
  - CPU-scheduling information : CPU를 주고받기 위해 필요한 스케쥴링 정보들
  - Memory-management information : 메모리 관련 정보들
  - Accounting information : 계정 정보들. 어떤 유저인가?
  - I/O status information : 어떤 자원을 오픈해서 lock을 걸었는지 등

### 참고 - TCB(Thread Control Block)

-> PCB는 Process ID와 상태, 우선순위, 메모리 정보 등을 저장한다
-> TCB는 Thread별로 존재하는 자료구조이며, PC와 Register Set(CPU 정보), 그리고 PCB를 가리키는 포인터를 가진다.
![](https://i.imgur.com/JHfNMHP.jpg)

> 🤔 위 사진대로라면... TCB가 Queue에 들어가는 것..
> 🤔 쓰레드가 코드는 공유하더라도, 실행하는 코드 라인이나, 사용하는 변수 값이 다르겠지.. 그래서 실제 CPU에 패치되는 코드는 PCB를 보고 확인할지라도 레지스터값은 각각의 TCB를 보는게 아닐까..

<br>
<br>
<br>

# 컨텍스트 스위치

![](https://i.imgur.com/StpUuUy.png)

- Context란?
  - 프로세스가 사용되고 있는 상태이며, 이는 PCB에 저장된다.
- CPU를 사용하는 프로세스는 계속 바뀐다.중간까지만 수행되고 Time slice로 만료되는 것들도 있고 Interrupt로 Blocked 상태가 되어, Sleep Queue로 빠지는 프로세스도 있다.
- 중간에 멈췄던 프로세스가 다시 CPU를 잡았을 때, 처음부터 실행하지 않기 위하여 PCB에 PC(Program Counter)와 레지스터 값들을 저장한다.
- 이렇게 CPU의 주인을 바꾸는 것을 Context Switch라 한다.
- 컨텍스트 스위치의 순서는 이렇다.
  1. 프로세스가 실행 중에 Interrupt 등이 발생하여, CPU를 Release 해야하는 상황이 발생한다.
  2. Kernel은 현재 프로세스가 진행해왔던 것들을, 프로세스의 PCB에 저장한다.
  3. 현재 수행중이던 프로세스가 CPU를 반납한다.
  4. 새로운 프로세스가 CPU를 할당 받는다.
  5. 새로운 프로세스의 PCB를 보고, CPU 레지스터와 PC값을 갱신한다.
  6. Time Slice가 끝나거나, Interrupt가 발생하기 전까지 프로세스를 동작한다.

즉 Context Switch이라는 것은 어떤 task가 CPU 코어를 다른 프로세스에게 넘겨주었을때 현재 프로세스의 현재 상태를 저장하고, 새로 획득한 프로세스의 문맥을 복원하는 것.

### 커널/유저모드와 컨텍스트 스위치

- user mode → kernel mode로 바뀌는 것은 context switch가 아님 (이 경우도 CPU 수행 정보를 PCB에 저장하게 되지만 context swtich보다는 오버헤드가 적다)

> Kernel mode execution의 주체는 누구일까?
> OS의 특정 Process? User Process?
> 정답은 User Process이다! Process가 권한을 가지고 직접 실행시킨다.

- kernel 이 메모리에 상주하는데, 이거를 커널 프로세스
- 인터럽트 핸들링 이런거 cpu가 독자적으로 하는게 아니라, 커널 프로세스가 cpu 점유하고 인터럽트 핸들링을 하는 것
- 그래서.. system call이 발생하면 커널에 있는 함수를 쓴다는 것
- 즉, 커널 프로세스 안에 있는 함수를 쓴다는 것인데.. 이때 일반적인 process에서 커널 프로세스로 컨텍스트 스위칭이 일어나는 것이 아닌가????

출처: https://sanghyunj.tistory.com/15 [sanghyunJ ]
