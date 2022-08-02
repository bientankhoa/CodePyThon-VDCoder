import math
n = int(input())

b = [int(i) for i in input().split()]

dem = 0

for i in range(n):
    if b[i] != 1:
        d = 0
        for j in range(2,int(math.sqrt(b[i])) + 1):
            if b[i] % j == 0:
                d = d + 1
        if d == 0:
            dem = dem + 1
            print(i+1, b[i])
if dem == 0:
    print("KHONG CO SO NGUYEN TO")