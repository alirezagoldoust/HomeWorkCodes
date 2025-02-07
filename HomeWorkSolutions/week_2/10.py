size_to_number = {
    "S":0,
    "M":1,
    "L":2,
    "XL":3,
    "XXL":4,
}
number_to_size = {
    0:"S",
    1:"M",
    2:"L",
    3:"XL",
    4:"XXL",
}

inventory = [int(number) for number in input().split()] + [0, 0]
n = int(input())
sizes = [size_to_number[input()] for _ in range(n)]

for size in sizes:
    if inventory[size]:
        print(number_to_size[size])
        inventory[size] -= 1
    elif inventory[size+1]:
        print(number_to_size[size+1])
        inventory[size+1] -= 1
    elif inventory[size-1]:
        print(number_to_size[size-1])
        inventory[size-1] -= 1
    elif inventory[size+2]:
        print(number_to_size[size+2])
        inventory[size+2] -= 1
    elif inventory[size-2]:
        print(number_to_size[size-2])
        inventory[size-2] -= 1
    else:
        print("No Shirt")