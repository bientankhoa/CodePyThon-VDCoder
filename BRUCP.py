from math import sqrt
def KtraCP(a):
    t = int(sqrt(a))
    if t * t == a:
        return True
    else :
        return False

n = int(input())
for i in range(1,n):
    for j in range(i+1,n+1):
        if KtraCP(i ** 2 + j ** 2) == True:
            print(i,j)