## pm2
Package manager : 소프트웨어 관리해주는 역할
- npm도 pacakge manager이며 nodejs에서 광범위하게 사용됨
- nodejs는 싱글스레드로 되어 있어 단일 CPU 코어에서 실행되기 때문에 CPU의 멀티코어 시스템은 사용할수 없음
    * 이러한 문제를 해결하기 위해 cluster 모듈을 통해 단일 프로세스를 멀티 프로세스로 늘릴 수 있는 방법을 제공함
    * 클러스터 모듈을 사용해서 마스터 프로세스에서 cpu 코어수만큼 워커 프로세스를 생성해서 모든 코어를 사용하게끔 개발하면 됨

* pm2 : node.js 의 프로세스를 관리해주는 역할  
    * 생산 프로세스 관리자로 서버 인스턴스들에 대한 로드 밸런싱  
    * 프로세스들이 계속 실행할 수 있는 환경을 제공  
    * 처리하지 못한 예외에 의해 스레드가 죽음으로 인해 애플리케이션이 죽는 현상을 방지  
    * nodejs 어플리케이션을 무중단으로 운영