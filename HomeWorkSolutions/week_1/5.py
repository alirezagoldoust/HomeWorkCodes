
n = int(input())

for i in range((n + 1)//2):
    print(" " * ((n - 1) // 2 - i) + (2 * i + 1) * "*" + " " * ((n - 1) // 2 - i) * 2 + (2 * i + 1) * "*")

for i in range((n - 3)//2, -1, -1):
    print(" " * ((n - 1) // 2 - i) + (2 * i + 1) * "*" + " " * ((n - 1) // 2 - i) * 2 + (2 * i + 1) * "*")