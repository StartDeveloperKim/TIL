# JVM(Java Virtual Machine)
 - JVM은 Java 애플리케이션을 실행하는 가상 컴퓨터이다.
 - 컴퓨터 하드웨어와 운영 체제에 의존하지 않고 Java 바이트 코드를 실행할 수 있게 해준다.
 - JVM은 자바 코드를 컴파일해서 생성된 바이트 코드를 실행하고, 메모리 관리와 가비지 컬렉션 등의 작업
을 처리한다.

## JVM의 역할
-  **플랫폼 독립성:** JVM은 "Write Once, Run Anywhere" 원칙을 실현하여, 한 번 작성한 자바 코드를 다양한 플랫폼에서 실행할 수 있도록 해줍니다. 
-  **바이트 코드 실행:** 자바 컴파일러에 의해 생성된 바이트 코드를 읽고 실행 가능한 기계 코드로 변환하여 프로그램을 실행합니다.
-  **메모리 관리:** 객체의 생성과 해제, 가비지 컬렉션 등 메모리 관리 작업을 처리하여 개발자가 메모리를 직접 관리할 필요가 없도록 합니다. 
- **다중 스레드 관리:** 다중 스레드 프로그래밍을 지원하여 여러 작업을 동시에 실행하고 관리합니다.

 ## JVM의 메모리 공간
 JVM은 프로그램 실행 중에 필요한 메모리를 관리하는데, 이 메모리는 여러 영역으로 분리되어 있다.
 #### Method
 - Method 영역은 클래스 정보와 정적 변수들이 저장되는 공간이다.
 - 이 영역은 모든 스레드가 공유하며, 클래스 로더에 의해 로딩된 클래스의 메타데이터, 상수 풀, 메서드와 필드의 정보 등이 저장된다.
 #### Heap
 - Heap은 객체들의 인스턴스와 배열을 저장하는 공간이다.
 - 동적으로 생성된 객체들이 할당되는 영역이고, 해당 영역은 Garbage Collection 작업으로 메모리를 관리하여 더 이상 사용되지 않는 객체들을 정리한다.
 #### Stack
 -  Stack은 각 스레드마다 별도로 할당되는 메모리 영역으로, 메서드 호출과 관련된 정보를 저장한다.
 - 메서드가 호출될 때마다 호출된 메서드의 정보와 지역 변수, 매게변수 등이 스택에 추가되며, 메서드가 반환되면 해당 정보가 제거된다.
 
#### PC 레지스터
- PC레지스터는 현재 실행 중인 명령어의 주소를 저장하는 공간이다.
- 스레드마다 별도로 유지되며, 명령어 실행 위치를 추적하고 다음에 실행할 명령어를 지정하는 역할을 한다.
#### Native Method Stack
- 자바 코드가 아닌 다른 언어로 작성된 네이티브 메서드를 위한 공간이다.
- 네이티브 메서드는 자바 코드에서 네이티브 라이브러리를 호출할 때 사용된다.
#### Direct Memory
- 네이티브 코드에서 직접적으로 메모리를 할당하고 관리하는 영역이다.
- 이는 Java Heap 외부에서 관리되는 메모리로, 네이티브 라이브러리를 통해 사용된다.
## JVM의 동작 원리
1. **컴파일**
> **개발자가 작성한 자바 소스 코드는 '.java' 파일로 저장된다. 이 소스 코드는 자바 컴파일러에 의해 바이트 코드로 변환한다.** 
2. **클래스 로딩**
> **변환된 바이트 코드는 JVM의 메모리 중 메서드 영역에 로딩된다. 이 때, 클래스 로더는 필요한 클래스를 찾아 로딩하고 초기화한다.**
3. **바이트 코드 해석 및 실행**
> **JVM은 바이트 코드를 인터프리터 또는 JIT 컴파일러를 통해 실행 가능한 기계 코드로 변환하여 실행한다.**
4. **메모리 관리 및 가비지 컬렉션**
> **JVM은 힙 영역에 생성된 객체들을 관리하고, 더 이상 사용되지 않는 객체들을 가비지 컬렉션을 통해 정리한다.**