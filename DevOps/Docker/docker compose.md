## Docker compose란
여러개의 컨테이너로부터 이루어진 서비스를 구축, 실행하는 순서를 자동으로 하여 관리를 간단하게 하는 것  
  
여러개의 컨테이너 설정 내용을 하나의 yaml 파일에 모아서 사용함  
  
compose 파일을 준비해서 커맨드를 1번 실행하는 것만으로 그 파일로부터 설정을 읽어들여 모든 컨테이너 서비스를 실행 시킬수 있음

## Docker compose 기본적인 명령

실행 : ```docker-compose up```  
중지 : ```docker-compose stop```  
  
실행하면서 빌드(서비스 시작 전 이미지를 새로 만드는 것) : ```docker-compose up --build```

## Docker compose 사용 방법
1. 각각의 컨테이너의 Dockerfile을 작성함
2. ```docker-compose.yml``` 파일을 작성하고, 각각 독립된 컨테이너의 실행 정의를 실시함
3. ```docker-compose up``` 커맨드를 실행하여 docker-compose.yml으로 정의한 컨테이너를 개시함

## Docker-compose.yml 파일 작성
* build
    * 해당 서비스의 이미지를 빌드하기 위한 Dockerfile이 위치하는 경로를 저장함

* ports
    * 호스트 OS와 컨테이너의 포트를 바인딩 시켜줌
    * 따옴표와 함께 문자열로 지정해야 함
    * 형식은 ```"host:container"``` 또는 ```"container"```
    * 외부로 노출시킬 포트의 맵핑을 명시하는 부분
    * 바인드가 필요한 호스트 외부 포트와 컨테이너 내부 포트를 지정

* image
    * docker-compose 안에서 베이스 이미지를 지정함

* command
    * 해당 서비스가 올라올 때 Dockerfile의 CMD 명령문을 무시하고 실행할 명령어를 설정함

* depends_on
    * 서비스 간의 종속성 순서대로 서비스를 시작함
    * ```A: depends_on: -B``` : A 애플리케이션이 올라오기 전에 B가 먼저 올라와야 함

* environment
    * 컨테이너의 환경 변수를 지정함