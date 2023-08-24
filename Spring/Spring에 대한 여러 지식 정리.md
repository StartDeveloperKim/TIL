# Spring
Spring은 Java 엔터프라이즈 애플리케이션을 개발하기 위한 경량 프레임워크며, 다양한 하위 프로젝트를 제공하며 POJO(Plain of Java Object)를 기반으로 제작할 수 있어 다른 라이브러리와도 호환성이 좋다. 

##  주요 특징
### 1. IoC(Inversion of Control) 컨테이너
- IoC 컨테이너 또는 스프링 컨테니어라고 한다.
- Spring은 IoC 컨테이너를 기반으로 하여 **객체의 생명 주기와 의존성 관리**를 담당한다. 
- 개발자는 객체 생성과 관리에 대한 부분을 프레임워크에 위임할 수 있다. 
![image](https://github.com/StartDeveloperKim/TIL/assets/97887047/8b3ce0d0-30de-4c62-9cb8-4e8ff05daf04)

### 2. DI(Dependency Injection)
- DI(의존성주입) 을 통해 개발자가 임의로 객체사이의 의존성을 연결해주지 않아도 된다. (**@Autowired**)
- XML 파일이나 Configuration 클래스 또는 어노테이션을 통해 Bean 인스턴스를 생성하고, 객체 간의 의존성을 자동으로 주입해준다.(명시적으로 해줄 수도 있음) 
- Spring의 DI는 싱글톤 패턴을 활용하여 하나의 Bean 인스턴스만을 생성하고 관리한다.
> 싱글톤이 Default이다.   `@Scope("prototype")` 을 사용하면 Prototype의 객체생성을 하는데 이는 요청마다 객체를 생성하는 방식이다.
### AOP(Aspect Oriented Programming)
- AOP는 관점 지향 프로그래밍이라는 뜻으로 비즈니스 로직이외의 성능측정 및 로그 출력과 같은 횡단 공통 로직을 따로 빼내어 관리 및 프로그래밍 할 수 있는 기능이다. 
- 애플리케이션의 여러 모듈에서 중복되는 코드를 효과적으로 관리할 수 있다.
## Bean 객체를 등록하는 방법
### 1. @Configuration 클래스에서 @Bean 사용
- @Configuration이 붙은 설정 클래스로 이동하여 @Bean을 활용하여 Bean 객체를 등록할 수 있다.
```
@Configuration
public class AppConfig {
    @Bean
    public MyService myService() {
        return new MyServiceImpl();
    }
}
```
### 2. @ComponentScan
- ComponentScan 기능을 활용하여 **@Component, @Controller, @Service, @Repository**가 있는 클래스를 자동으로 Bean 인스턴스로 등록한다.

```
 @Configuration
 @ComponentScan(basePackages = "com.example")
public class AppConfig {
	   // ...
}
```


### 3. XML 설정파일
- XML 설정파일로 Bean 인스턴스를 생성 및 등록할 수 있다. 
```
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="myService" class="com.example.MyServiceImpl" />
</beans>
```
## Bean을 주입받는 방법
### 1. 생성자 주입
 - 생성자 주입은 Bean으로 지정된 클래스가 인스턴스로 생성될 때 의존하고 있는 객체를 주입받는 방식이다.
 - 필드를 final로 설정할 수 있기에 객체의 **불변성**을 보장받을 수 있다.
 - **테스트 코드를 작성할 때 유용하다.** Mock 객체 또는 커스텀한 객체를 주입하여 단위 테스트를 구성할 수 있다.
```
@Service
public class MyService {

    private final MyRepository myRepository;

    @Autowired
    public MyService(MyRepository myRepository) {
        this.myRepository = myRepository;
    }
}

```
 > 현재 스프링버전에서는 한 클래스에 하나의 생성자가 있을 때 @Autowired를 자동으로 붙여준다.
### 2. 필드 주입
- 필드주입은 필드위에 @Autowired를 붙임으로써 DI를 하는 방식이다.
- 이 방식은 단위 테스트코드 작성에 어려움을 줄 수 있다. 외부에서 필드를 직접 주입하기 어렵기 때문이다.
```
@Service
public class MyService {

    @Autowired
    private MyRepository myRepository;
}

```
> 인텔리제이 같은 경우 필드주입을 할 시 노란색 줄로 주의 표시를 준다.
### 3. setter 메서드 주입, 일반 메서드 주입
- setter 메서드 또는 일반메서드를 통해 주입하는 방식이다.
- 이 방법들 같은 경우는 권장하지 않는다.  public으로 열어야하기 때문에 필드의 변경가능성을 열어두기 때문이다.
```
@Service
public class MyService {

    private MyRepository myRepository;

    @Autowired
    public void setMyRepository(MyRepository myRepository) {
        this.myRepository = myRepository;
    }
}

```

## MVC 패턴과 Spring MVC
### Model-View-Controller (MVC)
-   **Model:** 데이터와 비즈니스 로직을 담당하는 컴포넌트이다. 데이터베이스에서 정보를 가져오거나 계산을 수행하며, 애플리케이션의 상태와 동작을 관리한다.
-   **View:** 사용자에게 데이터를 표시하고 사용자 인터페이스를 제공하는 역할을 한다. 클라이언트에게 결과를 보여주는 데 사용된다.
-   **Controller:** 사용자의 요청을 처리하고 Model과 View를 연결하는 역할을 한다. 클라이언트의 요청을 받아 해당 요청에 따라 Model을 업데이트하고 적절한 View를 선택하여 데이터를 전달한다.

### Spring MVC
- Spring MVC는 Spring 프레임워크의 일부로서, 웹 애플리케이션의 개발을 위한 모델-뷰-컨트롤러 아키텍쳐를 구현하는 데 사용되는 웹 프레임워크이다.
- Spring MVC는 웹 애플리케이션의 코드를 모듈화하여 유지보수성을 향상시키고, 각각의 역할을 분리하여 개발하는 데 도움을 준다.

#### 구성요소
- DispatcherServlet : 모든 클라이언트의 요청을 받아 Spring MVC의 처리 과정을 시작하는 중앙 컨트롤러이다.
- HandlerMapping : 클라이언트의 요청 URL을 어떤 컨트롤러 클래스와 메서드가 처리할지를 매핑한다.
- HandlerAdapter : 컨트롤러의 메서드와 실제로 요청을 처리하는 객체 사이의 연결을 담당한다.
- Controller : 클라이언트의 요청을 처리하고, Model을 업데이트하고, 결과를 반환하는 역할을 한다ㅐ.
- ModelAndView : 컨트롤러가 처리한 결과 데이터와 해당 결과를 보여줄 View의 정보를 담고 있는 객체이다.
- ViewResolver : View 이름을 실제 View 객체와 매핑하여 최족적인 응답을 생성한다.
![enter image description here](https://terasolunaorg.github.io/guideline/1.0.1.RELEASE/en/_images/RequestLifecycle.png)
1. **사용자 요청 수신 (DispatcherServlet):**
	클라이언트의 요청이 서블릿 컨테이너에 도달하며 'DispatcherServlet'이 해당 요청을 맨 앞에서 받는다.
2. **컨트롤러 매핑 (HandlerMapping):** 
 `DispatcherServlet`은 `HandlerMapping`을 통해 클라이언트의 요청을 어떤 컨트롤러가 처리해야 하는지 결정한다.이때 `HandlerMapping`은 클라이언트 요청 URL을 컨트롤러와 매핑하여 적절한 컨트롤러를 선택한다.
3. **HandlerAdapter 호출:** 
선택된 컨트롤러가 요청을 처리하는 데 필요한 메서드를 실행하는데, 이때 `HandlerAdapter`가 사용된다.`HandlerAdapter`는 컨트롤러의 메서드와 요청 파라미터 간의 매핑 및 변환을 처리하며, 컨트롤러의 메서드 실행 결과를 받아온다.
4.  **컨트롤러 실행 (비즈니스 로직 수행):**
 `HandlerAdapter`는 컨트롤러의 메서드를 호출하여 요청에 맞는 비즈니스 로직을 실행한다. 컨트롤러는 Model 객체에 데이터를 저장하고, 해당 데이터를 기반으로 로직을 처리한다.
6.  **View 이름 반환:** 
컨트롤러는 처리된 결과를 기반으로 View의 이름을 반환한다. 이 View 이름은 클라이언트에게 보여줄 화면을 나타낸다.
    
7.  **ViewResolver 및 View 선택:** 
`ViewResolver`는 컨트롤러가 반환한 View 이름을 실제 View 객체와 매핑하여 최종적으로 사용할 View를 선택한다.
    
8.  **응답 생성 (클라이언트에게 결과 반환):** 
선택된 View는 Model에 있는 데이터를 사용하여 최종적인 응답 결과를 생성한다. 이 응답은 클라이언트에게 전달되어 브라우저에서 보여지게 된다.
