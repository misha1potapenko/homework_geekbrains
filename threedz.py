a = list(range(1, 101))
one = 'процент'
two = 'процента'
five = 'процентов'
for i in a:
    if i == 11:
        print(f'{i} {five}')
    if i % 10 == 1 and i != 11:
        print(f'{i} {one}')
    if i == 12:
        print(f'{i} {five}')
    if i % 10 == 2 and i != 12:
        print(f'{i} {two}')
    if i == 13:
        print(f'{i} {five}')
    if i % 10 == 3 and i != 13:
        print(f'{i} {two}')
    if i == 14:
        print(f'{i} {five}')
    if i % 10 == 4 and i != 14:
        print(f'{i} {two}')
    if i % 10 == 5:
        print(f'{i} {five}')
    if i % 10 == 6:
        print(f'{i} {five}')
    if i % 10 == 7:
        print(f'{i} {five}')
    if i % 10 == 8:
        print(f'{i} {five}')
    if i % 10 == 9:
        print(f'{i} {five}')
    if i % 10 == 0:
        print(f'{i} {five}')

