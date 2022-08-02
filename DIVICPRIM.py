from math import sqrt

def KtraSNT(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k % 3 == 0 or k == 1:
        return False
    i = 5
    while i <= sqrt(k):
        if k % i == 0 or k % (i+2) == 0:
            return False
        i += 6
    return True

n = int(input())

if KtraSNT(n) == True:
    print ("1")
    exit()

for i in range(2,5570):
    if KtraSNT(i) == True and KtraSNT(n-i) == True:
        print("2")
        exit()

print("3")