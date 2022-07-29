import math
c = [int(i) for i in input().split()]
a,b = c[0],c[1]
if a == 1 or b == 1:
    bcnn = max(a,b)
    print (bcnn)
if a != 1 and b != 1:
    ucln = math.gcd(a,b)
    bcnn = (a * b) / ucln
    print ("{:.0f}".format(bcnn))
