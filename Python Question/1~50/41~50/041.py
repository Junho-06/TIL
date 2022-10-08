# 각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a % b == 0:
        print("factor")
        continue
    elif b % a == 0:
        print("multiple")
        continue
    else:
        print("neither")
        continue