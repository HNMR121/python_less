#
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def users(name, surname, b_date, city, email, phone):
    return f"Name: {name} Surname: {surname} Date: {b_date} City: {city} Email: {email} Pnone: {phone}"


print(users(name="Alexander",
            surname="Ivanov",
            b_date="1990",
            city="Moscow",
            email="aaa@mail.ru",
            phone="123456"))
