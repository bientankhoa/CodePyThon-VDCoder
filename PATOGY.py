a = [int(i) for i in input().split()]
if  a[0]**2+a[1]**2==a[2]**2 or a[1]**2+a[2]**2==a[0]**2 or a[0]**2+a[2]**2==a[1]**2:
    print ("Ba so da nhap la bo so Pi-ta-go")
else :
    print ("Ba so da nhap khong la bo so Pi-ta-go")
