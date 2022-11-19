## VPC peering이란
다른 VPC 간에 Private IP로 통신가능하도록 연결하는 것을 말함  
  
보통의 VPC 간 통신은 Public IP 를 통해 이루어짐  
하지만 Public IP를 통해 통신을 할 경우 데이터의 안정성에 대한 문제가 발생할 수 있음  
  
VPC Peering을 사용하면 다른 VPC간에 Private IP로 통신하기 때문에 데이터의 안정성을 보장받을 수 있음

## VPC Peering특징
* 1 대 1 VPC 연결만 지원함
* 다른 리전의 VPC 및 다른 AWS계정의 VPC와도 연결이 가능함
* 연결된 VPC는 CIDR가 겹치면 안됨
* 단방향 통신과 양방향 통신 모두 지원함
    * 라우팅 테이블을 한쪽만 정의한 경우 단방향 통신을 지원하고 양쪽다 정의할 경우 양뱡향 통신을 지원함