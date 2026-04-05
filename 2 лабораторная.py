# TODO Напишите функцию find_common_participants
#создаём 2 2 группы и разделитель (zapata это запитая)
def find_common_participants(group1,group2,zapita=','):
    #разделяем 1 группу на список фамилий, (strip удаляет лишние пробелы)
    list1=[name.strip() for name in group1.split(zapita)]
    #тоже самое
    list2=[name.strip() for name in group2.split(zapita)]
    #находим общих участников с помощью &. set() превращает список во множество. list() обратно в список
    common=list(set(list1)&set(list2))
    #сортируем в алфавитном порядке
    common.sort()
    return common
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
