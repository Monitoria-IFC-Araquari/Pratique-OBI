tab = [list(map(int, input().split())) for _ in range(15)]
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
winner = 0
for i in range(15):
    for j in range(15):
        if tab[i][j] == 0:
            continue
        for di, dj in directions:
            if 0 <= i + 4 * di < 15 and 0 <= j + 4 * dj < 15:
                if all(tab[i + k * di][j + k * dj] == tab[i][j] for k in range(5)):
                    winner = tab[i][j]
                    break
        if winner:
            break
    if winner:
        break
print(winner)
