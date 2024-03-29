## MSA란
MicroService Architecture  
  
작고, 독립적으로 배포 가능한 각각의 기능을 수행하는 서비스로 구성된 프레임워크  
  
완전히 독립적으로 배포가 가능함, 다른 기술 스택이 사용 가능한 단일 사업 영역에 초점을 둠

## MSA 특징
* 어플리케이션 출시처럼 하나의 목표를 향해 일하지만 자기가 개발하는 서비스만 책임짐
* 마이크로서비스 기반의 어플리케이션을 다양한 언어와 기술로 구축할수 있음

## MSA 장점
* 각각의 서비스가 모듈화 되어서 모듈끼리 RPC, message-driven API등을 이용하여 통신함
* 각각 개별의 서비스 개발을 빠르게 하며, 유지보수 또한 쉽게 가능함
* 팀 단위로 적절한 수준에서 기술 스택을 다르게 가져갈 수 있음
* 서비스별로 독립적 배포가 가능함
    * 지속적인 배포(CD) 또한 가볍게 할수 있음
* 각각의 서비스들은 개별적으로 scale-out이 가능함

## MSA 단점
* 상대적으로 복잡함, 서비스가 분산되어 있기 때문에 내부 시스템의 통신을 어떻게 가져갈지 결정해야 함
* 트랜잭션을 유지하는게 어려워짐
* 통합 테스트가 어렵다
    * 개발 환경과 실제 운영환경을 동일하게 가져가는 것이 쉽지 않음
* 실제 운영환경에 배포하는 것이 쉽지 않음
    * 한개의 서비스가 다른 서비스들과의 연계가 정상적으로 이루어지고 있는지 확인해야함