from math import gcd

k = [int(i) for i in input().split()]
a,b,c,d = k[0],k[1],k[2],k[3]

ucln = gcd(gcd(a,b), gcd(c,d))

print (ucln)