# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


with open('taskfile3.txt', 'r', encoding='utf-8') as f_obj:
    content = {}
    for line in f_obj:
        key, value = line.split()
        content[key] = value
        if float(value) < 20000.00:
            print(f'{key}: зарплата меньше 20000')
        else:
            print("У всех сотрудников зарплата выше 20000")
    print(content)