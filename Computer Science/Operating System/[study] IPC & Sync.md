# IPC, 동기화(뮤텍스, 세마포어, 데드락, 레이스컨디션)


## Intro

프로세스는 독립적인 실행 객체이다.

객체라 불리는 이유는, 디스크에 실행 파일로 존재하는 프로그램을 더블 클릭하면 하나가 실행되고, 다시 더블 클릭하면 총 두 개가 실행되는 것처럼 프로그램의 인스턴스(객체)처럼 동작하기 때문이다. 서로 독립적인 프로세스는 다른 프로세스에게 영향을 받지 않는다. 그러나 독립되어 있기 때문에 서로 간의 통신이 어렵다는 문제가 있다. 이것을 해결하기 위해 Kernel 영역에서 IPC라는 것을 제공하게 되었고, 프로세스는 Kernel이 제공하는 IPC를 이용해서 프로세스간 통신을 할 수 있다.

<br>
<br>


# IPC(Inter Process Communication)
- 프로세스는 독립적인 경우도 있지만, 협력할 때도 있다. 협력하는 경우 IPC를 사용하게 된다.
- IPC는 크게 대표적으로 두 가지 방식로 나눌 수 있다. Shared memory 모델과 Message Queue모델이 있다.

1. **shared memory**
    - shared memory는 두 개 이상의 프로세스가 physical memory 공간을 공유함으로써 통신하는 방식이다.
    - Thread는 데이터 영역을 공유하므로 Thread간의 통신은 동기화만 빼면 비교적 자유롭다. 그러나 프로세스들은 별도의 독립적인 데이터 영역을 가지기 때문에 변수 차원의 공유를 하려면 physical memory에 공간을 마련해야된다.
    - physical memory에 두 개 이상의 프로세스가 접근하지 못하도록 semaphore와 같은 상호배제 도구를 사용해야 한다.
    - 예시로 POSIX shared memory
2. **message queue**
    - 예시로 pipe 나아가 socket이 있다.

> Shared Memory 방식은 하나의 파일을 read/write 하는 것
> Message Queue 방식은 프로세스 간 통로? 혹은 제3자가 개입하는 것..

<br>
<br>


