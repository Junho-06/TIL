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

* 전송계층
    * TCP/UDP

    * TCP(신뢰성)
        * 순서에 따라 패킷을 송신함
        * 서버에서 sequnce 번호 에 따라 처리하다가 문제가 있을때 재요청을 보낼수있음
        * 서버 여유공간에 따라 데이터 크기를 요청 가능함
    
    * UDP(비신뢰적 Protocol)
        * 데이터가 제대로 오지 않앗다면 데이터가 없는걸로 판단
        * TCP는 데이터가 없다면 재요청 했지만 UDP는 확인하지않음

    * First mile, Middle mile, Last mile
        * 전송하는 쪽이 first mile 수신하는 쪽은 last mile

* 세션계층
    * 세션에 대한 관리를 수행함
        * 3way handshake 이후 맺어지는 통신 경로 같은 경로들

* 표현계층
    * 암호화, OS가 알아들을수 있도록 16진수로 변환하는 역할
    * 압축을 통해 데이터를 빠르게 송.수신 할수 있는 환경도 구성 가능

* 응용계층
    * HTTP, SMTP, DNS 등 데이터를 변환해서 출력해주는 역할을 수행함