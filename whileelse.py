# break завершает выполнение цикла
# continue пропускает итерацию, согласно условию
# Данный цикл проверяет, все ли числа в списке являются чётными
a = [12, 14, 16, 18, 21]
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('No', last)
        break
else:
    print('Yes')
