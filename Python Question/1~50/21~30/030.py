# 두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성하시오.

while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")