## RabbitMQ 란
AMQP를 구현한 오픈소스 메세지 브로커  
```AMQP란 메세지 지향 미들 웨어를 위한 표준 응용 계층 프로토콜```
  
producers에서 consumers로 메세지(요청)를 전달할 때 중간에서 브로커 역할을 수행함

사용하는 케이스는 아래와 같음
* 요청을 많은 사용자에게 전달할 때
* 요청에 대한 처리시간이 길 때
* 많은 작업이 요청되어 처리를 해야할 때
  
해당하는 요청을 다른 API에게 위임하고 빠른 응답을 할 때 많이 사용함  
  
MQ를 사용하면 애플리케이션간에 결합도를 낮출 수 있다는 이점도 지님

## 주요 개념 정리
![](https://velog.velcdn.com/images/sdb016/post/5763f81e-b710-4a55-9a3e-d7ea16932595/image.png)
(사진출처 : https://velog.io/@sdb016/RabbitMQ-%EA%B8%B0%EC%B4%88-%EA%B0%9C%EB%85%90)
* Producer
    * 요청을 보내는 주체, 보내고자 하는 메세지를 exchange에 publish함
* Consumer
    * Producer로 부터 메세지를 받아 처리하는 주체
* Exchange
    * producer로부터 전달받은 메세지를 어떤 queue로 보낼지 결정하는 장소, 4가지 타입을 가짐
* Queue
    * consumer가 메세지를 consume하기 전까지 보관하는 장소
* Binding
    * Exchange와 Queue의 관계, 보통 사용자가 특정 exchange가 특정 queue를 binding하도록 정의함