## DNS

Domain Name Service

* DNS 서버는 53포트를 사용하고 TCP 통신을 사용함(3way handshake, 4way handshake)

* 도메인과 IP를 매핑시켜서 리스트 형으로 관리함

* 클라이언트가 request를 보내게 되면 DNS서버가 매핑 정보를 response 하게 됨

* 루트도메인은 웹사이트 주소의 마지막에 있는 정보를 관리
    * ex) .com / .net / .kr 등등

* DNS는 request가 들어오면 먼저 루트도메인에 요청을 하고 받은 정보에 관한 서버에 가서 사용자가 request한 도메인의 IP를 전달받게 되고 그 정보를 DNS서버가 직접 확인하고 맞다면 사용자에게 response 함