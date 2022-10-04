## 4 Layer
Segmentation, TCP, UDP, Socket, L4 Swich(Load Balancer), Port 등이 있음

* TCP와 UDP의 차이는 신뢰성이 있냐 없냐 임

* TCP
    * 인터넷상 에서 데이터를 메세지의 형태로 보내기 위해 IP와 함께 사용하는 프로토콜

* UDP
    * 데이터를 데이터그램 단위로 처리하는 프로그램

* Port
    * 프로토콜과 비슷한 개념
    * 데이터를 주고받기 위해 열린 하나의 관문

* Socket
    * TCP, UDP 방식을 설정할 수 있는 규약

* Segmentation, L4 Swich
    * 서버 1개가 원활하게 통신할수 있는 갯수를 넘으면 속도가 느려짐
    * L4 Swich = Load Balancer
        * L4 Swich는 들어오는 패킷 갯수를 연결되어 있는 서버들의 원활하게 통신할수 있는 갯수를 고려하여 적당히 분배해서 연결시킴
        * 고가용성 과 확장성 이라는 특징을 가짐
    * Segmentation
        * Segmentation 은 분할 이라는 뜻으로 10byte 의 데이터를 2byte의 Bandwith 로 보낸다고 하면 10byte의 데이터를 2byte 씩 5개로 분할하여 sequence를 지정해주고 데이터를 전송하면 도착지에서 sequence 차례대로 정렬하여 데이터를 읽어옴
        * 분할된 각각의 데이터들을 Segmentation 이라고 함