## 4 Way Handshake

Established 상태에서 정상적으로 Disconect 상태로 변환 하는 것

* 4 way Hand Shake 의 순서는
```
PC 1 : FIN + ACK
👇
PC 2 : ACK
👇
PC 2 : FIN + ACK
👇
PC 1 : ACK
```
이다.

* PC1과 PC2가 4 way handshake 로 established 상태를 끊어도 정상적으로 통신이 된다면 다시 established 상태로 돌아감