n=int(input())
a = [int(i) for i in input().split()]
s=0
for i in range(n):
    if a[i] == 1:
        s=s-1
    if a[i] == 2:
        s=s+1
print (abs(s))
    
