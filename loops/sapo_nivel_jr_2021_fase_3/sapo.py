M, N = map(int, input().split())
P = int(input())
lago = []
is_possible = 'S'
for i in range(P):
    posicoes = list(map(int, input().split()))
    lago.append(posicoes)

for i in range(P-1):
    cond_X = lago[i][0] - lago[i+1][0] > 3 or lago[i+1][0] - lago[i][0] > 3
    cond_Y = lago[i][1] - lago[i+1][1] > 3 or lago[i+1][1] - lago[i][1] > 3 
    if(cond_Y or cond_X):
        is_possible = 'N'
        break  

S_C, S_L = map(int, input().split())
R_C, R_L = map(int, input().split())

print(is_possible)