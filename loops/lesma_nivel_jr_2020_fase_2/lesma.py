A = int(input())
S = int(input())
D = int(input())

i = 0
d = 0

while i < A:
    i += S 
    d += 1
    
    if i >= A:
        break
    
    i -= D
    

print(d)

