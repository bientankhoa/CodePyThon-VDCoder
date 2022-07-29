n = int(input())
du = 0
s = 0
while n > 0:
    du = n % 10
    s = s + du
    n = n // 10
if s % 10 == 9:
    print ("YES")
else:
    print("NO")
