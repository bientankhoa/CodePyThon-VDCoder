from math import sqrt
def somayman(a):
    while a > 0:
        du = a % 10
        if (du != 6 and du != 8):
            return False
        a = a // 10
    return True

t = int(input())
b = [int(i) for i in input().split()]


for x in range(t):
    n = b[x]
    k = int(sqrt(n) + 1)
    d = 0
    for i in range(1,k):
        if n % i == 0:
            j = n // i
            if somayman(i) == True or somayman(j) == True:
                d = 1
                break
    if d == 1:
        print("YES")
    else:
        print("NO")
    

