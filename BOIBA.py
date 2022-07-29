c=[int(i) for i in input().split()]
m,n=c[0],c[1]
d=0
for i in range(m,n+1):
    if i%3==0:
        d=d+1
print (d)
        
    
