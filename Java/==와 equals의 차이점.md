# ==와 equals()의 차이
`==` 연산자와 `equals()` 메서드는 두 객체가 같은 객체인지 확인하는데 사용되는 연산자 및 메서드이다. 그러나 두 개념 간에는 동일성과 동등성이라는 개념적 차이가 있다.

**동일성 (Identity):** 
동일성은 두 객체가 메모리 상에서 정확히 같은 위치에 위치하는지를 판단한다. 다시 말해, 두 객체가 물리적으로 동일한 인스턴스인지를 검사한다.

**동등성 (Equality):** 
동등성은 두 객체가 논리적으로 같은 값을 가지는지를 판단한다. 예를 들어, 특정 필드의 값이 동일한 경우 두 객체를 논리적으로 같다고 판단한다.

`==` 연산자는 동일성을 판단하는 데 사용된다. 즉, 비교하는 두 객체가 메모리 상에서 동일한 위치에 있는지를 확인한다.

반면에 `equals()` 메서드는 동등성을 판단하는 데 사용된다. 하지만 기본적으로 Java의 모든 클래스는 `equals()`를 Object 클래스에서 상속받는다. 이 상태에서는 `equals()`가 내부적으로 `==` 연산자를 사용하여 동일성 비교를 수행한다. 따라서 개발자가 동등성을 비교하고자 한다면 해당 클래스에서 `equals()` 메서드를 오버라이딩하여 논리적인 비교를 의도에 맞게 구현해야 한다.


![image](https://github.com/StartDeveloperKim/TIL/assets/97887047/54f251fb-e3e3-4f2e-8864-0383fb6ef5e9)
