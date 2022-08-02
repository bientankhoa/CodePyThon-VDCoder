n = int(input())

b = [int(i) for i in input().split()]
count = 0 
if b[0] > b[1]:
    count = count + 1
if b[n-1] > b[n - 2]:
    count = count + 1

for i in range(1,n - 1):
    if b[i - 1] < b[i] and b[i] > b[i + 1]:
        count = count + 1

print(count)