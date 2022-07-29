n=int(input())
for i in range(n):
    a = [int(i) for i in input().split()]
    x,y,u,v,t = a[0],a[1],a[2],a[3],a[4]
    if abs(u-v)<=t:
        s = x*u+y*v
    else :
        if v>=u:
            s = u*x+u*y+y*t
        if u>v:
            s = v*x+v*y+x*t
    print (s)
