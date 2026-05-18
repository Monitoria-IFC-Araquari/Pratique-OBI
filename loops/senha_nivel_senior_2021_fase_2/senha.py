N, M, K = map(int, input().split())
passwd = list(input().strip())
words = [input().strip() for _ in range(M)]
letter_pos = [i for i, ch in enumerate(passwd) if ch == '#']
P = int(input())
for _ in range(P):
    idx = int(input())
    for i, pos in enumerate(letter_pos):
        passwd[pos] = words[i][idx - 1]
print(''.join(passwd))
