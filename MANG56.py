n = int(input())
a = [int(i) for i in input().split()]
i = 0
s = 0
while i <= n-1:
    if a[i] % 2 == 0:
        s = s + a[i]
    i = i + 2
print(s)
