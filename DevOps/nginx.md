## Nginx
* Nginx란
    * nginx는 경량 웹 서버
    * 클라이언트로부터 요청을 받았을 때 요청에 맞는 정적 파일을 응답해주는 HTTP Web Server로 활용되기도 하고, Reverse Proxy Server로 활용하여 WAS 서버의 부하를 줄일 수 있는 로드 밸런서로 활용되기도 함

* NginX의 흐름
    * nginx는 Event-Driven 구조로 동작하기 때문에 한 개 또는 고정된 프로세스만 생성하여 사용하고, 비동기 방식으로 요청들을 Concurrency 하게 처리할 수 있음
        * Event-Driven이란
            * apache의 C10K 문제점 해결(한 시스템에 동시 접속자수가 1만명이 넘어갈 때 효율적 방안)을 위해 만들어진 Event-Driven 구조의 웹서버SW 라고함
            * OSI 7 Layer 중 application Level 아래의 level 에서 Nginx 같은 웹서버가 HTTP 통신을 담당함
    ![nginx흐름](https://velog.velcdn.com/images%2Fwijihoon123%2Fpost%2Ff7a48e26-ba2f-46eb-a7f6-c0b67e99f03a%2Fnginx.png)
    * 위의 그림에서 보이듯이 Nginx는 새로운 요청이 들어오더라도 새로운 프로세스와 쓰레드를 생성하지 않기 때문에 프로세스와 쓰레드 생성 비용이 존재하지 않음
    * 적은 자원으로도 효율적인 운용이 가능함
    * nginx의 장점 덕분에 단일 서버에서도 동시에 많은 연결을 처리할 수 있음
    
* Nginx의 구조
    * nginx는 하나의 Master Process와 다수의 Worker Process로 구성되어 실행됨
    * Master Process는 설정 파일을 읽고, 유효성을 검사 및 Worker Process를 관리함
    * 모든 요청은 Worker Process에서 처리함, nginx는 이벤트 기반 모델을 사용함, Worker Process 사이에 요청을 효율적으로 분배하기 위해 OS에 의존적인 메커니즘을 사용함
    * Worker Process의 개수는 설정 파일에서 정의됨, 정의된 프로세스 개수와 사용 가능한 CPU 코어 숫자에 맞게 자동으로 조정
    ![nginx구조](https://velog.velcdn.com/images%2Fwijihoon123%2Fpost%2F3467a69b-25c0-49e1-ad76-51ee4143c49c%2Fnginx111.png)

* Nginx의 장단점
    * 단점
        * 동적 컨텐츠를 기본적으로 처리 할 수 없음
        * 동적 콘텐츠에 대한 PHP 및 기타 요청을 처리하려면 nginx가이를 실행하기 위해 외부 프로세서로 전달하고 렌더링 된 콘텐츠가 다시 전송 될 때까지 기다려야함
        * 동적 웹 페이지 컨텐츠를 가진 모든 요청을 위해 외부 자원과 연계
    * 장점
        * 이벤트 중심 접근 방식을 사용하여 클라이언트 요청 제공
        * 제한된 하드웨어 리소스로도 여러 클라이언트 요청을 동시에 효율적으로 처리
        * 단일 스레드를 통해 여러 연결을 처리 가능
        * 최소한의 리소스로 웹 서버의 아키텍처를 개선하기 위해 독립형 HTTP 서버로 배치 가능
        * 로드 밸런싱 : 요청이 많은 사이트를 운영하는 경우 하나의 서버가 아닌 여러대의 서버를 두고 운영을 하게 됨, 특정 서버에만 요청이 몰리지 않도록 하는 역할을 nginx가 수행하게 됨
        * 공격으로 부터 보호 : nginx를 사용하면 웹사이트나 서비스에서 실제 서버의 IP주소를 필요로 하지 않기 때문에 DDoS와 같은 공격이 들어와도 nginx를 공격하게 되지 실제 서버에는 공격이 들어오는 것을 막을 수 있음
        * 캐싱 : nginx는 콘텐츠를 캐싱할 수 있어 결과를 더 빠르게 응답하여 성능을 높일 수 있음