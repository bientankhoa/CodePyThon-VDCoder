# import math
e = [0 for i in range (10000001)]

def sdx(x):
    s = 0
    n = x
    while n > 0:
        du = n % 10
        s = s * 10 + du
        n = n // 10
    if x == s:
        return True
    else:
        return False

# def Ktrasnt(k):
#     if k == 2 or k == 3:
#         return True
#     if k == 1 or k % 2 == 0 or k % 3 == 0:
#         return False
#     i = 5
#     while i <= int(math.sqrt(k)):
#         if k % i == 0 or k % (i+2) == 0:
#             return False
#         i += 6
#     return True

def sang():
    e[0] = e[1] = 1
    j = 2
    while j * j <= 10000001:
        if e[j] == 0:
            for i in range(j*j,10000001,j):
                e[i] = 1
        j += 1

sang()

n = int(input())
x = n + 1
while True:
    if sdx(x) == True:
        if e[x] == 0:
            print(x)
            break
    x += 1