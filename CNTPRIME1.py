d = [0 for i in range(1000001)]
c = [0 for i in range(1000001)]

def eratos():
    d[0] = d[1] = 1
    j = 2
    while j * j <= 1000001:
        if d[j] == 0:
            for i in range(j*j, 1000001, j):
                d[i] = 1
        j += 1

def demso():
    c[0] = 0
    for i in range(1000001):
        if d[i] == 0:
            c[i] = c[i-1] + 1
        else:
            c[i] = c[i-1]

eratos()
demso()

n = int(input())
for i in range(n):
    a = [int(x) for x in input().split()]
    l,r = a[0],a[1]
    print(c[r] - c[l-1])
