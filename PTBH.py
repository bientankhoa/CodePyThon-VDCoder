import math
a=[int(i) for i in input().split()]
denta = a[1]**2 - 4*a[0]*a[2]
if denta < 0:
    print ("VO NGHIEM")
if denta > 0:
    print ("PT CO HAI NGHIEM")
    x2 = (-a[1] - math.sqrt(denta)) / (2*a[0])
    x1 = (-a[1] + math.sqrt(denta)) / (2*a[0])
    print ("X1 =","{:.2f}".format(x1))
    print ("X2 =","{:.2f}".format(x2))
if denta == 0:
    print ("PT CO NGHIEM KEP")
    x = -a[1]/(2*a[0])
    print ("X =","{:.2f}".format(x))
