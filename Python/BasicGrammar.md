## **자료형**

* 숫자 자료형
* 문자열 자료형
    * " " 또는 ' ' 안에 작성
* Boolean 자료형
    * True 또는 False
---
## **변수**
> 데이터를 저장하기 위해 프로그램에 의해 이름을 할당받은 메모리 공간
---
## **주석**
* 코딩을 할 때 넣는 설명문
    * 소스 코드를 더 쉽게 이해할 수 있게 만드는 것이 주 목적
---
## **연산자**
* ```+``` 덧셈
* ```-``` 뺄셈
* ```*``` 곱셈
* ```/``` 나눗셈
* ```%``` 나머지 구하기
* ```**``` 제곱
* ```//``` 소숫점 이하를 버리는 나눗셈
* ```>, <, >=, <=, ==, !=``` 부등호
* ```&, and```
* ```|, or```
* ```+=, -=, *=, /=```
---
## **함수**
* 숫자 처리 함수
    * ```abs()``` 절댓값
    * ```pow()``` 제곱
    * ```max()``` 최댓값
    * ```min()``` 최솟값
    * ```round()``` 반올림
        * math 모듈
            * ```floor()``` 내림
            * ```ceil()``` 올림
            * ```sqrt()``` 제곱근
* 랜덤 함수
    * random 모듈
        * ```random()``` 0~1 미만의 임의의 랜덤값
        * ```randrange(a, b)``` a~b 미만의 임의의 랜덤값
        * ```randint(a, b)``` a~b 이하의 임의의 랜덤값
* 문자열 처리 함수
    * ```(변수명).lower()``` 소문자로 변환
    * ```(변수명).upper()``` 대문자로 변환
    * ```(변수명[인덱스]).isupper()``` 인덱스 값이 대문자인지 확인
    * ```(변수명[인덱스]).islower()``` 인덱스 값이 소문자인지 확인
    * ```len(변수명)``` 변수의 길이 반환
    * ```(변수명).index("a")``` 변수 내의 a 위치 반환
    * ```(변수명).replace("a", "b")``` 변수 내의 a를 b로 변환
    * ```(변수명).find("a")``` 변수 내의 a의 위치를 반환
    * ```(변수명).count("a")``` 변수 내의 a의 갯수를 반환
---
## **탈출문자**
* ```\n``` : 줄바꿈
* ```\\``` : 문장 내에서 \ 사용
* ```\r``` : 커서를 맨 앞으로 이동
* ```\b``` : 한글자 삭제
* ```\t``` : 탭
---
## **자료구조**
* 리스트 [ ]
    * ```(리스트명).index("a")``` 리스트 내의 a 의 위치
    * ```(리스트명).append("a")``` 리스트 내에 a 추가
    * ```(리스트명).insert(1, "a")``` 리스트 내에 a를 1번째 위치에 추가
    * ```(리스트명).pop()``` 리스트 내에서 맨뒤에 값 삭제
    * ```(리스트명).count("a")``` 리스트 내에 a의 갯수 반환
    * ```(리스트명).sort()``` 리스트를 오름차순으로 정렬
    * ```(리스트명).reverse()``` 리스트 순서를 반대로 뒤집음
    * ```(리스트명).clear()``` 리스트 내의 모든내용 삭제
    * ```(리스트명).extend(다른 리스트명)``` 리스트에 다른 리스트 내용 추가
---
* 사전{ }
    * ```(사전명)[키]``` 키 에 해당하는 값 반환, 키가 없다면 에러
    * ```(사전명).get(키)``` 사전에서 키 에 해당하는 값 반환, 키가 없다면 None
    * ```(키) in (사전명)``` 사전안에 키가 있다면 True 없다면 False 반환
    * ```(사전명)[키] = " "``` 사전에 키에 해당하는 값 추가
    * ```del (사전명)[키]``` 사전에서 키에 해당하는 값 삭제
    * ```(사전명).keys()``` 키 값들만 반환
    * ```(사전명).values()``` value 들만 반환
    * ```(사전명).items()``` 키, value 둘다 반환
    * ```(사전명).clear()``` 사전 안의 모든값 삭제
