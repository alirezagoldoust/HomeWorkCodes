
n = int(input())
# dp = {"R": [0, 1, 1], "G": [0, 1, 1]}

# for i in range(3, n + 1):
#     dp_r = dp["G"][i-1] + dp["G"][i-2]
#     dp["R"].append(dp_r)

#     dp_g = dp["R"][i-1] + dp["R"][i-2]
#     dp["G"].append(dp_g)

# print(dp["G"][n] + dp["R"][n])

flag = [0, 1, 1]
for i in range(3, n+1):
    new_flag = flag[i-1] + flag[i-2]
    flag.append(new_flag)

print(2 * flag[n])