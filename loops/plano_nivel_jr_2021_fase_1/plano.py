X = int(input())
mes = int(input())
nu = 0

for i in range(mes):
    qtd = int(input())
    
    nu += X - qtd
   
nu += X

print(nu)