cook_book = {}
with open('data.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        dish = line.strip()
        num = int(file.readline().strip())
        ing_list = []
        for _ in range(num):
            name, qual, meas = file.readline().strip().split(' | ')
            ing_list.append({'ingredient_name': name, 'quantity': int(qual), 'measure': meas})
        cook_book[dish] = ing_list
        file.readline()

#print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    list = {}
    for dish in dishes:
        for d in cook_book[dish]:
            list1 = {}
            list1['measure'] = d['measure']
            if d['ingredient_name'] in list.keys():
                list[d['ingredient_name']]['quantity'] += person_count*d['quantity']
            else:
                list1['quantity'] = person_count*d['quantity']
                list[d['ingredient_name']] = list1
    print(f'Для заказанного меню на {person_count} гостей потребуется:')
    print(list)


dish_menu = []
z = 0
while z == 0:
    dish = input('Введите название блюда: ')
    if dish in cook_book.keys():
        dish_menu.append(dish)
        print('Блюдо принято!')
        c = input('Желаете продолжить? (Y/N) ')
        if c.capitalize() == 'Y':
            continue
        elif  c.capitalize() == 'N':
            z = 1
    else:
        print('Такого блюда нет в меню!')

p_count = int(input('Введите количество гостей: '))
get_shop_list_by_dishes(dish_menu, p_count)