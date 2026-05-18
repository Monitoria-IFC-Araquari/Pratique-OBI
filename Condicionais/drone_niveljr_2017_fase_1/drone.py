A = int(input())
B = int(input())
C = int(input())
H = int(input())
L = int(input())

if (A <= H and B <= L) or (A <= L and B <= H): 
    print("S") 
elif (A <= H and C <= L) or (A <= L and C <= H): 
    print("S") 
elif (B <= H and C <= L) or (B <= L and C <= H): 
    print("S") 
else: 
    print("N")
