V = int(input())
P, C, Q = list(map(str, input().split()))

if C == '*':
    resultado = int(P) * int(Q)

    if resultado > V:
        print('OVERFLOW')
    else:
        print('OK')
else:
    resultado = int(P) + int(Q)

    if resultado > V:
        print('OVERFLOW')
    else:
        print('OK')
