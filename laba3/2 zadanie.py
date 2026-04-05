def find_common_participants(group1, group2, sep=','):  # Функция принимает две строки и разделитель
    participants1 = group1.split(sep)  # Разбиваем первую строку в список
    participants2 = group2.split(sep)  # Разбиваем вторую строку в список
    common_participants = set(participants1) & set(participants2)  # Находим общих участников
    return sorted(common_participants)  # Возвращаем отсортированный список


participants_first_group = "Иванов|Петров|Сидоров"  # Первая группа
participants_second_group = "Петров|Сидоров|Смирнов"  # Вторая группа

print(find_common_participants(participants_first_group, participants_second_group, '|'))  # Проверка с разделителем |
