c = [float(i) for i in input().split()]
n,m = c[0],c[1]
count = 0
interestRate = 0
while n < m:
    interestRate = float("{:.0f}".format(n * 0.1))
    n = n + interestRate
    count = count + 1
print (count)
    
