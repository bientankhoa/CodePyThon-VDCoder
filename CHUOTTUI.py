a=[int(i) for i in input().split()]
x1,v1,x2,v2=a[0],a[1],a[2],a[3]
if (x1<x2 and v1<=v2) or (x1==x2 and v1<v2):
    print ("NO");
else :
    if (x2-x1)%(v1-v2)==0 :
        print ("YES");
    else :
        print ("NO")
