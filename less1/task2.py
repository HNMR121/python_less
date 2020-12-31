
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input("Введите время в секундах "))
day_sec = 86400
day = sec // day_sec
sec = sec % day_sec
hour_sec = 3600
hour = sec // hour_sec
sec = sec % hour_sec
minut = sec // 60
sec = sec % 60

print(f"{hour:02}:{minut:02}:{sec:02}")
