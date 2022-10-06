## HTTP, HTTPS

가장 큰 차이점은 보안

* HTTP는 기본으로 80port, HTTPS는 기본으로 443port

* HTTP
    * HTTP를 통해 통신을 하면 Sniffing을 통해 통신하는 정보를 볼수 있게 됨

* HTTPS
    * HTTP + SSL/TLS 통신이 HTTPS 통신이 됨
        * SSL/TLS는 secure통신이고 그중에서 암호화, 암호화는 trusted 관계가 필요함, 암호화를 풀수있는 키도 필요함
        * 이런 SSL/TLS를 HTTP에 추가한 것이 HTTPS

    * HTTPS는 양간의 암호화를 풀수있는 키를 미리 합의하고 데이터를 암호화 하여 보내게됨 