* 튜플 ( )
    * __튜플은 값 수정 불가__
    * ```(튜플명)[인덱스]``` 튜플에서 인덱스 의 값 반환
* 집합 { }
    * __집합은 중복이 불가, 순서가 없음__
    * ```(집합명) & (집합명)``` 두 집합의 교집합 값 반환
    * ```(집합명).intersection(집합명)``` 두집합의 교집합 값 반환
    * ```(집합명) | (집합명)``` 두 집합의 합집합 값 반환
    * ```(집합명).union(집합명)``` 두집합의 합집합 값 반환
    * ```(1집합명) - (2집합명)``` 2집합에 없는 1집합 값 반환 
    * ```(1집합명).difference(2집합명)``` 2집합에 없는 1집합 값 반환
    * ```(집합명).add("a")``` 집합에 a 라는 값 추가
    * ```(집합명).remove("a")``` 집합안에 a 라는 값 삭제
---
## **제어문**
* if
    ```
    if 조건:  
        실행 명령문
    elif 조건:  
        실행 명령문
    else:  
        실행 명령문
    ```
* for
    ```
    for (지역변수명) in (변수명):  
        실행 명령문
    ```
* while
    ```
    while 조건:  
        실행 명령문
    ```
* continue, break
    * 반복문 에서 continue 는 조건식으로 다시 돌려보냄,  
     break는 반복문 종료
---
## **함수**
```
def 함수명( ):  
함수에서 실행될 내용
```
* __함수명( )__ 으로 함수 사용가능
* ( ) 내에 함수에서 전달받을 전달값을 넣어줄수 있음
>a 와 b 라는 변수에 값을 입력받고 두 값을 더한 값을 반환하는 함수 👇
```python
def sum(a, b):
    return a + b
```
* 키워드값 👇
```python
def example(age, gender):
    print(age, gender)

example(age = 17, gender = "Man") # 출력 결과는 17, Man 이다
```
* 지역변수 와 전역변수
    * 전역 공간에 선언한 변수 는 함수 안에서 사용 불가능
    * ```global (변수명)``` 전역 공간에 있는 변수 를 함수 내에서 사용
---
## **표준입출력**
```python
print("python", "java", sep = " vs ")
# sep는 콤마가 있는 자리마다 sep의 값을 넣어준다
# 따라서 위 코드의 실행 결과는 "python vs java" 이다
```
```python
print("python", "java", end = "?")
# end는 문장의 끝부분에 end의 값을 붙여주는 것이다
# 따라서 위 코드의 실행 결괴는 pythonjava? 가 된다
```
* __sys 모듈__
    * ```file=sys.stdout``` 표준출력으로 처리함
    * ```file=sys.stderr``` 표준에러로 처리함
* ```(변수명).ljust(a)``` a 칸을 만들고 왼쪽으로 정렬하여 반환
* ```(변수명).rjust(a)``` a 칸을 만들고 오른쪽으로 정렬하여 반환
* ```(변수명).zfill(a)``` a 칸의 공간에 값을 넣고 빈공간은 0으로 채움
* ```input( )``` 사용자에게 입력을 받을수 있는 함수
    * 숫자를 입력받아도 문자열 형태로 저장하게 됨
---
## **출력 포맷**
* ```{0: }``` 빈자리는 빈공간 으로 두기  
* ```{0:a}``` a칸만큼 공간 확보  
* ```{0:>}```오른쪽 정렬
* ```{0:<}``` 왼쪽 정렬
* ```{0:_}``` 빈자리 _ 으로 채움
* ```{0:,}``` 3자리 마다 , 찍음
* ```{0:+}``` 양수면 앞에 + 음수면 앞에 + 붙임
* ```{0:f}``` 소숫점 출력
    * ```{0:.5f}``` 소숫점 5자리 까지 출력 (6자리에서 반올림)
