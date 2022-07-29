a = [int(i) for i in input().split()]
if abs(a[2]-a[0]) == abs(a[2]-a[1]):
    print ("Mouse_C")
elif abs(a[2]-a[0]) > abs(a[2]-a[1]):
    print ("Cat_B")
else:
    print ("Cat_A")
