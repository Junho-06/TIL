## Event Bridge 란
Event Bridge란 EDA(Event Driven Architecture)를 구성하는데 도움을 주는 서버리스 서비스  
  
AWS 뿐 아니라 SaaS서비스, 개인 어플리케이션에서 보내는 이벤트(데이터)를 받아 원하는 SNS나 lambda와 같은 타겟으로 보내주는 역할

## Event Bridge 구성요소
* Event  
이벤트소스에서 오는 이벤트 느낌  
AWS 서비스를 예로 들면 EC2의 상태가 바뀐다던지, ASG에 인스턴스가 추가될 때 **Event** 가 발생함

* Event Rule  
Event가 발생한 경우, Event Rule과 매칭되는 이벤트만 Event Rule에 연결된 Event Target으로 라우팅 됨  

* Event Target  
Event Rule의 필터링을 통과한 이벤트가 도착하는 대상  
하나의 Event Rule에 여러개의 Event Target등록이 가능함, 즉 해당 event rule의 이벤트 패턴을 만족하는 이벤트를 구독하는 느낌

* Event Bus  
이벤트를 받는 역할을 수행함  
Event Rule을 생성할 때, 하나의 Event Bus에 연결을 해야함. 이 Event Bus로 들어오는 이벤트만 Event Rule에서 필터링을 하게 됨