## ECR 이란
EC2 Container Registry는 Docker Container의 이미지를 저장하는 Repository 서비스 임  
 
기능은 Docker hub의 Repository서비스와 동일함

장점은 Container 이미지를 S3 에 저장하기 때문에 고가용성이 유지되고, AWS IAM 인증을 통해 이미지 push/pull 에 대한 권한 관리가 가능하다는 것