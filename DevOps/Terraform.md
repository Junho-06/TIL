## IaC란
IaC는 Infrastructure as Code 는 말그대로 코드를 통해 인프라를 관리하고 프로비저닝하는 것 을 말함  
 
IaC를 활용하면 인프라 사양을 담은 구성파일이 생성되므로 항상 동일한 구성을 프로비저닝 할 수 있음

### IaC의 장점
* 비용 절감
* 배포 속도 향상
* 오류 감소
* 인프라 일관성 향상
* 구 변동제거

### IaC 툴
* Chef
* Puppet
* Saltstack
* Terraform
* AWS CloudFormation

## Terraform 이란
테라폼 이란 클라우드 인프라스트럭처 자동화 도구  
  
테라폼은 하시코프에서 오픈소스로 개발중인 클라우드 인프라 스트럭처 자동화를 지양하는 IaC도구  
  
## Terraform 기본 개념
* 프로비저닝
    * 어떤 프로세스나 서비스를 실행하기 위한 준비 단계
    * 프로바이더로는 aws, 구글 클라우드 플랫폼, 마이크로소프트 애저와 같은 범요 클라우드 서비스를 비롯해 깃허브, 데이터 도구와 같은 특정 기능을 제공하는 서비스, mysql, 도커와 같은 로컬서비스를 지원함
* Resource
    * 리소스란 특정 프로바이더가 제공해주는 조작 가능한 대상의 최소 단위
* Plan
    * 테라폼 프로젝트 디렉터리 아래의 모든 .tf 파일의 내용을 실제로 적용 가능한지 확인 하는 작업
    * 테라폼은 이를 terraform plan 명령어로 제공하며, 이를 명령어로 실행하면 어떤 리소스가 생성되고, 수정되고, 삭제될지 보여줌
* apply
    * 테라폼 프로젝트 디렉터리 아래의 모든 .tf 파일의 내용대로 리소스를 생성, 수정, 삭제하는 일을 적용

## Terraform 명령어
* terraform init
    * 테라폼 프로젝트를 초기화 함
    * 테라폼은 테라폼 프로젝트를 초기화 할 때 프로바이더 설정을 보고 필요한 플러그인을 설치함
* terraform apply
    * 코드로 작성한 테라폼 설정을 적용하여 aws 리소스 등을 생성
* terraform destroy
    * 테라폼으로 생성된 infrastructure 삭제
* terraform plan
    * 이 파일을 저장하고 infrastrucure 실제로 적용하기 전에 변경 사항 체크

## Terraform 타입
* String
* Number
* Bool
* List(type)
* Set(type)
* Map(type)
* Tuple

## Terraform 구성 요소
* provider.tf
    * 리전이나 access key, secret key 같은 프로바이더에 대해 정의
* vars.tf
    * 각 변수에 대해 정의하는 hcl 파일
* terraform.tfvar
    * 리포지토리로 커밋하고 싶지 않은 중요 정보들을 저장
* instance.tf