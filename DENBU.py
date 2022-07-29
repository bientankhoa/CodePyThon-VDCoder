z = [int(i) for i in input().split()]
a,b,c,m,n,k = z[0],z[1],z[2],z[3],z[4],z[5]
s = m * a + k * b + (n - m - k) * c
print (s)
