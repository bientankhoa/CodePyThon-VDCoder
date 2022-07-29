a = [int(i) for i in input().split()]
n,k = a[0],a[1]
sh=1
s=0
d=0
for i in range(n):
    s=s+sh
    d=d+1
    if s+sh+3>k:
        break
    sh=sh+3
print(d)

