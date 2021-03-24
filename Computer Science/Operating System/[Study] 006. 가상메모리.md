# 가상 메모리

https://velog.io/@codemcd/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9COS-15.-%EA%B0%80%EC%83%81%EB%A9%94%EB%AA%A8%EB%A6%AC

## Logical address, 가상메모리가 필요한 이유

Real Memory System에선 CPU 발생시키는 논리주소(Logical address)와 메모리가 실제로 취급하는 실제주소(Physical Address)가 동일하다. 프로세스가 메인 메모리로 로드될 때 연속적으로 연결되어 로드되어야 한다.

소프트웨어 발전에 따라, 소프트웨어 크기가 커졌고 큰 용량의 소프트웨어를 메모리에 한 번에 올리는 것은 자원의 낭비가 심했다(사용되지 않는 데이터 영역이 많음). 따라서 가상메모리를 도입하게 됨.

<br>
<br>

## 가상메모리란?

가상 메모리는 메모리를 관리하는 방법의 하나로, 각 프로그램에 실제 메모리 주소가 아닌 가상의 메모리 주소를 주는 방식을 말한다. 이러한 방식은 멀티태스킹 운영 체제에서 흔히 사용되며, 실제 주기억장치(RAM)보다 큰 메모리 영역을 제공하는 방법으로 사용된다.
프로그램이 실행되기 위해 그 프로세스의 주소 공간 전체가 메모리에 올라와 있어야 하는 것은 아니다. 메모리의 연장 공간으로 디스크의 스왑 영역이 사용될 수 있기 때문에 프로그램 입장에서는 물리적 메모리 크기에 대한 제약을 생각할 필요가 없어진다.

- 프로세스마다 독립적으로 가지는 주소 공간으로 0에서부터 시작한다.
- CPU가 물리적 주소로 접근하기 위해 사용하는 참조하는 주소
- MMU(Memory-Management Unit)와 같은 하드웨어 장치를 통해 논리적 주소를 물리적 주소로 변환할 수 있다. (주소 바인딩)

<br>
<br>

## Virtual memory VS Real Memory System

- RM와 달리, VM은 논리주소와 실제주소가 동일하지 않다.
  - CPU는 명령어를 FETCH하기 위해(메모리에 접근하기 위해) 지속적으로 논리주소를 발생시킨다. 그러나 논리주소와 실제주소가 다르기 때문에 논리주소를 실제주소로 변환하는 작업을 필요로한다. 이 작업은 MMU가 해준다.
- RM은 프로세스가 로드될 때 연속적으로 이뤄져야하지만, VM은 프로그램이 PAGE단위로 분할되어 메모리에 분산 로드된다.(Scattered loading)
- RM에선 프로그램이 실행되려면, 프로그램 전체가 메모리에 로드되어야 했지만, VM에선 CPU에서 사용할 부분만 로드되어도 프로그램 실행이 가능하다.(Partial loading)
- 분할 로드되어 실행될 때, cpu가 필요한 page만 로드한다.(Demand paging)

<br>
<br>

### Logical vs Physical Address

- Logical 주소
  - 유저 프로세스에서 access하려는 주소. CPU에 의해 생성된 주소
  - 이를 실제 하드웨어에서 사용하는 pysical 주소와 매핑하는 과정이 필요하다.
- Physical 주소
  - an address seen by the memory unit
  - that is, the one loaded into the memory-address register
  - 메모리 어드레스를 가지고 특정 레지스터에 매핑해주어야 한다.

<br>
<br>

# Paging Policy

1. Fetch Policy : 디스크에서 메모리로 프로세스를 언제 가져와야 할지를 정하는 것.
2. Placement Policy : 디스크에서 메모리로 가져온 프로세스를 어느 위치에 저장 할 것인지 정하는 것.
3. Replace Policy : 메모리가 충분하지 않을 때 현재 메모리에 적재된 프로세스 중 제거할 프로세스를 결정하는 방법

- Paging System에서 프로세스의 페이지 구분
  - 파일 시스템에 원본이 존재하는 (text/data 부분의 초기화가 된 전역변수들) 관련 page를 File Backed page라고 부른다.
    - 원본이 존재하기 때문에, 교체될 때 바로 메모리에서 삭제한다.
    - 만약 data page가 dirty하면(변경이 발생했다면) anon page로 분류하여 아래와 같이 처리한다.
  - 프로세스 수행시 생기는 부분이라 파일로 쫒아낼 수 없는(원본이 없는 = anon page)를 Swap-backed Page라고 부른다
    - 이 페이지들이 쫒겨나야 될때는 디스크의 Swap Space로 쫒겨나게 된다.(heap/stack/data 부분의 초기화 안된 전역변수)

