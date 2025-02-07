

def flag(n, color):
    if n == 1 or n == 2:
        return 1
    
    if color == "R":
        return flag(n-2, "G") + flag(n-1, "G")

    if color == "G":
        return flag(n-2, "R") + flag(n-1, "R")

n = int(input())
print(flag(n, "R") + flag(n, "G"))