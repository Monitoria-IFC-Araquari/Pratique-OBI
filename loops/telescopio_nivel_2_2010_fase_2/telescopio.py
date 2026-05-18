def solve():
    a = int(input())
    n = int(input())
    count = 0
    for _ in range(n):
        f = int(input())
        if f * a >= 40000000:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()
