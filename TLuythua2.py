a = [int(i) for i in input().split()]
m,n = a[0],a[1]

s = 0
for i in range(1,m+1):
    s = s + i ** n

print(s)