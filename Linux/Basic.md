# **Network**
> **리눅스의 기초를 공부한걸 정리한 내용**
---
## **리눅스란??**
* 리눅스란 리누즈 토발즈에 의해 만들어진 컴퓨터 운영체제로, 자유 소프트웨어와 오픈 소스 개발의 가장 유명한 포본임
* 컴퓨터 역사상 가장 많은 참여자가 관여하고 있는 오픈소스로 누구나 개발에 참여하고 코드를 볼 수 있는 프로젝트임
---
## **리눅스의 구조**
![리눅스의 구조](https://velog.velcdn.com/images%2Fsoryeongk%2Fpost%2F358065f9-38a7-461c-ba26-c3891a92b106%2Fimage.png)
* 위 사진은 리눅스의 기본 구조로 크게 4가지로 분류 가능함
    * office 등의 문서편집기 혹은 웹브라우저와 같은 ```응용프로그램``` 에서 사용자가 명령을 내리면```shell(쉘)``` 은 이 명령을 해석함 그래서 쉘은 명령어 해석기 라고도 불림
    * 해석된 명령어를 ```kernel(커널)``` 에게 전달함, 커널은 ```하드웨어```를 제어하는 코드를 통해 소프트웨어와 커뮤니케이션을 하며, 시스템의 모든 자원을 통제/관리하는 역할을 수행함
    ---
## **리눅스의 특징과 종류**
* 리눅스는 UNIX(유닉스) 라는 운영체제를 기반으로 하고 있고, 뛰어난 안정성과 보안성, 높은 신뢰성과 성능이 특징임
* 시스템의 자원을 효율적으로 관리 및 사용할수 있으며, 멀티유저 와 멀티 태스킹을 지원하고 있음
    * ```Multi-User``` : 여러사 용자가 동시에 하나의 시스템에 접근할 수 있음
    * ```Multi-Tasking``` : 여러 개의 task(작업)를 동시에 실행하고, 교대로 컴퓨터의 자원을 사용할 수 있는 기능
* 대부분의 리눅스는 CLI(명령어창)와 GUI(그래픽)를 모두 지원하고 있고, 다양하고 강력한 네트워킹 기능 덕분에 서버용OS로 적합함
* PC서버에서도 엔터프라이즈 급의 성능을 제공하고, 성능이 낮은 PC에서도 작동함
* 오픈소스 프로젝트이기 때문에 커널 소스코드 및 모든 관련 자료가 공개되어 빠른 발전을 지원하고 있음
* 다양한 업무환경을 만족시키는 배포판이 존재하고 풍부한 응용프로그램을 제공하고 있음
    |패키지 형식|패키지 관리자|운영체제|
    |:---:|:---:|:---:|
    |레드헷(.rmp)|yum|CentOS, 페도라|
    |데비안 레드헷(.deb)|apt|우분투, 리눅스, 민트, 라즈비안|
    |안드로이드(.apk)|Android Package Manager|안드로이드 OS|
    ---
## **가장 사용도가 높은 리눅스**
* 우분투는 리눅스 중에서도 가장 높은 인지도를 자랑함
    * 데비안 GNU/Linux를 기반으로 제작된 데스크탑 환경을 사용하는 리눅스 배포판임
* 개인용 PC 환경에 최적화 되어있고, 간결하고 쉽게 사용할 수 있다는 점이 큰 장점임
* 높은 인지도와 많은 사용자를 보유하고 있어서 그에 따른 커뮤니티도 많음
---
## **GUI vs CLI**
* 대부분의 리눅스가 GUI와 CLI를 지원하고 있다고 함
* 이 둘은 각각 ```그래픽창```, ```명령창```을 의미함
* GUI(Graphical User Interface)
    * 일반적인 사용자가 흔히 사용하는 인터페이스와 비슷함
    * 사용자가 편리하게 사용할 수 있도록 기능을 아이콘, 이미지 등의 그래픽으로 나타낸 인터페이스임
    * 마우스 클릭이나 드래그앤드롭이 가능하고 수시로 확인이 가능하여 사용이 쉬움
* CLI(Command Line Interface)
    * 문자로 사용자와 컴퓨터가 상호작용하여 동작하는 인터페이스임
---
## **패키지 관리자 - apt**
* Advanced Packaging Tool의 약자로 데비안 리눅스(.dev) 또는 파생된 배포판(우분투)에서 소프트웨어를 설치, 제거, 업데이트할 때 사용함
* 과거에는 설치, 제거, 업데이트에서 ```apt-get```을, 검색과 확인에서는 ```apt-cache```를 따로 사용했음 최근에는 모두 ```apt```로 통일됨 
* 높은 권한이 필요한 활동에 대해서는 ```apt``` 앞에 ```sudo```를 함께 입력하여 권한을 획득해야 함
    * 권한, sudo
        * 패키지 설치와 같은 활동에서는 ```apt install ~~~```을 입력했을 때 ```permission denied```라는 메세지와 함께 활동이 제한될 수 있음
        * 이때 ```sudo```를 입력 함으로써 리눅스에서 모든 권한을 가지고 있는 최고 관리자 root의 권한을 획들할 수 있음
        * root는 운영체제의 모든 것을 제어할 권리를 가짐
    * 폴더별 권한
        * ```ls -al```명령어를 통해 모든 파일의 모든 속성을 확인할 수 있음
---
## **리눅스 파일 시스템**
* 파일이란, 주기억장치나 디스크처럼 하드웨어 저장공간에 저장되는 데이터 집합을 말함
* 파일시스템이란, 저장 장치 내에서 데이터를 읽고 쓰기 위해 미리 정한 약속임
* 하드디스크와 ssd는 데이터가 저장된 위치가 이 약속에 따라 달라짐
    * 때문에 파일 저장 및 검색을 할 수 있도록 관리하는 방법도 파일시스템이라고 말함
* 파일을 어떻게 관리할것인가에 대한 정책이라고 생각하면됨
* 대부분의 파일 시스템은 디렉토리와 파일의 형태로 구성되어 있음
* 리눅스의 파일 시스템은 root 파일 아래에 계층적으로 모든 파일과 디렉토리가 만들어짐
## **파일시스템의 종류**
* FAT: File Allocate Table
    * 파일 할당 테이블이라고 말하며, 디지털 카메라 등에 장착되는 대부분의 메모리 카드와 수많은 컴퓨터 시스템에 널리 쓰이는 파일 시스템의 종류임 
    * 너무 단순한 자료구조 탓에 작은 파일이 여러개 있을 경우 공간 활용을 제대로 하지 못한다는 단점이 있음 
    * 용량이 계속 커지고 있으며, 높은 호환성을 가짐
* NTFS: New Technology File System
    * Windows NT 계열의 새로운 파일 시스템으로 기존의 FAT 구조를 대체하기위해 만들어졌음 
    * 시스템 고장 및 손상 시, 디스크 볼륨을 재구성하여 일관성있는 상태로 복구가 가능하여 안정성이 높고, 보안성도 FAT보다 향상된 파일 시스템임
* EXT: EXTended file system
    * 확장 파일 시스템의 준말로 리눅스의 기본 파일 시스템임 
    * 성능을 향상시키면서 시리즈로 출시되고 있는데, 기본으로 사용되던 2차 확장 파일 시스템 EXT2를 완벽하게 호환하는 EXT3와 EXT4가 있음 
    * EXT3부터 큰 규모의 디렉토리를 접근하기 위해 해쉬를 통해 접근하는 H-tree를 사용하여 데이터 검색이 보다 용이해졌고, EXT4는 지금까지 중 가장 큰 초대형 파일 시스템임
## **리눅스 디렉토리의 구조**
* 모든 디렉토리는 최상위 디렉토리인 root이 하위로 만들어짐  

🌱root  
 ┣ 📦bin  
 ┣ 📦home  
 ┃ ┣ 📂soryeongk  
 ┃ ┃ ┣ 📂바탕화면  
 ┃ ┃ ┣ 📂폴더  
 ┃ ┃ ┗ 📜index.html  
 ┣ 📦lib  
 ┣ 📦user   
 ┣ 📦boot  
 ┗ 📦etc  
* bin: 기본 명령어들이 저장된 폴더
* boot: 리눅스의 boot(시작)와 관련한 명령이 들어간 폴더
* etc: 리눅스의 거의 모든 설정 파일이 들어간 폴더
* home: 말그대로 홈 폴더, 로그인한 계정에 따라  폴더가 만들어짐
* lib: 리눅스 및 각종 프로그램에서 사용되는 라이브러리들의 폴더
---
## **리눅스 명령어**
* ```head```, ```tail``` : 각각 처음과 끝의 N줄을 출력해주는 명령어로 ```cat```과 함께 자주 쓰임
    * 사용법 : ```cat [filename] | head -n[N]``` ```cat [filename] | tail -n[N]```
* ```alias``` : 지정 명령어
* ```su``` : 현재 사용자 변경하는 명령어
    * 사용법 : ```su [계정명, 없으면 root로]```를 입력하고 비밀번호 입력
* ```more``` : cat과 달리 화면 단위로 출력하며, 스페이스바로 한 칸씩 내리면서 내용 확인 가능
    * 사용법 : ```more [filename]```
* ```which``` : 절대 경로를 알려주는 것으로 명령어의 위치도 알 수 있음
* ```wc``` : 파일의 바이트, 문자, 단어 라인 수를 출력해주는 명령어
    * 사용법 : ```wc [option] [filename]```
* ```shutdown``` : 시스템 종료 및 재부팅 명령어
    * 사용법 : ```shutdown -r now``` : 즉시 재부팅  
    ```shutdown -h now``` : 즉시 종료
* ```diff``` : 두 파일 간의 차이를 보여주는 명령어
    * 사용법: ```diff [filename1] [filename2]``` filename1과 filename2의 차이를 보여줌
## **File Redirection**
* 표준 스트림의 흐름을 바꾸어 일반적인 표준 스트림(표준 입력 및 출력 그리고 오류)를 사용하지 않고 다른 경로인 파일로 재지정하는 것을 뜻함
* ```<```와```>```를 이용하여 사용 가능함
    * 표준스트림 이란 유닉스(unix)와 유닉스계열의 OS(linux, mac 등)에서 컴퓨터 프로그램과 단말기 사이에 존재하는 통로를 의미함
    * 표준스트림은 단말기와 프로그램 사이에서 일어나는 데이터 입출력을 추상화한 것
        * stdin: 표준입력-키보드 입력
        * stdout: 표준 출력-화면 출력(cat, ls)
        * stderr: 표준 오류 출력
## **piping command**
* file redirection 과 유사한 pipe는 ```|```로 명령을 구분함
* 여러가지 복잡한 명령어를 병렬로 작성할수 있음
---
## **리눅스의 메모장, nano editor**
* UNIX 호환 시스템에서 사용 가능한 가볍고 간단한 텍스트 에디터로, 손쉽게 파일 내용 수정이 가능함
    |단축키|기능|
    |:---:|:---:|
    |ctrl + o|저장|
    |ctrl + x|종료|
    |ctrl + w|검색|
    |Alt + 6|복사|
    |ctrl + u|붙여넣기|
    |ctrl + ^|여러 줄 선택|