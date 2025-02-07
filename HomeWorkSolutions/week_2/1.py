n = int(input())
output_names = {"M":[],"F":[]}

for i in range(n):
    name = input().split()
    output_names[name[1]].append(name[0])

name_count = {"M": {}, "F": {}}
for name in output_names["M"]:
    name_count["M"][name] = name_count["M"].get(name, 0) + 1

for name in output_names["F"]:
    name_count["F"][name] = name_count["F"].get(name, 0) + 1

max_count = {"M": 0, "F": 0}
max_count["M"] = max(name_count["M"].values())
max_count["F"] = max(name_count["F"].values())

most_common_name = {"M": [], "F": []}
for name, count in name_count["M"].items():
    if count == max_count["M"]:
        most_common_name["M"].append(name)

for name, count in name_count["F"].items():
    if count == max_count["F"]:
        most_common_name["F"].append(name)

most_common_name["M"].sort()
most_common_name["F"].sort()

print(most_common_name["F"][0])
print(most_common_name["M"][0])