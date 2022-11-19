## apache
* 웹서버 란
    * 웹 서버는 우리가 인터넷에서 흔히 사용하는 웹 페이지가 들어있는 파일을 사용자에게 제공해주는 서버 프로그램으로, 시스템 소프트웨어라 불림
    * 인터넷 사용자는 웹 브라우저를 통해 여러 페이지를 사용 하는데, 특정 페이지를 클릭할 경우 웹 서버로 HTTP 프로토콜을 이용해 페이지를 요청함
    * 웹 서버는 클라이언트에게 HTML문서로 된 페이지를 웹 브라우저로 전달함
    * 즉, 웹 서버는 사용자가 요청한 페이지를 전달하는 역할
        * 여기서 웹 브라우저는 클라이언트가 되며, 웹서버로부터 HTML 문서를 받아 사용자에게 보여줄 수 있는 중간자 역할을 수행

* 아파치 웹서버 란
    * 가장 널리 사용되는 웹 서버중 하나로, 초기의 웹 서버인 NCSA httpd를 기반으로 만들어졌고, 아파치 소프트웨어 재단에서 관리하고 있는 소프트웨어 임
    * 아파치 라이선스를 따르기 때문에 오픈소스로 공개되며 자유 소프트웨어로 무료로 사용할 수 있음
    * 리눅스나 윈도우 등 거의 모든 운영체제에서 사용할수 있으며 구축이 쉽고, 다양한 추가기능을 가지고 있기 때문에 현재 가장 인기있는 웹서버로 이용되고 있음
    * 요청당 스레드를 처리하는 구조인 아파치는 요청량이 많아지면 메모리 사용량이 높아져 성능이 떨어질수 있다는 단점이 있음
    * MPM 방식으로 HTTP 요청을 처리함
        * MPM : multi-process Module 로 크게 두가지 방식이 있음 (prefork 방식, worker 방식)
        * perfork mpm(다중 프로세스)
            * Client 요청에 대해 apache 자식 프로세스를 생성하여 처리함
            * 요청이 많을 경우 process를 생성하여 처리함
            * 하나의 자식프로세스당 하나의 스레드를 가짐
            * 스레드간 메모리 공유를 하지 않음, 이 방식은 독립적이기에 안정적인 반면, 메모리 소모가 크다는 단점이 있음
        * worker mpm(멀티 프로세스-스레드)
            * prefork 보다 메모리 사용량이 적고 동시접속자가 많은 사이트에 적합함, 각 프로세스의 스레드를 생성해 처리하는 구조
            * 스레드 간의 메모리 공유가 가능함
            * 프로세스 당 최대 64개의 스레드처리가 가능하며, 각 스레드는 하나의 연결만을 부여받음

- apache의 단점
    - 클라이언트 접속마다 process 혹은 thread를 생성하는 구조임
    - 동시접속 요청이 많이 들어오게 되면 CPU와 메모리 사용이 증가하고 추가적인 process/tread 생성비용이 드는 등 대용량 요청에 취약
    - apache 서버의 프로세스가 blocking 될 때 요청을 처리하지 못하고 처리가 완료될 때까지 대기상태에 있음, 이는 keep Alive(접속대기)로 해결이 가능하지만 효율이 떨어짐