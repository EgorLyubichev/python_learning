# guess = input()
# password = 'qwerty'
# while guess != password:
#     print('введён неверный пароль')
#     guess = input()

a = [1, 2, 3] * 5
print(a)
while 3 in a:
    a.remove(3)
    print(a)

text = 'fhghHRI234^$#'
while len(text) > 0:
    letter = text[0]
    if 'a' <= letter <= 'z':
        print(letter, 'small letter')
    elif 'A' <= letter <= 'Z':
        print(letter, 'big letter')
    elif letter.isdigit():
        print(letter, 'digit')
    else:
        print(letter, 'znak')
    text = text[1:]

number = -463787
number = abs(number)
while number > 0:
    r = number % 10
    print(r)
    number = number // 10

# Если этот код переложить на двойки, то этот алгоритм будет переводить числа в двоичную систему исчисления,
# только числа будут в обратном порядке
print('В двоичной системе исчисления: ')
source = 14
result = ''
while source > 0:
    last = source % 2
    result = result + str(last)
    source = source // 2
result = result[::-1]
print(result)
