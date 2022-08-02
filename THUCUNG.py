n = int(input())

a = [int(i) for i in input().split()]

maxx = max(a)
s = 0

for i in range(n):
    t = maxx - a[i]
    s = s + t

print(s)