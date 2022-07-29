import math

n = int(input())

a = []

count = 0

print("Cac uoc so cua",n)
print(int(1))
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        a.append(i)
        count = count + 1
        j = n//i
        if i != j:
            a.append(j)
            count = count + 1

a.sort()

for i in range(count):
    print(a[i])

print (n)