from pprint import pprint
from TimeyWimey import TimeLog


def create_book(book_name, log_name):
    with TimeLog(log_name):
        with open('cook.txt', encoding='UTF-8') as fi:
            cook_dict = {}
            for line in fi:
                dish_name = line.strip()
                cook_dict[dish_name] = []
                counter = int(fi.readline().strip())
                for i in range(counter):
                    ingredients = fi.readline().strip().split('|')
                    temp_dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1],
                                 'measure': ingredients[2]}
                    cook_dict[dish_name].append(temp_dict)
                fi.readline()
            return cook_dict


pprint(create_book('cook.txt', 'logs.txt'))
