guess = input()
password = 'qwerty'
while guess != password:
    print('введён неверный пароль')
    guess = input()

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
