# Factory Mehtod(생성패턴)
객체 생성을 처리하기 위한 디자인 패턴 중 하나로, 객체를 생성하는 코드를 클라이언트 코드로부터 분리하고 객체의 생성을 서브클래스에 위임한다.

이를 통해 클라이언트 코드는 구체적인 클래스의 인스턴스를 직접 생성하지 않고, 팩토리 메서드를 사용하여 객체를 생성한다.

## 목적
 - 객체 생성 로직의 중복을 방지한다.
 - 객체 생성 방식을 유연하게 변경할 수 있다.
 - 클라이언트 코드와 구체적인 클래스 간의 결합도를 낮춘다.

## 코드
```java
// Product: 도형(Shape) 인터페이스
public interface Shape {
    void draw();
}

// Concrete Products: 구체적인 도형 클래스들
public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("원을 그립니다.");
    }
}

public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("사각형을 그립니다.");
    }
}

// Creator: 도형을 생성하는 Factory Method를 선언하는 인터페이스
public interface ShapeFactory {
    Shape createShape();
}

// Concrete Creators: Factory Method를 구체화하는 클래스들
public class CircleFactory implements ShapeFactory {
    @Override
    public Shape createShape() {
        return new Circle();
    }
}

public class RectangleFactory implements ShapeFactory {
    @Override
    public Shape createShape() {
        return new Rectangle();
    }
}

// 클라이언트 코드
public class Client {
    public static void main(String[] args) {
        ShapeFactory circleFactory = new CircleFactory();
        Shape circle = circleFactory.createShape();
        circle.draw(); // "원을 그립니다." 출력

        ShapeFactory rectangleFactory = new RectangleFactory();
        Shape rectangle = rectangleFactory.createShape();
        rectangle.draw(); // "사각형을 그립니다." 출력
    }
}

```

## 장점
 - 유연성과 확장성, 코드의 재사용성 증가
 - 객체 생성 로직 추상화 덕분에 목 객체 생성 및 주입이 용이, 단위 테스트 작성 용이
 - 객체 생성 로직 캡슐화에 따른 코드의 유지보수성 향상

## 단점
 - 클래스 및 인터페이스 증가로 인한 복잡성 증가
 - 중간 객체를 생성함에 따른 오버헤드 증가
