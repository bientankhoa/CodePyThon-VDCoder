n = int(input())
if n < 10:
    print(n)
else :
    b = n // 10
    a = 0
    while b != a:
        s = n + 3 * b
        a = b
        b = s // 10
    print (s)
    
