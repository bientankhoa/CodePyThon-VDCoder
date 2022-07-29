a = [int(i) for i in input().split()]
n, k = a[0],a[1]

v = [int(i) for i in input().split()]

t = n - v[k-1] + 1
maxx = max(v[0],t)

for i in range(k-1):
    p = v[i+1] - v[i] + 1
    if p % 2 != 0:
        p = p + 1
        tg = p // 2
        if tg > maxx:
            maxx = tg
    else :
        tg = p // 2
        if tg > maxx:
            maxx = tg

print(maxx)