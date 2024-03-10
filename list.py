a = [True, 25, 'string', 25.6, [1, 2, 3]]
print(type(a))  # метод type() указывает класс объекта
print(len(a))
a = a + [42]  # так мы можем расширять список, добавлять элемент в конец
a = ['хъ'] + a  # так мы можем расширять список, добавлять элемент в начало
print(a)
print('умноженный список: ', [1, 2] * 3)  # Списки можно дублировать при помощи умножения
print('есть ли элемент в списке?: ', 42 in a)
# Оператор in даёт True/False в поиске вхождения элемента в список
b = [33, 42, 53, -21, 12, 678]
print('max: ', max(b))
print('min: ', min(b))
print('sum: ', sum(b))
print('sorted up: ', sorted(b))  # исходный список не меняется! сорт от меньшего к большему
print('sorted reverse: ', sorted(b, reverse=True))  # сортированный в обратном порядке, от большего к меньшему
print('списки можно сравнивать: ', [12, 11, 10] > [9, 15, 21, 400])
# Причем, сравнение идёт по первому элементу списков
print('сравнение идентичных списков', [1, 2, 3] == [1, 2, 3])
print('сравнение НЕ идентичных списков', [1, 2, 3] == [1, 2, 're'])  # такие списки на <, > сравнивать нельзя
marks = [4, 3, 5, 5, 2, 4, 5]
print('получить следнее значение списка чисел: ', sum(marks) / len(marks))

# В python списки изменяемые. Мы можем поместить в список любое новое значение:
marks[2] = 100
print(marks)
marks[3:5] = 101, 102  # присвоить сразу несколько значений
print(marks)
marks[2:5] = -1, 1  # оставит только два новых значений, остальные урезаны
print(marks)
del marks[0]  # удалить элемент из списка
print(marks)

# Копирование списков. Как и в java, если a=[1, 2, 3], затем пишем b=a, то мы копируем полностью ссылки
# на одни и те же значения. Если меняем какое-то значение в a, то и в b тоже значение поменяется.
# Чтобы этого не случилось, нужно список перезаписать:
a = [1, 2, 3]
b = a[:]
b[1] = 999
print('a: ', a)
print('b: ', b)

a.clear()  # this method clears all the elements of the list
print(a)

c = a.copy()  # this method equals c = a[:] - copies all the list

print(b.count(999))  # this method counts the value count into the list

b.insert(1, 12)  # вставить элемент в определенное место списка по индексу
print(b)

d = b.pop()  # удаляет значение с конца списка, при этом он возвращает нам его,
print(d)  # Т.е. мы его можем присвоить, при необходимости, переменной.

# .pop() можно использовать с индексом, и тем самым мы можем удалять определённый элемент списка по индексу
b.pop(1)
print(b)

b.remove(999)  # удаляет элемент по значению