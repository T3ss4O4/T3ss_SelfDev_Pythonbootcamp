# Write a Python function with the name "en_filter" which takes one parameter and checks whether a string has no "e" and "n".

def en_filter(string_in):
    if "e" not in string_in and "n" not in  string_in:
        return string_in
    else:
        return None

# Use a list comprehension which loops through the previous list from task 3 (community_members) and call (use) that function in the list comprehension.
# If the requirements are met, extend the function "en_filter" by implementing the code to append the string variable to the new list, created by the list comprehension.

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
result_list = [member for member in community_members if en_filter(member)]

# Print the final list.
print(result_list)