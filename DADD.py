n=int(input())
a=[int(i) for i in input().split()]
sd=0
sa=0
for i in range(n):
    if a[i]>0:
        sd=sd+1
    if a[i]<0:
        sa=sa+1
print ("SO DUONG:",sd)
print ("SO AM:",sa)