### Examples of IPC Systems
실제로 IPC를 어떻게 사용하는지 알아보자. (+ RPC)
![](https://i.imgur.com/nLFIZ3x.png)
- Shared Memory : POSIX Shared Memory
    - POSIX는 리눅스에 기반한 운영체제 표준
    - POSIX는 unix가 표준이 없이 난립하자, OS를 표준화한 것.(구현한게 아니라 인터페이스)
    - POSIX shared memory
        - 메모리 mapped-file을 사용한다.(프로세스끼리 공유할 파일을 메모리에 직접 생성하는데, 이 파일을 mapped-file이라고 한다.)
        - 우리가 파일을 오픈한다고 하면, 보통 파일은 하드디스크의 스토리지 스토리지 시스템(HDD)의 영역을 잡는다.
        - 그런데 메모리에 파일을 생성하면? 매우 빠를 것이다. 그래서 memory mapped-file을 사용할 수 있다.

<br>
<br>

#### Message Passing : Pipes
- 전통적으로 UNIX에서는 Pipes를 사용함.
- pipe는 두개의 프로세스가 커뮤니케이션 하는 일종의 도구이다.
    - unidirectional (단방향)/ bidirectional (양방향)
    - bidirectional한 경우, half-duplex인가 full-duplex인가?
    - 커뮤니케이팅하는 프로세스 간의 relationship이 존재하는가?
        - like 부모와 자식
    - 파이프가 네트워크를 통해서 갈 수 있는가?
- 크게 두 개의 파이프 타입이 존재한다.
    - **Ordinary pipes (이것만 다룰 것)**
        - 전형적으로, parent 프로세스가 child 프로세스와 커뮤니케이트 하기 위해 pipe를 생성한 형태.
    - **Named pipes:**
        - 파이프에 이름을 붙여준다.
        - parent-child relationship이 없어도 된다. 좀더 고도화된 상태
- Direct address: node Id, process Id
- Indirect address: mailbox, socket, channel, …

#### Pipe
- Pipe는 두 개의 프로세스를 연결하는 통로가 된다.
- Pipe는 Circular Queue로 구성되어 있다.
- 하나의 프로세스는 읽기만, 다른 하나의 프로세스는 쓰기만 가능하다.
- 한쪽 방향으로만 통신이 가능하기 때문에 반 이중 통신이라고 불린다. 따라서 양방향 통신을 하려면 두개의 Pipe를 만들어야 한다.
- Pipe의 Mutual Exclusion은 Kernel이 알아서 해준다.
- 빈 파이프의 읽기 시도는 reader를 blocked 상태로 만든다. 꽉 찬 파이프의 쓰기 시도는 writer를 blocked 상태로 만든다.
- writer가 pipe를 close해야 reader가 wake-up 된다.(ready 상태가 된다.)


<br>
<br>

### Ordinary pipes
![](https://i.imgur.com/fInTEYm.png)


두개의 파이프가 필요할 것 (가는것, 오는것)

- 두개의 프로세스가 producer-consumer 패션으로 커뮤니케이션한다.
    - producer는 write, consumer는 read
- 오직 one-way커뮤니케이션이 가능한 파이프(unidirectional) 두개를 사용해서 two-way 커뮤니케이션을 할 수 있다.

UNIX 시스템에는, 파이프라는 개념이 있다. 하나는 read end로, 하나는 write end로 생성해서 리턴해준다.
![](https://i.imgur.com/SBRNJmh.png)
![](https://i.imgur.com/a9CosBz.png)


<br>
<br>


### 파이프 모델이 fork와 어떻게 연결될까?

- fork()를 하는 순간 parent 프로세스가 돌고, child 프로세스가 concurrent하게 돌 것.
- 이때 pipe(fd)를 통해 두개의 파이프가 생성됨 → parent가 write를 하면 child가 read를 통해 받을 수 있음! 

<br>
<br>

## **Sockets**
> Socket은 Message Passing 모델의 일종이라고 볼 수 있다.

- 위의 것은 옛날 이야기. 현대에서 하나의 컴퓨터 안에서의 프로세스간의 통신 뿐 아니라, 서로 다른 컴퓨터의 프로세스간의 통신을 고려해야 할 것이다.
- 요즘에는 internet에 연결된 networked 컴퓨터만 사용하므로 다른 컴퓨터와 통신할 필요가 있다.
- a컴퓨터의 프로세스와 b컴퓨터의 프로세스가 통신하려면 어떻게 해야할까?
    - 서로를 어떻게 특정할까? → IP address
    - 이 둘을 연결하는 Pipe는 어떻게 특징하나? → port
    -> 이 IP와 port를 묶으면 소켓. 
- 커뮤니케이션을 위한 두개의 원격지를 잇는 파이프 형태의 커넥션을 의미하는 것.

![](https://i.imgur.com/LiljvCD.png)

- 이처럼 IP주소와 포트를 통해 서로를 특정할 수 있다. 이렇게 맺어진 소켓 커넥션으로 웹서버와 브라우저가 자원을 주고받는 것.
- 정리하면, 소켓은 일종의 파이프인데, IP 주소와 port로 바인딩되면 그것을 소켓이라고 한다!

<br>
<br>
<br>


---

# 동기화 (뮤텍스, 세마포어, 데드락, 레이스컨디션)

## Concurrent Programming의 문제점과 해결책

### Race Condition
- 협력하는 프로세스, 스레드 사이에서 실행 순서 규칙을 정하지 않으면 공유 자원의 일관성이 깨지게 된다.
- 즉, 병렬 프로그래밍에서 동기화가 없으면 Race Condition이 발생한다.
- Race Condition의 결과는, 병렬 프로그래밍에서 항상 똑같은 답을 반환해야 하는데, 매번 다른 결과를 반환하는 것이다.

#### 해결책
그에 대한 해결책으로 **상호 배제(Mutual Exclusion)**와 동기화가 있다.

- 프로세스 간 동기화 방식은 Semaphore, 스레드 간 동기화 방식은 Mutex (+ Condition) 등이 있다.
- 상호 배제는 임계구역의 접근할 수 있는 주체들의 갯수를 제한하는 것인데, 이 때 프로그래밍의 효율성을 위해 임계구역을 최대한 짧게 잡아야 한다.

<br>
<br>

#### Mutual Exclusion 설계 조건
1. mutex가 모두를 배제시켜선 안됨 = progress가 있어야 함
2. 한 스레드가 불공평하게 계속 연기되는 것을 막아야 함 (Bounded Waiting) -> Starvation과 Deadlock에 대한 대응이 되어 있어야 한다.
3. 퍼포먼스를 위해 critical section 진입과 종료부분은 짧아야 한다.


<br>
<br>

#### 상호배제 도구
1. lock
2. semaphore
3. monitor (S/W & H/W)
4. message



### Critical Section
두 개 이상의 스레드가 공유자원에 병행으로 접근하는 코드 부분을 의미한다. 공유자원에 동기화 없이 접근하면 레이스 컨디션이 발생한다. 해결책은 상호배제다.


<br>

### Semaphore (Process 동기화)
-  critical section 문제를 해결하기 위한 추상 자료형. 정수값 S을 가지고 P, V의 Atomic 연산을 할 수 있다. P는 critical section에 들어가기 전에 수행되고 V는 나올 때 수행된다.
- semaphore는 서로 다른 여러개 프로세스 동기화 처리를 위해 사용된다.
- semaphore는 signal mechanishm이다.
- 세마포어 동작을 위한 전역변수가 필요하다. 그 변수의 값으로 Critical Section에 누가 들어가 있는지를 판단한다.
    - Binary Semaphore : 세마포어 변수가 갖는 값이 0과 1이다. 값이 0이면 Critical Section에 아무 것도 없으므로 진입이 가능하고, 1이면 Blocked 된다. Critical Section에 들어가 있는 프로세스는, 임계구역을 나오면서, CS 진입 대기중인 프로세스를 Wake-up 한다. (= mutex ?)
    - Counting Semaphore : 세마포어 변수가 n의 값을 가지고, 임계구역에 프로세스가 들어갈 때 마다 -1을 한다. 즉, 여러개의 프로세스가 임계구역에서 활동이 가능하다.

![](https://i.imgur.com/tI4rdHF.png)
- Critical Section에 진입을 시도하지만(acquire), 이미 다른 프로세스가 존재한다면, 진입을 시도한 프로세스는 waiting 상태로 바뀐다.(blocked 상태 즉, busy waiting이 아님) 그래서, 이 임계구역 진입을 위해 대기하는 프로세스들을 세마포어의 대기큐(사진 상의 빨간 큐)에 넣어줘야 한다.

> 세마포어 변수 또한 임계구역이다.
> 근데 이 세마포어 변수는 커널이 관리해줌 v(^^)v

https://velog.io/@codemcd/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9COS-8.-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EB%8F%99%EA%B8%B0%ED%99%94-1#31-bank-account-problem%EC%9D%80%ED%96%89-%EA%B3%84%EC%A2%8C-%EB%AC%B8%EC%A0%9C

<br>
<br>


### Mutex (Thread 동기화) 
- mutex는 하나의 프로세스에서 여러개 스레드 동기화를 위해 사용된다.
- mutex는 locking mechanism이다. 즉 mutual exclusion을 위한 것으로서 lock의 owner가 존재한다.
- Process는 Code, Data, Stack, Heap 구조로 메모리를 할당 받는다. 기본적으로 프로세스는 최소 1개의 스레드(메인 스레드)를 갖는다.
- 메인 스레드 이외의 스레드는, Stack 만을 따로 할당 받고 Code와 Data, Heap 영역은 스레드 간 공유가 일어난다. 따라서, 두 개 이상의 스레드가 공유자원(Critical Section)에 동시에 접근하는 것을 막아야한다. 그 해결책이 상호배제(Mutual Exclusion)이다.

https://worthpreading.tistory.com/90

#### Mutex 동작
1. Mutex 전역변수를 생성
2. Thread들이 mutex에 대해 lock을 시도한다.(소유하려고 함)
3. lock 시도는 하나의 Thread만 성공을 하고, 성공한 Thread는 mutex를 소유하게 된다.
4. mutex를 소유하게 된 Thread는 Critical Section에서 작업을 수행한다.
5. 작업이 모두 끝나면, mutex를 unlock한다.
6. 대기하던 다른 Thread가 mutex를 lock하려 한다.
7. 대기중이던 Thread는 blocked 상태


#### Mutex + Condition
- Condition(조건 변수) 또한 스레드 간 동기화 도구로 mutex와 연계하여 쓰인다. 둘을 연계해서 좀 더 안전하게 동기화가 가능하다.
- mutex만 사용하면, 버퍼를 사이에 두고 읽고 쓰는데 문제가 발생할 수 있다. 이것을 간단하게 해결해주는 것이 condition이다.


#### 세마포어와 뮤텍스의 차이점?
```
세마포어는 공유 자원에 세마포어의 변수만큼의 프로세스(또는 쓰레드)가 접근할 수 있습니다.
반면에 뮤텍스는 오직 1개만의 프로세스(또는 쓰레드)만 접근할 수 있습니다.

현재 수행중인 프로세스가 아닌 다른 프로세스가 세마포어를 해제할 수 있습니다.
하지만 뮤텍스는 락(lock)을 획득한 프로세스가 반드시 그 락을 해제해야 합니다.
```


### Dead lock
- 교착상태는 상호 배제(Mutual Exclusion)에 의해 나타나는 문제점으로, 협력하는 스레드나 프로세스가 상호 배제해야 하는 자원을 각각 들고 있고, 서로의 자원을 요구하는 상황에서 발생한다.

1. Process A는 임계구역 1번을 수행하고, Process B는 임계구역 2번을 수행하고 있다.
2. Process A는 작업을 마치고 임계구역 2번으로 향하려 하고, Process B는 작업을 마치고 임계구역 1번으로 향하려 한다.
3. 그러나 두 프로세스가 향하려는 임계구역이 모두 점유된 상태이기 때문에 Blocked 상태로 무기한 대기하게 된다. 이렇게 무기한으로 대기하는 상태를 교착상태라고 한다.

#### 교착상태는 아래 4개의 조건을 모두 만족하는 경우에만 발생한다.
1. 상호배제: 한 번에 한개의프로세스만 공유자원에 접근해야 한다.
2. 점유와 대기: 최소한 하나의 자원을 점유하고 있으면서, 다른 프로세스에 의해 점유된 자원을 추가로 얻기 위해 대기하고 있어야 한다.
3. 비선점: 자원을 강제로 뺏을 수 없고 자발적으로 반납해야 한다. 
4. 순환대기: 각 프로세스가 꼬리를 물며 자원을 점유하고 있어야 한다.

#### 해결책
1. 예방과 회피 방식 교착 상태의 필요충분조건 4가지 중, 적어도 하나는 만족 못하도록 보장하는 방법이다. 그러나 이 방식은 자원의 이용률과 시스템 이용률이 감소할 수 밖에 없다는 것이다.
2. 교착상태를 허용하고 회복하는 방식
3. 교착상태를 무시하고 발생하지 않은 것처럼 동작하기





### Semaphore 
    - semaphore는 프로세스 간 동기화를 위한 도구이자, IPC로 분류된다. 동기화를 위한 도구지만, 프로세스 간 통신이 발생 했을 때를 전제로 사용하는 것이므로, Semaphore를 IPC로 분류한다.
    - 다른 IPC 방식들은 프로세스간 메시지 전송을 목적으로 하는데 반해, Semaphore는 프로세스 간 데이터를 동기화 하고 보호하는데 그 목적을 둔다.
    - 프로세스간 메시지 전송을 하거나, 혹은 Shared Memory를 통해서 특정 데이터를 공유하게 될 경우 공유된 자원에 여러개의 프로세스가 동시에 접근을 막는 것이 Semaphore다.

