def SumDigit(k):
    s = 0
    while k > 0:
        du = k % 10
        s = s + du
        k = k // 10
    return s

n = int(input())
a = [int(i) for i in input().split()]

for i in range(n):
    print(a[i],SumDigit(a[i]))
