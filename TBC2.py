a = [int (i) for i in input().split()]

s = 0

for i in range(4):
    s = s + a[i]

print("{:.2f}".format(s/4))