즉, 대부분 한 프로세스는 디스크/메인메모리/Swap Space 세 부분에 분할되어 존재한다.

# Fetch Policy

필요한 page를 불러올 때, MMU가 페이지 테이블로 접근하여 page가 메모리에 존재하는지 판단한다. 이때 테이블 엔트리의 valid bit가 0이면 **page fault**가 발생하고, handler에 의해 원하는 page를 가져오게 된다. 이 일련의 과정을 Demand paging이라 한다.

- demand paging에 의해, 쓰지 않는 페이지는 절대 메모리에 올라오지 않는다.

### page fault

valid bit이 0일 때, MMU가 CPU에게 보내는 Interrupt다.

1. page fault가 발생하면, CPU는 fault handler
2. DISK I/O를 하기 전, handler는 page cache를 뒤져서 해당 페이지가 있는지 확인한다.
3. page cache에 page가 없으면, fault handler가 DISK I/O를 시작하고 현재 프로세스는 Blocked가 되어, CPU는 다른 프로세스에게 할당된다.

- **page cache** - S/W로 구현한 cache
  - OS의 역사는 디스크의 속도와 CPU 속도의 간극을 줄여가는 역사다.
  - s/w cache란 I/O의 기계적 부분의 느린 속도를 보완하기 위해, 디스크에서 자주 쓰이는 데이터를 메모리로 caching 하는 것이다.
  - 디스크에서 4KB를 읽어오면, 우선적으로 사용하는 부분은 일부분이다. 안쓴 데이터는 메모리에 KEEP해둔다.(다른 프로세스가 사용할 수 있으니까)
  - 메모리에서 갱신된 데이터를 바로 디스크에 가서 갱신하지는 않는다.(퍼포먼스 하락할 가능성이 크기 때문이다. 따라서 DIRTY BIT을 사용)
  - delayed write들은 "sync" 명령어가 들어오면 dirty bit를 참고하여 디스크에 주기적으로 갱신한다.

#### **Clock Interrupt Handler**

- clock interrupt는 대부분 1/1000 초 마다 발생한다.(클락틱마다 발생하는 인터럽트)
- clock interrupt는 정전/기계 오류/malfunction이 아니면 최우선 순위를 가지는 interrupt다.
- clock interrupt handler가 하는일
  - clock interrupt를 통해 system time(실제 시간이 아니라, 부팅된 이후로 tick 얼마나 진행되었나를 카운트 함)을 유지한다.
  - sleep/alarm의 system call에 대한 시간을 측정하고 서비스한다.
  - 주기적으로 처리할 일들을 수행한다.
    1. Timeout Function : 커널 함수를 주기적으로 호출
    2. 커널 프로세스를 주기적으로 wake up 한다.
       - 커널 프로세스 : 클락 틱 안에 핸들링 할 수 없는 기능들을 프로세스화 한 것으로 File Sync(디스크 갱신), Swapper(메모리 청소)등의 일을 하는 커널 프로세스가 존재한다.
- Time slice한 시간을 다 쓰면 reschduling을 하도록 cpu에게 "상기" 시킨다.
  - clock interrupt handler가 rescheduling을 하는 것이 아니기 때문에
  - Time Slice가 다 지나면, clock interrupt handler가 스케쥴러에게 Rescheduling을 invoke하고 핸들러는 끝난다.
  - invoked 된 스케쥴러는 context switch 진행

### pre-paging

- page fault가 발생해서 해당 page를 들고올 때, 순차적으로 연결된 page 몇개를 함께 들고 온다. 따라서 pre-paging의 동작으로 page fault를 줄이려면, 순차적인 코딩이 중요하다.

page fault는 매우 적은 확률로 발생해야 효율적이다. 그러면 현실적으로 페이지 부재는 어느정도로 발생할까? 이는 지역성의 원리(Locality of reference)로 인해 페이지 부재 확률은 매우 낮다. 지역성의 원리는 '메모리 접근은 시간적 지역성과 공간적 지역성을 가진다'는 의미이다.

