m = int(input())

p = [int(i) for i in input().split()]

a = max(p)
b = min(p)

for i in range(m):
    if p[i] == a:
        vt1 = i
    if p[i] == b:
        vt2 = i

t = p[vt1]
p[vt1] = p[vt2]
p[vt2] = t

for i in range(m):
    print(p[i],end=" ")
