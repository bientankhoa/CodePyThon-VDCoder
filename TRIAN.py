n = int(input())

a = [int(i) for i in input().split()]

k = int(input())

for i in range(n):
    if a[i] == k:
        print (i+1)
        break