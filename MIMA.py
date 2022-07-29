n = int(input())
a = [int(i) for i in input().split()]
maxx=-1e10
minn=1e10
for i in range(n):
    if a[i]>maxx:
        maxx=a[i]
    if a[i]<minn:
        minn=a[i]
print ("SO LON NHAT:",maxx)
print("SO BE NHAT:",minn)
