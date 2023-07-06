# задание 3

import os


def write_file(directory_name):
    # создаем список с именами файлов необходимого формата
    list_of_files = []
    for name_file in os.listdir(directory_name):
        if '.txt' in name_file:
            list_of_files.append(name_file)

    # создаем словарь с данными для записи в новый файл
    dict_files = {}
    for file in list_of_files:
        with open(file, 'r', encoding='UTF-8') as f:
            quantity_lines = len(f.readlines())
        with open(file, 'r', encoding='UTF-8') as f:
            text = f.read()
        list_text_lines = []
        list_text_lines.append(quantity_lines)
        list_text_lines.append(text)
        dict_files[file] = list_text_lines

    # сортируем словарь файлов
    sorted_dict_files = {}
    sorted_dict_keys = sorted(dict_files, key=dict_files.get)
    for key in sorted_dict_keys:
        sorted_dict_files[key] = dict_files[key]

    # создаем новый файл для записи данных
    new_file = open("new_file.txt", "w+")

    # добавляем данные в новый файл
    for file in sorted_dict_files.items():
        name_file = file[0]
        number_of_lines = file[1][0]
        text_to_write = file[1][1]
        with open('new_file.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{name_file} \n{number_of_lines} \n{text_to_write} \n')

    print(f'Данные из файлов из папки {directory_name} записаны в файл new_file.txt')


write_file('files to write')