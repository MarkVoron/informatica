import json
import csv


# Имя входного CSV-файла
INPUT_FILENAME = "input.csv"

# Имя выходного JSON-файла
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открываем CSV-файл для чтения
    with open(INPUT_FILENAME, encoding="utf-8") as f:
        # Считываем все строки из CSV в список словарей
        # Каждый словарь = одна строка файла
        lines = [line for line in csv.DictReader(f)]

    # Открываем JSON-файл для записи
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        # Записываем данные в формате JSON
        # indent=4 нужен для красивого вывода с отступами
        json.dump(lines, f, indent=4)


# Проверяем, что файл запущен напрямую, а не импортирован как модуль
if __name__ == "__main__":
    # Вызываем основную функцию
    task()

    # Открываем результат и печатаем его на экран построчно
    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")

