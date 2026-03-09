list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2
#Берём элменты от начала списка до индекса
first_team = list_players[:middle_index]
#Берём элменты от индекса до конца списка
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
