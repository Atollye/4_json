#!/usr/bin/env python3
# /home/atollye/current/programming_exercises/4_json/pprint_json.py
import os
import sys
import json



"""
написать скрипт, который на вход принимает путь до файла с произвольными данными
 в формате JSON и выводит его содержимое в консоль в удобном для чтения виде:
  добавляет переносы строк, отступы слева и пробелы.

нужно проверить, передал ли пользователь путь к файлу,
 существует ли файл, json ли в файле, а затем обрабатывать.
"""

PATH = r"/home/atollye/current/programming_exercises/3_bars/shops.json"

def get_path_to_file():
    try:
        pth = sys.argv[1]
    except IndexError:
        pth = None
    return pth

def load_data(filepath):
    try:
        with open(filepath, "r") as file: 
            file_obj = json.load(file, encoding='utf-8')
    except json.JSONDecodeError:
        file_obj = None
    return file_obj

def error_exit(message):
    print(message)
    sys.exit()

def pretty_print_json(fileobj):
    out_str = json.dumps(fileobj, sort_keys=True, indent=4)
    print(out_str)

def main():
    pth = get_path_to_file()
    if not pth:
        error_exit("Вы не задали путь к файлу с json")
    if not os.path.isfile(pth):
        error_exit("Файл по введенному пути не существует")
    else:
        fileobj = load_data(pth)
    if not fileobj:
        error_exit("В файле не json")
    else:
        pretty_print_json(fileobj)

if __name__ == '__main__':
    main()





