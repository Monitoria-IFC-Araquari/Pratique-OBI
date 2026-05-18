import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    notas = list(map(int, data[1:1+n]))
    freq = [0] * 101
    for v in notas:
        freq[v] += 1
    maxf = max(freq)
    for v in range(100, -1, -1):
        if freq[v] == maxf:
            print(v)
            return

if __name__ == "__main__":
    solve()
