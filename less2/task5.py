# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
a = 1
cnt = len(my_list) - 1
for i in reversed(my_list):
    if i < a:
        if cnt == 0:
            my_list.insert(0, a)
        pass

    else:
        my_list.insert(cnt+1, a)
        break

    cnt = cnt-1

print(my_list)

# Нужно передедать по красивому поменять местами if else
# for i in reversed(my_list):
#     if i > a:
#         my_list.insert(cnt + 1, a)
#         break
#     elif cnt == 0:
#         my_list.insert(0, a)
#     cnt = cnt - 1
# print(my_list)

