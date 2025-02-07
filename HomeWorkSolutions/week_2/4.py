


n = int(input())
code_list = [input() for _ in range(n)]
duplicated_code_list = list(filter(lambda x: code_list.count(x) > 1, code_list))

final_list = []
for code in duplicated_code_list:
    if code not in final_list:
        final_list.append(code)

for code in final_list:
    print(code)
