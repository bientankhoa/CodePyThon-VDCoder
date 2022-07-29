c = [int(i) for i in input().split()]
a,b = c[0],c[1]
s=0
for i in range(a,b+1):
    if i%2==0:
        s=s+i
print (s)
