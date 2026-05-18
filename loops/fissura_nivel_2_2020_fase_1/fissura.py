N, F = map(int, input().split())
matriz=[]


for i in range(N):
  R = input()
  linha = []
  for i in range(N):
    linha.append(R[i])
  matriz.append(linha)    


checar = [[0,0]]
while len(checar):
  x,y = checar.pop()
  if(matriz[x][y] != "*" and F >= int(matriz[x][y])):
    matriz[x][y] = '*'
    if x < N-1:
      checar.append([x+1,y])
    if y < N-1:
      checar.append([x,y+1])
    if x > 0:
      checar.append([x-1,y])
    if y > 0:
      checar.append([x,y-1])

for i in range(len(matriz)):
  print(''.join(matriz[i]))