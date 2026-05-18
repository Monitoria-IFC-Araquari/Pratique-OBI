def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    l = int(input_data[1])
    tempos = list(map(int, input_data[2:2 + l]))
    count = [0] * n
    free_time = [0] * n
    for t in tempos:
        min_free = min(free_time)
        idx = free_time.index(min_free)
        count[idx] += 1
        free_time[idx] += t
    for i in range(n):
        print(i + 1, count[i])

if __name__ == '__main__':
    solve()
