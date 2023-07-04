# задание 1

from pprint import pprint


def get_cook_book(file):
    cook_book = {}

    # функция для получения словаря ингредиентов
    def get_dict_ing(str_block):
        products = str_block.split('|')
        dict_ing = {}
        dict_ing['ingredient_name'] = products[0]
        dict_ing['quantity'] = int(products[1])
        dict_ing['measure'] = products[2]
        return dict_ing

    # читаем файл с книгой рецептов и формируем словарь
    with open(file, 'r', encoding='UTF-8') as f:
        splitted_text = f.read().split('\n\n')
        for dish in splitted_text:
            dish_splitted = dish.splitlines()
            counter = 0
            name_dish = ''
            list = []
            for item in dish_splitted:
                if counter == 0:
                    name_dish = item
                if counter > 1:
                    list.append(get_dict_ing(item))
                counter += 1
            cook_book[name_dish] = list
    return cook_book


pprint(get_cook_book('recipes.txt'))
