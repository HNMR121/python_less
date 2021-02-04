# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("taskfile2.txt", "r", encoding="UTF-8") as file_o:
    data = file_o.readlines()
    print(f"Всего строк в файле: {len(data)}")
    count_line = 1
    for i in data:
        words = i.count(' ') + 1
        print(f"В {count_line} строке {words} слов")
        count_line += 1


"""Если ввести строку как пустую то считает как 1 слово, можно добавить if после for elif ищет '/n'"""