## AMI
EC2를 시작하기 위한 기본 세팅의 모음이라고 생각하자  
  
* EC2 인스턴스를 실행하기 위해 필요한 정보를 모은 단위
    * OS, 아키텍쳐 타입, 저장공간 등


## 아마존에서 정의한 AMI

```
AMI는 인스턴스를 시작하는 데 필요한 정보를 제공,
인스턴스 시작 시 AMI를 지정해야 한다.
동일한 구성의 인스턴스가 여러개 필요할 때 한 AMI에서 여러 인스턴스 시작이 가능하다.
서로 다른 구성의 인스턴스가 필요할 때 다양한 AMI를 사용해 인스턴스를 시작하면 된다.
```

## AMI가 포함 하는것들
* 1개 이상의 EBS 스냅샷 또는 인스턴스 저장 지원 AMI 경우 인스턴스의 루트 볼륨에 대한 템플릿
* AMI를 사용해 인스턴스를 시작할 수 있는 AWS 계정을 제어하는 시작 권한
* 시작될 때 인스턴스에 연결할 볼륨을 지정하는 블록 디바이스 매핑