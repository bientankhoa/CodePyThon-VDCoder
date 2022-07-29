n = int(input())
c = [int(i) for i in input().split()]
count = 0
for i in range(n):
    if c[i] % 5 == 0 and c[i] > 0:
        count = count + 1
print (count)
