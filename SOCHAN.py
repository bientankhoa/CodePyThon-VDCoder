n = int(input())

a = [int(i) for i in input().split()]

c = []

count = 0

for i in range(n):
    if a[i] % 2 == 0:
        count = count + 1

print (count)

for i in range(n):
    if a[i] % 2 == 0:
        print(a[i],end=" ")

