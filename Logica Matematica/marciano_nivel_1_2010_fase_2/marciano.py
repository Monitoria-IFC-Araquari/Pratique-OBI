L, A, P, R = map(int, input().split())
d = L * L + A * A + P * P
print('S' if d <= 4 * R * R else 'N')
