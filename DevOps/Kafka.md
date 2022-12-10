## Kafka란
Pub-Sub 모델의 메시지 큐  
분산환경에 특화되어있는 특징을 가지고 있음

## Kafka 구성요소
1. Event
    * Event는 Kafka에서 Producer와 Consumer가 데이터를 주고 받는 단위
2. Producer
    * Producersms Kafka에 이벤트를 게시(POST)하는 클라이언트 어플리케이션을 의미함
3. Consumer
    * Consumer는 이러한 Topic을 구독하고 얻어낸 이벤트를 처리하는 클라이언트 어플리케이션
4. Topic
    * 이벤트가 쓰이는 곳, Producer는 이 Topic에 이벤트를 게시함
    * Consumer는 Topic으로 부터 이벤트를 가져와 처리함
    * Topic은 파일시스템의 폴더와 유사하며, 이벤트는 폴더안의 파일과 유사함
    * Topic에 저장된 이벤트는 필요한 만큼 다시 읽을 수 있음
5. Partition
    * Topic은 여러 Broker에 분산되어 저장되며, 이렇게 분산된 Topic을 Partition이라고 함
    * 어떤 이벤트가 Partition에 저장될지는 이벤트의 key에 의해 정해지며, 같은 키를 가지는 이벤트는 항상 같은 Partition에 저장됨