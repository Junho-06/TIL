## RDS란
Relational DataBase Service의 약자로 관계형 데이터베이스로 세상에 존재하는 많은 데이터베이스 서비스들을 제공함

---
### RDS 종류
* Micrsoft SQL, Oracle, MySQL, Postgre, Aurora, Maria DB

---
### RDS 2가지 데이터 백업 기능
1. Automated Backups(자동백업)  
    * Retention Period(1~35일)안의 어떤 시간으로 돌아가게 할 수 있음
    * AB는 그날 생성된 스냅샷과 Transaction logs(TL)을 참고함
    * 디폴트로 AB기능이 설정되어 있으며 백업 정보는 S3에 저장
    * AB동안 약간의 I/O suspension 이 존재할 수 있음

2. DB snapshots(데이터베이스 스냅샷)
    * 주로 사용자에 의해 실행됨
    * 원본 RDS Instance를 삭제해도 스냅샷은 존재함