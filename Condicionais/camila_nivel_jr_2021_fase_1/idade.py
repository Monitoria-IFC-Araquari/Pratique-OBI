X = int(input())
Y = int(input())
Z = int(input())

if((X >= Y and X <= Z) or (X >= Z and X <= Y)):
    print(X)

elif((Y >= Z and Y <= X) or (Y >= X and Y <= Z)):
    print(Y)
 
elif((Z >= X and Z <= Y) or (Z >= Y and Z <= X)):
    print(Z)
