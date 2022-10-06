## CDN이란  
Content Delivery Networ의 약자로 지리적 제약 없이 전 세계 사용자 에게 빠르고 안전하게 콘텐츠를 전송할 수 있는 콘텐츠 전송 기술  

---
### CDN의 장점
1. 웹사이트 로딩 속도 개선
    * 오리진 서버의 트래픽 부하 및 비용 절감 가능
2. 인터넷 회선 비용 절감
    * 서버 비용이 감소함
3. 컨텐츠 제공의 안정성
    * 인터넷 서비스 제공자에 직접 연결되어 데이터를 전송 하므로 컨텐츠를 빠른 속도로 제공 가능
4. 웹사이트 보안 개선
    * 대규모 분산 서버 장비로 공격 트래픽을 완화 가능

---
## CloudFront란
CloudFront은 AWS에서 제공하는 CDN 서비스 임  
캐싱을 통해 사용자에게 좀 더 빠른 정송 속도를 제공함을 목적으로 함  
CloudFront는 전 세계에 Edge Location을 두고 Client에 가장 가까운 Edge location을 찾아 Latency를 최소화 시켜 빠른 데이터를 제공함

---
### CloudFront 구성
1. Origin Server
    * 원본 데이터를 가지고 있는 서버
    * AWS에서는 S3, EC2 instance를 나타냄
2. Edge Server(Edge location)
    * AWS에서 실질적으로 제공하는 전 세계에 퍼져있는 서버
    * Edge Server에는 요청 받은 데이터에 대해서 빠르게 응답해주기 위해 캐싱 기능을 제공

---
### CloudFront 작동방식
1. 사용자로부터 요청이 발생
2. 요청이 발생한 Edge Server는 요청이 발생한 데이터에 대하여 캐싱 여부를 확인함
3. 캐싱 데이터가 존재한다면 사용자에 요청에 맞게 응답하고, 존재하지 않으면 Origin Server로 요청함
4. 요청 받은 데이터에 대해 Origin server로부터 전달 받은 Edge server는 캐싱 데이터를 생성하고 사용자에게 응답함