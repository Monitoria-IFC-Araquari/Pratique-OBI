A, B, C, D = list(map(int, input().split()))

if B == D:
    fracao = (A + C) / B
    print(int(fracao), int(fracao / D))
else:
    mmc = B * D
    num1 = A * D
    num2 = B * C
    print(int(num1 + num2), int(mmc))
