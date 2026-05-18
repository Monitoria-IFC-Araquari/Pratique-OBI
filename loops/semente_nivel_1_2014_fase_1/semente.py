F, R = map(int, input().split())
germ = [float('inf')] * F
for _ in range(R):
    r = int(input()) - 1
    for i in range(F):
        germ[i] = min(germ[i], abs(i - r))
print(max(germ))
