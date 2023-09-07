# Singleton pattern(생성패턴)
싱글톤 패턴이란 특정 클래스의 인스턴스가 오직 하나만 생성되는 패턴을 의미한다.

## 목적
 - 리소스 공유
   여러 객체 간에 동일한 인스턴스를 공유하여 메모리 및 자원 사용을 최적화한다.
 - 중앙 집중적인 제어
   특정 클래스의 인스턴스를 단 한 번만 생성하고, 이 인스턴스에 대한 접근을 제한하여 예기치 않은 동작을 방지한다.

## 코드
```java
public class Singleton {

  private static Singleton instance;

  private Signleton() {
    // 싱글톤 클래스는 인스턴스가 또 생성되면 안되므로 기본 생성자를 private으로 지정한다.
  }

  public static Sigleton getInstance() {
    if (instance == null) {
      instance = new Singleton(); // 처음 호출 시에만 인스턴스를 생성
    }
    return instance;
  }
}
```

## 장점
 - 메모리 및 리소스 절약
 - 전역 접근 가능
## 단점
 - 테스트 코드 작성의 어려움
 - private 생성자이므로 상속이 불가함
 - 멀티쓰레드 환경에서 하나의 자원을 공유하므로 상태를 가지면 오류가 발생할 가능성이 높음
