name = 'Егор'
mid_name = 'Вячеславович'
balance = 555.55

text = '''Уважаемый {n} {m}, баланс Вашего счёта составляет {b} руб.'''.format(b=balance, m=mid_name, n=name)
# можно записать иначе:
text_f = f'''Уважаемый {name} {mid_name}, баланс Вашего счёта составляет {balance} руб.'''
# Также в фигурных скобках доступны методы и т.п. для переменных, а можно без переменных использовать
# какие-то вычисления:
text_f2 = f'''Уважаемый {name.upper()} {mid_name.lower()}, баланс Вашего счёта составляет {abs(-44.55 * 2) + 12} руб.'''


# а можно в строке использовать свои функции:
def f(x):
    return x ** 2


text_with_function = f'''Квадрат значения равен {f(3)}'''

print(text_with_function)

# можем переменные внести в словарь и обращаться к ним по ключу
d = {
    "name": 'Egor',
    "mid_name": 'Viacheslavovich',
    "balance": 555.12
}

message = f'''Dear {d["name"]} {d["mid_name"]}, your balance is {f(d["balance"])}'''

print(message)

# можем работать с массивом

gender = {
    "m": 'Дорогой',
    "f": 'Дорогая'
}

a = [
    ['Егор', 'Вячеславович', 555.55, 'm'],
    ['Татьяна', 'Александровна', 777.5, 'f'],
    ['Полина', 'Егоровна', 888.88, 'f']
]

for name, mid_name, balance, g in a:
    message2 = f"***{gender[g]} {name} {mid_name}! Ваш баланс равен {balance} руб."
    print(message2)
