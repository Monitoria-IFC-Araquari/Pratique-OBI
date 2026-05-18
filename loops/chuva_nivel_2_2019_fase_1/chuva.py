N, M = map(int, input().split())
matriz = []
novamatriz = []
checar = []


for i in range(N):
    vazamento = list(input())
    matriz.append(vazamento)

for i in range(M):
    if matriz[0][i]=='o':
        if(i>0):
            checar.append([0,i-1])
        if(i<M-1):
            checar.append([0,i+1])
        checar.append([1,i])
        break

while len(checar):
  i,j = checar.pop()
  if(matriz[i][j]=="." and ((i>0 and matriz[i-1][j]=='o') or (j>0 and matriz[i][j-1]=='o' and i<N-1 and matriz[i+1][j-1]=='#') or (j+1<M and matriz[i][j+1]=='o' and i<N-1 and matriz[i+1][j+1]=='#'))):
    matriz[i][j]='o'
    if j < M-1:
      checar.append([i,j+1])
    if j>0:
      checar.append([i,j-1])
    if i < N-1:
      checar.append([i+1,j])


#print(matriz)
for i in range(len(matriz)):
  print("".join(matriz[i]))
