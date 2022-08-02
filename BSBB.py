n = int(input())
s = 0
for i in range(1,n):
    d = (n-1) // i
    s = s + d

print(s)