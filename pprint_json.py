#!/usr/bin/env python3

import os
import sys
import json

"""
This script allows you to open a JSON file and print out its contents
 to the console in a human-readable form (i.e. with newlines, left
 indents for each data level and extra spaces between words).
"""


def get_path_to_file():
    try:
        pth = sys.argv[1]
    except IndexError:
        pth = None
    return pth


def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = None
    return data


def error_exit(message):
    print(message)
    sys.exit()


def pretty_print_json(data):
    out_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(out_str)


def main():
    pth = get_path_to_file()
    if not pth:
        error_exit("Вы не задали путь к файлу с json")
    if not os.path.isfile(pth):
        error_exit("Файл по введенному пути не существует")
    else:
        data = load_data(pth)
    if not data:
        error_exit("В файле не json")
    else:
        pretty_print_json(data)


if __name__ == '__main__':
    main()
