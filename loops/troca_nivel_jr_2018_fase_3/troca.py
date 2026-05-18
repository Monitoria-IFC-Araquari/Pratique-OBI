def solve():
    n, t = map(int, input().split())
    cima = list(map(int, input().split()))
    baixo = list(map(int, input().split()))
    diff = [0] * (n + 2)
    for _ in range(t):
        i, j = map(int, input().split())
        diff[i] += 1
        diff[j + 1] -= 1
    curr = 0
    out = []
    for i in range(n):
        curr += diff[i + 1]
        if curr % 2 == 0:
            out.append(cima[i])
        else:
            out.append(baixo[i])
    print(' '.join(map(str, out)))

if __name__ == '__main__':
    solve()
