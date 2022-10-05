## su와 sudo의 차이
* sudo는 현재 유저에서 일시적으로 super user의 권한을 빌릴 때 사용하며, su는 아예 super user로 접속한 상태
* ```su -root```처럼 root유저로 접속하게 되면 exit명령을 사용하기 전까지는 권한이 유지됨
1. sudo 는 우분투유저에서 일시적으로 super user의 권한을 빌릴 때
2. su 는 아예 super user로 접속하는 것