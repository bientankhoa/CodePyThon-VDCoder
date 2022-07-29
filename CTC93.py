def fact(k):
    gt = 1
    for i in range(1,k+1):
        gt = gt * i
    return gt

n = int(input())

a = []

for i in range(n):
    a.append(int(input()))
    print(fact(a[i]))
