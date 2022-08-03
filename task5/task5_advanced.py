# TASK 5 - ADVANCED.
# Given a .txt file with a string "1,2,3,4,5,6,7,8,10" inside. (create it yourself)
# Read the string of this file and use a list comprehension to
# iterate through the string and multiple each integer by itself
# and return a new list.
# Use a function for the multiplication with 1 parameter.
#
# At the end, save new list into a new file called "Task5a.txt"

def multiplier(list_in):
   result_list=[int(i)*int(i) for i in list_in]
   return result_list

i_file = open("Task5.txt","r")
content = i_file.read()
content_list = content.split(",")

final_list = multiplier(content_list)

o_file = open("Task5a.txt","w")
o_file.write(str(final_list))

i_file.close()
o_file.close()
