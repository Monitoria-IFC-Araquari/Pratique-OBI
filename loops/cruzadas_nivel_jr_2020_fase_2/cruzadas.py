H = input()
V = input()

index_H = -1
index_V = -1

for i, letra_H in enumerate(H):
    for j, letra_V in enumerate(V):
        if letra_H == letra_V:
            if i > index_H or (i == index_H and j > index_V):
                    index_H = i
                    index_V = j

if index_H == -1:
    print(-1, -1)
else:
    print(index_H + 1, index_V + 1)
    