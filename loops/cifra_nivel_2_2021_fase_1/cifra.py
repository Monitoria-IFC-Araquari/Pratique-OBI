alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
novapalavra = []

c = input()

for i in range(len(c)):
  if c[i] in vogais:
    novapalavra.append(c[i])
  else:
    letraposicao = alfabeto.index(c[i])
    novapalavra.append(c[i])
    tamanho = len(alfabeto)

    if c[i] == 'z':
      novapalavra.append('u')
      novapalavra.append('z')
    else:
      i=1
      consoante=''
      vogal=''
      while consoante=='' or vogal=='':
        
        if(vogal=='' and letraposicao-i>=0 and  (alfabeto[letraposicao-i] in vogais)):
          vogal = alfabeto[letraposicao-i]
        elif(vogal=='' and letraposicao+i<tamanho  and (alfabeto[letraposicao+i] in vogais)):
          vogal = alfabeto[letraposicao+i]

        if(consoante=='' and not(alfabeto[letraposicao+i] in vogais)):
          consoante = alfabeto[letraposicao+i]
        
        i+=1
      
      novapalavra.append(vogal)
      novapalavra.append(consoante)

print(''.join(novapalavra))


