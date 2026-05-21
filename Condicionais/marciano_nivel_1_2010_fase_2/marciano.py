L, A, P, R = map(int, input().split())

diagonal2 = L**2 + A**2 + P**2
diametro2 = (2 * R) ** 2

if diagonal2 <= diametro2:
    print("S")
else:
    print("N")