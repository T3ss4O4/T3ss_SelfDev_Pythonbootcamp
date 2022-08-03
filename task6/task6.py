# Given an empty list "random_values", write a Python function called "random_value_consumer" which takes 2 parameters of any data type in and adds the both parameters to that list.

def random_value_consumer(para1, para2):
    new_list = []
    new_list.append(para1)
    new_list.append(para2)
    return new_list

a = 4
b = "testforgood"

random_values = random_value_consumer(a,b)

# Write a new function called "analyse_list_elements" which takes 1 parameter. The function should print the length of each element of that list with its value and type.

def analyse_list_elements(input_list):
    for member in input_list:
        print(type(member), member, " -> ",len(str(member)))

analyse_list_elements(random_values)