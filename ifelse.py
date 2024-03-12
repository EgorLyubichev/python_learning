a = 12
b = 15
a, b = b, a
print(a)
print(b)
# в python можно сразу поменять переменные, не задействовав третью переменную

if 4 == 4.0:
    print('так выглядит if в python')

if 4 < 5 and 3 < 3.1:
    print('верно')
else:
    print('неверно')
print('так выглядит if-else')

c = int(input())
if c % 5 == 0:
    if c >= 10 and c <= 100:
        print('c кратно 5, находится в диапазоне 10-100')
    else:
        print('c кратно 5,  НЕ находится в диапазоне 10-100')
else:
    print('c не соответствует условиям')

if 1 > 5:
    print('1 > 5 is true')
elif 1 > 4:
    print('1 > 4 is true')
elif 1 > 3:
    print('1 > 3 is true')
elif 1 > 2:
    print('1 > 2 is true')
else:
    print('надоело считать') 
