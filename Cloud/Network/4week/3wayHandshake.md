## 3way HandShake

패킷이 어떻게 보내지느냐에 따라 달라짐

* ### 3way HandShake는 ```Syn```->```Syn + Ack```->```Ack```

* 보내는 PC에서 Syn이라는 것에 Sequence번호와 AckNum이라는 번호, WindowSize, myWindowSize를 담아서 보내게 됨
    * WindowSize : 받는 PC에서 쓸 값을 넣으라고 보냄  
    Squence번호 : 식별값  
    myWindowSize : 기본 65536

* 받은 PC는 receive 상태가 되고  자신의 squence넘버를 지정하고, AckNum은 받은 Sequence + 1 을 하고 받은PC의 WindowSize까지 반환함

* 보냈던 PC는 Syn에 상대방이 보낸 AckNum 번호를 sequence번호로 넣고 Acknum은 받은 squence번호를 넣어서 반환하게 되면 ```Established``` 상태가 되게 됨

* 중간에 패킷을 보냇는데 windowsize에 문제가 있다면 패킷 전송을 보류해놓고 패킷을 보낸쪽으로 지속적으로 windowsize를 물어보게 됨