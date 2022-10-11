먼저 WSGI라는 기술을 알아야함

---
### WSGI란
파이썬 애플리케이션이(파이썬 스크립트) 웹 서버와 통신하기 위한 인터페이스 임  
웹서버의 요청을 해석하여 파이썬 애플리케이션 쪽으로 전달하는 역할을 수행함

---
## Gunicorn이란
Python WSGI로 Web Server(Nginx)로부터 서버사이드 요청을 받으면 WSGI를 통해 서버 애플리케이션(Django)로 전달해주는 역할을 수행함  
  
Django의 runserver도 똑같은 역할을 수행하지만 보안적으로나 성능적으로 검증이 되지 않았기 때문에 production 환경에서 사용할 수 없음(개발용으로는 유용함)  
  
### production 환경에 적합한 Gunicorn
WSGI는 멀티 쓰레드를 만들 수 있기 때문에 Request 요청이 많아지더라도 효율적으로 처리가 가능함