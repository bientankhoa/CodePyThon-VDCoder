import math
c = [int(i) for i in input().split()]
a,b,c = c[0],c[1],c[2]
p = (a + b + c) // 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print ("{:.2f}".format(s))
