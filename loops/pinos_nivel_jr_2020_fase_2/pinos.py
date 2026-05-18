jogo = []
jogadas = 0

for i in range(7):
    ent = list(map(str, input().strip()))
    new_arr = ['0'] + ent + ['0']  
    jogo.append(new_arr)

jogo.insert(0, ['0'] * 9) 
jogo.append(['0'] * 9)     

for i in range(1, len(jogo)-1):
    for j in range(1, len(jogo)-1):
        if jogo[i][j] == 'o':
            if jogo[i-1][j] == 'o' and jogo[i-2][j] == '.':
                jogadas += 1 
            if jogo[i+1][j] == 'o' and jogo[i+2][j] == '.':
                jogadas += 1 
            if jogo[i][j-1] == 'o' and jogo[i][j-2] == '.':
                jogadas += 1  
            if jogo[i][j+1] == 'o' and jogo[i][j+2] == '.':
                jogadas += 1 

print(jogadas)