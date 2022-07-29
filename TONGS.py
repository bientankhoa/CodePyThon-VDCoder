n = int(input())
s = float()
for i in range(1,n+1):
    gt=1
    for x in range(1,i+1):
        gt=gt*x;
    s=s+float(1/gt)
print ("{:.10f}".format(s))
