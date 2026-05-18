N = int(input())

CN = []
tempo = 0
T = []

for _ in range(N):
    parts = input().split()
    M = parts[0]
    C = int(parts[1])

    if M == "R":
        CN.append(C)
    elif M == "E":
        CN.append(C)
        T.append(tempo)
    else:
        tempo += C
