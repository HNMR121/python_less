# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.




with open("taskfile5.txt", "w") as f_obj:
    f_obj.write(input("Введите числа для суммы "))

with open("taskfile5.txt", "r", encoding="UTF-8") as file_o:
    l = file_o.readlines()
    print(int(l[0].split()[0]) + int(l[0].split()[1]))

