A, L = map(int, input().split())
N = int(input())
best_id = -1
best_waste = 10**9
for i in range(1, N + 1):
    X, Y = map(int, input().split())
    if (X >= A and Y >= L) or (X >= L and Y >= A):
        waste = X * Y - A * L
        if waste < best_waste or (waste == best_waste and i < best_id):
            best_waste = waste
            best_id = i
print(best_id)
