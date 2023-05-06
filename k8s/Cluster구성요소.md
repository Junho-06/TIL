## 쿠버네티스 클러스터 구성

1. Control Plane (Master Node)  
클러스터 관리하는 역할을 담당함  
상태 관리 및 명령어 처리 수행

2. Node (Worker Node)  
어플리케이션 컨테이너 실행

---

### Control Plane
* API Server
    * 쿠버네티스 리소스와 클러스터 관리를 위한 API 제공
    * etcd를 데이터 저장소로 사용

* Scheduler
    * 노드의 자원 사용 상태를 관리하며, 새로운 워크로드를 어디에 배포할지 관리

* Controller Manager
    * 여러 컨트롤러 프로세스를 관리
    * 각 컨트롤러는 클러스터로부터 특정 리소스 상태의 변화를 감지하여 클러스터에 반영하는 reconcile 과정을 반복 수행

* etcd
    * 분산 Key - Value 저장소로 클러스터 상태를 저장함

---

### Node
* kubelet
    * 컨테이너 런타임과 통신하며 컨테이너 라이프사이클 고나리
    * API 서버와 통신하며 노드의 리소스 관리

* CRI
    * kubelet이 컨테이너 런타임과 통신할 때 사용되는 인터페이스
    * 쿠버네티스는 Docker, containerd, cri-o 컨테이너 런타임 지원

* kube-proxy
    * 오버레이 네트워크 구성
    * 네트워크 프록시 및 내부 로드밸런서 역할 수행