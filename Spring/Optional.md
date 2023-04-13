## Optional이란
먼저 NPE(NullPointerException)를 알아야한다  
  
NPE란 개발을 할 때 가장 많이 발생하는 예외 중 하나  
NPE를 피하기위해선 null 여부를 검사해야 하는데, null 검사를 해야하는 변수가 많은 경우 코드가 복잡해지고 번거로워짐  
  
### Optional?
Optional 클래스는 NPE를 방지할 수 있도록 도와주는 클래스 이다  
  
```Optional<T>```는 null이 올 수 있는 값을 감싸는 Wrapper클래스로, 참조하더라도 NPE가 발생하지 않도록 도와준다  
  
Optional 클래스는 value에 값을 저장하기 때문에 값이 null이더라도 바로 NPE가 발생하지 않으며, 클래스이기 때문에 각종 메소드를 제공해준다