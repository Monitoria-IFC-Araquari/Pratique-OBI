qtd = int(input())
valores = []
soma = 0
i = 0

while(i < qtd):
  nums = int(input())
  valores.append(nums)
  i += 1

valores.sort(reverse=True)

j = 2
while(j < qtd):
  #valores.pop(j)
  valores[j] = 0
  j += 3

for index in range(len(valores)):
  soma += valores[index] 
  
print(soma)