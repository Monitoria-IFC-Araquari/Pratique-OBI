a = str(input())
b = str(input())

if(len(b) > len(a)):
    a = '0' + a[0:]
elif(len(a) > len(b)):
    b = '0' + a[0:]

a_list = list(a)
b_list = list(b)

for i in range(len(a)):
    if(int(b[i]) > int(a[i])):
        a_list.remove(a[i])
    elif(int(a[i]) > int(b[i])):
        b_list.remove(b[i])
 
if(len(a_list) == 0):
    print(''.join(b_list), -1)
elif(len(b_list) == 0):
    print(-1, ''.join(a_list))
else:
    print(''.join(a_list), ''.join(b_list))

