# Kernel

OS는 컴퓨터의 복잡한 부분을 가려주고, 사용자가 쉽게 컴퓨터를 작동할 수 있도록 인터페이스를 제공하는데 목적이 있다.<br>Kernel은 OS의 핵심 부분으로, 자주 쓰이는 함수를 내장하고 있다. Kernel은 사용자가 볼 수 없는 부분이지만, 사용자는 알게 모르게 Kernel을 사용하게 된다.

**커널은 다음과 같은 일을 한다.**

- 메모리관리, 파일시스템 및 파일 접근 권한 관리
- I/O 관리(Device Driver와 **Interrupt Handling**)
- 프로세스 관리(CPU 관리 및 **IPC**)

**커널의 구성**

- Top-half
  프로세스와 커널의 대화 부분으로 system call함수가 담긴 부분이다.
- Bottom-half
  하드웨어와 커널의 대화부분으로, Device Driver - Interrupt Handler가 존재하는 공간이다.

### Trap

커널의 protection은 HW에 의해 이루어진다.<br>Trap이 보호해준다.

**무엇을 protection 하는가?**

1. 유저가 특권 명령어를 건드리는 것

   - **특권 명령어**는 I/O 명령어 등으로 machine level 명령어를 의미하는데, 이것은 커널이 건드려야 된다.
     예를들어 CPU 정지 명령어 같은 것을 유저가 잘못 건드리면 시스템 전체가 다운 될 수도 있기 때문에, 유저로부터 특권 명령어 접근을 보호한다.

2. 잘못된 메모리 주소 접근

<br>

**어떻게 보호하는가?**<br>
**Dual mode**를 제공하면서 protection 한다. <br>
모드는 다음과 같다.

1. User Mode
   프로세스만 수행 가능한 모드, 이 모드에선 특권 명령어 수행이 불가능하다.
2. Kernel Mode(System Mode)
   프로세스가 커널 함수를 호출하면, 특권 명령어가 수행된다.

<br>

### Kernel Mode

커널 모드의 on/off는 **Trap**이 해준다.<br> 즉, 커널 모드에 돌입하기 전에 Trap이 Mode를 바꿔주는 순간이 존재한다는 것이다.

1. 프로세스의 system call
   프로세스가 커널 함수를 호출하게 되면, Trap이 켜지고 kernel Mode로 변환이 일어난다. 비로소 프로세스는 **kernel의 Top-half에 담긴 system 함수를 사용할 수 있게 된다.** 시스템 함수가 종료되면 Trap이 꺼지고 다시 user mode로 돌아간다.
   - 유저가 사용하는 함수는 "라이브러리"에서 가져오는 것이므로 커널모드가 켜지지 않는다.
2. Interrupt Handler
   Interrupt가 발생하면 커널의 Bottom-half 부분이 동작하게 된다.
