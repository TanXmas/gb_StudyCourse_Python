# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def get_info(**kwargs):
    print(*kwargs.values())


get_info(name = input('Имя: '),
         surname = input('Фамилия: '),
         year_birth = int(input('Год рождения: ')),
         city = input('Город проживания: '),
         email = input('Email: '),
         phone = input('Телефон: '))
