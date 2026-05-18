A, B, C = map(int, input().split())
H, L = map(int, input().split())
dims = [A, B, C]
ok = False
for i in range(3):
    for j in range(i+1, 3):
        x, y = dims[i], dims[j]
        if (x <= H and y <= L) or (x <= L and y <= H):
            ok = True
print('S' if ok else 'N')
