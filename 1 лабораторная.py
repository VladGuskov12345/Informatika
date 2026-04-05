# TODO Напишите функцию для поиска индекса товара


#Определяем функцию с двумя параметрами
def find_first_index (items, target):
    for index, item in enumerate (items):
        #сравниваем item  искомым target
        if item == target:
            return index
        #если цикл закончился  ничего не нашли
    return None
#список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
#цикл для посика нескольких товаров
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_index (items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    #проверка
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
