import helper_functions
import json


i_file = helper_functions.my_file_opener('selfdev_members.json')

for list_item in i_file:
    print('please enter what ' + list_item['name'] + ' is addicted to!')
    list_item['addicted_to'] = input()

o_file = open("selfdev_members_enriched.json", "w")

o_file.write(json.dumps(i_file, indent=4))

o_file.close()


