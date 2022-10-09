## AJAX
AJAX는 JavaScript의 라이브러리중 하나이며 Asynchronous JavaScript And Xml(비동기식 자바스크립트와 xml)의 약자  
브라우저가 가지고있는 XMLHttpRequest 객체를 이용해서 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법  
JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술  
즉, 자바스크립트를 통해서 서버에 데이터를 요청하는 것

---
## AJAX를 사용하는 이유
JSON이나 XMl형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄수 있음

---
## AJAX의 장점
1. 웹페이지의 속도향상
2. 서버의 처리가 완료될 때까지 기다리지 않고 처리가 가능
3. 서버에서 Data만 전송하면 되므로 전체적인 코딩의 양이 줄어듬
4. 기존 웹에서는 불가능했던 다양한 UI를 가능하게 해줌

---
## AJAX의 단점
1. 히스토리 관리가 되지 않음
2. 페이지 이동없는 통신으로 인한 보안상의 문제가 있음
3. 연속으로 데이터를 요청하면 서버 부하가 증가할 수 있음

---
## AJAX의 진행과정
1. XMLGttpRequest Object를 만듬
    * request를 보낼 준비를 브라우저에게 시키는 과정
    * 이것을 위해서 필요한 method를 갖춘 object가 필요함
2. callback 함수를 만듬
    * 서버에서 response가 왔을 때 실행시키는 함수
    * HTML 페이지를 업데이트 함
3. Open a request
    * 서버에서 response가 왔을 때 실행시키는 함수
    * HTML 페이지를 업데이트 함
4. send the request