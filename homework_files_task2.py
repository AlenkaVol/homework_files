# задание 2

from pprint import pprint

cook_book = {
    'Запеченный картофель': [
     {'ingredient_name': 'Картофель ', 'measure': ' кг', 'quantity': 1},
     {'ingredient_name': 'Чеснок ', 'measure': ' зубч', 'quantity': 3},
     {'ingredient_name': 'Сыр гауда ', 'measure': ' г', 'quantity': 100}
    ],
    'Омлет': [
     {'ingredient_name': 'Яйцо ', 'measure': ' шт', 'quantity': 2},
     {'ingredient_name': 'Молоко ', 'measure': ' мл', 'quantity': 100},
     {'ingredient_name': 'Помидор ', 'measure': ' шт', 'quantity': 2},
    ],
    'Утка по-пекински': [
     {'ingredient_name': 'Утка ', 'measure': ' шт', 'quantity': 1},
     {'ingredient_name': 'Вода ', 'measure': ' л', 'quantity': 2},
     {'ingredient_name': 'Мед ', 'measure': ' ст.л', 'quantity': 3},
     {'ingredient_name': 'Соевый соус ', 'measure': ' мл', 'quantity': 60}
    ],
    'Фахитос': [
     {'ingredient_name': 'Говядина ', 'measure': ' г', 'quantity': 500},
     {'ingredient_name': 'Перец сладкий ', 'measure': ' шт', 'quantity': 1},
     {'ingredient_name': 'Лаваш ', 'measure': ' шт', 'quantity': 2},
     {'ingredient_name': 'Винный уксус ', 'measure': ' ст.л', 'quantity': 1},
     {'ingredient_name': 'Помидор ', 'measure': ' шт', 'quantity': 2}
    ]}

# функция для получения списка продуктов
def get_shop_list_by_dishes(dishes, person_count):
    dict_shop_list = {}
    for name_dish in dishes:
        ingredients = cook_book.get(name_dish)
        for ingredient in ingredients:
            dish_key = ingredient['ingredient_name']
            dish_measure = ingredient['measure']
            dish_quantity = ingredient['quantity']
            dict_measure_quantity = {}
            if dish_key in dict_shop_list.keys():
                for dish_key2, dict_measure_quantity2 in dict_shop_list.items():
                    if dish_key2 == dish_key:
                        dict_measure_quantity2['quantity'] += dish_quantity*person_count
            else:
                dict_measure_quantity['measure'] = dish_measure
                dict_measure_quantity['quantity'] = dish_quantity*person_count
                dict_shop_list[dish_key] = dict_measure_quantity
    return dict_shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

