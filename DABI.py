n = int(input())
k = n
du = 0
s = 0
while n > 0:
    du = n % 10
    s = s + du
    n = n // 10
if k % s == 0:
    print (int(1))
else:
    print(int(0))
