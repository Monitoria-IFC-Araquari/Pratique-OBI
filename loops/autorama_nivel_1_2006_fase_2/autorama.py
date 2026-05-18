K, N, M = map(int, input().split())
expected = [1] * (N + 1)
count = [0] * (N + 1)
last_time = [0] * (N + 1)

for t in range(1, M + 1):
    X, Y = map(int, input().split())
    if Y == expected[X]:
        count[X] += 1
        expected[X] = Y % K + 1
        last_time[X] = t

cars = list(range(1, N + 1))
cars.sort(key=lambda x: (-count[x], last_time[x]))
print(' '.join(map(str, cars)))
