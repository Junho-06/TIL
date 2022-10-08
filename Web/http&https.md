## HTTP란
서버/클라이언트 모델을 따라 데이터를 주고 받기 위한 프로토콜  
인터넷에서 하이퍼텍스트를 교환하기 위한 통신 규약으로, 80번 포트를 사용중

---
### HTTP구조
상태를 가지고 있지 않는 Stateless상태임  
Method, Path, Version, Headers, Body 등으로 구성됨  
![http구조](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbkdJ4Q%2FbtqK6AXLEtC%2FjBZzMuJBWzdLYmqILo5Ri1%2Fimg.png)  
  
---
### HTTPS란
HTTPS는 HTTP에 데이터 암호화가 추가된 프로토콜  
443포트를 사용하며, 네트워크 상에서 중간에 제3자가 정보를 볼 수 없도록 암호화를 지원하고 있음  
  
---
### HTTPS 암호화 방식
* HTTPS는 대칭키 암호화 방식과 비대칭키 암호화 방식 모두 사용하고 있음

1. 대칭키 암호화
    * 클라이언트와 서버가 동일한 키를 사용해 암호화/복호화를 진행함
    * 키가 노출되면 매우 위험하지만 연산 속도가 빠름

2. 비대칭키 암호화
    * 1개의 쌍으로 구성된 공개키와 개인키를 암호화/복호화 하는데 사용함
    * 키가 노출되어도 비교적 안전하지만 연산 속도가 느림