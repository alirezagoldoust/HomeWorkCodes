
name = input()

for i in range(len(name)):
    print(name[i] * (i + 1) + name[i+1:])