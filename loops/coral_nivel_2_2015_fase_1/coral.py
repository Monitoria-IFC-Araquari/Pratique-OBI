def solve():
    N = int(input())
    notas = list(map(int, input().split()))
    media = sum(notas) // N
    mov = 0
    for n in notas:
        if n > media:
            mov += n - media
    print(mov)
solve()