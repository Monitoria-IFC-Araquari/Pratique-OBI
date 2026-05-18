N = int(input())
mem = [int(input()) for _ in range(N)]
outs = []
i = 0
while i < N:
    if mem[i] == 1:
        x = mem[i + 1]
        y = mem[i + 2]
        mem[x] ^= 1
        mem[y] ^= 1
        i += 3
    elif mem[i] == 2:
        x = mem[i + 1]
        y = mem[i + 2]
        mem[x] = mem[x] + mem[y]
        i += 3
    else:
        outs.append(mem[i])
        i += 1
print('\n'.join(map(str, outs)))
