N, M = map(int, input().split())
x, y = 0, 0
escaped = False
for _ in range(N):
    C, D = input().split()
    D = int(D)
    if C == 'N':
        y += D
    elif C == 'S':
        y -= D
    elif C == 'L':
        x += D
    elif C == 'O':
        x -= D
    if x * x + y * y > M * M:
        escaped = True
print(1 if escaped else 0)
