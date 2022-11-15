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

print(cook_book)