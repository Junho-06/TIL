## 2 Layer
Dummy Hub, Bridge, Swich, ARP, RARP, MAC address 등이 있음

* Dummy Hub와 Swich 의 차이는 전송 방식과 가격

* Dummy Hub
    * A라는 컴퓨터가 D라는 컴퓨터를 찾고싶으면 Dummy Hub로 연결되있는
    컴퓨터 모두에게 D를 찾는 request를 보냄 만약 받는 컴퓨터가 D가 아니라면
    request를 버리게되고, 받는컴퓨터가  D라면 Response 를 Dummy Hub 로 보내게 되고 Dummy Hub 는 A라는 컴퓨터에게 D의 Response 를 보내줌
* Swich
    * A라는 컴퓨터가 D라는 컴퓨터를 찾고싶으면 Swich 에게 request를 보내게 되고
    Swich 는 가지고 있던 테이블에 있는 경로 중에 D의 주소를 찾아 a의 request 를 보내게 되고 request를 받은 D라는 컴퓨터는 Swich 로 response를 보내게 되고 Swich 가 A라는 컴퓨터에게 D의 response를 보내줌

* Bridge
    * 서로 다른 IP를 가지고 있는 2개의 컴퓨터가 통신을 하고 싶을때 Bridge 라는 다른 네트워크 대역을 연결시켜주는 네트워크 장비를 통해 통신을 가능하게 함

* ARP / RARP
    * 모든 컴퓨터는 물리적 아이디(LAN)와 논리적 아이디(IP)를 가지고 있음
    * 물리적 아이디는 변할수 없지만 논리적 아이디는 변할수 있음
    * LAN주소(AA:AA:AA:BB:BB:BB)(16진수)
        * AA:AA:AA는 LAN을 만든 회사의 고유번호(OUI)
        * BB:BB:BB는 LAN카드들의 각각의 고유번호(SegNum)
    * 두 컴퓨터가 통신을 할때 한 컴퓨터가 다른컴퓨터의 IP주소에 MAC address를 request하게 되고 request를 받은 컴퓨터는 MAC address를 response 하게 됨 그럼 response 를 받지 않은 컴퓨터는 정보를 MAC주소 테이블에 저장해놓고 다음 통신을 할 때에는 request를 하지 않음
    * IP를 물어봤을때 MAC address 를 반환 하는것이 ARP이다
    * MAC address를 물어봤을때 IP를 반환 하는것이 RARP