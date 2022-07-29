import math
n=int(input())
s=1
k=int(math.sqrt(n))
for i in range(2,k+1):
    if n%i==0:
        s=s+i
        j=n//i
        if i!=j:
            s=s+j
if (s==n):
    print ("YES")
else:
    print ("NO")
