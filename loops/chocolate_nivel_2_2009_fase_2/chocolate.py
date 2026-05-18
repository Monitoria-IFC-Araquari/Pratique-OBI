n, m = map(int, input().split())
value = [0] * (n + 1)
value[0] = -2
minus_two = []
single_hits = [[] for _ in range(n + m + 1)]
all_cnt = 1
minus_two.append(0)

for i in range(1, n + 1):
    if i - m - 1 >= 0:
        if value[i - m - 1] == -2:
            all_cnt -= 1
            if minus_two and minus_two[0] == i - m - 1:
                minus_two.pop(0)

    single_cnt = len(single_hits[i])
    single_val = single_hits[i][0] if single_cnt == 1 else None
    total = all_cnt + single_cnt

    if total == 0:
        value[i] = -2
        all_cnt += 1
        minus_two.append(i)
    elif total == 1:
        if single_cnt == 1:
            v = single_val
        else:
            j = minus_two[0]
            v = i - j
        value[i] = v
        if v > 0 and i + v <= n:
            single_hits[i + v].append(v)
    else:
        value[i] = -1

print('Paula' if value[n] != -2 else 'Carlos')
