a=int(input())
b=a//2
c=a%2+a//2
if (a<=1):
    print(int(0),int(0))
elif (a % 2 == 0):
    print ("{:.0f}".format(b),"{:.0f}".format(b))
else: print ("{:.0f}".format(b),"{:.0f}".format(c))
