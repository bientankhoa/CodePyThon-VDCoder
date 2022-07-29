c = [int(i) for i in input().split()]
a,x = c[0],c[1]
d = 0
while a < x:
    a = a + a * 0.011
    d = d + 1
print (d)
