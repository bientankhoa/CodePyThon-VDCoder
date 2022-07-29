n = int(input())
a = [int(i) for i in input().split()]
maxx = -1e10
for i in range(n - 1):
    if a[i] > maxx:
        maxx = a[i]
        vt = i + 1
print (maxx, vt)
