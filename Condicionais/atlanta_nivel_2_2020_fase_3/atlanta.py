import math

A = int(input())
B = int(input())

if A % 2 != 0:
    print("-1 -1")
else:
    S = A // 2 + 2
    disc = (S - 4) * (S - 4) - 4 * B
    if disc < 0:
        print("-1 -1")
    else:
        sqrt_disc = int(math.isqrt(disc))
        if sqrt_disc * sqrt_disc != disc:
            print("-1 -1")
        else:
            a = (S - 4 - sqrt_disc) // 2
            b = (S - 4 + sqrt_disc) // 2
            L = a + 2
            C = b + 2
            if a < 0 or b < 0 or (S - 4 - sqrt_disc) % 2 != 0 or (S - 4 + sqrt_disc) % 2 != 0:
                print("-1 -1")
            elif L > C:
                print(C, L)
            else:
                print(L, C)
