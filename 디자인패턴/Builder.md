# 빌더 패턴(생성패턴)
빌더 패턴은 객체 생성을 더 유연하고 가독성 있게 만들기 위한 디자인 패턴이다.

## 사용 목적
 - 복잡한 객체 생성
   객체의 생성 과정이 복잡하거나 다양한 파라미터를 넘겨야 하는 경우 빌더 패턴을 사용하여 객체를 구성할 수 있다.
 - 가독성과 유지보수성
   빌더 패턴은 가독성을 향상시키고 코드의 유지보수성을 높이는 데 도움을 준다.   

## 코드
```java
public class Product {
  private String name;
  private int price;
  private String category;

  private Product(Builder builder) {
    this.name = builder.name;
    this.price = builder.price;
    this.category = builder.category;
  }

  public static class Builder {
    private String name;
    private int price;
    private String category;

    public Builder(String name) {
      this.name = name;
    }

    public Builder price(int price) {
      this.price = price;
      return this;
    }

    public Builder category(String category) {
      this.category = category;
      return this;
    }

    public Product build() {
        return new Product(this);
    }
  }
}

public class Main {
  public static void main(String[] args) {
    Product product = new Product.Builder("Example")
                          .price(100)
                          .category("example category")
                          .build();
  }
}
```

## 장점
 - 가독성
   객체를 생성할 때 전달하는 파라미터를 명시적으로 전달할 수 있기에 가독성이 훨씬 좋아진다.
   만약 객체 생성에서 전달하는 파라미터의 개수가 4개 이상이거나(이펙티브자바) 동일한 자료형을 연속해서 전달한다면
   빌더 패턴을 고려하면 좋다.
## 단점
 - 추가적인 코드작성
   위와 같이 빌더 패턴을 사용하기 위해서는 추가적인 내부 클래스 작성이 필요하므로 코드가 장황해진다.
   하지만 이러한 단점은 Lombok 라이브러리를 사용하므로써 어느정도 해결이 된다.

#### Lombok 사용
```java
public class Product {
  private String name;
  private int price;
  private String category;

  @Builder
  public Product(String name, int price, String category) {
    this.name = name;
    this.price = price;
    this.category = category;
  }
}
```
