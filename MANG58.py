c = [int(i) for i in input().split()]
m,k = c[0],c[1]
a = [int (i) for i in input().split()]
count = 0
for i in range(m):
    if a[i] == k:
        count = 1
        print("CO K O VI TRI",i + 1)
        break
if count == 0:
    print("KHONG CO K")
