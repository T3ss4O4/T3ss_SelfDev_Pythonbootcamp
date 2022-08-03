list_99 = list(range(0, 101))
result_list = []

for member in list_99:
    if "9" in str(member):
        result_list.append(member*2)

    if "7" in str(member):
        list_99.remove(member)

print('Part a:')
print(result_list)

print('Part b:')
print(result_list[-1])

print('Part c:')
print(list_99)
