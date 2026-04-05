import json  # Подключаем модуль для работы с JSON

def task() -> float:
    with open("input.json", "r", encoding="utf-8") as file:  # Открываем JSON-файл для чтения
        data = json.load(file)  # Загружаем содержимое файла в Python-объект

    total = 0  # Переменная для суммы произведений

    for item in data:  # Перебираем каждый словарь в списке
        total += item["score"] * item["weight"]  # Прибавляем произведение score и weight

    return round(total, 3)  # Возвращаем сумму, округленную до 3 знаков после запятой


print(task())  # Печатаем результат
