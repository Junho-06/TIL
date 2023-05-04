## 먼저 GitOps란??
DevOps처럼 특정 도구가 아닌 방법론 이며 이름에서 알수있듯이 깃으로 관리 하겠다는 개념이다

DevOps를 적용하는 방법중 하나이며, 쿠버네티스를 대상으로 지속적 배포에 초점을 두고 있다

GitOps는 빌드와 테스트를 하는 지속적 통합 단계가 끝나고 난 후 배포 과정을 다루게 된다

## ArgoCD
Argo CD란 GitOps스타일의 지속적인 배포(CD, Continuous Delivery / Continuous Deployment)를 지원하는 도구이다

Git Repository의 내용이 업데이트 되면 변경된 내용을 Kubernets 클러스터에 동기화시켜주는 방식으로 동작한다

Argo CD는 Kubernetes와 같이 선언적으로 동작한다

Git Repository의 특정 경로를 지정하고, 해당 경로에 원하는 Kubernetes의 상태가 기술된 manifest파일들을 위치시키면 Argo CD가 해당 파일에 선언한 상태들과 동일하게 Object들을 배포해준다

ArgoCD를 사용하여 Kubernetes에 배포하면 Git에서 수정이 발생할 시, 자동으로 ArgoCD에서 수정하여 휴먼에러를 줄이고 지속적인 배포를 실현할 수 있다

또한 각 버전들은 Git 저장소에 기록되어 있으며 ArgoCD를 통하여 이전 버전으로의 롤백이나 새로운 버전으로 업그레이드가 편리해졌다