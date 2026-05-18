N, P = map(int, input().split())
I, R = map(int, input().split())
contaminados = set()
contaminado_existe = False
i = 0

while(i < P):
    A, *ID = map(int, input().split()) 
    
    i += 1

    if i == R and I in ID:
        contaminados.update(ID)
    elif i > R:
      for j in range(len(ID)-1):
        if ID[j] in contaminados:
           ID.pop(j)
           contaminado_existe = True
      if contaminado_existe:
        contaminados.update(ID)
        contaminado_existe = False
    
print(len(contaminados))