N = int(input())

P, C, Q = input().split()

P = int(P)
Q = int(Q)

if C == "+":
    resultado = P + Q
else:
    resultado = P * Q

if resultado > N:
    print("OVERFLOW")
else:
    print("OK")