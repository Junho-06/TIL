## ELB란
Elastic Load Balancing은 EC2 인스턴스, 컨테이너, IP 주소 등 여러 대상에 걸쳐 수신되는 트래픽을 자동으로 분산함  
등록된 대상의 상태를 모니터링하면서 상태가 양호한 대상으로만 트래픽을 라우팅함
![ELB 구조](https://media.amazonwebservices.com/blog/2014/elb_instances_1.png)

---
### ELB 주요 기능
1. NAT GateWay
    * 사설 IP주소를 공인IP주소로 변환 해주는 역할 수행
2. 터널링(Tunneling)
    * 인터넷 상에서 눈에 보이지 않는 통로를 만들어 통신할 수 있게 해줌
    * 데이터를 캡슐화해 연결된 상호간에만 캡슐화된 패킷을 구별해 캡슐화를 해제할 수 있음
3. DSR(Dynamic Source Routing protocol)
    * 로드 밸런서 사용시 서버에서 클라이언트로 되돌아가는 경우 목적지 주소를 스위치의 IP 주소가 아닌 클라이언트의 IP주소로 전달해서 네트워크 스위치를 거치지 않고 바로 클라이언트를 찾아감
        * ex) 들어오는 요청이 10MB인데 응답이 100MB라면 병목 현상이 발생함, 트래픽 흐름을 조정해서 큰 사이즈의 응답 패킷이 나갈 때 로드밸런서를 거치지 않고 바로 서버가 클라이언트로 보내게 하는 기능이 DSR
    * DSR은 스트리밍의 경우 응답 속도 이점이 크다는 장점이 있고, 실시간 응답이 중요한 애플리케이션의 경우도 잘 어울림

---
### ELB 장점
로드밸런서는 워크로드를 가상 서버와 같은 다수의 컴퓨팅 리소스로 분산함, 로드 밸런서를 사용하면 애플리케이션의 가용성과 내결함성이 높아짐  
  
애플리케이션에 대한 요청의 전체적인 흐름을 방해하지 않고 필요에 따라 로드 밸런서에게 컴퓨팅 리소스를 추가 및 제거할 수 있음  
  
로드 밸런서가 정상적인 대상에만 요청을 보내도록 컴퓨팅 리소스의 상태를 모니터링하는 상태 확인을 구성할 수 있음, 또한 컴퓨팅 리소스가 주요 작업에 집중할 수 있도록 암호화 및 복호화 작업을 로드 밸런서로 오프로드 할수 있음  

---
### ELB의 특징
Health Check : ELB가 직접 트래픽을 발생시켜서 Instance가 살아있는지 체크함  
  
지속적으로 IP 주소가 바뀌며 IP 고정이 불가능함 : 도메인 기반으로 사용하게됨  
  
Elastic Load Balancing은 ALB, NLB, GLB및 CLB를 지원함, 필요에 따라 가장 적합한 로드 밸런서 유형을 선택할 수 있음

---
### CLB, NLB, ALB, GLB

1. Classic Load Balancer
    * CLB는 가장 오래된 로드밸런서로 ELB의 가장 기본적인 형태
    * L4 계층부터 L7계층까지 로드밸런싱이 가능함
    * TCP, SSL, HTTP, HTTPS등 다양한 프로토콜을 수용가능함, Sticky Session 의 기능도 제공함
    * CLB는 하나의 URL만 가질수 있음

2. Network Load Balancer
    * NLB는 4계층에서 작동함
    * TCP/UDP 트래픽을 로드밸런싱하여 내부 인스턴스로 전달함
    * TCP/UDP 서버를 구축할 때 NLB는 굉장히 낮은 지연시간으로 최적의 성능을 보여줌
    * 로드 밸런서에 대한 고정 IP 주소를 지원함

3. Application Load Balancer
    * ALB는 7계층에서 작동함
    * HTTP/HTTPS 트래픽을 처리하는 로드밸런싱에 최적화 되어 있음
    * ALB는 Path-based routing을 지원하여 ALB에 연결된 인스턴스들은 여러개의 URL과 path를 가질수 있음
    * websocket이나 HTTP/1.1 이상의 프로토콜 지원, 향상된 라우팅 정책 등의 기능으로 CLB보다 많은 장점을 가짐

4. Gateway Load Balancer
    * 간편한 배포, 확장성 및 고가용성을 제공
    * 3rd-party를 이용하여 방화벽을 구축하는 경우에 발생하는 문제점 해결 가능