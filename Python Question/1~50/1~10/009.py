# 세 자리 자연수가 주어질 때 각 자리수의 위치에 들어갈 값을 구하는 프로그램을 작성하시오.

A = int(input())
B = int(input())

print(A * (B % 10))
print(A * (B % 100 // 10))
print(A * (B // 100))
print(A * B)