# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

viruchka = int(input("введите выручку фирмы "))
izdergh = int(input("введите издержки фирмы "))
pribil = viruchka - izdergh
if viruchka > izdergh:
    rentab = pribil / viruchka * 100
    print(f"фирма работает с прибылью {pribil} с рентабельностью {rentab}%")

elif viruchka < izdergh:
    print(f"фирма работает с убытком {pribil}")


elif viruchka == izdergh:
    print("фирма работает в ноль")