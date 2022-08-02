def snt(k):
    if k == 2 or k == 3:
        return True
    
    if k == 1 or k % 2 == 0 or k % 3 == 0:
        return False

    i = 5
    while i ** 2 <= k:
        if k % i == 0 or k % (i+2) == 0:
            return False
        i = i + 6
    return True

n = int(input())

if n <= 3:
    print("-1")
    exit()

if n == 4:
    print("2","2")

if n == 5:
    print("2","3")

for i in range(3, (n//2)+1, 2):
    if snt(i) == True:
        t = n - i
        if snt(t) == True:
            print(i,t)
            break