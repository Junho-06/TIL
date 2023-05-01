## 이미지 사이즈
Docker를 사용하다 보면 아래와 같은 문제가 발생할수 있음

* Docker 이미지 크기의 증가
* 매우 길어지는 빌드 시간

### 이미지 사이즈가 중요한 이유?
아래와 같음
- 큰 이미지는 더 많은 디스크 공간을 차지한다, Docker이미지를 저장해두는 중앙 저장소를 사용한다면 시간이 지날수록 새로운 큰 이미지와 구 버전들까지 저장하는 것이 어려워짐
- 네트워크상에서 큰 이미지를 전송할 때 많은 시간이 소요됨, 이 같은 지연 시간은 CI/CD 파이프라인의 퍼포먼스에 악영향을 끼침

### 가능하면 작은 Base 이미지 선택하기
예를 들어 Node 애플리케이션을 다커라이징(dockerizing) 하는 경우, 여러 base image 옵션을 선택할 수 있음

- jessie-*
- buster-*
- stretch-*
- alpine-*

jessie-*, buster-* 그리고 stretch-* 이미지는 Debian 기반이며, alpine-* 이미지는 Alpine Linux 프로젝트 기반으로 되어있음

Base이미지에 따라 어느정도 크기 조절이 가능함

### Multi-Stage Docker Builds 사용
Multi-Stage build는 하나의 Dockerfile내에서 여러 개의 이미지를 사용하여 쉽게 Docker 이미지를 최적화 할수 있음

Multi-Stage build를 사용하는 궁극적인 이유는, 여러 개의 단계로 세분화하여 런타임 이미지의 크기를 줄이는데에 있음

### 불필요한 파일 제거하기
많은 개발자가 NPM 패키지에 있는 테스트, markdown, typing 그리고 .map과 같은 파일을 기억 속에서 잊어버리곤 함  
패키지에 불필요한 것들을 지우는 데 node-prune을 사용하면 안전하게 제거할 수 있음

### 이미지 축소 과정에서 주의해야 할 점
* 베이스 이미지를 변경하면 운영체제 레벨 패키지의 부재로 애플리케이션이 느려질 수 있음
* 런타임 dependency를 development-time dependency로 명시하는 실수는 하지 말아야 함
* 불필요한 패키지라고 판단하여 지워버린 dependency는 본인이 모르는 다른 dependency에서 요구하는 패키지일 수도 있음
