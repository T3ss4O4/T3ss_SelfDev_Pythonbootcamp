# Now you need to recall your memory and open the newly created .json file.
# Check the previous tasks again if you forgot.
# Read the dictionary from the .json file into a variable of your choice and iterate through the list of dictionaries.
# Print a text which could look like the following example down below for each member of the dictionary:
# >>> Long (long#0003) likes to learn how to program because he is lazy"

import helper_functions

i_file = helper_functions.my_file_opener('selfdev_members.json')

for list_item in i_file:
    print(list_item['name'] + ' alias ' + list_item['discord_name'] + ' attends python class for the reason of: ' + list_item['reason_to_code'])
