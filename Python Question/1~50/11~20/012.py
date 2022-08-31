# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T = int(input())
i = 1

while (i <= T) :
    a, b = map(int, input().split())
    print("Case #%d: %d" %(i, (a+b)))
    i = i + 1