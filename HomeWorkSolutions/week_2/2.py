
n = int(input())
radical = int((2 * n - 2) ** 0.5)

ans = 0
for k in range(min(radical - 3, 0), radical + 3):
    if k * (k + 1) == 2 * n - 2:
        ans = 1
