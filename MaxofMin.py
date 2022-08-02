n = int(input())
a = [int(i) for i in input().split()]

maxx = -1e10

for i in range(n-2):
    b = min(a[i],a[i+1],a[i+2])
    if b > maxx:
        maxx = b

print(maxx)