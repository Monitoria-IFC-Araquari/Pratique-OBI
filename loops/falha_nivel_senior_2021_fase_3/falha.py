def solve():
    N = int(input())
    words = [input().strip() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            w1, w2 = words[i], words[j]
            if len(w1) != len(w2):
                continue
            for k in range(len(w1)):
                if w1[k] == w2[k]:
                    ans += 1
    print(ans)
solve()