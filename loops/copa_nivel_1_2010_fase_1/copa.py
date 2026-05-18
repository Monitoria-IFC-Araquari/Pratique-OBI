def solve():
    teams = [chr(ord('A')+i) for i in range(16)]
    for r in range(4):
        nxt = []
        for i in range(0, len(teams), 2):
            a, b = map(int, input().split())
            nxt.append(teams[i] if a > b else teams[i+1])
        teams = nxt
    print(teams[0])
solve()