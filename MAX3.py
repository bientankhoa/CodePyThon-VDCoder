a=input()
b=a.split()
c=[]
for x in b:
    c.append(int(x))
maxx=c[0]
if c[1]>maxx:
    maxx=c[1]
if c[2]>maxx:
    maxx=c[2]
print ("So lon nhat:",maxx)

