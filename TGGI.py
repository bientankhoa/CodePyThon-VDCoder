import math
a = [float(i) for i in input().split()]
if a[0]+a[1]>a[2] and a[1]+a[2]>a[0] and a[2]+a[0]>a[1]:
    
    if (a[2]**2 == a[0]**2 + a[1]**2) and (a[2] == a[0]) or (a[1]**2 == a[0]**2 + a[2]**2) and (a[1] == a[2]) or (a[0]**2 == a[2]**2 + a[1]**2) and (a[0] == a[1]):
        print ("VUONG CAN")
    elif a[0] == a[1] and a[0] == a[2] and a[1] == a[2]:
        print ("DEU")
    elif math.sqrt(a[0]**2 + a[1]**2) == a[2] or math.sqrt(a[0]**2 + a[2]**2) == a[1]**2 or math.sqrt(a[2]**2 + a[1]**2) == a[0]**2:
        print ("VUONG")
    elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        print ("CAN")
    else :
        print ("THUONG")
else :
    print ("KHONGPHAITAMGIAC")

    
