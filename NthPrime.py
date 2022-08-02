e = [0 for i in range(1000001)]

def eratos():
    e[0] = e[1] = 1
    j = 2
    while j ** 2 <= 1000001:
        if e[j] == 0:
            for i in range(j*j, 1000001, j):
                e[i] = 1
        j += 1

eratos()

for i in range(15):
    print(e[i],end=" ")

for i in range(15):   
    print(i,end=" ")