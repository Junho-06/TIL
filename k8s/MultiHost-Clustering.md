## 멀티호스트 환경과 클러스터링
하나의 호스트 머신에서 Docker를 설치하고 그 위에서 몇 개의 컨테이너를 가동시켜 서버를 작동시켰다고 가정함  
이미지의 작성이나 컨테이너의 시작 등은 호스트 머신에 설치된 Docker가 수행하고, 여러개의 Docker를 일원 관리할 때는  
Docker-Compose를 사용하여 애플리케이션의 실행 환경을 구축했다면 이 호스트에서 장애 발생 시 서비스가 정지 됨  
  
**대규모 웹 시스템에서 서비스 정지는 단순한 비즈니스 기회의 사실뿐만 아니라 기업의 사회적 신용을 잃게 할 우려가 있음**  
시스템의 일부에서 장애가 발생해도 서비스가 정지되지 않도록 만드는 장치가 필요함  
  
위 사항을 구현하는 기술 중 하나가 ```클러스터링``` 이다

> **클러스터링 이란?**  
여러대의 서버나 하드웨어를 모아서 한 대처럼 보이게 하는 기술을 뜻함  
  
클러스터링을 하게되면 아래 두가지 시스템 특성이 향상됨  
  
1. 가용성  
시스템에 있어서 가용성이란 시스템이 계속해서 가동될 수 있는 능력을 뜻함  
서버의 오류나 하드웨어의 고장 등이 발생해도 다른 정상적인 서버나 하드웨어가 대신해서 처리를 계속함으로써 높은 신뢰성을 확보 가능함  
  
2. 확장성  
고부하로 인한 시스템 다운을 피하기 위해 여러 대의 컴퓨터를 클러스터화하여 처리를 분산시킴으로써 높은 처리 성능을 얻을 수 있음  
Docker를 사용하면 단일 호스트 머신에서뿐만 아니라 여러 대의 호스트 머신 상에서 Docker를 작동시켜서 높은 가용성과 확장성을 가진 애플리케이션 실행 환경을 구축할 수 있음  
  
이와 같이 멀티호스트 환경에서 컨테이너들의 클러스터링을 수행하기 위한 툴을 **컨테이너 오케스트레이션 툴** 이라고 함  
 
 또한 멀티호스트 환경에서 컨테이너를 작동시키는 경우는 컨테이너의 장애나 호스트 머신의 가동 상황 등을 감시하는 장치를 고려해야함  
 컨테이너 실행 환경을 지원하는 통합 감시 툴이나 클라우드에 의한 감시 서비스 등이 Docker를 지원하고 있으므로 이용하는 것이 좋음