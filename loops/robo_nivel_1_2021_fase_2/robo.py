N, C, S = map(int, input().split())
cmds = list(map(int, input().split()))
pos = S
ans = 1
for cmd in cmds:
    pos = (pos + cmd - 1) % N + 1
    if pos == S:
        ans += 1
print(ans)
