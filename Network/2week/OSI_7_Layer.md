## OSI 7 Layer
End to End 통신에 사용됨

* 클라이언트 PC는 캡슐화를 진행하고 서버 PC는 디캡슐화를 진행함

* 각각의 계층들은 헤더들을 지니고 있음

```
응용계층 = Program
표현계층 = 출력 방식
세션계층 = 서로간의 세션 정보
전송계층 = TCP,UDP
네트워크계층 = Router를 통한 Routing
데이터링크계층 = Mac Address
물리계층 = Link(선)을 통한 연결
```

* 물리계층, 데이터링크계층, 네트워크 계층은 하위계층이라고 부름

* 전송계층, 세션계층, 표현계층, 응용계층은 상위계층이라고 부름

* 물리계층
    * 어떤선을 사용할 것인지 규격을 정하게됨, Dummby Hub와 Bridge와 Reapter 를 통해 데이터를 전달

* 데이터링크계층
    * MAC Address 를 관리하고 규정하는 계층
    * Swich를 통해 MAC Address를 전송

* 네트워크계층
    * Router라는 장비로 Routing table을 관리하고 사용하여 빠른 전송을 가능하게 하는 계층
    * IP address를 사용하여 전송함