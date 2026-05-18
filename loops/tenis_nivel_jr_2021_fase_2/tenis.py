A = int(input()) 
B = int(input()) 
C = int(input()) 
D = int(input()) 


times = [A, B, C, D] 
menor_diferenca = float('inf') 

for i in range(4): 
    for j in range(i + 1, 4): 
        time1 = [times[i], times[j]] 
        time2 = [times[k] for k in range(4) if k != i and k != j] 
         
        diferenca = abs(sum(time1) - sum(time2))  
    
        if diferenca < menor_diferenca: 
            menor_diferenca = diferenca

print(menor_diferenca) 