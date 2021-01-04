# CPU Scheduling

CPU 스케쥴링 방식은 크게 두가지로 나뉜다.

1. 비선점 nonpreemtive
   프로세스 종료, I/O 이벤트 발생 전까지 현재 CPU를 잡고 있는 프로세스의 실행을 보장시켜주는 방식
2. 선점 preemtive
   OS가 로직에 따라, 임의 프로세스에 CPU를 할당해주는 방식, 즉 한 프로세스가 CPU를 선점할 수 있는 방식

#### 비선점 스케쥴링 방식의 종류

1. FCFS (First Come Frist Served)
   대기 큐에 도착한 순서대로 CPU가 할당된다.
   **실행 시간이 짧은 프로세스가 뒤에 오는 경우가 많아지면 평균 대기시간이 길어진다.**

2. SJF (Shortest Job First)
   수행시간이 가장 짧다고 판단되는 작업을 먼저 수행.
   **평균 대기시간이 줄어들고, 더 많은 프로세스를 완료시키려는 방식이라 생각하면 된다.**

#### 선점 스케쥴링 방식의 종류

1. Priority Scheduling (우선순위 스케쥴링)
   대기 큐에 있는 프로세스들에게 우선순위를 부여하고, 우선순위 순으로 CPU를 사용하게 된다.

   - 우선순위는 계속 변경되는데, 그에 따라 애초에 우선순위가 낮은 프로세스의 **기아 Starvation문제**가 발생할 수 있다.

2. RR (Round Robin)
   CPU 사용시간의 limit(Time slice)을 걸어두는 로직으로 모든 프로세스가 Time slice만큼의 CPU 사용시간을 보장받게 된다.
   - **Time Slice를 프로세스의 평균 수행시간보다 짧게 잡으면 빈번한 Context Switch로 오버헤드 증가한다.**
   - **Time Slice를 너무 크게 잡으면, FCFS와 다름 없어진다.**
