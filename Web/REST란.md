## restAPI
rest의 정의
* Representational State Transfer의 약자
* 자원을 이름으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미함
* HTTP URI를 통해 자원을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미함
    * REST는 자원 기반의 구조(ROA) 설계의 중심에 resource가 있고 HTTP method를 통해 resource를 처리하도록 설계된 아키텍쳐를 의미함

---
### REST의 장단점
* 장점
    * HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구축할 필요가 없음
    * HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해줌
    * HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능함
    * 서버와 클라이언트의 역할을 명확하게 분리함

* 단점
    * 표준이 존재하지 않음
    * 사용할수 있는 메소드가 4가지 밖에 없음
    * 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 값이 어렵게 느껴짐

---
### REST가 필요한 이유
* 애플리케이션 분리 및 통합
* 다양한 클라이언트의 등장
* 멀티 플랫폼에 대한 지원을 위해 서비스 자원에 대한 아키텍처를 세우고 이용하는 방법중 하나

---
### REST 구성 요소
1. 자원 : URI
    * 모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재함
2. 행위 : HTTP Method
    * HTTP 프로토콜의 Method를 사용함
    * HTTP 프로토콜은 GET, POST, PUT, DELETE와 같은 메서드를 제공함
3. 표현
    * Client가 자원의 상태(정보)에 대한 조작을 요청하면 Server는 이에 적절한 응답을 보냄
    * REST에서 하나의 자원은 JSON, XML, TEXT, RSS등 여러 형태의 Representation으로 나타내어 질 수 있음

---
### REST 특징
1. Server-Client(서버 클라이언트 구조)
    * 자원이 있는 쪽이 Server, 자원을 요청하는 쪽이 Client가 됨
        * REST Server: API를 제공하고 비즈니스 로직 처리 및 저장을 책임짐
        * Client: 사용자 인증이나 context(세션, 로그인 정보) 등을 직접 관리하고 책임짐
    * 서로 간 의존성이 줄어듬
2. Stateless(무상태)
    * HTTP 프로토콜은 Stateless Protocol이므로 REST 역시 무상태성을 가짐
    * Client의 context를 Server에 저장하지 않음
    * Server는 각각의 요청을 완전히 별개의 것으로 인식하고 처리함
3. Cacheable(캐시 처리 기능)
    * 웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 그대로 활용 가능
        * 즉, HTTP의 특징중 하나인 캐싱 기능을 적용 가능함
    * 대량의 요청을 효율적으로 처리하기 위해 캐시가 요구됨
    * 캐시 사용을 통해 응답시간이 빨라지고 REST Server 트랜잭션이 발생하지 않기 때문에 전체 응답시간, 성능, 서버의 자원 이용률을 향상 시킬수 있음
4. Layered System(계층화)
    * Client는 REST API Server만 호출함
    * PROXY, 게이트웨이 같은 네트워크 기반의 중간 매체를 사용할 수 있음
5. Code-On-Demand(optional)
    * server로부터 스크립트를 받아서 Client에서 실행함
6. Uniform Interface(인터페이스 일관성)
    * URI로 지정한 Resource에 대한 조작을 통일되고 한정적인 인터페이스로 수행함
    * HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능함