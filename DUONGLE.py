x = int(input())

if x % 2 == 0:
    x = x - 1
else :
    x = x - 2

sl = (x + 1) // 2
s = ((x + 1) * sl ) // 2
    
print (int(s))
