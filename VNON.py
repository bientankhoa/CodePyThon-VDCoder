import math
c = [int(i) for i in input().split()]
h,r = c[0],c[1]
s = math.pi * 1/3 * r**2 * h
print("{:.8f}".format(s))

