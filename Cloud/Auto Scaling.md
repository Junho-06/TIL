## Auto Scaling
클라우드 컴퓨팅의 대표적인 장점으로는 필요에 따라 서비스를 빠르게 확장하거나 축소할 수 있는 유연성을 들 수 있음  
  
오토스케일링은 클라우드의 유연성을 돋보이게 하는 핵심기술로 CPU, 메모리, 디스크, 네트워크 트래픽과 같은 시스템 자원들의 메트릭 값을 모니터링하여 서버 사이즈를 자동으로 조절하는 서비스

## 오토 스케일링의 목표
1. 정확한 수의 EC2 인스턴스를 보유하도록 보장
    * 그룹의 최소 인스턴스 숫자와 최대 인스턴스 숫자를 관리
    * ex) 애플리케이션을 실행하기 위해 인스턴스가 3개가 필요하다면, 3대 이상의 인스턴스가 항상 떠있을 수 있도록 보장
    * 최소 숫자 이하로 내려가지 않도록 인스턴스 숫자를 유지(인스턴스 추가)
    * 최대 숫자 이상 늘어나지 않도록 인스턴스 숫자 유지(인스턴스 삭제)
2. 다양한 스케일링 정책 사용 가능
    * CPU의 부하에 따라 인스턴스 크기 늘리기/줄이기
3. 가용영역에 인스턴스가 골고루 분산될 수 있도록 인스턴스를 분배
    * 서비스 장애가 발생하더라도 문제없이 서비스 이용

## ASG
ASG는 Auto Scaling Group으로 자동으로 서버 인스턴스에 대해 크기를 관리해주는 기능임  

## ASG 장점
서비스 특성 상 사용자가 몰리는 시간, 몰리지 않는 시간에 최소/최대 값을 지정하여 서버 비용을 효율적으로 관리가 가능함

ASG로 어떤 인스턴스 수가 자동으로 변경됐는지 알림을 받아 서비스에 이상이 있는지 확인할수 있다는 장점이 있음