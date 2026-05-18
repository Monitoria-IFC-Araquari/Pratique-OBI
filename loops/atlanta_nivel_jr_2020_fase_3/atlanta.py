A = int(input())
B = int(input())

for L in range(3, int((A + B) ** 0.5) + 2):
        if (A + B) % L == 0:
            C = (A + B) // L
            if C >= 3:
                if A == (L * C) - (L - 2) * (C - 2) and B == (L - 2) * (C - 2):
                    print(max)