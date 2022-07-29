c = [int(i) for i in input().split()]
a,b = c[0],c[1]
d = 0
if a == b:
    print (int(0))
while a != b:
    a = 2 * a
    d = d + 1
    if a > b:
        if a - b >= b - (a / 2):
            print (d-1)
            break
        if a - b < b - (a / 2):
            print (d-1)
            break
    if a == b:
        print (d)
    