---
## **파일입출력**
* ```open("파일이름", "모드", encoding="utf8")```
    * 파일이름에 해당하는 파일을 정해진 모드로 utf8로 열기
```python
print("example", file=example_file)
#example_file 이라는 변수명에 있는 파일에 example라는 글을 씀
```
* ```(파일변수명).write("a")``` 파일에 a라는 글을 씀
* ```(파일변수명).read()``` 파일 내용을 읽어옴
* ```(파일변수명).readline()``` 파일내용을 줄별로 읽고 커서는 다음줄로 이동
    * ```(파일변수명).readlines()``` 👆와 기능은 같지만 리스트 형으로 저장
* ```(파일변수명).close()``` 파일 닫기
---
## **pickle 모듈**
```python
import pickle  
# 👆모듈 임포트 하기
profile_file = open("profile.pickle", "wb")  
# 👆 .pickle 형태로 만듬, b는 바이너리 모드
```
* ```pickle.dump(변수명, 파일변수명)```  
    * 변수에 있는 정보를 파일변수에 저장
* ```pickle.load(파일변수명)```  
    * 파일에 있는 정보를 불러옴
* ```(파일변수명).close( )``` 파일 닫기  
* **with**
    * with 는 pickle, txt 등 여러가지 확장자에 사용가능
    * ```with open("파일명", "모드") as (파일변수명):```  
        * 파일명 에 해당하는 파일을 지정한 모드로 불러옴
        * with 문이 끝날시 파일이 자동으로 닫힘
---
## **클래스**
```python
class example:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        # self.name, self.gender, self.age 는 멤버 변수
        print("{0} 님의 나이는 {1} 세 이고 성별은 {2} 입니다."  
        .format((self.name, self.age, slft.gender))

h1 = example("h1", 17, "남자")
h2 = example("h2", 17, "여자")
# h1 님의 나이는 17 세 이고 성별은 남자 입니다.
# h2 님의 나이는 17 세 이고 성별은 여자 입니다.
```
---
## **멤버 변수**
* 멤버 변수는 ```(변수명).(멤버 변수)``` 로 사용 가능함
---
## **메소드**
* 클래스가 갖고 있는 기능이다. 데이터와 멤버 변수에 대한 접근 권한을 갖는다.
```python
class example:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class example2:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def say(self, say):
        print("{0} 님이 {1} 라고 말함".format(self.name, say))
    # self.(변수명)은 멤버변수를 쓴다는것이고
    # (변수명)은 전달받은값 그대로를 쓴다는것
```
---
## **상속**
```python
class example:
    def __init__(self, name):
        self.name = name

class example2(example):
        def __init__(self, name, gender, age):
        # self.name = name 를 정의할 필요가 없음
        example.__init__(self.name)
        self.gender = gender
        self.age = age
# example2가 example 클래스를 상속받음
```
## **다중상속**
```python
class example1:
    def __init__(self, name):
        self.name = name

class example2(example1):
        def __init__(self, name, gender, age):
        # self.name = name 를 정의할 필요가 없음
        example1.__init__(self.name)
        self.gender = gender
        self.age = age
# example2가 example1 클래스를 상속받음

class example3:
    def __init__(self, tall):
        self.tall = tall

class exmaple4(example1, example3):
    def __init__(self, name, tall):
        example1.__init__(self, name)
        example3.__init__(self, tall)
# example4 가 exmple1, example3 를 상속받아서 사용함
```
---
## **메소드 오버라이딩**
* 자식 클래스에서 정의한 메소드를 새롭게 정의하여 사용하는것
```python
class example1:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def say(self, say):
        print("{0} 님이 {1} 라고 말함".format(self.name, say))

example_human = exmaple1("example", "남자" 17) # 클래스로 변수 선언
example.say(example.name, "test") # 메소드 오버라이딩
```
---
## **pass**
```python
class example1:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class example2(example1):
    def __init__(self, name, gender, age):
        pass # 아무것도 실행하지않고 넘어감
```
* pass 는 클래스 뿐만 아니라 함수에서도 사용이 가능함
---
## **super**
```python
class example1:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class example2(example1):
    def __init__(self, name, gender, age):
        # example1.__init__(self, name, gender, age)
        super().__init__(name, gender, age)
        # super() 는 self 를 사용하지않음
```
* ```super()``` 는 다중상속에서 문제가 발생함
    * ```def (클래스명)._init__``` 으로 해결가능 (단 self 를 포함)
