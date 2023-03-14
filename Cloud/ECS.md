## ECS 란
ECS는 완전관리형 컨테이너 오케스트레이션 서비스 이다.  
  
### 컨테이너 오케스트레이션?
- 컨테이너의 배포, 관리, 확장, 네트워킹을 자동화 해주는 유형

### ECS의 구성 요소
1. Cluster
2. Service
3. Task Definition
4. Task
5. Container Instance

#### Cluster
- ECS의 가장 기본 단위로 Cluster는 Task 또는 Service의 논리적인 그룹이다
- 컴퓨팅 자원을 포함하지 않으며, ECS에서 컨테이너를 실행시키기 위해 Container Instance가 Cluster에 포함되어야 한다
- Cluster는 Container Instance를 조직할 수 있는 권한을 가지고 있고, Cluster에서 Service나 Task를 실행하면 조건을 만족하는 Container Instance를 찾아서 해당 Instance에 컨테이너를 실행함
- Fargate를 사용하면 Container Instance없이 컨테이너를 실행 가능함  
  
#### Service
- Service는 Task를 지속적으로 관리하는 단위
- Service는 Cluster 내에서 지정된 Task 수만큼 동시에 실행하고 관리할 수 있음
- ELB와 연동하여 실행중인 Task를 찾아 자동으로 ELB에 등록 및 제거하는 Auto Scaling 역할도 담당  
  
#### Task Definition
- Task Definition은 Task를 실행하기 위한 설정을 저장하고 있는 단위
- Task Definition은 컨테이너 별로 실행하고자 하는 이미지를 지정할 수 있으며, CPU나 Memory와 같은 정보도 지정할 수 있고, 하나 혹은 둘 이상의 Task Definition을 포함할 수 있음
- Task Definition은 Cluster에 종속되어있지 않음  
  
#### Task
- Task는 ECS의 최소 실행 단위로 하나 이상의 컨테이너 묶음
- Task를 실행하는 방법에는 Task Definition으로 직접 Task를 실행하는 방법과 Service를 정의하는 방법이 있음
    - Task Definition으로 직접 실행된 Task의 경우 처음 한 번 실행된 이후 관리되지 않음
- Task는 Cluster에 속한 Container Instance에 배포됨  
  
#### Container Instance
- Task가 배포되는 Cluster에 등록된 EC2 Instance를 Container Instance라고 함
- ECS는 EC2 Instatnce에 ECS Container Agent를 설치하고 Cluster에 Container Instanc로 등록할 수 있음
- 하나의 Cluster에 여러 개의 Container Instance가 있을 수 있으며, 하나의 Container Instance안에서도 여러개의 Task가 있을 수 있음