- 시간적 지역성: CPU는 어느 메모리 공간을 읽은 후, 시간이 지나도 그 공간을 다시 읽을 확률이 매우 높다는 것을 말한다.
  - 대표적인 예로 반복문이 있다. 반복문은 하나의 코드 공간을 여러 번 읽는다.
- 공간적 지역성: CPU가 메모리 공간을 읽을 때는 인접한 범위 내에서 읽는다는 의미이다.
  - 프로그램은 대부분 절차적인 순서로 구현되어 있어 순서대로 읽는 경우가 빈번하다.

#### example 자세히.

1. MMU가 페이지 번호로 TLB를 check한다.
   - pte의 valid bit == 1 이면, 메모리 바로 접근
2. pte의 valid bit == 0 이면, **page fault** 발생하여 커널모드가 켜진다.
   - 주체가 MMU에서 Fault Handler로 바뀐다.
3. page cache에 해당 페이지가 있는지 확인하고, 있으면 바로 page를 로드??
   - pte를 업데이트 한다.(valid bit, frame number 등)
4. page cahce에 해당 페이지가 없으면 DISK I/O를 시작한다.
   1. 현재 프로세스가 Blocked 처리되고
   2. CPU를 release한다.
5. DISK I/O가 끝나면, pte를 업데이트 한다.(valid bit, frame number 등)
6. I/O가 끝난 프로세스는 대기큐에 들어가서 스케쥴 받기를 기다린다.
7. 스케쥴을 받으면 Page Fault가 발생한 부분부터 다시 코드를 실행한다.

## demanding paging

![](https://i.imgur.com/GPbnwJF.png)
현재 필요한(요구되어지는) 페이지만 메모리에 올리는 것을 Demanding Paging(요구 페이징) 이라고 한다.

## Prepaging

Prepaging은 pure demanding paging과 반대대는 개념이다. 프로그램을 실행할 때 필요할 것이라 판단되는 페이지를 미리 올리는 것이다. 이것의 장점은 page fault가 발생할 확률이 적으므로 속도면에서 빠르지만, 단점으로 미리 올라간 페이지를 사용하지 않는다면 메모리가 낭비된다.

## Page Replacement Algorithm

page fault 발생 시 비용이 큰 disk I/O가 발생하기 때문에 page fault를 방지하는 것이 중요하다. page replacement algorithm은 page fault가 발생했을때 메모리가 꽉 찬 경우 어떤 페이지을 내쫓을 것인지에 대한 것으로 page fault rate을 줄이도록 설계한다.

### LRU(Least Recently Used)

- 시간 지역성(최근에 참조된 페이지가 가까운 미래에 다시 참조될 가능성이 높은 성질)을 이용한 방법.
- 가장 오래 전에 참조된 페이지를 쫓아냄
- LRU는 근사 해를 구하므로 OPT보다는 page fault가 많이 발생하지만, FIFO보다는 일반적으로 적게 일어난다. 그러므로 현재 대부분 환경에서는 LRU를 사용하고 있다.

### LFU(Least Frequetly Used)

- 참조 횟수가 가장 적은 페이지를 쫓아냄
- 장기적인 관점에서의 참조 성향을 고려하지만 시간 지역성을 고려하지는 못함
  - ex) 예전에 많이 사용되었던 페이지가 더이상 사용되지 않음에도 교체 대상이 되지 않는 문제 발생할 수 있다

### Clock Algorithm

![](https://camo.githubusercontent.com/aae45e04326fc645bb0a723fd15e606963bd100a82500b7b9d9d03de8ef6b2ff/687474703a2f2f70616765732e63732e776973632e6564752f7e626172742f3533372f6c6563747572656e6f7465732f666967757265732f7332312e636c6f636b2e676966)

- LRU나 LFU 알고리즘은 페이지의 참조 순서나 참조 횟수를 (linked list나 heap과 같은 자료구조를 사용하여) 소프트웨어적으로 유지해야하는 오버헤드가 있다. 클락 알고리즘은 하드웨어적인 지원으로 LRU를 근사하여 최근에 참조되지 않은 페이지 중 하나를 교체하는 알고리즘으로 **Not Recently Used** 알고리즘으로도 불린다.
- 메모리 내의 페이지에 대한 참조 비트를 가지고 있고 이는 참조되었을 때 1로 설정되고 clock의 시곗바늘(iterator, handle)이 돌면서 0으로 설정한다. 시곗바늘이 가리키는 페이지의 참조 비트가 0일 경우 해당 페이지는 시곗바늘이 한 바퀴 도는 동안 참조되지 않은 페이지를 의미하므로 교체 대상이 된다.
  - 알고리즘 개선을 위해 modified_bit를 사용할 수 있다. modified_bit은 최근에 수정되었음을 의미하며 따라서 swap out될 때 변경 사항을 저장해야하므로 disk I/O가 발생한다. 따라서 modified_bit가 0인 페이지를 우선적으로 교체 대상으로 설정한다.

## Page Frame의 Allocation

프로그램마다 몇 개의 page frame을 할당할 것인지의 문제. 프로그램이 원활하게 실행되기 위해서는 page fault가 적게 발생해야 하며, 일정 수준 이상의 frame을 할당 받아야 한다.

- ex) code, data, stack 영역 동시에 접근, for문 순회할 때 for문 내의 코드 반복 접근
- Global replacement : 다른 프로세스에 할당된 frame 뺏어올 수 있음.
  - LRU, LFU 전체 페이지 대상으로
  - Working set, PFF 알고리즘
