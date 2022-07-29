import math
a=[int(i) for i in input().split()]
kc1=math.sqrt(a[0]**2+a[1]**2)
kc2=math.sqrt(a[2]**2+a[3]**2)
if kc1<kc2:
    print("A")
elif kc1>kc2:
    print("B")
else :
    print ("BANG NHAU")