---
## **예외처리**
* 어떠한 에러가 발생했을때 그 에러에 대한 처리를 하는것
```python
try:
    #실행할 문장들
except (에러명1):
    #에러 발생시 실행할 문장
except (에러명2):
    #여러 에러에 대비 가능
except:
    #원하는 에러가 아닌 나머지 오류에 대한 대비
```
---
## **에러 발생시키기**
* 의도적으로 에러가 필요할때 발생시킬수 있음
```python
try:
    #실행할 문장들
    raise (에러명) #에러명에 해당하는 에러를 발생
except (에러명):
    #에러 발생시 실행할 문장들
```
---
## **사용자 정의 예외처리**
* 사용자가 원하는 에러를 만들어서 필요할때 사용 가능
```python
class exampleError(Exception):
    # Error 클래스 내의 내용
try:
    #실행 문장
    raise exampleError
except exmapleError:
    #사용자 정의 에러 발생시 실행할 문장
```
---
## **finally**
* try 문 내의 마지막에 쓸수있음
```python
try:
    #내용
finally:
    #try 문이 끝날때 실행할 내용
    #에러가 발생해도 finally문은 실행 됨
```
---
## **모듈**
* 필요한 것들이 모아져 있는 파일
* 확장자는 .py 임
```python
#example1.py
def example(name):
    print("안녕하세요 {0}님".format(name))
#main.py
#import 모듈명 은 모듈에 있는 모든걸 가져오느것
#위의 문장은 from 모듈명 import * 와 같은 의미
#import 모듈명 은 사용할때 모듈명.함수이름 이로 해야함
#from 모듈명 improt * 은 사용할떄 모듈명 생략 가능
import exmaple1
example1.example("test")
#import 모듈명 as 원하는 이름 을 하게 되면 다음부터 원하는 이름으로 호출 가능
import example1 as ex1
ex1.example("test")
#from 모듈명 import 함수명 은 모듈에서 자신이 지정한 함수 가져오기 함수를 사용할때 모듈명이 생략 됨
from example1 import example
example("test")
```
---
## **패키지**
* 패키지는 모듈이 모인 집합 이다
* 하나의 디렉토리에 여러 모듈 파일을 넣은것이 패키지 이다
* ```import 패키지명.모듈```
    * 객체를 만들때 패지키명.모듈명.클래스이름() 으로 사용해야함
    * 클래스 안에 있는 함수는 .함수명()으로 사용 가능
* ```from 패키지명.모듈명 import 클래스명```
    * 객체를 만들때는 클래스이름()
    * 클래스 안에 있는 함수는 .함수명()으로 사용 가능
* ```from 패키지명 import 모듈명```
    * 객체를 만들때는 모듈명.클래스명()
    * 클래스 안에 있는 함수는 .함수명()으로 사용 가능
---
## **\_\_all\_\_**
* ```from 패키지명 import *```
    * 패키지의 공개 범위를 설정하지 않아서 위 문법은 사용을 못함
* \_\_init\_\_.py 파일 안에 ```__all__ = ["모듈명"]``` 을 해줘야함
    * ```__all__ = ["모듈명"]``` 해준 파일은 ```from 패키지명 import *```이 사용 가능해짐