- Local replacement : 현재 수행중인 프로세스에게 할당된 frame 내에서만 replacement. 프로세스마다 페이지 프레임을 미리 할당하는 것을 전제로 함. - 프로세스별로 LRU, LFU 등의 알고리즘 독자적으로 운영 가능
  <br>

### Thrashing

![](https://camo.githubusercontent.com/f20829996c2494e914591c5f5ed9fadc22f30d71f7a136442c5838ce30de4c13/68747470733a2f2f696d67312e6461756d63646e2e6e65742f7468756d622f5238303078302f3f73636f64653d6d746973746f72793226666e616d653d687474707325334125324625324674312e6461756d63646e2e6e65742532466366696c65253246746973746f7279253246323632334234333635373539313744313144)

프로세스가 필요한 최소의 page frame을 할당받지 못한 경우 발생하는 문제

- page fault rate 증가
- cpu utilization 감소
  - page fault로 인한 disk I/O 빈번하게 발생 -> process block, context swtich 발생 -> OS가 프로세스를 실행하는 시간보다 page fault를 처리하는 오버헤드가 커지므로 cpu utilization은 감소한다.

<br>

### Working-set

![](https://camo.githubusercontent.com/8fa002216e42f6a5acb24e1c768d5bb7554ee8a8bc6ec496d35b4c1befa3b1ab/68747470733a2f2f6578616d72616461722e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031362f31302f4578616d706c652d342e362e706e67)

프로세스는 일정 시간동안 특정 주소 영역을 집중적으로 참조하는 경향이 있고 이렇게 집중적으로 참조되는 페이지들의 집합을 지역성 집합이라고 한다. 워킹셋 알고리즘은 이러한 지역성 집합이 메모리에 동시에 올라갈 수 있도록 하여 thrashing을 방지하는 알고리즘이다.

- 워킹셋 : 현재 시점에서 윈도우만큼의 시간 간격에서 참조된 페이지들의 집합
- 프로세스의 워킹셋을 구성하는 페이지들이 모두 메모리에 올라갈 수 있는 경우에만 할당
- 아닌 경우에는 할당된 페이지 프레임 모두 반환한다. 프로세스의 주소 공간 전체를 swap out(Suspended)

<br>

### Page Fault Frequency: PFF

페이지 부재의 비율은 프로세스에 할당된 프레임의 수에 반비례한다. 즉, 할당된 프레임의 수가 적을수록 페이지 부재 비율은 늘어난다.
![](https://camo.githubusercontent.com/345c89bbbf74e538fa320f2ec980824304b654f54ede5dfa7fd5fa7e041824a7/68747470733a2f2f6c68332e676f6f676c6575736572636f6e74656e742e636f6d2f70726f78792f444466534750794f566743364d76335a4a4f57582d4c6472706a376c6a647170527a47533176477038714c4c383267737531657371587233722d537969784c586155447869455a5a4a70384837775a7736456961325447434451785762565a7051364e57775937793267336158583374483669446e365434)

프로세스의 page fault frequency를 주기적으로 조사하고 이 값에 근거하여 각 프로세스에 할당할 프레임 수를 조절한다.

- page fault frequency > upper bound: 프로세스에 할당된 프레임 수가 부족하다고 판단 -> 페이지 프레임 할당량 증가
- page fault frequency < lower bound: 프로세스에게 필요 이상으로 많은 프레임이 할당된 것으로 판단 -> 페이지 할당량 감소
