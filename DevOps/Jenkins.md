## Jenkins란
CI(지속적인 통합)을 제공하는 CI툴  

다수의 개발자들이 하나의 프로그램을 개발할 때 버전 충돌을 방지하기 위해 각자 작업한 내용을 공유영역에 있는 저장소에 지속적으로 업로드 함으로써 지속적 통합이 가능하도록 도와줌

## 젠킨스 사용시 이점
1. 프로젝트 표준 컴파일 환경에서의 컴파일 오류 검출
2. 자동화 테스트 수행
3. 정적 코드 분석에 의한 코딩 규약 준수여부 체크
4. 프로파일링 툴을 이용한 소스 변경에 따른 성능 변화 감시
5. 결합 테스트 환경에 대한 배포작업

이 외에도 파이썬과 같은 스크립트를 이용해 손쉽게 자신에게 필요한 기능을 추가 할 수도 있음

### 젠킨스의 특징
* 각종 배치 작업의 간략화
    * CLI로 실행되던 작업들이 젠킨스 덕분에 웹 인터페이스로 손쉽게 실행할수 있음

* Build 자동화의 확립
    * 이미 빌드 관리 툴을 이용해 프로젝트를 진행하고 있다면 젠킨스를 사용하지 않을 이유가 없음
    * 젠킨스와 연동하여 빌드 자동화를 통해 프로젝트 진행의 효율성을 높일수 있음

* 자동화 테스트
    * 젠킨스는 버전관리시스템과 연동하여 코드 변경을 감지하고 자동화 테스트를 수행함

* 코드 표준 준수여부 검사
    * 실시하지 못한 코드 표준 준수 여부의 검사나 정적 분석을 통한 코드 품질 검사를 빌드 내부에서 수행함으로써 기술적 부채의 감소에도 크게 기여함

* 빌드 파이프라인 구성
    * 2개 이상의 모듈로 구성되는 레이어드 아키텍처가 적용 된 프로젝트에는 그에 따른 빌드 파이프라인 구성이 필요함
    * 젠킨스는 파이프라인 구성을 간단히 할수 있고, 스크립트를 통해서 매우 복잡한 제어까지도 가능함