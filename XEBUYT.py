n = int(input())

a = []
b = []

for i in range(n):
    s = [int(i) for i in input().split()]
    a.append(s[0])
    b.append(s[1])

maxx = -1e10
c = b[0]
for i in range(1,n):
    c = c - a[i] + b[i]
    if (c > maxx):
        maxx = c
    
print(maxx)