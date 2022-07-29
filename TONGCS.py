n = int(input())
s = 0
while n > 0:
    du = n % 10
    s = s + du
    n = n // 10
print (s)
