n = int(input())

run = 1

s = 0

for i in range (n):
    s = s + run
    run = run + 3
print(s)

chay = 1

for i in range(n):
    print(chay,end=" ")
    chay = chay + 3
    