import json


def my_file_opener(file_name):
    i_file = open(file_name, encoding='utf-8')
    content_dict = json.loads(i_file.read())
    i_file.close()
    return content_dict
