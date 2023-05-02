### 쿠버네티스를 사용해야 하는 이유
쿠버네티스는 컨테이너 오케스트레이션 시스템 이다

컨테이너 오케스트레이션 시스템에는 여러 종류가 있지만 그중에서도 쿠버네티스를 왜 사용해야 할까?

1. Planet Scale
* 구글에서 수 십억 개의 컨테이너를 운영할 수 있게 한 원칙 유지
* 행성 규모로 확장할 수 있는 스케일

2. Never Outgrow
* 다양한 요구사항을 만족할 수 있는 유연함
* 테스트용 로컬 규모부터 글로벌 서비스 규모까지 유연하게 크기 조정 가능
* 필요한 기능이 없을 경우 CRD를 통환 확장 가능

3. Run Anywhere
* 온프레미스 / 퍼블릭 클라우드 / 하이브리드 환경 어디서나 동작함
* 대부분의 리눅스 환경에서 동작하기 때문에 환경 이동에 제약이 없음