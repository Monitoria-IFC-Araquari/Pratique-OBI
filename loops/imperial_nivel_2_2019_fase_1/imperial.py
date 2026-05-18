 # Esse valor é a quantidade máxima de números da sequência que poderiam ser marcados com um círculo, de modo que a sequência de números marcados não contenha dois números iguais consecutivos e seja composta de no máximo dois números distintos.

N = int(input())
nums = []
todos = []
contagens = []


sequencia = 0
i = 0 

while i < N:
    num = int(input())
    nums.append(num)
    if(not(num in todos)):
      todos.append(num)
    i += 1
tamanho = len(todos)
if(tamanho==1):
  contagens.append(1)
else:
  for i in range(tamanho): 
    for j in range(tamanho):
      if(todos[i]!=todos[j]):
        procurar='i'
        contagem=0
        for k in range(len(nums)):
          if(procurar=='i' and nums[k]==todos[i]):
            contagem+=1
            procurar='j'
          elif(procurar=='j' and nums[k]==todos[j]):
            contagem+=1
            procurar='i'
        contagens.append(contagem)

print(max(contagens))
