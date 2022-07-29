n = float(input())
e = float(0)
i = 1
e = 0
while e <= n:
    e = e + 1/(i*i)
    i = (i + 1)
print ("{:.9f}".format(e))