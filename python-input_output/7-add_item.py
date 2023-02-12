#!/usr/bin/python3
"""
7. Load, add, save

"""
import json
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile('add_item.json'):
    my_lists = load_from_json_file('add_item.json')
    my_lists.extend(sys.argv[1:])
    save_to_json_file(my_lists, 'add_item.json')
    load_from_json_file('add_item.json')
else:
    with open('add_item.json', 'a+', encoding='utf-8') as f:
        my_list = []
        my_list.extend(sys.argv[1:])
        save_to_json_file(my_list, 'add_item.json')
        load_from_json_file('add_item.json')
