# Task: Build Part a) from nr. 4 as a list comprehension
# Then outsource the list comprehension as its own function and call it on the list
# Comment in and out to see results

list_99 = list(range(0, 101))

# build as list comprehension:


# result_list = [(member*2) for member in list_99 if "9" in str(member)]

# build as reusable function:


def comp_function(new_list):
    final_list = []
    for i in new_list:
        if "9" in str(i):
            final_list.append(i * 2)
    return final_list


result_list = comp_function(list_99)


print('Part a:')
print(result_list)
