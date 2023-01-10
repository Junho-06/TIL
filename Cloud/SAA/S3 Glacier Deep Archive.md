## S3 Glacier Deep Archive란
AWS 에서 제공하는 가장 저렴한 archive storage로 주로 데이터 백업 및 아카이브 저장소로 활용 된다  
  
AWS Archive 아카이빙 기능이 강화된 AWS Glacier Deep Archive 서비스도 함께 제공함  
  
AWS Giacier는 데이터 복제와 암호화 및 IAM 권한 정책을 통해 물리적/논리적으로 데이터를 보호함

## S3 Glacier Deep Archive 특징
1. 저렴한 비용  
가장 저렴한 AWS Deep Archive의 경우, 월 1$ 미만으로 1TB의 데이터를 저장할 수 있다. 단, 최소 90일 저장을 기본 정책으로 사용하기 때문에, 90일 미만에 삭제된 데이터에 대해서도 90일에 대한 저장비용이 청구됨  
데이터 송수신 비용의 경우, 서로 다른 Region에 대해서만 비용이 청구된다. 따라서, AWS Glacier와 동일한 Region에 생성된 EC2 인스턴스에서 데이터를 주고 받기 위한 추가적인 비용 부담은 없음, VAT는 별도로 적용됨

2. 아카이빙  
AWS Glacier는 아카이빙 저장소로 요청 즉시 데이터를 불러오는 것은 불가능하며 Storage class에 따라 검색 시간과 비용이 다르게 적용됨  
AWS Glacier에 데이터가 저장될 때에는, 아카이빙 되는 데이터에 대한 인덱스와 메타데이터(32KB)가 함께 저장됨  
메타데이터는 AWS Glacier에 저장된 데이터를 인식/검색 하기 위해 사용됨

3. No Key  
S3와 달리, AWS Glacier는 사용자가 업로드한 데이터에 접근하기 위한 key를 지정할 수 없음

4. 높은 안정성  
AWS Glacier는 기본적으로 하나의 Region에서 여러 AZ에 대해 데이터 복제가 asynchronous하게 이루어짐, 추가적으로 cross-region 복제도 지원함

5. LifeCycle  
사용자는 Lifecycle 설정을 통해 AWS S3 에 저장된 object중 드물게 사용되는 것들을 AWS Glacier 혹은 AWS Glacier Depp Archive로 쉽게 이전할 수 있음

6. 암호화  
AWS Glacier에 저장된 데이터는 기본적으로 저장소와 소유자만 접근 가능함, 추가적으로 저장된 데이터에 대한 암호화 기능도 제공  
데이터 암호화는 Advanced Encryption Standard(AES) 256비트 대칭키를 사용하며, 데이터 전송에 대한 보안을 위해 SSL을 지원함

7. API / SDK 지원  
AWS Glacier는 REST API 와 Java, .NET SDK를 지원함

8. 저장소 잠금  
개별 AWS Glacier 저장소에 대한 잠금 정책을 지원함  
대표적으로 Write Once Read Many(WORM) 설정을 추가하여 데이터에 대한 수정을 제한할 수 있음

9. 저장소 액세스 정책  
억세스 정책은 기본적으로 IAM을 활용한 사용자 기반 권한 정책과, 리소스 기반 권한 정책으로 나뉨  
AWS Glacer는 두 가지의 권한 정책을 모두 지원한다. 따라서, 저장소 레벨에서 모든 사용자에게 동일하게 적용되는 권한 정책