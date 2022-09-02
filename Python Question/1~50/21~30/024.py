# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

N = int(input())
d = 2

while N != 1:
    if N % d != 0:
        d += 1
    else:
        N //= d
        print(d)