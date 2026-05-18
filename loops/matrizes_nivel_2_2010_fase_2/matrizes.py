N = int(input())
P, Q, R, S, X, Y = map(int, input().split())
I, J = map(int, input().split())

ans = 0
for k in range(1, N + 1):
    a = (P * I + Q * k) % X
    b = (R * k + S * J) % Y
    ans += a * b
print(ans)
