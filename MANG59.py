n = int(input())

a = [int(i) for i in input().split()]

for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            kg = a[i]
            a[i] = a[j]
            a[j] = kg

for i in range(n):
    print(a[i],end=" ")