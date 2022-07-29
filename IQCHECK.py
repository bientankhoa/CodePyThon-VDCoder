n = int(input())
a = [int(i) for i in input().split()]
if a[0] % 2 == 0 and a[1] % 2 == 0 and a[2] % 2 != 0:
    print (a[2])
    
if a[0] % 2 == 0 and a[1] % 2 != 0 and a[2] % 2 == 0:
    print (a[1])
    
if a[0] % 2 != 0 and a[1] % 2 == 0 and a[2] % 2 == 0:
    print (a[0])
    
if a[0] % 2 == 0 and a[1] % 2 != 0 and a[2] % 2 != 0:
    print (a[0])
    
if a[0] % 2 != 0 and a[1] % 2 == 0 and a[2] % 2 != 0:
    print (a[0])
    
if a[0] % 2 != 0 and a[1] % 2 != 0 and a[2] % 2 == 0:
    print (a[2])
    
if a[0] % 2 == 0 and a[1] % 2 == 0 and a[2] % 2 == 0:
    for i in range(3,n):
        if a[i] % 2 != 0:
            print(a[i])
            break
        
if a[0] % 2 != 0 and a[1] % 2 != 0 and a[2] % 2 != 0:
    for i in range(3,n):
        if a[i] % 2 == 0:
            print(a[i])
            break
