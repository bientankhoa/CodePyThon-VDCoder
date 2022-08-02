n = int(input())
s = (n * (n + 1)) // 2
k = 1
while k ** 2 <= n:
    s = s - (k**2)
    k += 1

print(s)