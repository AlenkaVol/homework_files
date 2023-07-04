# задание 3

# функция для подсчета количества строк в файле
def count_lines(file):
    quantity_lines = 0
    with open(file, 'r', encoding='UTF-8') as f:
        quantity_lines = len(f.readlines())
    return quantity_lines


# print(count_lines('1.txt'))
# print(count_lines('2.txt'))
# print(count_lines('3.txt'))

# функция для записи данных в итоговый файл
def write_file(file_write, file_read):
    file_name = file_read
    amount_lines = count_lines(file_read)
    with open(file_read, 'r', encoding='UTF-8') as f:
        text = f.read()
    # переменная с текстом из итогового файла для проверки
    with open(file_write, 'r', encoding='UTF-8') as f:
        text_file_write = f.read()
    # записываем в итоговый файл все переменные поочереди (в конец)
    with open(file_write, 'a', encoding='UTF-8') as f:
        if file_name not in text_file_write:
            f.write(f'{file_name} \n{amount_lines} \n{text} \n')
            print(f'Файл {file_read} записан в файл {file_write}')
        else:
            print(f'Файл {file_read} уже был записан в файл {file_write}')


write_file('final_file.txt', '2.txt')
write_file('final_file.txt', '1.txt')
write_file('final_file.txt', '3.txt')