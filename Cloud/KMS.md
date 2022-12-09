## KMS란
KMS는 암호키를 쉽게 생성하고 제어할 수 있게 해주는 관리형 서비스  
  
암호키를 사용하여 AWS 서비스에 암호화를 시켜줌 
AWS에서 리소스들을 암호화하는데 사용됨

## KMS 사용 이유
아무에게나 보여주지 않는 정보들을 보호하기 위한 목적

## KMS Key 관리 방식
1. AWS Managed key
    * AWS 서비스들이 KMS 를 통해 Key를 서비스 받는 것으로, 내부적으로 자동으로 일어나게 되며 사용자가 직접적으로 제어가 불가능함
2. Customer Managed key
    * 사용자가 직접 Key를 생성하고 관리하는 것
3. Custom key stores