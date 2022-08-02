m = int(input())
b = [int(i) for i in input().split()]
for i in range(m):
    for j in range(m-1):
        if b[j] > b[j+1]:
            t = b[j]
            b[j] = b[j+1]
            b[j+1] = t
for i in range(m):
    print(b[i], end=" ")
