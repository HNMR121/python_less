# 6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

json_d = {}
with open('taskfile6.txt', "r", encoding="UTF-8") as f_obj:
    content = f_obj.read().splitlines()
    for line in content:
        s = line.split(":")[1]
        nums = re.findall(r'\d+', s)
        key = line.split(":")[0]
        s = line.split(":")[1]
        nums_sum = 0
        for i in nums:
            nums_sum = int(i) + nums_sum
        value = nums_sum
        json_d[key] = value
    print(json_d)
