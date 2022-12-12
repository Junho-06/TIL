## EFS란
AWS EFS(Elastic File System)은 AWS 클라우드 서비스와 온프레미스 리소스에서 사용할 수 있는 간단하고 확장 가능하며 탄력적인 파일 스토리지를 제공하는 서비스  
  
EFS는 리눅스 인스턴스를 위한 확장성, 공유성 높은 파일 스토리지로, EC2 Linux 인스턴스에 마운트된 Network File System을 통해 VPC에서 필요한 파일에 접근하거나 AWS Direct Connect로 연결된 온프레미스 서버의 파일에 접근할 수 있음

## EFS 특징
* 스케일링
    * 수천 개의 EC2에서 동시에 액세스 가능하며, 탄력적으로 파일을 추가하고 삭제함에 따라 자동으로 Auto Scaling 가능, 미리 크기를 프로비저닝할 필요가 없음
    * 페타바이트 단위 데이터까지로 확장 가능
    * 최대 1천개의 파일 시스템 생성 가능
* 가용성
    * VPC 내에서 생성되며, 파일 시스템 인터페이스를 통해 EC2에 액세스
    * 여러 가용영역에서 액세스 가능
    * 여러 가용영역에 중복 저장되기 때문에 하나의 가용영역이 파괴되더라도 다른 AZ에서 서비스 제공 가능
    * EBS와는 달리 multi AZ를 지원하고 network를 타기 때문에 security group으로 제어됨
* 스토리지 클래스
    * Standard Class
        * 자주 액세스하는 파일을 저장하는데 사용하는 클래스
    * Infrequent Access Class
        * 저장기간이 길지만 자주 액세스하지 않는 파일을 저장하기 위한 클래스
* 수명 주기 관리
    * lifecycle을 통해 잘 접근하지 않는 파일은 자동으로 EFS IA로 옮겨 저렴하게 이용할 수 있음
* 성능 모드 / 처리량 모드
    * 처리량 모드에 있어서 대부분의 파일 시스템에 Bursting Mode를 권장하지만, 처리량이 많을 경우 Provisioned Mode를 권장 함
    * 성능 모드에 있어서 액세스하는 EC2가 매우 많을 경우, MAX I/O mode를 사용하는 것이 바람직하며, 그 밖의 경우 General Mode를 사용하는 것이 권장 됨
* 파일 마운트
    * EFS DNS 이름으로 mount 해서 여러 인스턴스에서 동시에 사용할 수 있음
    * Block storage와 마찬가지로 File Stroage도 mount 하면 내 로컬의 파일 시스템처럼 사용할 수 있음
    * AWS EFS를 사용하여 기존 파일 시스템에서 AWS DataSync로 파일을 전송할 수 있음
* 파일 백업 옵션
    * DataSync
        * 온프레미스 스토리지와 AWS EFS 파일 시스템 간의 상시 연결을 유지하여 둘 사이에서 데이터를 쉽게 이동하도록 도움
        * DataSync는 대량의 데이터를 정기적으로 가져오기 및 내보내기, 일회성 데이터 마이그레이션 또는 데이터 복제 및 복구에 사용할 수 있음
        * 리전간 전송에도 AWS DataSync를 사용할 수 있음
    * AWS Transfer Family
        * SFTP, FTPS, FTP를 지원하는 완전관리형 파일 전송 서비스
        * AWS EFS 내부 및 외부 파일 전송을 가능하게 함
        * AWS Transfer Family 엔드포인트는 EFS 파일 시스템과 동일한 리전에 있어야 함
    * AWS Backup
        * AWS EFS의 백업 정책 및 예약을 자동화하고 추적함
    * EFS-to-EFS Backup
        * EFS 파일의 증분 백업을 자동으로 생성