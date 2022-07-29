n = int(input())

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

count = 0
j = 0
i = 0

while j <= n - 1 and i <= n-1:
    if a[i] == b[j]:
        count = count + 1
        i = i + 1
    elif a[i] > b[j]:
        j = j + 1
    else :
        i = i+ 1

print(count)