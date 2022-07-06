## **가상환경**
* 가상환경에서 설치한 pip들은 global이나 다른 가상환경에 영향을 주지않음
* 버전이 달라서 충돌이 일어나는 것을 방지 가능

1. ```python -m venv (가상환경이름)```
2. ```cd Scrpits```
3. ```activate```
4. 가상환경 실행완료
5. ```pip install django```
6. 가상환경 내에서 ```py -m django --version``` 를 쳐서  
 django 가 다운로드 됫는지 확인
---
## **프로젝트 생성**
* 원하는 경로로 이동 한 후에 ```__django-admin startproject (프로젝트명)__```  
을 통해서 프로젝트를 생성
* 생성된 프로젝트 파일을 보면 manage.py, \_\_init\_\_.py, settings.py, urls.py, wsgi.py가 생성된다
---
## **서버구동**
* 서버가 잘 작동하는지 확인하기 위해서는 프로젝트명 으로 경로를 변경하고 ```__py manage.py runserver__``` 를 입력하고 http://127.0.0.1:8000 으로 이동하여 확인
* 이렇게 해서 구동되는 웹서버는 순수 Python으로 작성된 웹서버 이기 때문에 오로지 개발목적으로 사용해야함, 상용 목적으로 사용하기 위해서는 NginX, Apache 같은 웹서버 사용
---
## **APP 생성**
* App는 특정한 기능을 수행하는 웹 어플리케이션을 말한다,  
프로젝트는 이런 특정한 웹 사이트를 위한 앱들과 각 설정들을 한데 묶은 것이다,  
프로젝트는 다수의 앱을 포함 할수 있고, 앱은 다수의 프로젝트에 포함될 수 있다
* ```py manage.py startapp (앱이름)``` 으로 앱 생성 가능
---
## **Django의 흐름**
![Django의 흐름](https://camo.githubusercontent.com/2e25813262f91a4aecbd912334e37b7d953558ba15fbe5934636d2ac04f11ca4/68747470733a2f2f692e737461636b2e696d6775722e636f6d2f724c6653432e6a7067 "Django의 흐름")
* wsgi.py : 웹서버와 비즈니스 로직 사이를 연결해주는 인터페이스.  
 ↓
* middleware : http request를 처리하기 전에 거치는 관문.settings.py에 설정된 middleware들을 순차적으로 통과.  
 ↓
* urls.py : request와 매칭되는 callable object(FBV/CBV) 반환하여 실행.  
↓
* views.py : CBV 라면 dispatch 메소드를 통해 최종 request를 처리할 함수가 선택됨.
이후 함수를  
실행하면서  models.py에서 필요한 데이터를 읽어옴.
적절한 template renderer이  
 선택되어 responser생성.  
↓
* middleware : response는 다시 미들웨어들을 통과.  
역방향으로 미들웨어 리스트의 마지막 원소부터 지나감.  
↓
* wsgi.py : 인터페이스를 통해 response가 웹서버로 전달.
---
## **데이터베이스**
* (프로젝트명)/setting.py 파일을 보면 기본적으로 SQLite로 구성되어 있음
* 다른 데이터베이스를 사용하고 싶다면 적절한 데이터베이스 바인딩을 설치하고 데이터베이스 연결 설정과 맞게끔 DATABASE 'default' 항목의 값을 바꿔줘야한다