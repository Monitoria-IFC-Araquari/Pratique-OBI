import math

N , M = map(int, input().split())

for i in range(M, 0, -1):
    if math.gcd(i, N) == 1:
        print(i)
        break
    