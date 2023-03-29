### 먼저 컨테이너란?
IT에서는 특별히 정해진 정확한 정의가 없다고한다  
**무언가를 모아놓고 여러 기능을 수행하는 논리적인 공간** 이라는 느낌이 이해하기 좋은 의미인 것 같다  
  
때문에 컨테이너는 특정 프레임워크만의 특징이 아니고, 다른 것들도 가지고 있는 개념이다

### IoC (Inversion of Control)
"제어의 역전" 이라는 의미이고, 객체나 메소드의 생성주기를 컨테이너가 관리해주는 것을 뜻한다  
  
쉽게 말해 프로그램의 흐름을 컨테이너가 관리해주는 것이다

User에게 Team을 설정하는 코드를 Java로 짠다고 예를 들어보자
```Java
class User {
   private String name;
   private String Team team;
   
   /* getter/setter 메소드들 */
}
class Team {
   private name;
   
   /* getter/setter 메소드들 */
}

// 일일히 다 적어줘야 함
public static void main(String[] args) {
    User user = new User();
    Team team = new Team();
}
```
객체도 생성하고, setter로 설정도 하는 등 개발자가 많은 것을 해줘야한다  
프레임워크를 쓰면 그럴 필요가 없어진다
```Java
@Bean
class User {
   private String name;
   private String Team team;
   
   /* getter/setter 메소드들 */
   
   public setTeam(Team team) {
      this.team = team;
}
@Bean
class Team {
   private name;
   
   /* getter/setter 메소드들 */
}
public static void main(String[] args) {
   /* 아무것도 안해도 됨 */
}
```
@Bean 어노테이션으로 객체가 컨테이너에 빈으로 등록된다  
등록된 객체는 컨테이너가 알아서 처리해주기 때문에 개발자가 신경쓸게 없어진다  
  
객체를 생성하고, 관계를 맺는 등의 역할은 모두 프레임워크가 해주는 것이다  
개발자는 오직 비즈니스 로직에만 집중하면 되는 것이다  
  
이런 프로그램의 흐름, 제어가 개발자에서 프레임워크로 넘어갔다고 하여, 제어의 역전 이라고 부르는 것이다

### DI (Dependency Injection)
의존성 주입이라는 뜻으로, IoC와 함께 IoC/DI 라고 부른다  
  
의존성 주입은 위에 나왔던 예제의 Setter 메소드와 같다
```Java
class User {
   private String name;
   // 의존성을 가짐
   private String Team team;
   
   /* getter/setter 메소드들 */
   public void setTeam(Team team) {
      this.team = team;
   }
}
class Team {
   private name;
   
   /* getter/setter 메소드들 */
}
public static void main(String[] args) {
   User user = new User();
   Team team = new Team();
   
   // 의존성 주입
   user.setTeam(team);
}

```
User가 Team을 속성으로 가지고 있는 것을 의존성을 지닌다 라고 하고  
user의 setTeam으로 Team 속성을 정의해주는 것을 의존성 주입 이라고 한다  
  
스프링은 위와 같은 DI를 지원해준다
```Java
public static void main(String[] args) {
   User user = new User();
   Team teamA = new Team();
   
   // teamB로 바꾸고 싶음
   user.setTeam(teamA);
}
```
지금은 팀A를 DI하고 있지만, 팀A가 아닌 팀B를 DI하고 싶을 수도 있다  
그럼 teamA를 지우고 teamB라는 객체를 생성해야 하고, 소스코드도 수정해야 한다  
  
코드가 더 길다면 답이 더 없어질 것이다  
스프링은 위 같은 비효율적 DI를 알아서 해준다
```Java
@Bean
class User {
   // 자동 DI
   @Autowired
   private String Team team;
   
   // 알아서 Team 빈을 찾아서 주입해 줌
   public void setTeam(Team team) {
      this.team = team;
   }
}
@Bean
class Team {
   /* getter/setter 메소드들 */
}
public static void main(String[] args) {
   /* Setter 메소드 안써도 됨
}
```
@Autowired로 인해 빈으로 등록된 Team을 찾아서 Setter에 자동으로 넣어진다
코드가 훨씬 간결해지고, 복잡한 의존 관계를 개발자가 작성할 필요도 없어진다