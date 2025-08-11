import os

def generate_cook_book(file):
    with open(file, 'r', encoding='utf-8') as file:
        cook_book_dict = {}
        for line in file:
            dish = line.strip()
            count = int(file.readline())
            ingredients = []
            for i in range(count):
                ingredient = file.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
            cook_book_dict[dish] = ingredients
            file.readline()
    return cook_book_dict

cook_book = generate_cook_book('recipes.txt')
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    all_ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            all_ingredients.setdefault(
                ingredient['ingredient_name'], {'measure': ingredient['measure'],'quantity': 0}
            )
            all_ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

            sorted_ingredients = {
                name: {'measure': value['measure'], 'quantity': value['quantity']}
                for name, value in sorted(all_ingredients.items())
            }

    return sorted_ingredients
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# print(shop_list)


def check_length_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        count_str = len(f.readlines())
    return count_str

def stats_files_in_dir(dir_path):
    all_files = os.listdir(dir_path)
    file_stats = {}
    for file in all_files:
        length_file = check_length_file(dir_path+'/'+file)
        file_stats[file] = length_file

    sorted_files = {
        name: value
        for name, value in sorted(file_stats.items(), key=lambda item: item[1])
    }
    return sorted_files

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def concat_all_files_in_dir(dir_path):
    dict_for_concat = stats_files_in_dir(dir_path)
    with open(f'{dir_path}/results.txt', 'w', encoding='utf-8') as f:
        for key, values in dict_for_concat.items():
            file_content = read_file(f"{dir_path}/{key}")
            f.write(f"{key}\n{values}\n{file_content}\n\n")


concat_all_files_in_dir('exercise3')