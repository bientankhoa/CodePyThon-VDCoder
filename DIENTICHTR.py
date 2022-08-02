from math import pi

c = [int(i) for i in input().split()]
a,b,r = c[0],c[1],c[2]

s = (a * b) - r ** 2 * pi

print("{:.2f}".format(s))